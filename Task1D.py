#tak42

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
def run():

    stations = build_station_list()
    list_of_rivers = rivers_with_station(stations)



    print(len(list_of_rivers))
    print("stations")
    sorted_river_list = sorted(list_of_rivers)
    print("The first 10: ")
    print(sorted_river_list[:10])  

    print("\n")
    
    specific_station_list = []
    for station in stations:
        if station.river in [
                'River Aire', 'River Cam', 'River Thames'
        ]:
            specific_station_list.append(station)
    dictionary = stations_by_river(specific_station_list)            
    print(dictionary)

if __name__ == "__main__":
  run()
