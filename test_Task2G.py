from floodsystem.stationdata import build_station_list
from floodsystem.analysis import *

def test_town_risk():
    stations = build_station_list()
    risk_assessment(stations)
    low, moderate, high, severe = town_risk(stations)
    assert len(low) >= 0
    assert len(moderate) >= 0
    assert len(high) >= 0
    assert len(severe) >= 0