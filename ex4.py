from osgeo import ogr

folderPath = "Тестовий_файл_фігури"
shapefile = ogr.Open(folderPath+"/shapefile.shp")
layer = shapefile.GetLayer(0)
for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    id_n = feature.GetField('ID')
    name = feature.GetField("NAME")
    geometry = feature.GetGeometryRef()
    print(i, name, geometry.GetX(), geometry.GetY())
shapefile = None
