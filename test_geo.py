from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius, rivers_by_station_number

#ml2015

def test_station_within_radius():
    """1C-Checks there is at least one station within 100km of CBD.
    Checks the list type is a list.
    Checks the list contains MonitoringStation type objects"""
    stations = build_station_list()
    within_radius = stations_within_radius(stations,(52.2053, 0.1218), 100)
    assert len(within_radius)>1
    assert type(within_radius)==list
    for station in within_radius:
        assert type(station)==MonitoringStation

def test_rivers_by_station_number():
    """1E-Checks there are more than 10 rivers' data for a function call where N=10.
    Checks the list type is a list
    Checks the list contains tuples"""
    stations = build_station_list()
    river_numbers=rivers_by_station_number(stations,10)
    assert len(river_numbers)>=10
    assert type(river_numbers)==list
    for river in river_numbers:
        assert type(river)==tuple


#tak42