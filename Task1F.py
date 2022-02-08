#ml2015

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    inconsistent_stations_objects = inconsistent_typical_range_stations(stations)
    inconsistent_stations_name=[]
    for station in inconsistent_stations_objects:
        inconsistent_stations_name.append(station.name)
    inconsistent_stations_name_sort = sorted(inconsistent_stations_name)
    
    print(inconsistent_stations_name_sort)

if __name__ == "__main__":
    run()