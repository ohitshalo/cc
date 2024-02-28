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
    y = levels
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1))

    # Display plot
    plt.show()
