# PredCSM
#### 目录：  
- 背景
- 安装 
- 使用
### 背景
近些年来提出了一些可以用于癌症驱动突变识别的工具，但是至今还没有可以用于预测癌症驱动同义突变的特异性工具。鉴于此，我们开发了PredCSM工具（Predictor for cancer driver synonymous mutations)，用于识别体细胞癌症驱动同义突变。
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
validScore6.txt：各个模型在突变频次为6的训练集上十折交叉验证结果
