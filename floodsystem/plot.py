#tak42
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list

def plot_water_levels(station, dates, levels): 
    
    plt.axhline(y = station.typical_range[0])
    plt.axhline(y = station.typical_range[1])
    

    plt.plot(dates, levels)
    range = []
    stations = build_station_list()
    for station in stations:
        if station.name in [
            stationname
        ]:
            range.append(station.typical_range)                               
    low_value = range[0][0]
    high_value = range[0][1]
    plt.axhline(y=low_value)
    plt.axhline(y=high_value)
    
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station " + stationname)
    
    plt.show()
    # Display plot
    plt.tight_layout()  

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    plt.tight_layout()  
    plt.show()
   

def plot_water_levels_with_fit(station, dates, levels, p): 
    
    float_dates = matplotlib.dates.date2num(dates)
    poly, d = polyfit(dates, levels, p)
    plt.plot(dates, poly(float_dates-d))

    plt.plot(dates, levels)

    plt.axhline(y = station.typical_range[0])
    plt.axhline(y = station.typical_range[1])


    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    plt.tight_layout()  

    plt.show()
   
