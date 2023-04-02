from osgeo import gdal
from osgeo import osr
import random
import struct
import numpy

import os

filepath = "Зразок растра.tiff"
if os.path.exists(filepath):
    os.remove(filepath)
    print("Файл видалено")
else:
    print("Файлу не виявлено")

driver = gdal.GetDriverByName("GTIFF")
dstFile = driver.Create(filepath, 360, 180, 1, gdal.GDT_Int16)

spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS("WGS84")
dstFile.SetProjection(spatialReference.ExportToWkt())

originX = -180
originY = 90
cellWidth = 1.0
cellHeight = 1.0
dstFile.SetGeoTransform([originX, cellWidth, 0, originY, 0, -cellHeight])

band = dstFile.GetRasterBand(1)

values = []
for row in range(180):
    row_data = []
    for col in range(360):
        row_data.append(random.randint(1, 100))
    values.append(row_data)

fmt = "<" + ("h" * band.XSize)
for row in range(180):
    scanline = struct.pack(fmt, * values[row])
    band.WriteRaster(0, row, 360, 1, scanline)

array = numpy.array(values, dtype=numpy.int16)
band.WriteArray(array)
