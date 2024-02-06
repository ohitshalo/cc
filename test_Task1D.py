
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station, stations_by_river

def test_rivers_by_station():
    stations = build_station_list()
    assert len(rivers_by_station(stations)) > 0
    assert type(rivers_by_station(stations)) == list

def test_station_by_rivers():
    stations = build_station_list()
    assert len(stations_by_river(stations)) > 0
    assert type(stations_by_river(stations)) == list
