import arcpy
import time
import os
from arcpy import env
from arcpy.sa import *
arcpy.env.workspace = "I:/Project/BHLU/Projection"
for i in range(24,25):
    #os.makedirs("I:/Project/BHLU/Projection/FID_{}".format(i))
    for year in range(1993,2016):
        input_raster = "I:/Project/BHLU/Subset_part/FID_{}/year_{}.img".format(
            i,year)
        output_raster = "I:/Project/BHLU/Projection/FID_{}/year_{}.img".format(
            i,year)
        arcpy.ProjectRaster_management(
            input_raster,output_raster,"Cylindrical Equal Area (world).prj")
        print i,year
