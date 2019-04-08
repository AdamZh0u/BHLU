## use arcpy to subset the raster by mask(bh land shp)
import arcpy

arcpy.env.workspace = "F:/DataBase/Data/LC maps full 1992-2015 serie"
# raster data sets directory
data_list = arcpy.ListDatasets()
# except the last one
raster_list = data_list[:-1]
# in python2 ,there should have an u before the string to encoding.
# like u'ESACCI-LC-L4-LCCS-Map-300m-P1Y-1992-v2.0.7.tif'
print raster_list


# subset by the total shp
year = 1992
for raster in raster_list:
    #raster sybset by shp
    ra_SubBy_totalShp = arcpy.sa.ExtractByMask(raster, "F:/DataBase/Data/hotspots_2016_1/hotspots_2016_land.shp")
    #save raster
    ra_SubBy_totalShp.save("I:/Project/BHLU/Subset_total/totalSub_"+str(year))
    # procedure message
    print str(year)+" done"
    year += 1
