"""
GDE 全域对偶演化方程 主求解器
严格对应 LSG 标准矩阵形式：
d²Φ/dt² = αL²Φ - βLΦ - γN(Φ) + δΛ²Φ
"""
import numpy as np
from .operators import (
    build_3d_laplacian,
    build_3d_gradient,
    build_lambda_coupling,
    build_global_operator
)


class GDE_LSG_Solver:
    """
    LSG 多层截面 GDE 演化求解器
    可配置截面数量、空间格点、物理常数，适配全尺度场景
    """

    def __init__(
        self,
        nx: int = 32,
        ny: int = 32,
        nz: int = 32,
        n_layers: int = 8,
        dx: float = 1.0,
        dlambda: float = 1.0,
        alpha: float = 0.15,
        beta: float = 0.8,
        gamma: float = 0.05,
        delta: float = 0.1,
    ):
        # 数值离散参数
        self.nx, self.ny, self.nz = nx, ny, nz
        self.n_layers = n_layers
        self.n_spatial = nx * ny * nz
        self.n_total = n_layers * self.n_spatial
        self.dx = dx
        self.dlambda = dlambda

        # GDE 物理常数
        self.alpha = alpha    # 正维度凝聚四阶项
        self.beta = beta      # 负维度弥散二阶项
        self.gamma = gamma    # 正负维度互易耦合
        self.delta = delta    # 层间平滑扩散

        # 构造全域算子
        self._build_operators()

    def _build_operators(self):
        """构造所有全域稀疏算子，初始化时执行一次"""
        L_single = build_3d_laplacian(self.nx, self.ny, self.nz, self.dx)
        G_single = build_3d_gradient(self.nx, self.ny, self.nz, self.dx)

        self.L_global = build_global_operator(L_single, self.n_layers)
        self.G_global = build_global_operator(G_single, self.n_layers)
        self.Lambda_global = build_lambda_coupling(
            self.n_layers, self.n_spatial, self.dlambda
        )

    def rhs(self, Phi: np.ndarray) -> np.ndarray:
        """
        计算 GDE 方程右端项 d²Φ/dt²
        输入：全域场向量 (n_total,)
        输出：二阶时间导数 (n_total,)
        """
        LPhi = self.L_global.dot(Phi)
        # 1. 正维度凝聚四阶项 αL²Φ
        term1 = self.alpha * self.L_global.dot(LPhi)
        # 2. 负维度弥散二阶项 -βLΦ
        term2 = -self.beta * LPhi
        # 3. 层级扩散项 δΛ²Φ
        term3 = self.delta * self.Lambda_global.dot(self.Lambda_global.dot(Phi))
        # 4. 非线性互易耦合项 -γ·∇·(∇²Φ · ∇Φ)
        GPhi = self.G_global.dot(Phi)
        diag_LPhi_GPhi = np.repeat(LPhi, 3) * GPhi
        term4 = -self.gamma * self.G_global.T.dot(diag_LPhi_GPhi)

        return term1 + term2 + term3 + term4

    def verlet_step(self, Phi_prev: np.ndarray, Phi_curr: np.ndarray, dt: float):
        """单步 Verlet 积分，返回下一时刻场量"""
        rhs_curr = self.rhs(Phi_curr)
        Phi_next = 2 * Phi_curr - Phi_prev + dt ** 2 * rhs_curr
        return Phi_next

    def evolve(self, Phi0: np.ndarray, dt: float, steps: int) -> np.ndarray:
        """
        完整演化序列
        输入：初始场 Phi0，初始速度为0
        输出：轨迹数组 (steps+1, n_total)
        """
        # 初始静止，构造第一步
        Phi1 = Phi0 + 0.5 * dt ** 2 * self.rhs(Phi0)
        trajectory = [Phi0.copy(), Phi1.copy()]

        Phi_prev, Phi_curr = Phi0, Phi1
        for _ in range(steps):
            Phi_next = self.verlet_step(Phi_prev, Phi_curr, dt)
            trajectory.append(Phi_next.copy())
            Phi_prev, Phi_curr = Phi_curr, Phi_next

        return np.array(trajectory)

    def init_gaussian_pulse(self, center_layer: int = None, sigma: float = 3.0):
        """生成初始高斯扰动，用于测试与正演"""
        if center_layer is None:
            center_layer = self.n_layers // 2

        Phi0 = np.zeros(self.n_total)
        x = np.linspace(-self.nx//2, self.nx//2, self.nx)
        y = np.linspace(-self.ny//2, self.ny//2, self.ny)
        z = np.linspace(-self.nz//2, self.nz//2, self.nz)
        X, Y, Z = np.meshgrid(x, y, z, indexing="ij")

        gauss = np.exp(-(X**2 + Y**2 + Z**2) / (2 * sigma**2)).flatten()
        start = center_layer * self.n_spatial
        end = start + self.n_spatial
        Phi0[start:end] = gauss
        return Phi0