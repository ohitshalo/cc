
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def polyfit(dates, levels, p):
    x = []
    for date in dates:
        x.append(plt.dates.date2num(date))
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




    
