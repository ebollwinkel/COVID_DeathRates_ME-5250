# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
import json
import datetime as dt

def scrape_country(country, website):
    if website == "Worldometer":
        scrape_worldometer(country)
    elif website == "NYT": 
        scrape_nyt(country)

def scrape_worldometer(country):
    response = requests.get("https://www.worldometers.info/coronavirus/#countries")
    if response.status_code != 200:
        print("Error fetching page")
        exit()
    else:
        content = response.content
    soup = BeautifulSoup(content,"html.parser")
    table = soup.find(id="main_table_countries_yesterday2")
    table_tr = table.find('tbody').find_all('tr')
    headers_tr = table.find('thead').find('tr')
    headers = []
    count_data = []
    for i in headers_tr:
        newString = ""
        for j in i:
            if (str(j) == '\n'):
                pass
            elif (str(j) == "<br/>"):
                newString = newString + " "
            else:
                newString = newString + str(j)
        if newString == '':
            pass
        else:
            newString = newString.replace('\xa0',' ')
            newString = newString.replace('<nobr>', '')
            newString = newString.replace('</nobr>', '')
            headers.append(newString)
        
    headers = headers[0:15]
        #for j in i.children:
            #if (str(j) == "<nobr>") or (str(j) == '\n'):
                #pass
            #elif str(j) == '<br/>':
                #newString = newString + " "
            #else:
                #newString = newString + str(j)
       # if newString == "":
            #pass
        #else:
            
            #headers.append(newString)
    #headers.pop(-1)
    #print(headers)
    #print(len(headers))
    #print(us_html_data)
    
    for i in table_tr:
        myString = ""
        myList = []
        #myList = i.get_text().strip().split('\n')
        #print(myList)
        row = i.contents
        #print(len(row))
        for j in range(0,30):
            if j % 2 == 0:
                continue
            try:
                myList.append(int(sliceCarrot(str(row[j]).replace('\n','').replace(',','')).strip().replace('+','')))
            except ValueError:
                myList.append(sliceCarrot(str(row[j]).replace('\n','').replace(',','')).strip().replace('+',''))
        count_data.append(myList)
        #print(len(myList))
    #print(count_data)
    
        #for j in row:
            #print(j)
        #newString = ""
        #for j in i:
            #if (str(j) == '\n'):
                #pass
           # else:
                #newString = str(j).replace('+','')
        #if newString == "":
            #pass
        #else:
            #print(newString)
            #try:
                #count_data.append(int(newString.replace(',','')))
            #except ValueError:
                #count_data.append(None)
    #count_data.insert(0,None)
    #print(count_data)
    #print(len(headers)==len(count_data))
     
    dataDict = {}
    for i in range(len(count_data)):
        myDict = {}
        for j in range(2,len(headers)):
            myDict.update({headers[j]:count_data[i][j]})
        dataDict.update({count_data[i][1]:myDict})
    
    deaths = {"Date Scraped" : str(dt.datetime.now())}
    keys = dataDict.keys()
    for i in keys:
        if (i == "Asia") or (i == "North America") or (i == "South America") or (i == "Europe") or (i == "Africa") or (i == "Oceania") or (i == "World"):
            continue
        deaths.update({i: {"Total Deaths": dataDict[i]["Total Deaths"], "Daily Deaths": dataDict[i]["New Deaths"]}})
    fileDict = {}
    if country == "All":
        fileDict.update(deaths)
        jsonString = json.dumps(fileDict)
        with open("data.json", "w") as i:
            i.write(jsonString)
    else:
        fileDict.update(deaths["Date Scraped"])
        fileDict.update(deaths[country])
        jsonString = json.dumps(fileDict)
        with open("data.json", "w") as i:
            i.write(jsonString)
    
    #print(dataDict)

    #deaths = {"Date Scraped": str(dt.datetime.now()), "Total Deaths": dataDict["Total Deaths"], "Daily Deaths": dataDict["New Deaths"]}
    #jsonString = json.dumps(deaths)
    #with open("data.json", "w") as i:
        #i.write(jsonString)
def sliceCarrot(myString):
    startInd = -1
    endInd = len(myString)+1
    riseStart = 0
    riseEnd = 0
    for i in range(len(myString)):
        if myString[i] == '<':
            riseStart = 1
        if myString[i] == '>':
            riseStart = 0
        if (riseStart == 0) and (riseEnd == 1) and (startInd == -1):
            startInd = i + 1
        if (startInd > (-1)) and (riseStart == 1) and (riseEnd == 0):
            endInd = i            
        if myString[i] == '<':
            riseEnd = 1
        if myString[i] == '>':
            riseEnd = 0
    if (startInd == -1) and (endInd == len(myString)+1):
        return myString
    elif myString[startInd:endInd].__contains__('<'):
        return sliceCarrot(myString[startInd:endInd])
    else:
        return myString[startInd:endInd]
scrape_country("All", "Worldometer")
#print(sliceCarrot('<span style="color:#00B5F0; font-style:italic; ">MS Zaandam</span>'))


def scrape_nyt(country):
    # URL to New York Times World Covid Data
    URL = "https://www.nytimes.com/interactive/2021/world/covid-cases.html"
    page = requests.get(URL)

    # Connect to URL and find data table
    soup = BeautifulSoup(page.content, "html.parser")
    tables = soup.findChildren('table')

    # Get second table
    my_table = tables[1]

    # Find tbody children elements of the data table
    tbody = my_table.findChildren(['tbody'])

    # Find all tr elements in tbody
    rows = tbody[1].find_all('tr')

    # Create new dictionary for data and add time stamp
    data = {}
    data["Date Scraped"] = str(dt.datetime.now())

    # Scrape data and save to data dictionary
    for row in rows: 
        country_element = row.find("td", class_="name")
        deaths_element = row.find_all("td")
        country_name = country_element.text.strip()
        death_num = deaths_element[4].text.strip()
        if(country_name.__contains__("\xa0›")): 
            country_name = country_name[:len(country_name)-2]

        data[country_name] = death_num
    
    # Save data to json file
    with open("dataNYT.json", "w") as writeJSON:
        json.dump(data, writeJSON, ensure_ascii=False)

