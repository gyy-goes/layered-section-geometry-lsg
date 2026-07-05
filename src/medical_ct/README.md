# Medical-CT 医学CT三维重建模块
## 模块定位
基于Common-LSG通用几何内核的医学CT场景专属优化模块，支持任意角度非正交截面重建、靶器官精准分割、术前三维建模。

## 核心功能
1. 标准DICOM CT数据解析，自动转换HU值
2. 金属伪影、射束硬化伪影专属消除算法
3. 人体多组织HU值边界约束，提升重建分层精度
4. 对接Common-LSG非正交重建内核，输出顺滑三维体模型

## 依赖
- 底层内核：Common-LSG v0.1+
- 第三方依赖：numpy, pydicom

## 调用示例
```python
from Medical_CT.hardware_adapt.dicom_ct_parser import DicomCTParser
from Common_LSG.slice_rebuild import SectionRebuilder

parser = DicomCTParser()
ct_data = parser.load_dicom_series("./dicom_data")
rebuilder = SectionRebuilder()
model = rebuilder.non_orthogonal_rebuild(ct_data.section_stack, ct_data.spacing)
开源声明
本模块场景优化代码遵循 MIT 协议，底层几何内核永久归入人类公共知识领域，禁止基于本模块核心逻辑申请独占专利。