import os
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
import glob
num_filters = 128  # default 128
# batchsize = 1
patchsize = 256  # default 128

checkpoint_dir = 'train_crop12345'  # default train
last_step = 200000  # defauilt 1000000
Lambda = 0.001
for j in range(8):
	for i in range(16):
		data_glob = '../Dataset/train/crop/crop_batch' + str(i)+'/*.png'
		file_path = data_glob.rstrip('*.png').rstrip('/')
		files = os.listdir(file_path)
		batchsize = int(len(files)/8)  # default 8
	# train command
		train_command = 'python bls2017.py train --num_filters ' + str(num_filters)+ ' --batchsize '+str(batchsize) + ' --patchsize '\
						+ str(patchsize) + ' -v --data_glob ' +str(data_glob) + ' --checkpoint_dir ' + str(checkpoint_dir)+' --last_step '+ str(last_step) +' --lambda '+ str(Lambda)

	# train
		print(train_command)
		os.system(train_command)
		#subprocess.call(train_command, shell=True)
		for eventspath in glob.iglob(os.path.join(checkpoint_dir,'*.MSI')):
			os.remove(eventspath)
		print('Training for batch ' +str(i)+ ' for the ' +str(j)+ ' round is done' )

print('Training is done!')
print('Training is done!')
print('Training is done!')

