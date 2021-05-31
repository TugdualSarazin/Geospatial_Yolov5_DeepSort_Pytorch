class ConfigAdriPolice:
    video_path = 'data/bcn_jaume/jaume_adri/police_adri_01.mp4'
    video_save_path = 'data/bcn_jaume/jaume_adri/police_adri_01_analysis.mp4'
    refpoints_geojson_path = 'data/bcn_jaume/jaume_adri/police_adri_01_refpoints.geojson'
    converter_path = 'data/bcn_jaume/jaume_adri/police_adri_01_converter'
    history_geojson_path = 'data/bcn_jaume/jaume_adri/police_adri_01_geohistory.geojson'
    frame_rate = 10
    yolo_thres = 0.10

class ConfigAdriPolice20(ConfigAdriPolice):
    video_save_path = 'data/bcn_jaume/jaume_adri/police_adri_01_analysis_20.mp4'
    frame_rate = 20

class ConfigPolice:
    video_path = 'data/bcn_jaume/jaume_police.mp4'
    video_save_path = 'data/bcn_jaume/jaume_police_analysis.mp4'
    refpoints_geojson_path = 'data/bcn_jaume/jaume_police_refpoints.geojson'
    converter_path = 'data/bcn_jaume/jaume_police_converter'
    history_geojson_path = 'data/bcn_jaume/jaume_police_geohistory.geojson'
    frame_rate = 1
    yolo_thres = 0.10


class ConfigPolice10(ConfigPolice):
    video_save_path = 'data/bcn_jaume/jaume_police_analysis_10.mp4'
    history_geojson_path = 'data/bcn_jaume/jaume_police_geohistory_10.geojson'
    frame_rate = 10
    yolo_thres = 0.10


class ConfigJaume5:
    video_path = 'data/bcn_jaume/jaume_5_10am.MOV'
    video_save_path = 'data/bcn_jaume/jaume_5_10am_analysis.MOV'
    refpoints_geojson_path = 'data/bcn_jaume/jaume_5_10am_refpoints.geojson'
    converter_path = 'data/bcn_jaume/jaume_5_10am_converter'
    history_geojson_path = 'data/bcn_jaume/jaume_5_10am_geohistory.geojson'
    frame_rate = 10
    yolo_thres = 0.10


class ConfigAdriMVI_9512:
    video_path = 'data/bcn_jaume/jaume_adri/MVI_9512.MOV'
    video_save_path = 'data/bcn_jaume/jaume_adri/MVI_9512_analysis.MOV'
    refpoints_geojson_path = 'data/bcn_jaume/jaume_adri/MVI_9512_refpoints.geojson'
    converter_path = 'data/bcn_jaume/jaume_adri/MVI_9512_converter'
    history_geojson_path = 'data/bcn_jaume/jaume_adri/MVI_9512_geohistory.geojson'
    frame_rate = 1
    yolo_thres = 0.10

class ConfigAdriMVI_9512_10(ConfigAdriMVI_9512):
    video_save_path = 'data/bcn_jaume/jaume_adri/MVI_9512_analysis_10.MOV'
    history_geojson_path = 'data/bcn_jaume/jaume_adri/MVI_9512_10_geohistory.geojson'
    frame_rate = 10


class ConfigRomaTrimmed:
    video_path = 'data/roma/placa_trimmed.mp4'
    video_save_path = 'data/roma/placa_trimmed_analysis.mp4'
    refpoints_geojson_path = 'data/roma/placa_refpoints.geojson'
    converter_path = 'data/roma/placa_converter'
    history_geojson_path = 'data/roma/placa_trimmed_geohistory.geojson'
    frame_rate = 2
    yolo_thres = 0.10


class Config(ConfigAdriMVI_9512_10):
    def __init__(self):
        print(f'Config : {self.video_path}')
