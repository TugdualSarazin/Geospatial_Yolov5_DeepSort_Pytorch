import cv2
import pyshine as ps

from config import Config
from converter import converter_from_ref
from ref_points import RefPoints, get_ref_pt_video_xy, ref_pt_name, set_ref_pt_video_xy

window_name = 'Select Points'
point_color = (255, 255, 255)


def draw_points(frame, geo_points):
    for geo_pt in geo_points.ref_points.features:
        xy = get_ref_pt_video_xy(geo_pt)
        if xy:
            x, y = xy
            cv2.circle(frame, (x, y), 3, point_color, -1)
            cv2.putText(img=frame, text=ref_pt_name(geo_pt), org=(x + 6, y - 8),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=.3, color=point_color, thickness=1)


def draw_text_to_do(frame, geo_points):
    geo_pt = geo_points.next_empty_point()
    text = "Finish ! Press enter to quite."
    if geo_pt:
        text = f'Place point: {ref_pt_name(geo_pt)}'
    height, width, _ = frame.shape

    ps.putBText(frame, text, text_offset_x=30, text_offset_y=int(height / 4), vspace=15, hspace=25, font_scale=2.0,
                background_RGB=(0, 250, 250), text_RGB=(255, 250, 250))


def select_points(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        init_frame, geo_points = params

        geo_pt = geo_points.next_empty_point()
        if geo_pt:
            # Save point
            set_ref_pt_video_xy(geo_pt, x, y)
            geo_points.save()

        else:
            print("No more point to set")

        draw_current_state(init_frame, geo_points)


def draw_current_state(init_frame, geo_points):
    frame = init_frame.copy()
    draw_points(frame, geo_points)
    draw_text_to_do(frame, geo_points)
    cv2.imshow(window_name, frame)


def main():
    geo_points = RefPoints(Config.refpoints_geojson_path)

    video = cv2.VideoCapture(Config.video_path)

    ret, init_frame = video.read()

    draw_current_state(init_frame, geo_points)
    cv2.setMouseCallback(window_name, select_points, [init_frame, geo_points])
    cv2.waitKey(0)
    # Save converter
    converter_from_ref(geo_points).save(Config.converter_path)

    # TODO: only here to test, must be deleted
    # converter = load_converter(Config.converter_path)
    # pts_frame = [[pt.properties['video_x'], pt.properties['video_y']] for pt in geo_points.ref_points.features]
    # pts_4326 = converter.convert_frame_to_geo_point(pts_frame)
    # features = [Feature(geometry=pt) for pt in pts_4326]
    # feature_collection = FeatureCollection(features)
    # with open('blabla.json', 'w') as geojson_file:
    #     geojson.dump(feature_collection, geojson_file)


if __name__ == '__main__':
    main()
