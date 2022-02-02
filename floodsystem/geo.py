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
    while i<9:
        final_river_list.append(river_descending[i])
        i+=1
    while river_descending[i][0]==river_descending[i-1][0]:
        final_river_list.append(river_descending[i])
        i+=1

    final_river_list=[(t[1], t[0]) for t in final_river_list]

    return final_river_list