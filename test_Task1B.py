 

from floodsystem.station import inconsistent_typical_range_stations

from floodsystem.stationdata import build_station_list

 

stations = build_station_list()

 

list = inconsistent_typical_range_stations(stations)

inconsistent_list =[]

 

for station in list:

    name = station.name

    inconsistent_list.append(name)

 

print(sorted(inconsistent_list))