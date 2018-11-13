import os
import subprocess
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 


num_filters = 128  # default 128
# batchsize = 1
patchsize = 256  # default 128
data_glob = '../Dataset/train/crop/crop_batch1/*.png'
checkpoint_dir = 'train_crop1234'  # default train
last_step = 100  # defauilt 1000000
file_path = data_glob.rstrip('*.png').rstrip('/')
files = os.listdir(file_path)
batchsize = int(len(files)/4)  # default 8
# train command
train_command = 'python bls2017.py train --num_filters ' + str(num_filters)+ ' --batchsize '+str(batchsize) + ' --patchsize '\
                + str(patchsize) + ' -v --data_glob ' +str(data_glob) + ' --checkpoint_dir ' + str(checkpoint_dir)+' --last_step '+ str(last_step)

# compress command
compress_file_name = 'les-krivec-434_crop_1.png'
compress_command = 'python bls2017.py compress ' + str(compress_file_name) + ' compressed1.bin --num_filters ' + str(num_filters) + ' -v --checkpoint_dir ' + str(checkpoint_dir)

# decompress command
decompress_command = 'python bls2017.py decompress compressed1.bin decompressed1.png --num_filters ' + str(num_filters) + ' -v --checkpoint_dir ' + str(checkpoint_dir)


# train
# print(train_command)
# os.system(train_command)
# compress
print(compress_command)
os.system(compress_command)
# decompress
print(decompress_command)
os.system(decompress_command)

print('Training, Compressing and Decompressing is done!')

