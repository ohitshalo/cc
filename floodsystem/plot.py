import numpy as np
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib
import datetime





def plot_water_levels(station, dates, levels):

    #this will plot the recent water levels for a given station

 

    plt.plot(dates, levels)

 

    plt.xlabel('data')

    plt.ylabel('water level (m)')

    plt.title('station ' + str(station.name))

    plt.xticks(rotation = 45)

    plt.tight_layout()

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    y = levels
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1))

    # Display plot
    plt.show()


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
