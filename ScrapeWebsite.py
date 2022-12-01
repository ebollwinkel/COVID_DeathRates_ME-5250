# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
import re

def scrape_country(country, website):
    response = requests.get("https://www.worldometers.info/coronavirus/country/us/")
    if response.status_code != 200:
        print("Error fetching page")
        exit()
    else:
        content = response.content
    soup = BeautifulSoup(content,"html.parser")
    table = soup.find(id="usa_table_countries_yesterday")
    table_tr = table.find_all('tr')
    headers_tr = table_tr[0]
    us_html_data = table_tr[1]
    headers = []
    us_data = []
    #for i in headers_tr.children:
        #newString = ""
        #for j in i:
            #print(type(j))
            #if (str(j) == "<nobr>") or (str(j) == '\n'):
                #pass
            #elif str(j) == '<br/>':
                #newString = newString + " "
           # else:
                #newString = newString + str(j)
        #if newString == "":
            #pass
        #else:
            #newString = newString.replace('\xa0',' ')
            #newString = newString.replace('<nobr>', '')
            #newString = newString.replace('</nobr>', '')
            #headers.append(newString)
        
    print(headers)
    #print(us_html_data)
    for i in us_html_data:
        newString = ""
        for j in i:
            if (str(j) == '\n'):
                pass
            else:
                newString = str(j).replace('+','')
        if newString == "":
            pass
        else:
            us_data.append(int(newString))
    print(us_data)
def flatten(myList):
    newList = []
    for i in myList:
        if type(i) is list:
            newList.extend(flatten(i))
        else:    
            newList.append(i)
    return newList
scrape_country(1,1)