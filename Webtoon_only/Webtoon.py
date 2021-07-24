from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.lezhin.com'
week = ['/ko/scheduled?day=1', '/ko/scheduled?day=2', '/ko/scheduled?day=3', '/ko/scheduled?day=4', '/ko/scheduled?day=5', '/ko/scheduled?day=6', '/ko/scheduled?day=0', '/ko/scheduled?day=n']
day_id = ['scheduled-day-1', 'scheduled-day-2', 'scheduled-day-3', 'scheduled-day-4', 'scheduled-day-5', 'scheduled-day-6', 'scheduled-day-0', 'scheduled-day-n']

id_list = []
title_list = []
author_list = []
genre_list = []
tags_list = []
platform_list = []
age_list = []
rate_list = []
complete_list = []
thumbnail_list = []
url_list = []
num = 0

for i in range(8):
    URL = url + week[i]
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=r'C:/Users/82108/Downloads/chromedriver_win32/chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get(URL)

    sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    tmp = soup.find('ul', {'id' : day_id[i]})
    title = tmp.find_all('div', {'class' : 'lzComic__title'})
    author = tmp.find_all('span', {'class' : 'lzComic__artist'})
    genre = tmp.find_all('span', {'class' : 'lzComic__genre'})
    url_tmp = []
    for href in tmp.find_all('li', {'class' : 'lzComic__item'}):
        url_tmp.append(url + href.find('a')['href'])
    
    p = 0

    for j in range(len(title)):
        t = title[j].text
        if (t in title_list):
            p += 1
            continue

        id_list.append(num)
        num += 1
        title_list.append(t)
        author_list.append(author[j].text)
        genre_list.append(genre[j].text)
        platform_list.append('레진코믹스')
        url_list.append(url_tmp[j])

        driver.get(url_tmp[j])
        sleep(1)

        p += 1

        '''
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'comicInfo__category comicInfo__category--genre')
            )
        )
        '''
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        '''
        genre = soup.find('span', {'class' : 'comicInfo__category comicInfo__category--genre'})
        genre_list.append(genre)
        '''

        tags = soup.find('div', {'class' : 'comicInfo__tags'}).text.strip()
        tags_list.append(tags)

        driver.back()

        sleep(3)

        

total_data = pd.DataFrame()
total_data['id'] = id_list
total_data['title'] = title_list
total_data['author'] = author_list
total_data['genre'] = genre_list
total_data['tag'] = tags_list
total_data['platform'] = platform_list
total_data['age'] = age_list
total_data['rate'] = rate_list
total_data['complete'] = complete_list
total_data['thumbnail'] = thumbnail_list
total_data['website'] = url_list
total_data.to_csv('레진코믹스_웹툰.csv', encoding='utf-8-sig')