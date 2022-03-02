#tak42
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import floodwarning
from datetime import datetime, timedelta 
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.utils import sorted_by_key

def run():

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)   
    
    #Creating list of stations of inconsistent data so can discount from final 5
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    
    # Current 5 stations that have greatest water level
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
            dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=1))
            warning_level = floodwarning(station, dates, levels, 15)        
            if warning_level == 'severe' or warning_level == 'high':
               print(station.town, warning_level)
           
if __name__ == "__main__":
 print("*** Task 2G: CUED Part IA Flood Warning System ***")
 run()

