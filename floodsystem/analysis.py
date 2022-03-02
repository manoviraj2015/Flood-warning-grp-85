#tak42
import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    float_dates = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(float_dates - float_dates[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, float_dates[0]

def floodwarning(station, dates, levels, p):
    poly, d = polyfit(dates, levels, p)
    poly_d1 = np.polyder(poly)      #first derivative of polynomial 
    poly_d2 = np.polyder(poly_d1)   #second derivative of polynomial

    high_value = station.typical_range[1]
    low_value = station.typical_range[0]
    latest_level = levels[0]
    poly_d2_latest = poly_d2(0)

    #setting default to be moderate
    warning = 'moderate'

    #severe when above highest level and increasing
    if (latest_level > high_value and poly_d2_latest > 0):
        warning = 'severe'
    #high when above highest level but decreasing    
    elif (latest_level > high_value and poly_d2_latest < 0):
        warning = 'high'
    #high when near highest level and increasing
    elif (abs(latest_level - high_value) > abs(latest_level-low_value) and poly_d2_latest > 0):
        warning = 'high'
    #moderate when near highest level but decreasing
    elif (abs(latest_level - high_value) > abs(latest_level-low_value) and poly_d2_latest < 0):   
         warning = 'moderate'   
    #moderate when near lower level and increasing
    elif (abs(latest_level - high_value) < abs(latest_level-low_value) and poly_d2_latest > 0):  
         warning = 'moderate'
    #low when near lower level and decreasing
    elif (abs(latest_level - high_value) < abs(latest_level-low_value) and poly_d2_latest < 0):
         warning = 'low'
    elif (latest_level < low_value and poly_d2_latest < 0):
         warning = 'low'
    
    return warning
    
