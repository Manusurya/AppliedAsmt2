# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 10:38:33 2023

@author: manus
"""

# importing the required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
THe following codes are used for displaying all the rows and
columns in a dataframe(beacuse I needed to know some index values)

#pd.set_option('display.max_rows',None)
#pd.set_option('display.max_columns',None)
#pd.set_option('display.width',None)
#pd.set_option('display.max_colwidth',None)
'''


def read_file(file_name, yrs, cntrs, col, indicator):
    '''
    defining a function that returns two dataframes,
    one with countries as columns and other with years
    as columns. Function takes file name and the required
    filters as its attribute
    '''
    # reading the file
    df0 = pd.read_csv(file_name, skiprows=4)
    # cleaning the dataframe
    df1 = df0.groupby(col, group_keys=True)
    df1 = df1.get_group(indicator)
    df1 = df1.reset_index()
    a = df1['Country Name']
    df1 = df1.iloc[cntrs, yrs]
    df1 = df1.dropna(axis=1)
    df1.insert(loc=0, column='Country Name', value=a)
    # taking the transpose
    df2 = df1.set_index('Country Name').T
    return df1, df2


def plot_bar(data, col, ylbl, titl):
    '''
    defining a function that returns a bar plot.
    The function takes the dataframe as its attribute
    and returns a graph over the required columns. It also
    adds a title and label for y axis.
    '''
    ax = data.plot(x=col, rot=45, figsize=(50, 25),
                   kind='bar', title=titl, fontsize=50)
    ax.legend(fontsize=36)
    ax.set_xlabel('Country', fontsize=40)
    ax.set_ylabel(ylbl, fontsize=40)
    ax.set_title(titl, pad=20, fontdict={'fontsize': 40})
    return


def plot_line(data, ylbl, titl):
    '''
    defining a function that returns a dashdot line plot.
    The function takes the dataframe as its attribute
    and returns a graph over the required columns. It also
    adds a title and label for y axis.
    '''
    ax = data.plot(linestyle='dashdot', figsize=(
        50, 25), kind='line', fontsize=50)
    # adding legend properties for a more visible legend
    legend_properties = {'weight': 'bold', 'size': 36}
    ax.legend(fontsize=36, prop=legend_properties)
    ax.set_xlabel('Year', fontsize=40)
    ax.set_ylabel(ylbl, fontsize=40)
    ax.set_title(titl, pad=20, fontdict={'fontsize': 40})
    return


def stats_f(file_name, years, cntry):
    '''
    defining a function that returns a dataframe
    containing all the stats of the required country.
    Function takes file name and the required
    filters and countryname as its attribute.
    '''
    # reading the data file
    df = pd.read_csv(file_name, skiprows=4)
    # cleaning the data
    df1 = df.groupby('Country Name', group_keys=True)
    df1 = df1.get_group(cntry)
    df1 = df1.reset_index()
    df1 = df1.iloc[:, years]
    df1 = df1.dropna(axis=0)
    df1 = df1.dropna(axis=1)
    df2 = df1.set_index("Indicator Name").T
    return df2


def heatMap(value2, colours, title_name):
    '''
    defining a function that returns a correlation heatmap.
    The function takes the correlation table as its attribute
    and returns a map over the requred parameters. It also
    adds a title and colour pallete for the heatmap.
    '''
    fig, ax = plt.subplots(figsize=(20, 20))
    im = ax.imshow(value2, cmap=colours)
    cbar = ax.figure.colorbar(im, ax=ax, shrink=0.85)
    # add tick labels
    ax.set_xticks(np.arange(len(x)), labels=x, size=20)
    ax.set_yticks(np.arange(len(x)), labels=x, size=20)
    # Rotate the tick labels to be more legible
    plt.setp(ax.get_xticklabels(), rotation=90,
             ha="right", rotation_mode="anchor")
    ax.set_title(title_name, size=30)
    fig.tight_layout()


# creating lists with the indices of required years and countries
years = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
year = [5, 15, 25, 35, 45, 55, 65]
countries = [29, 40, 55, 77, 81, 109, 263]

# creating the required dataframes for plotting
aglnd_1, aglnd_2 = read_file("API_19_DS2_en_csv_v2_5346672.csv", year,
                             countries, "Indicator Name", "Agricultural land (% of land area)")
arable_1, arable_2 = read_file("API_19_DS2_en_csv_v2_5346672.csv",
                               years, countries, "Indicator Name", "Arable land (% of land area)")
forest_1, forest_2 = read_file("API_19_DS2_en_csv_v2_5346672.csv",
                               years, countries, "Indicator Name", "Forest area (% of land area)")
co2_1, co2_2 = read_file("API_19_DS2_en_csv_v2_5346672.csv", years, countries,
                         "Indicator Name", "CO2 emissions from liquid fuel consumption (kt)")
urbp_1, urbp_2 = read_file("API_19_DS2_en_csv_v2_5346672.csv", year,
                           countries, "Indicator Name", "Urban population (% of total population)")
urbp_3, urbp_4 = read_file("API_19_DS2_en_csv_v2_5346672.csv",
                           year, countries, "Indicator Name", "Urban population")
brazil = stats_f("API_19_DS2_en_csv_v2_5346672.csv", [
                 3, 35, 40, 45, 50, 55, 60, 64], "Brazil")
india = stats_f("API_19_DS2_en_csv_v2_5346672.csv", [
                3, 35, 40, 45, 50, 55, 60, 64], "India")

# using the describe function to explore the data
co2_d = co2_1.describe()
co2_d.to_csv('CO2des.csv')
# using the mean function to find the average CO2 production in different countries over the years
co2_2.mean()
# using the max function to find the highest amount of CO2 produced in the countries
co2_2.max()

# plotting the required bar and line plots
plot_bar(urbp_1, "Country Name", 'Number', 'Urban population')
plot_bar(urbp_3, "Country Name", 'Percentage',
         'Urban population (% of total population)')
plot_bar(aglnd_1, "Country Name", 'Percentage',
         'Agricultural land (% of land area))')
plot_line(co2_2, 'Kiloton(kt)',
          'CO2 emissions from liquid fuel consumption (kt)')
plot_line(arable_2, 'Percentage', 'Arable land (% of land area)')
plot_line(forest_2, 'Percentage', 'Forest area (% of land area)')

# making a list of parameters to understand their corrlation
x = ["Agricultural land (% of land area)", "Forest area (% of land area)",
     "CO2 emissions (kt)", "Urban population"]
# slicing out the required parameters
brazil = brazil.loc[:, x]
india = india.loc[:, x]

# producing the required heatmap
heatMap(brazil.corr(), "YlGn", "Brazil's Heatmap")
heatMap(india.corr(), "RdYlBu", "India's Heatmap")
