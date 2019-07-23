import time
import os

yearlist = [1992,2015]
lef = ", x, 999, x, x, 1, x, IDF_EIMG\n"

fo = open("I:\Project\BHLU-1\scripts\Caculate_Frag\Batch/batch.txt", "w")
for i in range(0,36):
    for year in yearlist:
        input_raster = "I:/Project/BHLU/ReclassTo3/FID_{}/year_{}.img".format(
            i,year)
        text = input_raster+lef
        fo.write(text)
        print i
fo.close()