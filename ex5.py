import pyproj

UTM_X = 565718.523517
UTM_Y = 3980998.9244
srcProj = pyproj.Proj(proj="utm", zone="17", ellps="clrk66", units="m")
dstProj = pyproj.Proj(proj='longlat', ellps='WGS84', datum='WGS84')
long, lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)
print("Координата 17-ї зони UTM" + "({:.4f}, {:.4f}) ".format(UTM_X, UTM_Y) + "=({:.4f}, {:.4f})".format(long, lat))

angle = 315  # 315 градусів = північний схід, distance = 10000
geod = pyproj.Geod(ellps='clrk66')
long2, lat2, invAngle = geod.fwd(long, lat, angle, 10000)
print("Координата {:.4f}, {:.4f}".format(lat2, long2) + " знаходиться за 10 км на північний схід від " + "{:.4f}, {:.4f}".format(lat, long))

