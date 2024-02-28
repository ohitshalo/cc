from floodsystem.flood import stations_highest_rel_level

from floodsystem.stationdata import build_station_list, update_water_levels

 

def run():

 

    stations = build_station_list()

    update_water_levels(stations)

 

    result = stations_highest_rel_level(stations, 10)

 

    for item in result:

 

        print(str(item.name) + ": " + str(item.relative_water_level()))

 

if __name__ == "__main__":

    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    run()

 