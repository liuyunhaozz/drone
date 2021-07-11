# *_* : coding: utf-8 *_*

# 将图片中的 'color' 去掉

import os

# label_dir = os.listdir('label')
# print(len(label_dir))  >> 5632
# js = {}
img_dir = os.listdir('images')
label_dir = os.listdir('ptxt')
path = r'images'

for index, name in enumerate(img_dir):
    # print(name)
    os.rename(os.path.join(path, name), os.path.join(path, str(index) + '.jpg'))


for index, name in enumerate(label_dir):
    # print(name)
    os.rename(os.path.join('ptxt', name), os.path.join('ptxt', str(index) + '.txt'))
print('Rename Success!')
