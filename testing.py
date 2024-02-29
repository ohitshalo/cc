from floodsystem.stationdata import *
from floodsystem.flood import *

stations = build_station_list()
update_water_levels(stations)
print(stations_level_over_threshold(stations, 2))