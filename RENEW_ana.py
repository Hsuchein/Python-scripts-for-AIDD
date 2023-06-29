import pandas as pd
count = 1
with open(r'G:\data\MD\05162\metad\RENEW_new','w') as outfile:
    with open(r'G:\data\MD\05162\metad\RENEW','r') as infile:
        for line in infile.readlines() :
            templine = list(filter(None,line.split(' ')))
            float_templine = [float(x) for x in templine]
            if float_templine[1] < 1.0 and float_templine[2] < 1.0 :
                outfile.write(templine[1] + ' ' + templine[2] + ' ' + templine[3])
            count += 1
            if count % 100 == 0:
                print(count)
                
