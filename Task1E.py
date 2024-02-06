from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    print(rivers_by_station_number(stations_by_river(build_station_list()),9))

if __name__ == "__main__":
    run() 
