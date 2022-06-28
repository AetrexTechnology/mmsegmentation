_base_ = [
    '../_base_/models/pointrend_r50.py',
    '../_base_/default_runtime.py',
    '../_base_/datasets/feetarch5k.py',
    '../_base_/schedules/schedule_160k.py'
]
norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    pretrained='open-mmlab://resnet101_v1c',
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