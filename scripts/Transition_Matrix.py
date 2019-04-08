# Import arcpy module
import arcpy

#for i in range(0, 35, 1):
i = 35
raster_95 = r'I:\BHLU_2\T95_15\1' + '\\' + str(i)
raster_15 = r'I:\BHLU_2\T95_15\2' + '\\' + str(i)
outDbase = r'I:\BHLU_2\T95_15\3' + '\\dbase' + str(i)
outExcel = r'I:\BHLU_2\T95_15\4' + '\\date' + str(i) + '.xls'
arcpy.gp.TabulateArea_sa(raster_95, "VALUE", raster_15, "VALUE", outDbase, ".002777777778")
arcpy.TableToExcel_conversion(outDbase, outExcel, "NAME", "CODE")

