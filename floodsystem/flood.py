"""This module contains a collection of functions related to
flood data.

"""

def stations_level_over_threshold(stations,tol):
    
    threshold_list=[]
    for station in stations:
        m=station.relative_water_level()
        if m==None:
            pass
        elif m>tol:
            threshold_list.append((station, m))
    
    final_threshold_list = sorted(threshold_list, key=lambda x: x[1], reverse=True)

    return final_threshold_list