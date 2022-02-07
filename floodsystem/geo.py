# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_within_radius(stations, centre,r):
    station_radius_list=[]
    for station in stations:
        if haversine(centre, station.coord)<=r:
            station_radius_list.append(station)
    return station_radius_list


def rivers_by_station_number(stations, N):
    river_list=[]
    for station in stations:
        river_list.append(station.river)
    
    river_by_number=[]
    for river in river_list:
        if river not in [x[1] for x in river_by_number]:
            number = river_list.count(river)
            river_by_number.append((number, river))
    
    river_descending=sorted(river_by_number, reverse=True)

    final_river_list=[]
    i=0
    while i<N:
        final_river_list.append(river_descending[i])
        i+=1
    while river_descending[i][0]==river_descending[i-1][0]:
        final_river_list.append(river_descending[i])
        i+=1

    final_river_list=[(t[1], t[0]) for t in final_river_list]

    return final_river_list

def stations_by_distance(stations, p):                           
    list = []
    for station in stations:
       distance = haversine(p, station.coord)
       list.append((station.name, station.town, distance ))         
    return sorted_by_key(list, 2, reverse = False)    

def rivers_with_station(stations):
    rivers_list = []
    for station in stations:
        rivers_list.append(station.river) 
    final_river_list = set(rivers_list)
    return final_river_list                            

def stations_by_river(stations):         
    river_dict = {}
    for station in stations:
        if station.river in river_dict:
            river_dict[station.river].append(station.name)
            river_dict[station.river].sort()
        else:
            river_dict[station.river] = [station.name]
    return river_dict

