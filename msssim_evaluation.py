# -*- coding: utf-8 -*-
# python msssim.py --original_image=original.png --compared_image=distorted.png

# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
#
# import argparse
#
# import numpy as np
# import tensorflow as tf
# import tensorflow_compression as tfc
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import subprocess
file_path = "../Dataset/test/resize"
files = os.listdir(file_path)
files = [file_path + '/' + s for s in files if os.path.splitext(s)[1] == '.png']
num_filters = 128  # default 128
checkpoint_dir = 'train_crop1234'  # default train
compress_file_path =file_path + '/compress/'
decompress_file_path =file_path + '/decompress/'

for ori_img in files:
    # compress
    compress_file_name = ori_img.strip(file_path+'/')
    compressed_file_name = compress_file_path+'compressed_' + compress_file_name.strip('.png') + '.bin'
    compress_command = 'python bls2017.py compress ' + str(ori_img) + ' ' + str(
        compressed_file_name) + ' --num_filters ' + str(num_filters) + ' -v --checkpoint_dir ' + str(checkpoint_dir)
    print(compress_command)
    subprocess.call(compress_command)

    # decompress
    decompressed_file_name = decompress_file_path+'decompressed_' + compress_file_name
    decompress_command = 'python bls2017.py decompress ' + str(compressed_file_name) + ' ' + str(
        decompressed_file_name) + ' --num_filters ' + str(num_filters) + ' -v --checkpoint_dir ' + str(checkpoint_dir)
    print(decompress_command)
    subprocess.call(decompress_command)

    # EVALUATE
    msssim_command = 'python msssim.py --original_image='+ori_img+' --compared_image='+decompressed_file_name
    msssim_command1 = 'msssim.py --original_image=' + ori_img + ' --compared_image=' + decompressed_file_name

    print(msssim_command)
    subprocess.call(msssim_command)
    #msssim=subprocess.check_call(msssim_command)
print('Test Image Preprocessing is done')