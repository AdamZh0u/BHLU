import arcpy

arcpy.env.workspace = "I:/Project/BHLU/Subset_total"
datalist = arcpy.ListDatasets()
raster_list = datalist[:]

i = 35
raster_92 = raster_list[0]
raster_02 = raster_list[9]
raster_15 = raster_list[-1]

outDbase = "I:/Project/BHLU/Tabulate/"
outExcel = "I:/Project/BHLU/Tabulate/"
arcpy.gp.TabulateArea_sa(raster_92, "VALUE", raster_02, "VALUE", outDbase+"ma_92-02.dbf")
arcpy.gp.TabulateArea_sa(raster_02, "VALUE", raster_15, "VALUE", outDbase+"ma_02-15.dbf")
arcpy.TableToExcel_conversion(outDbase+"ma_92-02.dbf", outExcel+"ma_92-02.xls", "NAME", "CODE")
arcpy.TableToExcel_conversion(outDbase+"ma_02-15.dbf", outExcel+"ma_02-15.xls", "NAME", "CODE")