#tak42
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list

def plot_water_levels(station, dates, levels): 
    # Plotting the levels against dates
    stationname = station
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


def plot_water_levels_with_fit(station, dates, levels, p):
    station_name = str(station)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station " + station_name)

    # Plot original data points
    plt.plot(dates, levels)
    
    # Plot polynomial fit at 30 points along interval
    float_dates = matplotlib.dates.date2num(dates)
    x1 = np.linspace(float_dates[0], float_dates[-1], 30)
    p_coeff = np.polyfit(float_dates, levels, p)
    poly = np.poly1d(p_coeff)
    plt.plot(x1, poly(x1 - float_dates[0]))

    # Display plot
    plt.show()
