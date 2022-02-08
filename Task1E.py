#ml2015

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    stations = build_station_list()
    by_station_number = rivers_by_station_number(stations, 9)
    print (by_station_number)

if __name__ == "__main__":
    run()