import numpy as np
from random import normalvariate, randint
import os
from PIL import Image
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt

def resizeImg(**args):
    args_key = {'ori_img': '', 'dst_img': '', 'save_q': 100}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]
    image = Image.open(arg['ori_img'])
    w = image.size[0]
    h = image.size[1]
    sizeMax =1200
    sizeMin =640
    random_size = randint(sizeMin,sizeMax)
    if w < h:
        image.resize((random_size,round(h/w * random_size)),Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])
    else:
        image.resize((round(w/h * random_size),random_size), Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])

def random_crop(**args):
    args_key = {'ori_img': '', 'dst_img': '', 'save_q': 100}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]
    image = Image.open(arg['ori_img'])
    w = image.size[0]
    h = image.size[1]
    size =256
    new_left = randint(0,w - size)
    new_upper = randint(0,h - size)
    image = image.crop((new_left,new_upper,size+new_left,size+new_upper))
    return image.resize((size,size),Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])

save_q = 100
file_path = "../Dataset/train"
files = os.listdir(file_path)
files = [file_path + '/' + s for s in files if os.path.splitext(s)[1] == '.png']
i=0
crop_num = 8

for ori_img in files:
    i+=1
    dst_img = file_path + '/resize/' + ori_img.rstrip('.png').lstrip(file_path) + '_resize.png'
    resizeImg(ori_img=ori_img, dst_img=dst_img, save_q=save_q)
    for i in range(crop_num):
        dst_img = file_path + '/crop/'+ori_img.rstrip('.png').lstrip(file_path) + '_crop_' + str(i)+'.png'
        random_crop(ori_img=ori_img, dst_img=dst_img, save_q=save_q)
    print('precessing for image ' + str(i) + ' is done')