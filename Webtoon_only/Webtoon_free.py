from logging import NullHandler
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.lezhin.com/ko/free?genre=_all&page='
# 레진코믹스 카테고리 별 url

title_list = []

for i in range(3):
    URL = url + str(i)
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=r'C:/Users/82108/Downloads/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get(URL)

    sleep(0.5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    tmp = soup.find('section', {'id' : 'free-list'})
    title = tmp.find_all('div', {'class' : 'lzComic__title'})

    for j in range(len(title)):
        t = title[j].text
        if (t in title_list):
            continue
        
        title_list.append(t)
    sleep(3)

    ##### 완결목록 분류 #####

##### 기다리면 무료 따로 분류 #####

total_data = pd.DataFrame()
total_data['title'] = title_list
total_data.to_csv('레진코믹스_웹툰_무료.csv', encoding='utf-8-sig')