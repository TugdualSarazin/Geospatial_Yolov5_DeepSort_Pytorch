import geojson
from pyproj import Transformer
import numpy as np


class RefPoints:
    def __init__(self, filename):
        self.filename = filename

        with open(self.filename) as geojson_file:
            self.ref_points = geojson.load(geojson_file)

        self.remove_video_data()
        self.fill_epsg3857()
        self.save()

    def remove_video_data(self):
        for pt in self.ref_points.features:
            if pt.properties.get('video_x'):
                del pt.properties['video_x']
            if pt.properties.get('video_y'):
                del pt.properties['video_y']

    def fill_epsg3857(self):
        # Init crs transformer
        geo_crs = self.ref_points.crs['properties']['name']
        transformer = Transformer.from_crs(geo_crs, "epsg:3857")

        for pt in self.ref_points.features:
            xy_src = pt.geometry.coordinates
            xy_dst = transformer.transform(xy_src[0], xy_src[1])
            pt.properties['3857_x'] = xy_dst[0]
            pt.properties['3857_y'] = xy_dst[1]

    def save(self):
        with open(self.filename, 'w') as geojson_file:
            geojson.dump(self.ref_points, geojson_file, sort_keys=True)

    def next_empty_point(self):
        return next(
            (pt for pt in self.ref_points.features if get_ref_pt_video_xy(pt) is None),
            None
        )

    def video_xy_matrix4(self):
        pts = self.ref_points.features[:4]
        xys = [[pt.properties['video_x'], pt.properties['video_y']] for pt in pts]
        return np.array(xys, dtype=np.float32)

    def csr3857_xy_matrix4(self):
        pts = self.ref_points.features[:4]
        xys = [[pt.properties['3857_x'], pt.properties['3857_y']] for pt in pts]
        return np.array(xys, dtype=np.float32)


def ref_pt_name(pt):
    name = pt.properties.get('name')
    if name:
        return name
    return str(pt.geometry.coordinates)


def set_ref_pt_video_xy(pt, x, y):
    pt.properties['video_x'] = x
    pt.properties['video_y'] = y


def get_ref_pt_video_xy(pt):
    x = pt.properties.get('video_x')
    y = pt.properties.get('video_y')
    if x is None or y is None:
        return None
    return x, y
