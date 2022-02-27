from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import datetime, timedelta 
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
     
   # Fetch data over past 10 days
    for station in stations:
            dt = 10
            dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
            for date, level in zip(dates, levels):
             plot_water_levels(station.name, dates, levels)
    next 



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
