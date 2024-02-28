from floodsystem.datafetcher import fetch_measure_levels

from floodsystem.flood import stations_highest_rel_level

from floodsystem.plot import plot_water_levels

from floodsystem.stationdata import build_station_list, update_water_levels

import datetime

 

def run():

    station_list = build_station_list()

    update_water_levels(station_list)

    stations = stations_highest_rel_level(station_list,5)

 

    for items in stations:

        result = fetch_measure_levels(items.measure_id, datetime.timedelta(days = 10))

        plot_water_levels(items, result[0], result[1])

   

if __name__ == "__main__":

    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    run()