from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance






def test_stations_by_distance():

 

    stations = build_station_list()

    p = (52.2053, 0.1218)

    list = stations_by_distance((stations[:10]),p)

    assert len(list) > 0

    list2 = stations_by_distance((stations[-10:]),p)

    assert len(list2) > 0