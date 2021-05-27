import numpy as np
import os
outpath = './out/'
os.makedirs(outpath, exist_ok=True)

for num in range(6,7):
    for name in ['test2_neg_closeby{}_process_cs_quchong_closeby_match_features.txt'.format(num),'test2_pos_closeby{}_process_cs_quchong_closeby_match_features.txt'.format(num)]:
        data = np.loadtxt(name,delimiter='\t',dtype=str)
        data[data=='na'] = 'nan'
        data[data=='Na'] = 'nan'
        data[data=='NaN'] = 'nan'
        data[data=='NA'] = 'nan'
        np.savetxt(outpath+name,data[:,5:],delimiter='\t',fmt='%s')



