


from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

 

from floodsystem.geo import stations_within_radius

stations = build_station_list() #create list of all the stations




#new_stations = stations_within_radius(stations, (52.2053, 0.1218), 10 )

print(stations_within_radius(stations, (52.2053, 0.1218), 10 ))

 