
from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_within_radius


 

stations = build_station_list() #create station list

 

def test_stations_within_radius():

    list = stations_within_radius(stations, (52.2053, 0.1218), 10 )

    assert len(list) > 0

 