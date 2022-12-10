#Script to plot data from data.json and dataNYT.json file using the bokeh module

##### IMPORT NECESSARY MODULES #####
#import json module
import json

#import bokeh module for plotting, changing plot colors, and plotting multiple plots
from bokeh.plotting import figure, output_file, show
from bokeh.colors.groups import blue, purple, green, orange, brown, yellow
from bokeh.layouts import column

#### GET DATA FROM JSON FILE ####
#open json file for worldometer website
json_data = open('data.json')
#open json file for NYT website
json_data_NYT = open('dataNYT.json')

#open json file
with open('data.json') as json_data:
    covid_data = json.load(json_data)

with open('dataNYT.json') as json_data_NYT:
    covid_data_NYT = json.load(json_data_NYT)

#create list of country names
all_countries = []
for entry in covid_data:
    all_countries.append(list(covid_data[entry].keys()))

#flatten all_countries nested list
countries_WoM = list()
for sub_list in all_countries:
    countries_WoM += sub_list

countries_WoM = countries_WoM[1:21] #only use 20 countries for plot readability

#create list of country names from NYT
countries_NYT = list(covid_data_NYT.keys())
countries_NYT = countries_NYT[1:11] #get rid of data that is not the name of a country

#initialize empty array for daily and cumulative deaths
daily_deaths = []
daily_deaths_NYT = []
cumulative_deaths = []

#loop through covid_data to fill arrays of daily and cumulative death rates
for entry in covid_data:
    for name in countries_WoM:
        daily_deaths.append(covid_data[entry][name]['Daily Deaths'])
        cumulative_deaths.append(covid_data[entry][name]['Total Deaths'])

for name in countries_NYT:
    daily_deaths_NYT.append(covid_data_NYT[name])


#split data into world regions from worldometer data
#european countries
european_countries = [countries_WoM[3],
                      countries_WoM[4],
                      countries_WoM[8],
                      countries_WoM[9],
                      countries_WoM[10],
                      countries_WoM[11],
                      countries_WoM[12],
                      countries_WoM[16]]

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
asian_countries = [countries_WoM[0],
                      countries_WoM[2],
                      countries_WoM[6],
                      countries_WoM[7],
                      countries_WoM[13],
                      countries_WoM[17],
                      countries_WoM[18]]

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
americas_countries = [countries_WoM[1],
                      countries_WoM[5],
                      countries_WoM[15],
                      countries_WoM[19]]

americas_daily_deaths = [daily_deaths[1],
                      daily_deaths[5],
                      daily_deaths[15],
                      daily_deaths[19]]

americas_cumulative_deaths = [cumulative_deaths[1],
                      cumulative_deaths[5],
                      cumulative_deaths[15],
                      cumulative_deaths[19]]


#split data into world regions from NYT data
#european countries
european_countries_NYT = [countries_NYT[0],
                      countries_NYT[7],
                      countries_NYT[8],
                      countries_NYT[9]]

european_daily_deaths_NYT = [daily_deaths_NYT[0],
                      daily_deaths_NYT[7],
                      daily_deaths_NYT[8],
                      daily_deaths_NYT[9]]

#asian countries
asian_countries_NYT = [countries_NYT[1],
                      countries_NYT[2],
                      countries_NYT[3],
                      countries_NYT[4]]

asian_daily_deaths_NYT = [daily_deaths_NYT[1],
                      daily_deaths_NYT[2],
                      daily_deaths_NYT[3],
                      daily_deaths_NYT[4]]

#oceania countries
oceania_countries_NYT = [countries_NYT[5],
                      countries_NYT[6]]

oceania_daily_deaths_NYT = [daily_deaths_NYT[5],
                      daily_deaths_NYT[6]]


#### CREATE LISTS OF COLORS FOR BAR PLOTS FOR WORLDOMETER ####
#blues (for daily deaths)
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

#purples (for cumulative deaths)
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

#browns (for european countries)
colors_brown = [brown()._colors[brown()._colors.index("Bisque")],
                 brown()._colors[brown()._colors.index("BurlyWood")],
                 brown()._colors[brown()._colors.index("RosyBrown")],
                 brown()._colors[brown()._colors.index("SandyBrown")],
                 brown()._colors[brown()._colors.index("Chocolate")],
                 brown()._colors[brown()._colors.index("DarkGoldenrod")],
                 brown()._colors[brown()._colors.index("Peru")],
                 brown()._colors[brown()._colors.index("SaddleBrown")]]

