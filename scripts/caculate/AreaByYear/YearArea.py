import arcpy
import time
d = {}
for i in range(0,36):
    d[i]={}
    for year in range(1992,2016):
        dic ={}
        input_raster = "I:/Project/BHLU/Reclass/FID_{}/year_{}.img".format(
            i,year)
        GetSizex = arcpy.GetRasterProperties_management(input_raster, "CELLSIZEX")
        GetSizey = arcpy.GetRasterProperties_management(input_raster, "CELLSIZEY")
        sizex = float(GetSizex.getOutput(0))
        sizey = float(GetSizey.getOutput(0))
        fields = ["Value","Count"]
        with arcpy.da.SearchCursor(input_raster, fields) as cursor:
            for row in cursor:
                dic[row[0]]=row[1]*sizex*sizey
        d[i][year]=dic
        print i,year
f = open('I:\Project\BHLU-1\scripts\caculate\AreaByYear\sample.txt', 'w')
f.write(str(d))
f.close()
print time.asctime( time.localtime(time.time()) )
