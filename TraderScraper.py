from bs4 import BeautifulSoup
import requests
#In the funture use either lines 4 and 5 to make a csv file for the data
#import csv
#import os
#Or pandas can make the csv file
#import pandas as pd

all_trade_pages = []

def page_adder(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, features="html.parser")
    num_of_pages = soup.find_all('b')
    max_pages = max((int(tag.text) for tag in num_of_pages), default=1)
    base_url = url.split('?')[0]
    for p in range(1, max_pages + 1):
        all_trade_pages.append(f"{base_url}?page={p}")

#In future try to go to https://www.capitoltrades.com/politicians
#then use soup to go to each politican instead of manually grabbing every url
#that way you can get all poiticans faster
politician = [
    #Only first 12 politicians to show up
    "https://www.capitoltrades.com/politicians/A000148", #Jake Auchincloss
    "https://www.capitoltrades.com/politicians/M001236", #Tim Moore
    "https://www.capitoltrades.com/politicians/E000296", #Dwight Evans
    "https://www.capitoltrades.com/politicians/K000375", #Bill Keating
    "https://www.capitoltrades.com/politicians/J000305", #Sara jacobs
    "https://www.capitoltrades.com/politicians/C001103", #Buddy Carter
    "https://www.capitoltrades.com/politicians/S001203", #Tina Smith
    "https://www.capitoltrades.com/politicians/M001242", #Bernie Moreno
    "https://www.capitoltrades.com/politicians/S001211", #Greg Stanton
    "https://www.capitoltrades.com/politicians/B001291", #Brian Babin
    "https://www.capitoltrades.com/politicians/M001234", #Kelly Morrison
    "https://www.capitoltrades.com/politicians/C001068" #Steve Cohen

]

politician_page_1 = [site + "?page=1" for site in politician]
for site in politician_page_1:
    page_adder(site)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

for url in all_trade_pages:
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, features="html.parser")

    table = soup.find('table')

    if table is None:
        if url.endswith("?page=1"):
            name = soup.find('h1').text.strip()
            print(name)
            print("No trade activity in the last 3 years")
        continue

    world_titles = soup.find_all('th')

    world_table_titles = [title.text for title in world_titles]
    #print(world_table_titles[:6])

    name = soup.find('h1').text.strip()
    #table = soup.find('table')
    column_data = table.find_all('tr')

    if url.endswith("?page=1"):
        print(name)
        print(world_table_titles[:6])

    for row in column_data:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data[:-1]]
        if individual_row_data:
            print(individual_row_data)


