"""This module contains a collection of functions related to
flood data.

"""

def stations_level_over_threshold(stations,tol):
    
    threshold_list=[]
    for station in stations:
        if station.relative_water_level()==None:
            pass
        elif station.relative_water_level()>tol:
            threshold_list.append((station.relative_water_level(),station))

    threshold_list_descending=sorted(threshold_list, reverse=True)
    final_threshold_list=[(t[1], t[0]) for t in threshold_list_descending]

    return final_threshold_list


    