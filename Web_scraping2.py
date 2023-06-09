from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import csv
URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(URL)
headers=["Star_name","Distance","Mass","Radius"]


time.sleep(1)
final_data=[]
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find_all("table")
table_rows=star_table[7].find_all('tr')
temp_list=[]
for trTag in table_rows:
    tdTags=trTag.find_all("td")
    row = [i.text.rstrip() for i in tdTags]
    temp_list.append(row)

Star_name=[]
distance=[]
mass=[]
radius=[]      
for i in range(1,len(temp_list)):
    Star_name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])
print(Star_name)
for index,name in enumerate(Star_name):
    final_data.append([name,distance[index],mass[index],radius[index]])

print(Star_name)
print(distance)
print(mass)
print(radius)
    
    
with open('Scrapeddata_csv.csv','w',newline='',encoding='utf8')as f:
    writer=csv.writer(f)
    writer.writerow(headers)
    writer.writerows(final_data)