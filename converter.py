import cv2
import numpy as np
from geojson import Point
from pyproj import Transformer


class Converter:
    epsg3857_to_epsg4326 = Transformer.from_crs("epsg:3857", "epsg:4326")

    def __init__(self, convert_matrix):
        self.convert_matrix = convert_matrix

    def convert_frame_to_geo_point(self, pts_frame):
        pts_frame_xy = np.array([pts_frame], dtype=np.float32)
        # Project to 3857
        pts_3857 = cv2.perspectiveTransform(pts_frame_xy, self.convert_matrix)
        # Project to 4326 as geo point
        pts_4326 = []
        for pt4326 in self.epsg3857_to_epsg4326.itransform(pts_3857[0]):
            pts_4326.append(Point((pt4326[1], pt4326[0])))
        return pts_4326

    def save(self, path):
        np.save(path, self.convert_matrix)


def converter_from_ref(ref_points):
    matrix_video = ref_points.video_xy_matrix4()
    matrix_3857 = ref_points.csr3857_xy_matrix4()

    convert_matrix, status = cv2.findHomography(matrix_video, matrix_3857)

    return Converter(convert_matrix)


def load_converter(path):
    convert_matrix = np.load(path + '.npy')
    return Converter(convert_matrix)
