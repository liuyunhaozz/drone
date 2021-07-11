# *_* : coding: utf-8 *_*

# 利用标签文件将数据集转为 coco 格式

import json
import cv2
import os
import pandas as pd
import sys

# 读取图像和标签文件
img_dir = os.listdir('images')
label_dir = os.listdir('label')



# 开始构建 json 文件

js = {}

js["images"] = []
for index, name in enumerate(img_dir):
    dic = {}
    dic["height"] = 640
    dic["width"] = 480
    dic["id"] = index
    dic["file_name"] = name
    js["images"].append(dic)


js["categories"] = []
dic = {}
dic["supercategory"] = "target"
dic["id"] =  1 # 类别 id 从 1 开始
dic["name"] = "target"
js["categories"].append(dic)



js["annotations"] = []

annotations_id = 1

for index, name in enumerate(label_dir):
    with open(os.path.join('label', name)) as file:
        lines = file.readlines()
        # print(lines)
        for line in lines:
            lst = line.split()
            if len(lst) != 5:
                print(f'error in label {name}')
                sys.exit()
            dic = {}

            try:
                x = float(lst[1]) * 480 
                y = float(lst[2]) * 640
                w = float(lst[3]) * 480
                h = float(lst[4]) * 640
            except ValueError:
                print(f'Valueerror in label {name}')
                sys.exit()
            # dic["segmentation"] = [[x - w/2, y - h/2, x + w/2, y - h/2, x + w/2, y + h/2, x - w/2, y + h/2]]
            dic["segmentation"] = [[]]
            dic["iscrowd"] = 0
            
            dic["area"] = w * h
            dic["image_id"] = index
            dic["bbox"] = [x - w/2, y - h/2, w, h]
            dic["category_id"] = 1
            dic["id"] = annotations_id
            annotations_id += 1
            
            js["annotations"].append(dic)


with open("trainval1.json", "w") as f:
    json.dump(js, f, indent=2)
    print('make successfully')

