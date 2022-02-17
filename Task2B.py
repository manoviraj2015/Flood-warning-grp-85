#ml2015 

from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    station_list_over_threshold=stations_level_over_threshold(stations, 0.8)
    
    for tup in station_list_over_threshold:
        print(tup[0].name, tup[1])

if __name__ == "__main__":
  run()