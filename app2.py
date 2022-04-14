#!/usr/bin/env python
# coding: utf-8

# In[ ]:
pip install selenium
pip install bs4

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import streamlit as st

# accessing Chromedriver
def getData(search):
    driver = webdriver.Chrome('chromedriver')

    #search = 'spoons'
    # Open login page

    driver.get('https://www.daraz.pk/catalog/?q={}&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34937MnH6tM'.format(search))
    driver.execute_script("window.scrollTo(0, 4000);")

    from selenium.webdriver.common.by import By
    p = []

# locate submit button by_xpath
    for i in range(1,40):
        xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{}]/div/div/div[2]/div[2]/a'.format(i)

# sign_in_button = driver.find_element_by_xpath('/html/body/nav/div/a[2]')

        sign_in_button = driver.find_element(by=By.XPATH, value=xpath)

# .click() to mimic button click

        p.append(sign_in_button.text)

    driver.get('https://www.daraz.pk/catalog/?_keyori=ss&from=input&page=2&q={}&spm=a2a0e.home.search.go.35e34937MnH6tM'.format(search))
    driver.execute_script("window.scrollTo(0, 4000);")

# locate submit button by_xpath
    for i in range(1,40):
        xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{}]/div/div/div[2]/div[2]/a'.format(i)

# sign_in_button = driver.find_element_by_xpath('/html/body/nav/div/a[2]')

        sign_in_button = driver.find_element(by=By.XPATH, value=xpath)

# .click() to mimic button click

        p.append(sign_in_button.text)
    return p
    
st.title("Daraz Scraper")
search = st.text_input('Enter search term')

if search != '':
    try:
        time.sleep(5)
        p = getData(search)
        time.sleep(5)
        st.subheader(p)
        st.subheader(" Recent Repositories")
    #st.table(repo_info)
    except:
        st.subheader("User doesn't exist")


# In[ ]:




