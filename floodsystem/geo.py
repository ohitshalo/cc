# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
import floodsystem.utils

def rivers_by_station(stations):
    river = []
    for station in stations:
        if not station.name:
            pass
        else:
            if station.river not in river:
                river.append(station.river)
    return sorted(river)
        

def stations_by_river(stations):
    stationstoriver = []
    for station in stations:
        river = False
        for i, entry in enumerate(stationstoriver):
            if entry["river"] == station.river:
                stationstoriver[i]["station"].append(station.name)
                river = True
                break
        if not river:
            stationstoriver.append({"river": station.river, "station": [station.name]})
    for station in stationstoriver:
        station["station"] = sorted(station["station"])
    return stationstoriver



def rivers_by_station_number(stations, N):
    riverstonumber = []
    top = []
    for station in stations:
        riverstonumber.append((station["river"], len(station["station"])))
    riverstonumber = sorted_by_key(riverstonumber,1)
    for i in range(N):
        top.append(riverstonumber[-(i+1)])
    return top

stations = build_station_list() #creates an list of all the stations

 

#Code/function required for task1B

def stations_by_distance(stationslist, p):

    station_list = []  #empty list for stations

   

    for station in stationslist:

        station_list.append((station.name, haversine(station.coord, p))) #adds stations to the list

 

    list1 = floodsystem.utils.sorted_by_key(station_list, 1)

    return list1

 

#Code/function required for task1C

def stations_within_radius(stations, centre, r):   

    station_list2 = [] #empty list for stations

 

    for station in stations:

        if haversine(station.coord, centre) < r:

            station_list2.append((station.name, haversine(station.coord, centre))) #adds stations into the list

 

    list2 = floodsystem.utils.sorted_by_key(station_list2, 0) #sorts stations alphabetically

    return list2