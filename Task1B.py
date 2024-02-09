from floodsystem.stationdata import build_station_list

from haversine import haversine, Unit

from floodsystem.geo import stations_by_distance

 

def run():

    p =(52.2053,0.1218)   #set parameter for p

    print(("**Distance from city centre to closest 10 stations**: ") ,(stations_by_distance((build_station_list()),p)[:10])) #execute function

    print(("**Distance from city centre to furthest 10 stations**:  "), (stations_by_distance((build_station_list()),p))[-10:])

 

if __name__ == "__main__":

    run()