import os
import argparse
import mmcv
from mmedit.apis import init_model, restoration_inference
from mmedit.core import tensor2img


def main():
    count = 0
    model = init_model(args.config, args.weight, device='cuda:0')
    img_list = os.listdir(root_test)
    img_list.sort()
    for img_name in img_list:
        count += 1
        print(count)
        img = restoration_inference(model, root_test+img_name)
        sr_img = tensor2img(img)
        mmcv.imwrite(sr_img, root_save+img_name.replace(".png", "_pred.png"))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='inference')
    parser.add_argument('--config', help='config file')
    parser.add_argument('--weight', help='pretrained weight')
    args = parser.parse_args()
    root_test = '../datasets/testing_lr_images/testing_lr_images/'
    root_save = '../result/'
    main()
