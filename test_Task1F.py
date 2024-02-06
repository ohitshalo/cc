from floodsystem.station import inconsistent_typical_range_stations

from floodsystem.stationdata import build_station_list

 

stations = build_station_list()

 

newlist = inconsistent_typical_range_stations(stations)

 

proper_inconsistent_list =[]

 

def inconsistent_typical_range_stations():

    x = inconsistent_typical_range_stations(stations)

    assert len(x) == 30