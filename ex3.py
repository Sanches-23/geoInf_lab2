import os.path
import random
import shutil

from osgeo import ogr, osr

folderPath = "Тестовий_файл_фігури"
if os.path.exists(folderPath):
    shutil.rmtree(folderPath)
    print("Файл видалено")
else:
    print("Файлу не виявлено")

os.mkdir(folderPath)

driver = ogr.GetDriverByName("ESRI Shapefile")
path = os.path.join(folderPath, "shapefile.shp")
datasource = driver.CreateDataSource(path)

spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS('WGS84')

layer = datasource.CreateLayer("layer", spatialReference)

field = ogr.FieldDefn("ID", ogr.OFTInteger)
field.SetWidth(4)
layer.CreateField(field)

field = ogr.FieldDefn("NAME", ogr.OFTString)
field.SetWidth(20)
layer.CreateField(field)

for i in range(100):
    id_n = 1000 + i
    lat = random.uniform(-90, +90)
    long = random.uniform(-180, +180)
    name = "point-{}".format(i)
    wkt = "POINT({} {})".format(long, lat)
    geometry = ogr.CreateGeometryFromWkt(wkt)
    feature = ogr.Feature(layer.GetLayerDefn())
    feature.SetGeometry(geometry)  # задати геометрію об'єкта
    feature.SetField("ID", id_n)  # встановити значення його атрибутів
    feature.SetField("NAME", name)
    layer.CreateFeature(feature)
    feature.Destroy()  # знищити об'єкт, звільнивши ресурси

datasource.Destroy()  # знищити джерело даних, звільнивши ресурси
