# yapf:disable
log_config = dict(
    interval=100,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=False),
        dict(type='WandbLoggerHook',interval=100,
            init_kwargs=dict(
                project='trash_segmentation',
                entity = 'hyeonjini',
                name = 'UperNet_swin_base_4_12_oversampling3'
            ),
            )
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
cudnn_benchmark = True
