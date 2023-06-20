_base_ = [
    'C:/Users/zliu/Utilities/OpenMMLab/mmsegmentation/configs/_base_/models/pointrend_r50.py',
    'C:/Users/zliu/Utilities/OpenMMLab/mmsegmentation/configs/_base_/default_runtime.py',
    'C:/Users/zliu/Projects/openmmlab/configs/mmseg_configs/datasets/creditcard50k.py',
    'C:/Users/zliu/Projects/openmmlab/configs/mmseg_configs/schedules/schedule_160k.py'
]
norm_cfg = dict(type='SyncBN', requires_grad=True)
model = dict(
    pretrained='C:/Users/zliu/Utilities/OpenMMLab/models/resnet101_v1c-e67eebb6.pth',
    backbone=dict(depth=101),
    decode_head=[
    dict(
        type='FPNHead',
        in_channels=[256, 256, 256, 256],
        in_index=[0, 1, 2, 3],
        feature_strides=[4, 8, 16, 32],
        channels=128,
        dropout_ratio=-1,
        num_classes=2,
        norm_cfg=norm_cfg,
        align_corners=False,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0)),
    dict(
        type='PointHead',
        in_channels=[256],
        in_index=[0],
        channels=256,
        num_fcs=3,
        coarse_pred_each_layer=True,
        dropout_ratio=-1,
        num_classes=2,
        align_corners=False,
        loss_decode=dict(
            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0))
    ],
    train_cfg=dict(num_points=128),
    test_cfg=dict(subdivision_num_points=512)
)
lr_config = dict(warmup='linear', warmup_iters=200)