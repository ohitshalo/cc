
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .flood import stations_level_over_threshold
from .datafetcher import fetch_measure_levels
from .geo import stations_by_town
from .stationdata import update_water_levels

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[0], levels, p)
    poly = np.poly1d(p_coeff)
    return (poly, x[0])

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    x_plot = np.linspace(x[0], x[-1], 100)
    typical_min = np.full(len(dates), station.typical_range[0])
    typical_max = np.full(len(dates), station.typical_range[1])
    plt.plot(dates, levels, label = "Water level", color = "red")
    plt.plot(dates, typical_min, label = "Typical minimum level", linestyle = "dashed", color = "purple")
    plt.plot(dates, typical_max, label = "Typical maximum level", linestyle = "dashed", color = "blue")
    plt.plot(x_plot, poly(x_plot - x[0]), color = "green")
    plt.xlabel('Date')
    plt.ylabel('Water Level/m)')
    plt.xticks(rotation=45)
    plt.title(station.name + " Water Level")
    plt.show()

def assign_risk_factor(risk, assignment):
    """
    Updates the flood risk factor of each station in the list
    
    """
    for i in range(0, len(risk) - 1):
        station = risk[i][0]
        station.risk_factor = assignment

def risk_assessment(stations):
    """
    Risk factors from 1 (low), 2 (moderate), 3 (high), and 4 (severe) are assigned to each station
    1 = current relative water level between 1 and 1.5
    2 = current relative water level between 1.5 and 2
    3 = current relative water level above 2 and 2.5
    4 = current relative water level above 2
    """
    #create lists of tuples, where each tuple has a station object and its relative water level
    update_water_levels(stations)
    low = stations_level_over_threshold(stations, 1)
    moderate = stations_level_over_threshold(stations, 1.5)
    high = stations_level_over_threshold(stations, 2)
    severe = stations_level_over_threshold(stations, 2.5)

    assign_risk_factor(low, 1)
    assign_risk_factor(moderate, 2)
    assign_risk_factor(high, 3)
    assign_risk_factor(severe, 4)


def town_risk(stations):
    """
    Assesses the risk of each town using the highest risk station in that town
    Sorts the towns into lists of severity levels of low, moderate, high, and severe
    Returns the lists of severity levels sorted alphabetically
    
    """
    #get dictionary mapping towns to stations
    towns_dict = stations_by_town(stations)
    low = []
    moderate = []
    high = []
    severe = []
    for key, value in towns_dict.items():
        #default risk of 0
        town_risk = 0
        #town risk is the risk factor of the highest risk station in that town
        for station in value:
            if station.risk_factor > town_risk:
                town_risk = station.risk_factor
            else:
                pass
        #sort towns into lists of severity levels
        if town_risk == 1:
            low.append(key)
        elif town_risk == 2:
            moderate.append(key)
        elif town_risk == 3:
            high.append(key)
        elif town_risk == 4:
            severe.append(key)

    low.sort()
    moderate.sort()
    high.sort()
    severe.sort()

    return low, moderate, high, severe


    
