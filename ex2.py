from osgeo import gdal
import struct

filepath = "Зразок растра.tiff"
srcFile = gdal.Open(filepath)
band = srcFile.GetRasterBand(1)

fmt = "<" + ("h" * band.XSize)  # Довжина рядка каналу = 180
for row in range(band.YSize):
    scanline = band.ReadRaster(0, row, band.XSize, 1, band.XSize, 1, band.DataType)
    row_data = struct.unpack(fmt, scanline)
    print(row_data)
values = band.ReadAsArray()
for row in range(band.XSize - 180):  # відлік з нуля
    print(values[row])
