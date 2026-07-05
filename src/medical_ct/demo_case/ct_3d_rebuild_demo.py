"""
医学CT三维重建Demo
调用链路：DICOM解析 -> 伪影优化 -> 组织约束 -> Common-LSG核心重建 -> 三维导出
"""
import os
from Medical_CT.hardware_adapt.dicom_ct_parser import DicomCTParser
from Medical_CT.noise_optimize.ct_artifact_removal import CTArtifactOptimizer
from Medical_CT.scene_constraint.ct_tissue_constraint import CTTissueConstraint
from Common_LSG.slice_rebuild import SectionRebuilder
from Common_LSG.io_utils import STLExporter

def ct_rebuild_pipeline(dicom_folder, output_stl_path, target_tissue="bone"):
    # 1. 解析DICOM数据
    parser = DicomCTParser()
    ct_data = parser.load_dicom_series(dicom_folder)
    
    # 2. 伪影校正
    optimizer = CTArtifactOptimizer()
    corrected_data = optimizer.beam_hardening_correction(ct_data.section_stack)
    
    # 3. 组织约束
    constraint = CTTissueConstraint()
    constrained_stack = [constraint.apply_hu_boundary_constraint(s, target_tissue) for s in corrected_data]
    
    # 4. 调用Common-LSG核心重建
    rebuilder = SectionRebuilder()
    volume_model = rebuilder.non_orthogonal_rebuild(constrained_stack, ct_data.spacing)
    
    # 5. 导出STL模型
    exporter = STLExporter()
    exporter.export(volume_model, output_stl_path)
    print(f"CT三维重建完成，模型已导出至：{output_stl_path}")

if __name__ == "__main__":
    ct_rebuild_pipeline("./sample_ct", "./output/bone_model.stl", target_tissue="bone")