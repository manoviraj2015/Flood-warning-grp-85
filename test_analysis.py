#tak42
from floodsystem.analysis import polyfit
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta 
import datetime
import numpy as np

#def test_polyfit():
#    stations = build_station_list()
#    update_water_levels(stations)

#    for station in stations:
#        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
#        #Removing empty lists
#        if dates == [] or levels == []:
#           pass
#        else:
#            poly, d0 = polyfit(dates, levels, 4)
#            assert isinstance(poly, np.poly1d)
#            assert isinstance(d0, float)
#            assert d0 >= 0 #Should be bigger than 0
    
def test_floodwarning():
     stations = build_station_list()
     update_water_levels(stations)
     inconsistent_stations = inconsistent_typical_range_stations(stations)
     station_list = []
     for station in stations:
      if station in inconsistent_stations:
        next
      elif station.latest_level != None:
        station_list.append((station.name, station.latest_level ))
     sorted_station_list = sorted_by_key(station_list, 1 , reverse = True)  
     spliced_sorted_station_list = sorted_station_list[1:40]
    
   
     for station in stations: 
          if station.name in [
           spliced_sorted_station_list[0][0], spliced_sorted_station_list[1][0],  spliced_sorted_station_list[2][0] 
           , spliced_sorted_station_list[3][0] , spliced_sorted_station_list[4][0] , spliced_sorted_station_list[5][0] , spliced_sorted_station_list[6][0] , spliced_sorted_station_list[7][0], spliced_sorted_station_list[8][0], spliced_sorted_station_list[9][0], spliced_sorted_station_list[10][0],  spliced_sorted_station_list[11][0], spliced_sorted_station_list[12][0], spliced_sorted_station_list[13][0], spliced_sorted_station_list[14][0], spliced_sorted_station_list[15][0], spliced_sorted_station_list[16][0], spliced_sorted_station_list[17][0], spliced_sorted_station_list[18][0], spliced_sorted_station_list[19][0], spliced_sorted_station_list[20][0], spliced_sorted_station_list[21][0], spliced_sorted_station_list[22][0]
    ]:
           dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
           #Removing empty lists
           if dates == [] or levels == []:
              pass
           else:
             warning = floodwarning(station, dates, levels, 15)
             assert warning == "severe" or warning == "high" or warning == "moderate" or warning == "low"
