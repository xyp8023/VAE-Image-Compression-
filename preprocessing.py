# import os
# import cv2
# import numpy as np
#
# def load_data(img_dir):
#     return np.array([cv2.imread(os.path.join(img_dir, img)).flatten() for img in os.listdir(img_dir) if img.endswith(".png")])
#
# # PATH = 'images/*.png'
# # import os
# list_of_imgs = []
# img_dir = "/images/"
# for img in os.listdir("."):
#     img = os.path.join(img_dir, img)
#     if not img.endswith(".png"):
#         continue
#     a = cv2.imread(img)
#     if a is None:
#         print ("Unable to read image", img)
#         continue
#     list_of_imgs.append(a.flatten())
# train_data = np.array(list_of_imgs)


# import tensorflow as tf
# import os
#
# # list files name
# files = os.listdir("../Dataset/2048-1356")
# files = ["..Dataset/2048-1356/" + s for s in files if os.path.splitext(s)[1] == '.png']
# files = [os.path.abspath(s) for s in files ]
#
#
# # Here generating a tensor of type string that include all the filename with png extention
# filename_queue  = tf.train.string_input_producer(files)
# # Initializing a file Reader
# image_reader = tf.WholeFileReader()
#
# # Here the file all the files mentioned ie filename queue and
# # returns the  the file name and the pixelvalue in form of a tensor !
# imageName,imagefile= image_reader.read(filename_queue)
# image = tf.image.decode_png(imagefile)
# #image_size =tf.size(image)
# tf.global_variables_initializer()
# with tf.Session() as sess:
#     tf.global_variables_initializer().run()
#     # Coordinate the loading of image files.
#     coord = tf.train.Coordinator()
#     threads = tf.train.start_queue_runners(coord=coord)
#
#     # Get an image tensor and print its value.
#     image_tensor = sess.run([image])
#     #image_tensor_size=sess.run([image_size])
#     # image_size =tf.size(image_tensor)
#     print(image_tensor)
#     #print(image_tensor_size)
#     # Finish off the filename queue coordinator.
#     coord.request_stop()
#     coord.join(threads)


# import tensorflow as tf
# import os
# from PIL import Image
# # list files name
# files = os.listdir("../Dataset/2048-1356")
# files = ["..Dataset/2048-1356/" + s for s in files if os.path.splitext(s)[1] == '.png']
# files = [os.path.abspath(s) for s in files ]
# image_reader = tf.WholeFileReader()
# for s in files:
#     imageName, image_raw_data = image_reader.read(s)
#     # image_raw_data = tf.gfile.FastGFile(s, 'rb').read()
#
#     with tf.Session() as sess:
#         img_data = tf.image.decode_jpeg(image_raw_data)
#         print(tf.size(img_data))
#        # plt.imshow(img_data.eval())
#         #plt.show()


import numpy as np
from random import normalvariate, randint
import os
from PIL import Image
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 等比例地把图片较短的一边缩放到区间[256,480]
def rescale(image):
    w = image.size[0]
    h = image.size[1]
    sizeMax =1200
    sizeMin =640
    random_size = randint(sizeMin,sizeMax)
    if w < h:
        return image.resize((random_size,round(h/w * random_size)))
    else:
        return image.resize((round(w/h * random_size),random_size))

# 随机裁剪图片
def random_crop(image):
    w = image.size[0]
    h = image.size[1]
    size =256
    new_left = randint(0,w - size)
    new_upper = randint(0,h - size)
    return image.crop((new_left,new_upper,size+new_left,size+new_upper))

