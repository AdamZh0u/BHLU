import arcpy

arcpy.env.workspace = r"I:\BHLU_2\test.mdb"

feature_list = arcpy.ListDatasets()
print feature_list

remap = arcpy.sa.RemapRange([[1, 49, 1], [50, 109, 2], [110, 119, 3], [120, 129, 6], [130, 139, 3],
                             [140, 159, 7], [160, 179, 2], [180, 189, 4], [190, 199, 5], [200, 209, 8], [210, 219, 9],
                             [220, 256, 10]])

year = 1995
for feature in feature_list:
    outExtractByMask = arcpy.sa.ExtractByMask(feature, r"I:\BHLU_2\hotspots_2016\hotspots_2016_land.shp")
    outExtractByMask.save("extract_"+year)
    outReclass = arcpy.sa.Reclassify(outExtractByMask, "VALUE", remap)
    outReclass.save("Reclass_"+year)
    year += 1

