#tak42

#from .utils import sorted_by_key  # noqa

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():

  stations = build_station_list()

  the_list = stations_by_distance(stations, (52.2053, 0.1218))

  print("The closest 10 stations: ")           
  print(the_list[:10])
  print("The furthest 10 stations: ")           
  print(the_list[-10:])


if __name__ == "__main__":
  print("**sorting stations by distance**")
  run()

