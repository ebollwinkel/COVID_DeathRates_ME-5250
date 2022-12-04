#import json module
import json

#import bokeh module
from bokeh.plotting import figure, output_file, show

#open json file for worldometer website
json_data = open('data.json')

#open json file
with open('data.json') as json_data:
    covid_data = json.load(json_data)

#create list of country names
countries = list(covid_data.keys())
countries = countries[2:] #get rid of data that is not the name of a country

#initialize empty array for daily and cumulative deaths
daily_deaths = []
cumulative_deaths = []

#loop through covid_data to fill arrays of daily and cumulative death rates
for name in countries:
    daily_deaths.append(covid_data[name]['Daily Deaths'])
    cumulative_deaths.append(covid_data[name]['Total Deaths'])
    

