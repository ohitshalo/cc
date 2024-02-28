
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .flood import stations_level_over_threshold
from .datafetcher import fetch_measure_levels
from .geo import stations_by_town

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
    plt.plot(dates, typical_min, label = "Typical minimum level", linestyle = "dashed", color = "aqua")
    plt.plot(dates, typical_max, label = "Typical maximum level", linestyle = "dashed", color = "steelblue")
    plt.plot(x_plot, poly(x_plot - x[0]), color = "darkgreen")

    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name + " Water Level")

    plt.tight_layout()
    
    plt.legend()
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
    3 = current relative water level above 1.5
    4 = current relative water level above 3
    """
    #create lists of tuples, where each tuple has a station object and its relative water level
    low = stations_level_over_threshold(stations, 1)
    moderate = stations_level_over_threshold(stations, 1.5)
    high = []
    severe = []
    dt = 1

    for i in range(0, len(moderate) - 1):
        station = moderate[i][0]
        relative_water_level = moderate[i][1]
        #try and except to catch stations with no level history
        try:
            #fetch levels over the past 24 hours
            dates, levels = fetch_measure_levels(station.measure_id, timedelta(days=dt))
            #if water level has increased, perform polyfit analysis
            if levels[-1] > levels[0]:
                p = 3
                poly, d0 = polyfit(dates, levels, p)
                future_day = datetime.now() - timedelta(days=dt)
                future_day_N = matplotlib.dates.date2num(future_day)
                day_diff = matplotlib.dates.date2num(dates[0])
                water_level = poly(future_day_N - day_diff)
                predicted_relative_level = (water_level - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])
                #if the predicted relative water level is above 3, classify as severe (if not, classify as high)
                if predicted_relative_level > 3:
                    severe.append(moderate[i])
                else: 
                    high.append(moderate[i])
            #if water level has not increased but relative water level is above 3, classify as severe
            elif relative_water_level > 3:
                severe.append(moderate[i])
            #if water level has not increased but relative water level is between 2 and 3, classify as high
            elif relative_water_level > 2:
                high.append(moderate[i])
            else:
                pass
        except Exception:
            pass
    
    low = [i for i in low if i not in moderate]
    moderate  = [i for i in moderate if i not in high and i not in severe]

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


    
