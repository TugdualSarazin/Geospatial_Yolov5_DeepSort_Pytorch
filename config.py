class ConfigPolice:
    video_path = 'data/bcn_jaume/jaume_police.mp4'
    refpoints_geojson_path = 'data/bcn_jaume/jaume_police_refpoints.geojson'
    converter_path = 'data/bcn_jaume/jaume_police_converter'
    history_geojson_path = 'data/bcn_jaume/jaume_police_geohistory.geojson'
    yolo_thres = 0.10

class ConfigJaume5:
    video_path = 'data/bcn_jaume/jaume_5_10am.MOV'
    refpoints_geojson_path = 'data/bcn_jaume/jaume_5_10am_refpoints.geojson'
    converter_path = 'data/bcn_jaume/jaume_5_10am_converter'
    history_geojson_path = 'data/bcn_jaume/jaume_5_10am_geohistory.geojson'
    yolo_thres = 0.10


class ConfigRoma:
    video_path = 'data/roma/placa.mp4'
    refpoints_geojson_path = 'data/roma/placa_refpoints.geojson'
    converter_path = 'data/roma/placa_converter'
    history_geojson_path = 'data/roma/placa_geohistory.geojson'
    yolo_thres = 0.10


class ConfigRomaTrimmed:
    video_path = 'data/roma/placa_trimmed.mp4'
    refpoints_geojson_path = 'data/roma/placa_refpoints.geojson'
    converter_path = 'data/roma/placa_converter'
    history_geojson_path = 'data/roma/placa_trimmed_geohistory.geojson'
    yolo_thres = 0.10

class Config(ConfigRomaTrimmed):
    def __init__(self):
        print(f'Config : {self.video_path}')
