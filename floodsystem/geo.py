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
