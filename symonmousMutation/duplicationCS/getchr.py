import numpy as np
import os
path = './chr/'

os.makedirs(path, exist_ok=True)
for num in range(6,7):
    for name in ['test2_neg_closeby{}_process_cs_quchong_closeby_match_features'.format(num),'test2_pos_closeby{}_process_cs_quchong_closeby_match_features'.format(num)]:
        data = np.loadtxt(name+ '.txt', delimiter='\t', dtype=str)[0:,0:5]
        np.savetxt(path + name+'.txt', data, delimiter='\t', fmt='%s')