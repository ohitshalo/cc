from floodsystem.datafetcher import fetch_measure_levels

from floodsystem.plot import plot_water_levels

from floodsystem.stationdata import build_station_list, update_water_levels

import datetime

 
def test_plot_water_levels():
    station = [build_station_list()[0]]
    update_water_levels(station)
    data = fetch_measure_levels(station[0].measure_id, datetime.timedelta(days=10))
    plot_water_levels(station[0], data[0],data[1])
    if len(data) > 0:
        test1 = True
    else:
        test1 = False
    assert test1 == True