"""
交通动态去噪模块（场景专属）
底层依赖：Common-LSG constraint_algo 点云平滑算子
功能：移除车载点云中的动态车辆、行人，保留静态道路设施
"""
from Common_LSG.constraint_algo import PointCloudSmoother

class DynamicTrafficDenoise(PointCloudSmoother):
    def dynamic_vehicle_remove(self, point_cloud):
        """动态车辆、行人移除，保留静态道路结构"""
        static_cloud = self.moving_object_filter(point_cloud)
        return static_cloud

    def road_edge_optimize(self, road_mesh):
        """道路边缘顺滑优化"""
        smooth_mesh = self.gradient_smooth_mesh(road_mesh, smooth_level=1)
        return smooth_mesh