import os
import numpy as np

result_dir = 'result-'
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

ssim_fname ='Output_SSIM.txt'
with open(ssim_fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [float(x.strip()) for x in content]
average_msssim = np.mean(content)
print('average MS-SSIM: {:0.4}'.format(average_msssim))

mse_fname = 'Output_MSE.txt'
with open(mse_fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [float(x.strip()) for x in content]
average_mse = np.mean(content)
print('average MSE: {:0.4}'.format(average_mse))

psnr_fname = 'Output_PSNR.txt'
with open(psnr_fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [float(x.strip()) for x in content]
average_psnr = np.mean(content)
print('average PSNR: {:0.4}'.format(average_psnr))

with open('Output_RESULT.txt', 'a+') as text_file:
    text_file.write('average MS-SSIM: {:0.4}\n'.format(average_msssim))
    text_file.write('average MSE: {:0.4}\n'.format(average_mse))
    text_file.write('average PSNR: {:0.4}\n'.format(average_psnr))

os.rename("Output_RESULT.txt", result_dir+"/Output_RESULT.txt")
os.rename("Output_PSNR.txt", result_dir+"/Output_PSNR.txt")
os.rename("Output_MSE.txt", result_dir+"/Output_MSE.txt")
os.rename("Output_SSIM.txt", result_dir+"/Output_SSIM.txt")