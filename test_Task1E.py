from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def test_rivers_by_station_number():
    stations = stations_by_river(build_station_list())
    assert len(rivers_by_station_number(stations, 3)) == 3
    assert len(rivers_by_station_number(stations, 0)) == 0
    assert type(rivers_by_station_number(stations, 10)) == list