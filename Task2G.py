from floodsystem.stationdata import build_station_list
from floodsystem.analysis import *

def run():
    """
    Task 2G: list the towns where you assess the risk of flooding to be greatest
    Note: new functions written for this task are in analysis.py, along with explanations of criteria in making the assessment
    
    """
    stations = build_station_list()

    risk_assessment(stations)
    low, moderate, high, severe = town_risk(stations)

    print(f"Towns with severe risk of flooding: {severe}")
    print(f"Towns with high risk of flooding: {high}")
    print(f"Towns with moderate risk of flooding: {moderate}")
    print(f"There are {len(low)} towns with low risk of flooding")

if __name__ == '__main__':
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()