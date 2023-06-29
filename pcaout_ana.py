import pandas as pd

count = 1
rowlist = []
for i in range (0,11) :
    for j in range (i+1,11) :
        rowlist.append('d'+str(i)+str(j))


df = pd.DataFrame(columns = rowlist)

i = 0
with open (r'G:\data\MD\05162\metad\PCA\PCA','r') as pcafile:
    for line in pcafile.readlines() :
        filterline =list(filter(None,line.split(' ')))
        filterline[-1] = filterline[-1].rstrip('\n')
        while True :
            df.loc[i] = filterline[1:]
            i += 1
            print(df)
            break
 
df.to_csv('pcaout_handled.csv', index=False)