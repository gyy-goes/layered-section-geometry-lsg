永久记录本目录分层架构（本次给你的完整文件夹树）

2.1 Medical-CT 医学 CT 三维重建模块
Medical-CT/
├─ scene_constraint/
│  └─ ct_tissue_constraint.py
├─ noise_optimize/
│  └─ ct_artifact_removal.py
├─ hardware_adapt/
│  └─ dicom_ct_parser.py
├─ demo_case/
│  └─ ct_3d_rebuild_demo.py
└─ README.md
### 2.2 Medical-Ultrasound 超声成像三维重建模块
#### 目录结构
Medical-Ultrasound/
├─ scene_constraint/
│ └─ us_acoustic_constraint.py
├─ noise_optimize/
│ └─ us_speckle_denoise.py
├─ hardware_adapt/
│ └─ us_signal_parser.py
├─ demo_case/
│ └─ us_3d_rebuild_demo.py
└─ README.md
2.3 Geo-MountainNav 山区无人机离线导航模块
Geo-MountainNav/
├─ scene_constraint/
│  └─ terrain_gradient_constraint.py
├─ noise_optimize/
│  └─ pointcloud_outlier_clean.py
├─ hardware_adapt/
│  └─ lidar_vision_parser.py
├─ demo_case/
│  └─ mountain_nav_map_demo.py
└─ README.md
2.4 Ocean-SubNav 水下潜航海底测绘导航模块
Ocean-SubNav/
├─ scene_constraint/
│  └─ seabed_terrain_constraint.py
├─ noise_optimize/
│  └─ sonar_scatter_denoise.py
├─ hardware_adapt/
│  └─ multibeam_sonar_parser.py
├─ demo_case/
│  └─ seabed_rebuild_demo.py
└─ README.md
3.1 Aerospace-Space 航空航天大尺度测绘模块
Aerospace-Space/
├─ scene_constraint/
│  └─ large_scale_distortion_constraint.py
├─ noise_optimize/
│  └─ remote_sensing_stripe_denoise.py
├─ hardware_adapt/
│  └─ satellite_aerial_parser.py
├─ demo_case/
│  └─ aerospace_3d_rebuild_demo.py
└─ README.md
3.2 Industrial-3DInspect 工业 3D 无损检测模块
Industrial-3DInspect/
├─ scene_constraint/
│  └─ defect_boundary_constraint.py
├─ noise_optimize/
│  └─ industrial_ct_artifact_optimize.py
├─ hardware_adapt/
│  └─ industrial_ct_parser.py
├─ demo_case/
│  └─ defect_detect_rebuild_demo.py
└─ README.md
3.3 Architecture-BIM 建筑 BIM 逆向建模模块
Architecture-BIM/
├─ scene_constraint/
│  └─ building_structure_constraint.py
├─ noise_optimize/
│  └─ pointcloud_dynamic_denoise.py
├─ hardware_adapt/
│  └─ tilt_photography_parser.py
├─ demo_case/
│  └─ bim_reverse_rebuild_demo.py
└─ README.md
3.4 Robot-Vision 机器人视觉环境感知模块
Robot-Vision/
├─ scene_constraint/
│  └─ workspace_constraint.py
├─ noise_optimize/
│  └─ motion_blur_optimize.py
├─ hardware_adapt/
│  └─ depth_camera_parser.py
├─ demo_case/
│  └─ embedded_low_power_rebuild_demo.py
└─ README.md
3.5 Energy-OilGeo 油气地质勘探模块
Energy-OilGeo/
├─ scene_constraint/
│  └─ stratum_deposition_constraint.py
├─ noise_optimize/
│  └─ seismic_noise_suppress.py
├─ hardware_adapt/
│  └─ seismic_logging_parser.py
├─ demo_case/
│  └─ reservoir_3d_model_demo.py
└─ README.md
3.6 VirtualReality-VRAR 虚拟现实空间重建模块
VirtualReality-VRAR/
├─ scene_constraint/
│  └─ spatial_plane_constraint.py
├─ noise_optimize/
│  └─ depth_hole_repair.py
├─ hardware_adapt/
│  └─ rgbd_vr_parser.py
├─ demo_case/
│  └─ lightweight_real_rebuild_demo.py
└─ README.md
3.7 Traffic-SmartRoad 智慧道路高精建图模块
Traffic-SmartRoad/
├─ scene_constraint/
│  └─ road_flatness_constraint.py
├─ noise_optimize/
│  └─ dynamic_traffic_denoise.py
├─ hardware_adapt/
│  └─ vehicle_lidar_parser.py
├─ demo_case/
│  └─ road_hd_map_demo.py
└─ README.md
3.8 Bio-Microscope 生物显微三维成像模块
Bio-Microscope/
├─ scene_constraint/
│  └─ cell_layer_constraint.py
├─ noise_optimize/
│  └─ microscope_noise_optimize.py
├─ hardware_adapt/
│  └─ confocal_microscope_parser.py
├─ demo_case/
│  └─ micro_3d_rebuild_demo.py
└─ README.md