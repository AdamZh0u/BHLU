import arcpy
import time
import os
from arcpy import env
from arcpy.sa import *
outDbase = "I:\Project\BHLU-1\scripts\caculate\Matrix_Excel\\"
for i in range(0,36):
    raster92 = "I:/Project/BHLU/Reclass/FID_{}/year_{}.img".format(
                i,1992)
    raster15 = "I:/Project/BHLU/Reclass/FID_{}/year_{}.img".format(
                i,2015)
    arcpy.gp.TabulateArea_sa(raster92, "VALUE", raster15, "VALUE", outDbase+"Matrix_ID{}_92-02.dbf".format(i))
    arcpy.TableToExcel_conversion(outDbase+"Matrix_ID{}_92-02.dbf".format(i), outDbase+"Matrix_ID{}_92-02.xls".format(i), "NAME", "CODE")
    print i

