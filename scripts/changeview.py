import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "I:/Project/BHLU"
raster92 = "I:\Project\BHLU\Subset_total\IMG/totalsub_1992.img"
raster05 = "I:\Project\BHLU\Subset_total\IMG/totalsub_2015.img"

Table = "reclass"
##
outReclass92 = ReclassByTable(raster92,Table,"FROM","TO","OUT","NODATA")
outReclass92.save("I:/Project/BHLU/change/class92.img")
##
outReclass05 = ReclassByTable(raster05,Table,"FROM","TO","OUT","NODATA")
outReclass05.save("I:/Project/BHLU/change/class15.img")
##
outCon = Con(outReclass05 - outReclass92==0 , outReclass92 , outReclass05 - outReclass92 )
#
outCon.save("I:/Project/BHLU/change/com.img")
