import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import t

# set DOF & alpha for t distribution
degrees_of_freedom = 19 #except one WT residue, we exclude one largest ddG(usually caused by P mutation)
t_alpha = 0.05
# set alpha for BHC
BHC_alpha = 0.065

ddg = []
total = []
linestore = [0]
mut_site = [0]
temp_line= []

AAname = ['E','D','H','R','K','S','T','Q','N','M','C','F','Y','W','G','A','P','V','L','I']

def t_test_forp(avg , std) :
    t_value = np.sqrt(19)*avg / std
    t_value_ref = t.ppf(1 - t_alpha/2, degrees_of_freedom)
    #print('t value is :',t_value)
    #print('t ref value if :',t_value_ref)
    p_value = 2 * (1 - t.cdf(abs(t_value), degrees_of_freedom))
    return p_value

#data read
with open(r'C:\Users\Administrator\Desktop\pytry\ddg_all.out' ,'r') as out :
    for line in out.readlines() :
        i=0                                  # if your result doesnt contain same redundant data , you can just turn off the same-data-detection
        same_flag = True                     #
        for i in range(len(linestore)):      #
            if line[0:11] == linestore[i] :  # 0:11 contains str--'ddG: K84Y' to recoginize residue only not the value
                same_flag=False              #
                break                        #
            i+=1                             #
        if same_flag :                       #
            linestore.append(line[0:11])
            if len(line.split(' ')) > 1 :
                temp_line = list(filter(None,line.split(' ')))
                ddg_str = temp_line[1]
                total_str = temp_line[2]
                ddg.append(ddg_str)
                total.append(total_str)

print(ddg[1:])
print(total[1:])

#data tranfered by pandas

#df initiate
df = pd.DataFrame(columns= AAname,index = [ddg[1][0:-1]])

j = 1
dfline = 0
i = 1
#while j < len(linestore) - 2 : # !!! first line is descriptor line, second line is '/n' !!! So in your file must contain '/n' !!!
while i < len(total) :
    df.loc[ddg[j][0:-1],ddg[i][-1]] = total[i]

    if i % 19 == 0:
        row_values = df.iloc[dfline].astype(float).tolist()  # 将一行转换为列表
        row_values.remove(max(row_values))  # 创建不包含最大值的列表
        average_without_max = pd.Series(row_values).mean()  # 计算平均值
        std_without_max = pd.Series(row_values).std()  # 计算标准差

        df.loc[ddg[j][0:-1],'Averages'] = average_without_max
        df.loc[ddg[j][0:-1],'Var'] = std_without_max*std_without_max
        df.loc[ddg[j][0:-1],'Std'] = std_without_max
        df.loc[ddg[j][0:-1],'p_value'] =t_test_forp(df.loc[ddg[j][0:-1],'Averages'],df.loc[ddg[j][0:-1],'Std'])
        j+=19
        dfline += 1
        #print(df)
    i+=1
#print(df) 

sort_by_p_out = df.astype(float).sort_values('p_value',ascending = True) #sort df by p_value for BHC

#print(sort_by_p_out)


original_file_path = "handled_rosetta_ddg.csv"
df.to_csv(original_file_path,sep=',',index=True)
#with open(r'.\output','w') as outputfile:
#    i=2
#    for i in range(len(ddg)) :
#        print(ddg[i],"  ",total[i],file=outputfile)

BHC_file_path = 'BHC_rosetta_ddg.csv'
sort_by_p_out.to_csv(BHC_file_path,sep=',',index=True)

sort_by_p_in= pd.read_csv(r'C:\Users\Administrator\Desktop\pytry\BHC_rosetta_ddg.csv')

print(sort_by_p_in)

N = df.shape[0] #number of rows in df
BH_flag = True
k = 1
while BH_flag : 
    if sort_by_p_in.loc[k,'p_value']*N/k > BHC_alpha:
        print('k value is:',k,'  p_value is:',sort_by_p_in.loc[k,'p_value'])
        BH_flag = False
        break
    k += 1
print('BE CAREFUL! THE INDEX FROM 0 TO ',k-1," IS THE DATA WE NEED")