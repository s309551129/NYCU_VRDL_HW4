_base_ = './configs/restorers/edsr/edsr_x3c64b16_g1_300k_div2k.py'

data = dict(
    train=dict(
        type='RepeatDataset',
        times=1000,
        dataset=dict(
            lq_folder='../data_x3/train/LR',
            gt_folder='../data_x3/train/HR',
            ann_file='../data_x3/train/train.txt')),
    val=dict(
        lq_folder='../data_x3/valid/LR',
        gt_folder='../data_x3/valid/HR'),
    test=dict(
        lq_folder='../data_x3/valid/LR',
        gt_folder='../data_x3/valid/HR'))

# optimizer
optimizers = dict(generator=dict(type='Adam', lr=1e-4, betas=(0.9, 0.999)))

load_from = None
