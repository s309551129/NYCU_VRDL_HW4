# NYCU_VRDL_HW4
This repository is about HW4 in Visual Recognition using Deep Learning class, NYCU. In this assignment, we need to train a model to reconstruct a high-resolution image from a low-resolution input. It is a task related to super-resolution, which is important in many fields such as surveillance or medical imaging.
# Environment
Please install the MMediting package from this website in advance:
```
https://github.com/open-mmlab/mmediting
```
Follow the steps to install MMediting and run requirements.txt to set the environment:
```
pip3 install -r ./mmediting/requirements.txt
```
# Prepare Dataset
You can download the dataset from codalab in-class competition:
```
https://codalab.lisn.upsaclay.fr/competitions/622#participate-get_data
```
After downloading, please add some directories so that the overall file should be setting like the following:
```
${data_x3}
  +- train
    +- HR
    +- LR
  +- valid
    +- HR
    +- LR
${dataset}
  +- datasets
    +- training_hr_images
      +- training_hr_images
        |  +- 2092.png
        |  +- 8049.png
        |  +- ...
    +- testing_lr_images
      +- testing_lr_images
        |  +- 00.png
        |  +- 01.png
        |  +- ...
${mmediting}
  +- edsr_x3_config.py
  +- inference.py
  +- ...
${result}
preprocess.py
```
You can run this command to get HR-LR training pairs and split them into training set and validation set. 
```
python3 preprocess.py
```
# Training
To train the model, run this command:
```
python3 ./mmediting/tools/train.py edsr_x3_config.py
```
# Evaluation
Download the pretrained weight from the link:
```
https://drive.google.com/drive/folders/17r0enWkAP0ZD2eOXL80Rvz2VYwuBvOs8
```
You can run this command to generate super-resolution images for testing data:
```
python3 ./mmdetection/inference.py --config edsr_x3_config.py --weight {path of pretrained weight}
```
# Results
PSNR => 28.1912<br>
# Reference
EDSR
```
https://arxiv.org/pdf/1707.02921.pdf
```
MMediting
```
https://github.com/open-mmlab/mmediting
```
