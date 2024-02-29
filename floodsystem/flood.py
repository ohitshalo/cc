from .station import MonitoringStation

from .utils import sorted_by_key

 

def stations_level_over_threshold(stations, tol):
    result = []
    for item in stations:
        if item.relative_water_level() != None:
            if item.relative_water_level() > tol:
                result.append([item, item.relative_water_level()])
    return sorted_by_key(result, 1, True)

def stations_highest_rel_level(stations, N):
    #returns fist N stations which are most at risk of flooding
    result = stations_level_over_threshold(stations, -(10**100))   
    return_data = []
    for i in range(N):
        return_data.append(result[i][0])
    return return_data