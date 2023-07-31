import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(7, 7))

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    # array with years up to 2050
    years = np.append(df['Year'], list(range(max(df['Year'])+1, 2051)))

    result_first = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    plt.plot(years, result_first.intercept + result_first.slope * years, 'r', label='fitted line')


    # Create second line of best fit
    after_2000 = df.loc[df['Year'] >= 2000]
    result_second = linregress(after_2000['Year'], after_2000['CSIRO Adjusted Sea Level'])
    years = np.append(after_2000['Year'], list(range(max(after_2000['Year']) + 1, 2051)))

    plt.plot(years, result_second.intercept + result_second.slope * years, 'g')

    # Add labels and title
    ax.set(xlabel='Year', ylabel='Sea Level (inches)')
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()