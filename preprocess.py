import os
from PIL import Image

min_size = 144


def check_min_size(img, h, w):
    flag = False
    if h < min_size:
        h = min_size
        flag = True
    if w < min_size:
        w = min_size
        flag = True
    if flag is True:
        img = img.resize((h, w), resample=Image.BICUBIC)
    return img, h, w


def get_divisible_size(h, w, scale):
    h, w = h - (h % scale), w - (w % scale)
    return h, w


def main(root, root_train, root_valid, scale):
    count = 0
    ann_train = open(root_train + "train.txt", "w")
    ann_valid = open(root_valid + "valid.txt", "w")
    img_list = os.listdir(root)
    img_list.sort()
    for img_name in img_list:
        count += 1
        print(count)
        img = Image.open(root+img_name)
        size = img.size
        img, h, w = check_min_size(img, size[0], size[1])
        h, w = get_divisible_size(h, w, scale)
        # resize
        hr_img = img.resize((h, w), resample=Image.BICUBIC)
        lr_img = img.resize((h // scale, w // scale), resample=Image.BICUBIC)
        # save
        if count <= 270:
            hr_img.save(root_train+"HR/"+img_name)
            lr_img.save(root_train+"LR/"+img_name)
            ann_train.write("{img_name} ({h},{w},3)\n".format(img_name=img_name, h=h, w=w))
        else:
            hr_img.save(root_valid+"HR/"+img_name)
            lr_img.save(root_valid+"LR/"+img_name)
            ann_valid.write("{img_name} ({h},{w},3)\n".format(img_name=img_name, h=h, w=w))


if __name__ == '__main__':
    root = "./datasets/training_hr_images/training_hr_images/"
    root_train = "./data_x3/train/"
    root_valid = "./data_x3/valid/"
    scale = 3
    main(root, root_train, root_valid, scale)
