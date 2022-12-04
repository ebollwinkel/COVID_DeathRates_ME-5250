#import json module
import json

#import bokeh module for plotting, changing plot colors, and plotting multiple plots
from bokeh.plotting import figure, output_file, show
from bokeh.colors.groups import blue, purple, green, orange, brown
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
    

#split data into world regions
#european countries
european_countries = [countries[3],
                      countries[4],
                      countries[8],
                      countries[9],
                      countries[10],
                      countries[11],
                      countries[12],
                      countries[16]]

european_daily_deaths = [daily_deaths[3],
                      daily_deaths[4],
                      daily_deaths[8],
                      daily_deaths[9],
                      daily_deaths[10],
                      daily_deaths[11],
                      daily_deaths[12],
                      daily_deaths[16]]

european_cumulative_deaths = [cumulative_deaths[3],
                      cumulative_deaths[4],
                      cumulative_deaths[8],
                      cumulative_deaths[9],
                      cumulative_deaths[10],
                      cumulative_deaths[11],
                      cumulative_deaths[12],
                      cumulative_deaths[16]]

#asian countries
asian_countries = [countries[0],
                      countries[2],
                      countries[6],
                      countries[7],
                      countries[13],
                      countries[17],
                      countries[18]]

asian_daily_deaths = [daily_deaths[0],
                      daily_deaths[2],
                      daily_deaths[6],
                      daily_deaths[7],
                      daily_deaths[13],
                      daily_deaths[17],
                      daily_deaths[18]]

asian_cumulative_deaths = [cumulative_deaths[0],
                      cumulative_deaths[2],
                      cumulative_deaths[6],
                      cumulative_deaths[7],
                      cumulative_deaths[13],
                      cumulative_deaths[17],
                      cumulative_deaths[18]]

#american countries (all of the americas)
americas_countries = [countries[1],
                      countries[5],
                      countries[15],
                      countries[19]]

americas_daily_deaths = [daily_deaths[1],
                      daily_deaths[5],
                      daily_deaths[15],
                      daily_deaths[19]]

americas_cumulative_deaths = [cumulative_deaths[1],
                      cumulative_deaths[5],
                      cumulative_deaths[15],
                      cumulative_deaths[19]]

#create list of bar colors
#blues
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

#purples
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

#browns
colors_brown = [brown()._colors[brown()._colors.index("Bisque")],
                 brown()._colors[brown()._colors.index("BurlyWood")],
                 brown()._colors[brown()._colors.index("RosyBrown")],
                 brown()._colors[brown()._colors.index("SandyBrown")],
                 brown()._colors[brown()._colors.index("Chocolate")],
                 brown()._colors[brown()._colors.index("DarkGoldenrod")],
                 brown()._colors[brown()._colors.index("Peru")],
                 brown()._colors[brown()._colors.index("SaddleBrown")]]

#greens
colors_green = [green()._colors[green()._colors.index("LimeGreen")],
                green()._colors[green()._colors.index("Chartreuse")],
                green()._colors[green()._colors.index("SpringGreen")],
                green()._colors[green()._colors.index("LightGreen")],
                green()._colors[green()._colors.index("DarkSeaGreen")],
                green()._colors[green()._colors.index("SeaGreen")],
                green()._colors[green()._colors.index("DarkGreen")]]

#orange
colors_orange = [orange()._colors[orange()._colors.index("OrangeRed")],
                 orange()._colors[orange()._colors.index("Coral")],
                 orange()._colors[orange()._colors.index("DarkOrange")],
                 orange()._colors[orange()._colors.index("Orange")]]
                

#begin plotting data from worldometer
#PLOT DAILY DEATH RATES
#instantiate figure object
daily_plot = figure(title="Daily Deaths due to COVID", x_range=countries, width=1400)

#plot data
daily_plot.vbar(x=european_countries, top=european_daily_deaths, color = colors_brown, legend_label= 'europe')
daily_plot.vbar(x=asian_countries, top=asian_daily_deaths, color = colors_green, legend_label='asia')
daily_plot.vbar(x=americas_countries, top=americas_daily_deaths, color = colors_orange, legend_label= 'americas')
daily_plot.vbar(x=countries, top=daily_deaths, color=colors_blue, legend_label=" all countries")

#enable interactive legend
daily_plot.legend.click_policy = "hide"

#PLOT CUMULATIVE DEATH RATES
cumulative_plot = figure(title="Cumulative Deaths due to COVID", x_range=countries, width=1400)

#plot data
cumulative_plot.vbar(x=countries, top=cumulative_deaths, color=colors_purple, legend_label="cumulative deaths")

#enable interactive legend
cumulative_plot.legend.click_policy = "hide"

both_plots = column(daily_plot, cumulative_plot)
show(both_plots)