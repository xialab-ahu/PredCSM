# PredCSM
#### 目录：  
- 背景
- 安装 
- 使用
### 背景
基于癌症基因组测序数据识别癌症驱动突变，已成为精准医学领域的重要研究方向。虽然近些年提出了一些可以用于识别癌症驱动突变的工具，但是至今无用于预测癌症驱动同义突变的特异性工具。鉴于此，我们开发了PredCSM工具（Predictor for Cancer Driver Synonymous Mutations)，这是一个针对体细胞癌症驱动同义突变的专属预测工具。
### 环境要求
Python >= 3.6  
其他的环境安装：  
cd symonmousMutation  
pip install -r requirement.txt
### 使用
cd code  
python trainRF.py
### 输出文件
test1Score.txt：独立测试集1上的各个模型结果  
test2Score.txt：独立测试集2上的各个模型结果  
validScore6.txt：各个分类器在突变频次为6的训练集上十折交叉验证结果
