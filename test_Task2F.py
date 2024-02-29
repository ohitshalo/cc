from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import plot_water_level_with_fit
import datetime
import matplotlib as plt

def test_plot_water_level_with_fit():
    stations = (build_station_list()[:5])
    update_water_levels(stations)
    highest_stations = stations_highest_rel_level(stations, 1)
    days = 2
    for station in highest_stations:
        station_identification = station.measure_id
        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days = days))
        plot_water_level_with_fit(station, dates, levels, 4)
    
    assert len(highest_stations) == 1
    assert len(dates) >= 0
    assert len(levels) >= 0

