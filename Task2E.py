#tak42
from floodsystem.plot import plot_water_levels
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import datetime, timedelta 
from floodsystem.datafetcher import fetch_measure_levels
import datetime
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
    spliced_sorted_station_list = sorted_station_list[1:6]

    #Producing the graphs
    for station in stations: 
          if station.name in [
           spliced_sorted_station_list[0][0], spliced_sorted_station_list[1][0],  spliced_sorted_station_list[2][0] 
           , spliced_sorted_station_list[3][0] , spliced_sorted_station_list[4][0]
           ]:
              dates, levels = fetch_measure_levels(
              station.measure_id, dt=datetime.timedelta(days=10))      #Fetch data over past 10 days
              plot_water_levels(station, dates, levels)
                        
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

   
