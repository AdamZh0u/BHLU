import time
import os
import pandas as pd

outDbase = "I:\Project\BHLU-1\scripts\caculate\Matrix_Excel\\"
writer=pd.ExcelWriter(outDbase+"ouput_92-15.xls")
for i in range(0,36):
    excel = outDbase+"Matrix_ID{}_92-02.xls".format(i)
    df=pd.read_excel(excel,index_col = "OID")
    df.rename(columns={'VALUE':'初期类型', 'VALUE_1':'转为末期裸地', 'VALUE_2':'转为末期生态',
                       'VALUE_6':'转为末期农田','VALUE_7':'转为末期城镇',}, inplace = True)
    dic ={1:"裸地",2:"生态",6:"农田",7:"城镇"}
    df=  df.replace(dic)
    df.to_excel(writer,sheet_name = "ID_{}".format(i))
    print(i)
writer.save()
writer.close()
