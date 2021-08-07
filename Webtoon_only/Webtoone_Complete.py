from logging import NullHandler
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.lezhin.com'
# 레진코믹스 카테고리 별 url
category = ['/ko/romance?page=', '/ko/boys?page=', '/ko/drama?page=', '/ko/bl?page=']
category_num = [53, 28, 94, 129]

id_list = []
title_list = []


for i in range(4):
    page_num = 0
    for page_num in range(category_num[i]):
        URL = url + category[i] + str(page_num) + '&sub_tags=all'
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path=r'C:/Users/82108/Downloads/chromedriver_win32/chromedriver.exe')
        driver.implicitly_wait(3)
        driver.get(URL)

        sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        buttonFilter = driver.find_element_by_css_selector("#exhibit-container > div.lzFilter > button")
        buttonFilter.click()
        ar = driver.find_element_by_name("data-ga-event-label=버튼_필터_완결")



        tmp = soup.find('ul', {'id' : 'exhibit-sub-tags'})
        title = tmp.find_all('div', {'class' : 'lzComic__title'})
        

        for j in range(len(title)):
            t = title[j].text
            if (t in title_list):
                continue

            title_list.append(t)
       
total_data = pd.DataFrame()
total_data['title'] = title_list
