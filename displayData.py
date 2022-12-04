#import json module
import json

#import bokeh module for plotting, changing plot colors, and plotting multiple plots
from bokeh.plotting import figure, output_file, show
from bokeh.colors.groups import blue, purple
from bokeh.layouts import column

#open json file for worldometer website
json_data = open('data.json')

#open json file
with open('data.json') as json_data:
    covid_data = json.load(json_data)

#create list of country names
countries = list(covid_data.keys())
countries = countries[2:22] #get rid of data that is not the name of a country

#initialize empty array for daily and cumulative deaths
daily_deaths = []
cumulative_deaths = []

#loop through covid_data to fill arrays of daily and cumulative death rates
for name in countries:
    daily_deaths.append(covid_data[name]['Daily Deaths'])
    cumulative_deaths.append(covid_data[name]['Total Deaths'])
    

#begin plotting data from worldometer
#PLOT DAILY DEATH RATES
#instantiate figure object
daily_plot = figure(title="Daily Deaths due to COVID", x_range=countries, width=1400)

#create list of bar colors
colors_blue = [blue()._colors[blue()._colors.index("LightSteelBlue")],
          blue()._colors[blue()._colors.index("PowderBlue")],
          blue()._colors[blue()._colors.index("SkyBlue")],
          blue()._colors[blue()._colors.index("DeepSkyBlue")],
          blue()._colors[blue()._colors.index("DodgerBlue")],
          blue()._colors[blue()._colors.index("CornflowerBlue")],
          blue()._colors[blue()._colors.index("SteelBlue")],
          blue()._colors[blue()._colors.index("RoyalBlue")],
          blue()._colors[blue()._colors.index("MediumBlue")],
          blue()._colors[blue()._colors.index("MidnightBlue")],
          blue()._colors[blue()._colors.index("LightSteelBlue")],
          blue()._colors[blue()._colors.index("PowderBlue")],
          blue()._colors[blue()._colors.index("SkyBlue")],
          blue()._colors[blue()._colors.index("DeepSkyBlue")],
          blue()._colors[blue()._colors.index("DodgerBlue")],
          blue()._colors[blue()._colors.index("CornflowerBlue")],
          blue()._colors[blue()._colors.index("SteelBlue")],
          blue()._colors[blue()._colors.index("RoyalBlue")],
          blue()._colors[blue()._colors.index("MediumBlue")],
          blue()._colors[blue()._colors.index("MidnightBlue")]]

#plot data
daily_plot.vbar(x=countries, top=daily_deaths, color=colors_blue)

#PLOT CUMULATIVE DEATH RATES
cumulative_plot = figure(title="Cumulative Deaths due to COVID", x_range=countries, width=1400)

#create list of bar colors
colors_purple = [purple()._colors[purple()._colors.index("Thistle")],
                 purple()._colors[purple()._colors.index("Plum")],
                 purple()._colors[purple()._colors.index("Orchid")],
                 purple()._colors[purple()._colors.index("Magenta")],
                 purple()._colors[purple()._colors.index("MediumOrchid")],
                 purple()._colors[purple()._colors.index("MediumPurple")],
                 purple()._colors[purple()._colors.index("DarkViolet")],
                 purple()._colors[purple()._colors.index("DarkMagenta")],
                 purple()._colors[purple()._colors.index("Indigo")],
                 purple()._colors[purple()._colors.index("SlateBlue")],
                 purple()._colors[purple()._colors.index("Thistle")],
                 purple()._colors[purple()._colors.index("Plum")],
                 purple()._colors[purple()._colors.index("Orchid")],
                 purple()._colors[purple()._colors.index("Magenta")],
                 purple()._colors[purple()._colors.index("MediumOrchid")],
                 purple()._colors[purple()._colors.index("MediumPurple")],
                 purple()._colors[purple()._colors.index("DarkViolet")],
                 purple()._colors[purple()._colors.index("DarkMagenta")],
                 purple()._colors[purple()._colors.index("Indigo")],
                 purple()._colors[purple()._colors.index("SlateBlue")]]

#plot data
cumulative_plot.vbar(x=countries, top=cumulative_deaths, color=colors_purple)

both_plots = column(daily_plot, cumulative_plot)
show(both_plots)