import numpy as np
import os
outpath = './out/'
os.makedirs(outpath, exist_ok=True)

for num in range(2,10):
    for name in ['train_neg_closeby{}.vcf'.format(num),'train_pos_closeby{}.vcf'.format(num)]:
        data = np.loadtxt(name,delimiter='\t',dtype=str,)
        data[data=='na'] = 'nan'
        data[data=='Na'] = 'nan'
        data[data=='NaN'] = 'nan'
        data[data=='NA'] = 'nan'
        np.savetxt(outpath+name,data[:,5:],delimiter='\t',fmt='%s')



