from floodsystem.flood import stations_level_over_threshold

from floodsystem.stationdata import build_station_list, update_water_levels

 

def run():

    print('hello')

    #creates a list of stations

    stations = build_station_list()

    #gets current water level values

    update_water_levels(stations)

    #finds which stations have a water level ratio value over 0.8

    result = stations_level_over_threshold(stations, 0.8)

    #prints off the stations with a ratio greater than 0.8

    for item in result:

        print(str(item[0].name) + ": " + str(item[1]))




if __name__ == "__main__":

    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()