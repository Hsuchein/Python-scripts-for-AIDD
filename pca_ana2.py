import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 读取CSV文件
data = pd.read_csv(r'G:\data\MD\05162\metad\PCA\pcaout_handled1.csv')

# 提取特征数据（假设数据的列从0到n-1，最后一列为标签）
X = data.iloc[:, :].values
XT = X.T
# 数据标准化
scaler = StandardScaler()

XT_scaled = scaler.fit_transform(XT)

print(XT_scaled.shape[0])
print(XT_scaled.shape[1])
'''
    if i == 0 :
        transformed_X = np.array(temp_columns_scaled)
        print(len(temp_columns_scaled))
    else :
        transformed_X = np.insert(transformed_X, i, temp_columns_scaled, axis=0)
    if i % 100 == 0:
        print(i)   
    i += 1
'''
    
# 执行PCA分析
pca1 = PCA()
X_pca = pca1.fit_transform(XT_scaled)
pca2 = PCA()
X_pca = pca2.fit_transform(XT)

pc1 = pca1.components_[0]
pc2 = pca1.components_[1]

pc3 = pca2.components_[0]
pc4 = pca2.components_[1]



# 输出PCA结果
i = 0
with open(r'G:\data\MD\05162\metad\PCA\pc.xvg','w') as output:
    while i < len(pc1)  :
        output.write('  ' + str(pc1[i])+'  '+str(pc2[i])+'\n')
        i +=1

i = 0
with open(r'G:\data\MD\05162\metad\PCA\pc_notscaled.xvg','w') as output:
    while i < len(pc1)  :
        output.write('  ' + str(pc3[i])+'  '+str(pc4[i])+'\n')
        i +=1

