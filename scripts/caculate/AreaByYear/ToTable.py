import json
import pandas as pd
import os

file = open('I:\Project\BHLU-1\scripts\caculate\AreaByYear\sample.txt', 'r') 
js = file.read()
file.close() 

dic = eval(js)

outDbase = "I:\Project\BHLU-1\scripts\caculate\\"
writer=pd.ExcelWriter(outDbase+"ouput_92-15.xls")
for i in dic:
    df=pd.DataFrame([])
    for year in dic[i]:
        for n in dic[i][year]:
            df.loc[n,year]=dic[i][year][n]
    df.to_excel(writer,sheet_name = "ID_{}".format(i))
writer.save()
writer.close()