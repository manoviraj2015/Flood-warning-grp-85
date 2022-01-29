#ml2015 

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():

    stations = build_station_list()

    cam_station_list = stations_within_radius(stations, (52.2053, 0.1218), 10)

    cam_name_list=[]
    for station in cam_station_list:
        cam_name_list.append(station.name)
    
    sorted_list=sorted(cam_name_list)
    print(sorted_list)

if __name__ == "__main__":
    run()