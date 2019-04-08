import arcpy
import time
import os

arcpy.env.workspace = "I:/Project/BHLU/Subset_total"
clip_feature = 'F:/DataBase/Data/hotspots_2016_1/hotspots_2016_land.shp'
datalist = arcpy.ListDatasets()
raster_list = datalist[:]

outworkspace = 'I:/Project/BHLU/Subset_part'
i = 1992
# create floders otherwisw the arcpy.save will raise an str() exception error
for x in range(0,36):
    os.makedirs("I:/Project/BHLU/Subset_part/FID_{}".format(x))

for raster in raster_list:
    for row in arcpy.SearchCursor(clip_feature):
        mask = row.getValue('Shape')
        outPath = "I:/Project/BHLU/Subset_part/FID_{}/year_{}.img".format(row.getValue("FID"),i)#
        outExtractByMask = arcpy.sa.ExtractByMask(raster, mask)
        outExtractByMask.save(outPath)
        print("{}   {}   {}".format(row.getValue("FID"),i,time.ctime()))
    i+=1

# to do list : error and re begin
