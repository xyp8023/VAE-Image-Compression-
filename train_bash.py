import os
import subprocess
num_filters = 256  # default 128
# batchsize = 1
patchsize = 256  # default 128
data_glob = '../Dataset/2048-1356/crop/*.png'
checkpoint_dir = 'train_crop'  # default train
last_step = 10000  # defauilt 1000000
file_path = data_glob.rstrip('*.png').rstrip('/')
files = os.listdir(file_path)
batchsize = len(files)  # default 8
# train command
train_command = 'python bls2017.py train --num_filters ' + str(num_filters)+ ' --batchsize '+str(batchsize) + ' --patchsize '\
                + str(patchsize) + ' -v --data_glob ' +str(data_glob) + ' --checkpoint_dir ' + str(checkpoint_dir)+' --last_step '+ str(last_step)

# compress command
compress_file_name = 'fineas-anton-143501_crop_5.png'
compress_command = 'python bls2017.py compress ' + str(compress_file_name) + ' compressed.bin --num_filters ' + str(num_filters) + ' -v --checkpoint_dir ' + str(checkpoint_dir)

# decompress command
decompress_command = 'python bls2017.py decompress compressed.bin decompressed.png --num_filters ' + str(num_filters) + ' -v --checkpoint_dir ' + str(checkpoint_dir)


# train
print(train_command)
os.system(train_command)
# compress
print(compress_command)
os.system(compress_command)
# decompress
print(compress_command)
os.system(decompress_command)

print('Training, Compressing and Decompressing is done!')

