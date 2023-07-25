from bs4 import BeautifulSoup 
import requests 
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#url = 'https://www.mottoauction.com/Auction/Code/X1FBK019'
url = input("Enter url : ")
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

driver.get(url)

for i in range(2):
    driver.execute_script("window.scrollTo(0, 900)")
    time.sleep(2)

soup = BeautifulSoup(driver.page_source,'html.parser')

car_lis = soup.find_all('div',{'class':'carlist-item'})

title_lis = []


body_lis = []
gear_lis = []
color_lis = []
km_lis = []

owner_lis = []
wheel_lis = []
reg_lis = []
province_lis = []


for i in car_lis: 

    title = i.find('header')
    title_lis.append(title.text.strip())
    print(title.text.strip())

    blue_label = i.find('div',{'class':'spec'}).find_all('strong')

    
    body = blue_label[0].text.strip()
    print(body)
    body_lis.append(body)

    gear = blue_label[1].text.strip()
    print(gear)
    gear_lis.append(gear)

    color = blue_label[2].text.strip()
    print(color)
    color_lis.append(color)


    km = blue_label[3].text.strip()
    km_lis.append(km)
    print(km)

    owner = blue_label[4].text.strip()
    owner_lis.append(owner)
    print(owner)

    wheel = blue_label[5].text.strip()
    wheel_lis.append(wheel)
    print(wheel)

    reg = blue_label[6].text.strip()
    reg_lis.append(reg)
    print(reg)

    province = blue_label[7].text.strip()
    print(province)
    province_lis.append(province)

df = pd.DataFrame()

df['Car Name'] = title_lis
df['Body'] = body_lis 
df['Gear'] = gear_lis 
df['Colour'] = color_lis 
df['Km'] = km_lis 
df['Owner'] = owner_lis 
df['Wheel Drive'] = wheel_lis 
df['Reg'] = reg_lis 
df['Province'] = province_lis 

df.to_excel('Car.xlsx')


print("Finish")