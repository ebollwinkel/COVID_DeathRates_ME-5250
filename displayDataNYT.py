#Script to plot data from dataNYT.json file using the bokeh module

##### IMPORT NECESSARY MODULES #####
#import json module
import json

#import bokeh module for plotting, changing plot colors, and plotting multiple plots
from bokeh.plotting import figure, output_file, show
from bokeh.colors.groups import blue, green, orange, brown
from bokeh.layouts import column

#### GET DATA FROM JSON FILE ####
#open json file for NYT website
json_data = open('dataNYT.json')

#open json file
with open('dataNYT.json') as json_data:
    covid_data = json.load(json_data)
    
#create list of country names
countries = list(covid_data.keys())
countries = countries[1:11] #get rid of data that is not the name of a country

#initialize empty array for daily and cumulative deaths
daily_deaths = []

#loop through covid_data to fill arrays of daily death rates
for name in countries:
    daily_deaths.append(covid_data[name])

#split data into world regions
#european countries
european_countries = [countries[0],
                      countries[7],
                      countries[8],
                      countries[9]]

european_daily_deaths = [daily_deaths[0],
                      daily_deaths[7],
                      daily_deaths[8],
                      daily_deaths[9]]

#asian countries
asian_countries = [countries[1],
                      countries[2],
                      countries[3],
                      countries[4]]

asian_daily_deaths = [daily_deaths[1],
                      daily_deaths[2],
                      daily_deaths[3],
                      daily_deaths[4]]

#oceania countries
oceania_countries = [countries[5],
                      countries[6]]

oceania_daily_deaths = [daily_deaths[5],
                      daily_deaths[6]]


#### CREATE LISTS OF COLORS FOR BAR PLOTS ####
#blues (for daily deaths)
colors_blue = [blue()._colors[blue()._colors.index("LightSteelBlue")],
          blue()._colors[blue()._colors.index("SkyBlue")],
          blue()._colors[blue()._colors.index("DodgerBlue")],
          blue()._colors[blue()._colors.index("SteelBlue")],
          blue()._colors[blue()._colors.index("MediumBlue")],
          blue()._colors[blue()._colors.index("LightSteelBlue")],
          blue()._colors[blue()._colors.index("SkyBlue")],
          blue()._colors[blue()._colors.index("DodgerBlue")],
          blue()._colors[blue()._colors.index("SteelBlue")],
          blue()._colors[blue()._colors.index("MediumBlue")]]

#browns (for european countries)
colors_brown = [brown()._colors[brown()._colors.index("Bisque")],
                 brown()._colors[brown()._colors.index("RosyBrown")],
                 brown()._colors[brown()._colors.index("Chocolate")],
                 brown()._colors[brown()._colors.index("Peru")]]

#greens (for asian countries)
colors_green = [green()._colors[green()._colors.index("LimeGreen")],
                green()._colors[green()._colors.index("Chartreuse")],
                green()._colors[green()._colors.index("LightGreen")],
                green()._colors[green()._colors.index("SeaGreen")]]

#orange (for oceania countries)
colors_orange = [orange()._colors[orange()._colors.index("OrangeRed")],
                 orange()._colors[orange()._colors.index("DarkOrange")]]


#### PLOT DATA FROM NYT ####
#PLOT DAILY DEATH RATES
#instantiate figure object
daily_plot = figure(title="Daily Deaths due to COVID", x_range=countries, width=1400)

#plot data
daily_plot.vbar(x=european_countries, top=european_daily_deaths, color = colors_brown, legend_label= 'Europe')
daily_plot.vbar(x=asian_countries, top=asian_daily_deaths, color = colors_green, legend_label='Asia')
daily_plot.vbar(x=oceania_countries, top=oceania_daily_deaths, color = colors_orange, legend_label= 'Oceania')
daily_plot.vbar(x=countries, top=daily_deaths, color=colors_blue, legend_label="all countries")

#enable interactive legend
daily_plot.legend.click_policy = "hide"

#generate web page with both plots
both_plots = column(daily_plot)
show(daily_plot)