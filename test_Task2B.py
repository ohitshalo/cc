from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

stationset = []
stationset.append(MonitoringStation("A", "A", "A", (0,0), (0,1), "RiverA", "TownA"))
stationset.append(MonitoringStation("B", "B", "B", (0,1), (0,1), "RiverB", "TownB"))
stationset.append(MonitoringStation("C", "C", "C", (0,2), (0,1), "RiverC", "TownC"))
stationset.append(MonitoringStation("D", "D", "D", (0,3), (0,1), "RiverD", "TownD"))
stationset.append(MonitoringStation("E", "E", "E", (0,4), (0,1), "RiverE", "TownE"))
stationset.append(MonitoringStation("F", "F", "F", (0,5), (0,1), "RiverF", "TownF"))

def test_stations_level_over_threshold():
    for i in range(6):
        stationset[i].latest_level = i
    result = stations_level_over_threshold(stationset, 2.5)
    correctresultlevels = [5,4,3]
    assert len(result) == 3
    for i in range(3):
        assert result[i][1] == correctresultlevels[i]