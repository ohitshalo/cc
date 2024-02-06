# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key # noqa

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

