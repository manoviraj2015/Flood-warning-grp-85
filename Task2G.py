#tak42
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import floodwarning
from datetime import datetime, timedelta 
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit

def run():

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations) 

    #take for the past 5 days
    dt = 5

    valid_station_list = []
    for station in stations:
        if station.latest_level != None and station.typical_range[0] != None and station.typical_range[1] != None:
            valid_station_list.append(station.name)
    
    for station in stations:
        if station.name in [
            valid_station_list
        ]:
            dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
            warning_level = floodwarning(station, dates, levels, 4)      #setting the polynomial to be of order 4   
        if warning_level == 'severe':
             print(station.town)

if __name__ == "__main__":
 print("*** Task 2G: CUED Part IA Flood Warning System ***")
 run()
