"""
运动模糊优化模块（场景专属）
底层依赖：Common-LSG constraint_algo 平滑算子
功能：抑制机器人运动导致的图像模糊，适配低光照场景
"""
from Common_LSG.constraint_algo import AdaptiveSmoother

class MotionBlurOptimize(AdaptiveSmoother):
    def motion_blur_restore(self, section_matrix, motion_direction="horizontal"):
        """运动模糊自适应修复"""
        restored_matrix = self.deblur_adaptive(section_matrix, direction=motion_direction)
        return restored_matrix

    def low_light_enhance(self, section_matrix):
        """低光照环境图像增强，保留边缘细节"""
        enhanced_matrix = self.low_light_gray_enhance(section_matrix)
        return enhanced_matrix