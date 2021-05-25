import geojson
from geojson import FeatureCollection, Feature

from config import Config
from converter import load_converter


class GeoHistory:
    def __init__(self, converter_path):
        self.converter = load_converter(converter_path)
        self.features = FeatureCollection([])

    def add_points(self, frame_idx, bbox, ids=None, offset=(0, 0)):
        frame_pts = []
        user_ids = []

        for i, box in enumerate(bbox):
            x1, y1, x2, y2 = [int(i) for i in box]
            x1 += offset[0]
            x2 += offset[0]
            y1 += offset[1]
            y2 += offset[1]
            # Add bottom center of the square to frame points
            frame_pts.append([int((x1 + x2) / 2), y2])
            # Add user_id
            user_ids.append(int(ids[i]) if ids is not None else 0)

        # Convert video points to geo epsg4326 points
        geo_pts = self.converter.convert_frame_to_geo_point(frame_pts)

        # Put geo points in the collection
        for geo_pt, frame_pt, user_id in zip(geo_pts, frame_pts, user_ids):
            self.features.features.append(Feature(
                geometry=geo_pt,
                properties={'user_id': user_id,
                            'frame_id': frame_idx,
                            'frame_x': frame_pt[0],
                            'frame_y': frame_pt[1]}
            ))

    def save(self):
        # Save the collection
        # TODO: move at the end of the process
        with open(Config.history_geojson_path, 'w') as geojson_file:
            geojson.dump(self.features, geojson_file)
