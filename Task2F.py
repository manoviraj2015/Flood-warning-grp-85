#tak42
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from datetime import datetime, timedelta 
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.plot import plot_water_levels, plot_water_levels_with_fit

def run():   
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)    
    # Current 5 stations that have greatest water level
    station_list = []
    for station in stations:
       if station.latest_level != None:
        station_list.append((station.name, station.latest_level ))
    sorted_station_list = sorted_by_key(station_list, 1 , reverse = True)  
    spliced_sorted_station_list = sorted_station_list[1:6]
    #Fetch data over past 2 days
    dt = 2 
    #Producing the graphs
    for station in stations: 
          if station.name in [
           spliced_sorted_station_list[0][0], spliced_sorted_station_list[1][0], spliced_sorted_station_list[2][0]
           , spliced_sorted_station_list[3][0] , spliced_sorted_station_list[4][0]
           ]:
              dates, levels = fetch_measure_levels(
              station.measure_id, dt=datetime.timedelta(days=dt))
              
              #NEED TO PLOT THE POLYNOMIAL
              coefficient = polyfit(dates,levels,4)
              print(coefficient)
              plot_water_levels_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()

   
