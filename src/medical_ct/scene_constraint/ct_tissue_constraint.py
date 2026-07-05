"""
CT医学影像组织约束模块（场景专属）
底层依赖：Common-LSG constraint_algo 基类
功能：基于HU值范围对人体组织进行层级边界约束，提升重建组织分界精度
"""
from Common_LSG.constraint_algo import BaseSectionConstraint

class CTTissueConstraint(BaseSectionConstraint):
    # 人体组织标准HU值范围约束
    TISSUE_HU_RANGE = {
        "air": (-1000, -800),
        "lung": (-800, -300),
        "fat": (-100, -50),
        "soft_tissue": (20, 80),
        "bone": (300, 3000)
    }

    def apply_hu_boundary_constraint(self, section_matrix, tissue_type="soft_tissue"):
        """
        对单截面矩阵施加HU值边界约束，保留目标组织灰度区间
        :param section_matrix: 单截面灰度矩阵（来自Common-LSG切片重建输出）
        :param tissue_type: 目标组织类型
        :return: 约束后的截面矩阵
        """
        min_hu, max_hu = self.TISSUE_HU_RANGE.get(tissue_type, (-1000, 3000))
        constrained_matrix = self.base_boundary_constrain(section_matrix, min_hu, max_hu)
        return constrained_matrix

    def multi_tissue_layer_constrain(self, section_matrix):
        """
        多组织层级约束，按HU值自动分层，适配LSG层级积分逻辑
        """
        layer_masks = {}
        for tissue, (hu_min, hu_max) in self.TISSUE_HU_RANGE.items():
            mask = (section_matrix >= hu_min) & (section_matrix <= hu_max)
            layer_masks[tissue] = mask
        return self.layer_mask_merge(section_matrix, layer_masks)