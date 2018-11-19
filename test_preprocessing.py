# -*- coding: utf-8 -*-
import numpy as np
from random import normalvariate, randint
import os
from PIL import Image


def resizeImg(**args):
    args_key = {'ori_img': '', 'dst_img': '', 'save_q': 100}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]
    image = Image.open(arg['ori_img'])
    w = image.size[0]
    h = image.size[1]
    #sizeMax =1200
    #sizeMin =640
    #random_size = randint(sizeMin,sizeMax)
    size_w = int(np.floor(w/256))
    size_h = int(np.floor(h/256))

    image.resize((size_w*256,size_h*256),Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])


# def random_crop(**args):
#     args_key = {'ori_img': '', 'dst_img': '', 'save_q': 100}
#     arg = {}
#     for key in args_key:
#         if key in args:
#             arg[key] = args[key]
#     image = Image.open(arg['ori_img'])
#     w = image.size[0]
#     h = image.size[1]
#     size =256
#     new_left = randint(0,w - size)
#     new_upper = randint(0,h - size)
#     image = image.crop((new_left,new_upper,size+new_left,size+new_upper))
#     return image.resize((size,size),Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])

save_q = 100
file_path = "../Dataset/test"
files = os.listdir(file_path)
files = [file_path + '/' + s for s in files if os.path.splitext(s)[1] == '.png']

for ori_img in files:
    dst_img = file_path + '/resize/' + ori_img.rstrip('.png').lstrip(file_path) + '_resize.png'
    resizeImg(ori_img=ori_img, dst_img=dst_img, save_q=save_q)
print('Test Image Preprocessing is done')