from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation


def test_build_station_list():
    for station in build_station_list()[:1]:
        assert type(station) == MonitoringStation
    assert type(build_station_list()) == list
    assert len(build_station_list()) > 0
