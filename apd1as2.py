  # -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 10:38:33 2023

@author: manus
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#pd.set_option('display.max_rows',None)
#pd.set_option('display.max_columns',None)
#pd.set_option('display.width',None)
#pd.set_option('display.max_colwidth',None)

def read_file(file_name,yrs,cntrs,col,indicator):
    df0= pd.read_csv(file_name, skiprows=4)
    df1=df0.groupby(col, group_keys= True)
    df1= df1.get_group(indicator)
    df1 = df1.reset_index()
    a = df1['Country Name']
    df1= df1.iloc[cntrs,yrs]
    df1= df1.dropna(axis = 1)
    df1.insert(loc=0, column='Country Name', value=a)
    df2 = df1.transpose()
    df2 = df1.set_index('Country Name').T
    return df1,df2

def plot_bar(data, col, ylbl, titl):
    ax=data.plot(x=col, rot=45, figsize=(50,25), kind= 'bar', title= titl,fontsize=50)
    ax.legend(fontsize=36)
    ax.set_xlabel('Country', fontsize=40)
    ax.set_ylabel(ylbl,fontsize=40)
    ax.set_title(titl,pad=20, fontdict={'fontsize':40})
    return


def plot_line(data, ylbl, titl):
    ax=data.plot(linestyle='dashdot',figsize=(50,25), kind= 'line', fontsize=50)
    legend_properties = {'weight':'bold','size':36}
    ax.legend(fontsize=36, prop=legend_properties)
    ax.set_xlabel('Year', fontsize=40)
    ax.set_ylabel(ylbl,fontsize=40)
    ax.set_title(titl,pad=20, fontdict={'fontsize':40})
    return

def stats_f(file_name,years,col, value1):
    df= pd.read_csv(file_name, skiprows=4)
    df1=df.groupby(col, group_keys= True)
    df1= df1.get_group(value1)
    df1 = df1.reset_index()
    df1= df1.iloc[:,years]
    df1= df1.dropna(axis = 0)
    df1= df1.dropna(axis = 1)
    df2 = df1.set_index("Indicator Name").T
    return df2


def heatMap(value2, colours,title_name):
    fig, ax = plt.subplots( figsize=(20,20))
    im = ax.imshow(value2,cmap=colours)
    cbar = ax.figure.colorbar(im,ax = ax,shrink=0.85 )
    # add tick labels
    ax.set_xticks(np.arange(len(x)),labels=x,size=20)
    ax.set_yticks(np.arange(len(x)),labels=x,size=20)
    # Rotate the tick labels to be more legible
    plt.setp(ax.get_xticklabels(),rotation = 90,ha = "right",rotation_mode = "anchor")
    ax.set_title(title_name, size=30)
    fig.tight_layout()

    
years = [5,10,15,20,25,30,35,40,45,50,55,60,65]
year=[5,15,25,35,45,55,65]
countries=[29,40,55,77,81,109,263]
aglnd_1,aglnd_2=read_file("API_19_DS2_en_csv_v2_5346672.csv",year,countries,"Indicator Name","Agricultural land (% of land area)")
arable_1,arable_2=read_file("API_19_DS2_en_csv_v2_5346672.csv",years,countries,"Indicator Name","Arable land (% of land area)")
forest_1,forest_2=read_file("API_19_DS2_en_csv_v2_5346672.csv",years,countries,"Indicator Name","Forest area (% of land area)")
co2_1,co2_2=read_file("API_19_DS2_en_csv_v2_5346672.csv",years,countries,"Indicator Name","CO2 emissions from liquid fuel consumption (kt)")
urbp_1,urbp_2=read_file("API_19_DS2_en_csv_v2_5346672.csv",year,countries,"Indicator Name","Urban population (% of total population)")
urbp_3,urbp_4=read_file("API_19_DS2_en_csv_v2_5346672.csv",year,countries,"Indicator Name","Urban population")


co2_d=co2_1.describe()
co2_d.to_csv('CO2des.csv')

plot_bar(urbp_1,"Country Name",'Number','Urban population')
plot_bar(urbp_3,"Country Name",'Percentage','Urban population (% of total population)')
plot_bar(aglnd_1,"Country Name",'Percentage','Agricultural land (% of land area))')
plot_line(co2_2,'Kiloton(kt)','CO2 emissions from liquid fuel consumption (kt)')
plot_line(arable_2,'Percentage','Arable land (% of land area)')
plot_line(forest_2,'Percentage','Forest area (% of land area)')


#color=['viridis', 'plasma', 'inferno', 'magma', 'cividis']
brazil = stats_f("API_19_DS2_en_csv_v2_5346672.csv",[3,35,40,45,50,55,60,64],"Country Name","Brazil")
india=stats_f("API_19_DS2_en_csv_v2_5346672.csv",[3,35,40,45,50,55,60,64],"Country Name","Brazil")
x=["Agricultural land (% of land area)","Forest area (% of land area)","CO2 emissions (kt)","Urban population"]
brazil = brazil.loc[:,x ]
india=india.loc[:,x]
heatMap(brazil.corr(),"YlGn","Brazil's Heatmap")
heatMap(india.corr(),"RdYlBu","India's Heatmap")  
