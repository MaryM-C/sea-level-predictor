import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y, c='aquamarine')

    # Create first line of best fit
    regline1 = linregress(x,y)
    years_extended = np.arange(1880, 2051, 1)
    line = [regline1.slope * xi + regline1.intercept for xi in years_extended]
    plt.plot(years_extended, line)

    # Create second line of best fit
    df_copy = df.loc[df['Year'] >= 2000]
    x2 = df_copy['Year']
    y2 = df_copy['CSIRO Adjusted Sea Level']
    
    regline2 = linregress(x2, y2)
    years_cut = np.arange(2000, 2051, 1)
    line2 = [regline2.slope * xi + regline2.intercept for xi in years_cut]
    plt.plot(years_cut, line2)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()