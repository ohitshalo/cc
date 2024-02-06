from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station, stations_by_river

def run():
    river = rivers_by_station(build_station_list())
    def first_ten(list):
        result = []
        for i in range(10):
            result.append(list[i])
        return result

    print (f"{len(river)} stations. First 10 - {first_ten(river)}")

    for river in stations_by_river(build_station_list()):
        if river["river"] in ["River Aire", "River Cam", "River Thames"]:
            print (river["station"])

if __name__ == "__main__":
    run() 
