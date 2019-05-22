
import arcpy
import time
import os
from arcpy import env
from arcpy.sa import *

env.workspace = "I:\Project\BHLU\Reclass"
Table = "reclass"

for i in range(0,36):
    os.makedirs("I:/Project/BHLU/Reclass/FID_{}".format(i))
    for year in range(1992,2016):
        input_raster = "I:/Project/BHLU/Projection/FID_{}/year_{}.img".format(
            i,year)
        outReclass = ReclassByTable(input_raster,Table,"FROM","TO","OUT","NODATA")
        output_path = "I:/Project/BHLU/Reclass/FID_{}/year_{}.img".format(
            i,year)
        outReclass.save(output_path)
        print i,year