#greens (for asian countries)
colors_green = [green()._colors[green()._colors.index("LimeGreen")],
                green()._colors[green()._colors.index("Chartreuse")],
                green()._colors[green()._colors.index("SpringGreen")],
                green()._colors[green()._colors.index("LightGreen")],
                green()._colors[green()._colors.index("DarkSeaGreen")],
                green()._colors[green()._colors.index("SeaGreen")],
                green()._colors[green()._colors.index("DarkGreen")]]

#orange (for americas countries)
colors_orange = [orange()._colors[orange()._colors.index("OrangeRed")],
                 orange()._colors[orange()._colors.index("Coral")],
                 orange()._colors[orange()._colors.index("DarkOrange")],
                 orange()._colors[orange()._colors.index("Orange")]]


#### CREATE LISTS OF COLORS FOR BAR PLOTS FOR NYT ####
#blues (for daily deaths)
colors_blue_NYT = [blue()._colors[blue()._colors.index("LightSteelBlue")],
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
colors_brown_NYT = [brown()._colors[brown()._colors.index("Bisque")],
                 brown()._colors[brown()._colors.index("RosyBrown")],
                 brown()._colors[brown()._colors.index("Chocolate")],
                 brown()._colors[brown()._colors.index("Peru")]]

#greens (for asian countries)
colors_green_NYT = [green()._colors[green()._colors.index("LimeGreen")],
                green()._colors[green()._colors.index("Chartreuse")],
                green()._colors[green()._colors.index("LightGreen")],
                green()._colors[green()._colors.index("SeaGreen")]]

#yellow (for oceania countries)
colors_yellow_NYT = [yellow()._colors[yellow()._colors.index("Yellow")],
                 yellow()._colors[yellow()._colors.index("Gold")]]


#### PLOT DATA FROM WORLDOMETER ####
#PLOT DAILY DEATH RATES
#instantiate figure object
daily_plot = figure(title="Daily Deaths due to COVID\nWorldometer data", x_range=countries_WoM, width=1400)

#plot data
daily_plot.vbar(x=european_countries, top=european_daily_deaths, color = colors_brown, legend_label= 'Europe')
daily_plot.vbar(x=asian_countries, top=asian_daily_deaths, color = colors_green, legend_label='Asia')
daily_plot.vbar(x=americas_countries, top=americas_daily_deaths, color = colors_orange, legend_label= 'Americas')
daily_plot.vbar(x=countries_WoM, top=daily_deaths, color=colors_blue, legend_label=" All countries")

#enable interactive legend
daily_plot.legend.click_policy = "hide"

#PLOT CUMULATIVE DEATH RATES
#instantiate figure object
cumulative_plot = figure(title="Cumulative Deaths due to COVID\nWorldometer data", x_range=countries_WoM, width=1400)

#plot data
cumulative_plot.vbar(x=european_countries, top=european_cumulative_deaths, color = colors_brown, legend_label= 'Europe')
cumulative_plot.vbar(x=asian_countries, top=asian_cumulative_deaths, color = colors_green, legend_label= 'Asia')
cumulative_plot.vbar(x=americas_countries, top=americas_cumulative_deaths, color = colors_orange, legend_label='Americas')
cumulative_plot.vbar(x=countries_WoM, top=cumulative_deaths, color=colors_purple, legend_label="Cumulative deaths")

#enable interactive legend
cumulative_plot.legend.click_policy = "hide"

#### PLOT DATA FROM NYT ####
#PLOT DAILY DEATH RATES
#instantiate figure object
daily_plot_NYT = figure(title="Daily Deaths due to COVID\nNYTimes data", x_range=countries_NYT, width=1400)

#plot data
daily_plot_NYT.vbar(x=european_countries_NYT, top=european_daily_deaths_NYT, color = colors_brown_NYT, legend_label= 'Europe')
daily_plot_NYT.vbar(x=asian_countries_NYT, top=asian_daily_deaths_NYT, color = colors_green_NYT, legend_label='Asia')
daily_plot_NYT.vbar(x=oceania_countries_NYT, top=oceania_daily_deaths_NYT, color = colors_yellow_NYT, legend_label= 'Oceania')
daily_plot_NYT.vbar(x=countries_NYT, top=daily_deaths_NYT, color=colors_blue_NYT, legend_label="all countries")

#enable interactive legend
daily_plot_NYT.legend.click_policy = "hide"

#generate web page with both plots
plots = column(daily_plot, cumulative_plot, daily_plot_NYT)
show(plots)




