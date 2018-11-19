import os
import numpy as np
fname = 'Output.txt'
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [float(x.strip()) for x in content]
average_msssim = np.mean(content)
print(average_msssim)