# 水平翻转图片
def horizontal_flip(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


files = os.listdir("../Dataset/2048-1356")
files = ["../Dataset/2048-1356/" + s for s in files if os.path.splitext(s)[1] == '.png']
# files = [os.path.abspath(s) for s in files ]

# for file in files:
#     image = Image.ANTIALIAS.open(file)
#     fig1=plt.figure()
#     plt.imshow(image)
#     # plt.show()
#     fig2 = plt.figure()
#     rescaled_image = rescale(image)
#     plt.imshow(rescaled_image)
#     # croped_image = random_crop(rescaled_image)
#     # plt.imshow(croped_image)
#     plt.show()
#     print

# 等比例压缩图片
def resizeImg(**args):
    args_key = {'ori_img': '', 'dst_img': '', 'dst_w': '', 'dst_h': '', 'save_q': 75}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]

    im = Image.open(arg['ori_img'])
    ori_w, ori_h = im.size
    widthRatio = heightRatio = None
    ratio = 1
    if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
        if arg['dst_w'] and ori_w > arg['dst_w']:
            widthRatio = float(arg['dst_w']) / ori_w  # 正确获取小数的方式
        if arg['dst_h'] and ori_h > arg['dst_h']:
            heightRatio = float(arg['dst_h']) / ori_h

        if widthRatio and heightRatio:
            if widthRatio < heightRatio:
                ratio = widthRatio
            else:
                ratio = heightRatio

        if widthRatio and not heightRatio:
            ratio = widthRatio
        if heightRatio and not widthRatio:
            ratio = heightRatio

        newWidth = int(ori_w * ratio)
        newHeight = int(ori_h * ratio)
    else:
        newWidth = ori_w
        newHeight = ori_h

    im.resize((newWidth, newHeight), Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])

    '''  
    image.ANTIALIAS还有如下值：  
    NEAREST: use nearest neighbour  
    BILINEAR: linear interpolation in a 2x2 environment  
    BICUBIC:cubic spline interpolation in a 4x4 environment  
    ANTIALIAS:best down-sizing filter  
    '''


# 裁剪压缩图片
def clipResizeImg(**args):
    args_key = {'ori_img': '', 'dst_img': '', 'dst_w': '', 'dst_h': '', 'save_q': 75}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]

    im = Image.open(arg['ori_img'])
    ori_w, ori_h = im.size

    dst_scale = float(arg['dst_h']) / arg['dst_w']  # 目标高宽比
    ori_scale = float(ori_h) / ori_w  # 原高宽比

    if ori_scale >= dst_scale:
        # 过高
        width = ori_w
        height = int(width * dst_scale)

        x = 0
        y = (ori_h - height) / 3

    else:
        # 过宽
        height = ori_h
        width = int(height * dst_scale)

        x = (ori_w - width) / 2
        y = 0

        # 裁剪
    box = (x, y, width + x, height + y)
    # 这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标
    # 所包围的图像，crop方法与php中的imagecopy方法大为不一样
    newIm = im.crop(box)
    im = None

    # 压缩
    ratio = float(arg['dst_w']) / width
    newWidth = int(width * ratio)
    newHeight = int(height * ratio)
    newIm.resize((newWidth, newHeight), Image.ANTIALIAS).save(arg['dst_img'], quality=arg['save_q'])


#保存的图片质量
save_q = 100
sizeMax = 1200
sizeMin = 640
#源图片
for ori_img in files:
    image = Image.open(ori_img)
    w = image.size[0]
    h = image.size[1]
    random_size = randint(sizeMin, sizeMax)
    # 目标图片大小
    if w < h:
        dst_w, dst_h = random_size, round(h / w * random_size)
        # return image.resize((random_size, round(h / w * random_size)))
    else:
        dst_w, dst_h = round(w / h * random_size), random_size
        # return image.resize((round(w / h * random_size), random_size))
#目标图片
    dst_img = ori_img.rstrip('.png') + '_clipresize.png'
#裁剪压缩
    # clipResizeImg(ori_img=ori_img,dst_img=dst_img,dst_w=dst_w,dst_h=dst_h,save_q = save_q)
#等比例压缩
    resizeImg(ori_img=ori_img,dst_img=dst_img,dst_w=dst_w,dst_h=dst_h,save_q=save_q)