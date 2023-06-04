import pandas as pd
import matplotlib.pyplot as plt
import palettable
import seaborn as sns



# 使用heatmap函数绘制热力图

df = pd.read_csv(r'C:\Users\Administrator\Desktop\pytry\handled_rosetta_ddg.csv')
listname = df.iloc[:,0].tolist()
dfnew = df.iloc[:,1:21]
dfmin = dfnew.min().min()
print(dfmin)
print(listname)
df_transposed = dfnew.transpose()
print(df_transposed)
sns.heatmap(df_transposed, vmax=40,vmin = dfmin ,xticklabels = listname)

# 显示热力图
plt.xlabel('The residues within 8 Ångström of ligands')
plt.ylabel('Saturated mutation residues')
plt.title('Heatmap of Saturated Mutations')

plt.show()


#plt.figure(dpi=120)
#sns.heatmap(data=df.columns[1:],#矩阵数据集，数据的index和columns分别为heatmap的y轴方向和x轴方向标签                        )
#plt.title('所有参数默认')

#headline = df.iloc[1]
#listline = df.columns[0]
#print(headline)
#print(listline)
