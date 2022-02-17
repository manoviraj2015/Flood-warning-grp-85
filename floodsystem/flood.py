"""This module contains a collection of functions related to
flood data.

"""
#ml2015

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


def stations_highest_rel_level(stations, N):
    list_highest_level = []
    for station in stations:
        m=station.relative_water_level()
        if m==None:
            pass
        else:
            list_highest_level.append((station,m))
    
    sorted_list_highest_level = sorted(list_highest_level, key=lambda x: x[1], reverse=True)

    i=0
    short_list=[]
    while i<N:
        short_list.append(sorted_list_highest_level[i][0])
        i+=1

    return short_list
