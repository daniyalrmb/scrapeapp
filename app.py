import pandas as pd 
import streamlit as st
import time
import urllib3
import requests
import json
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from fake_useragent import UserAgent

def getData(search):
    listt = []
    t0 = time.time()


    chrome_options = webdriver.ChromeOptions()
    ua = UserAgent()
    userAgent = ua.random
    chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--proxy-sever=socks5://127.0.0.1:0000')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("window-size=1200x600")
    chrome_options.add_argument("--window-position=0,0")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
 
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


    start_url = 'https://www.olx.com.pk/items/q-{}'.format(text)
    driver.get(start_url)
    time.sleep(2)
    source = driver.page_source
    data = re.findall('" aria-label="Title">(.*)</div><div class="_52497c97"', source)
    #listt.append(data)

    # b'<!DOCTYPE html><html xmlns="http://www....
    driver.quit()
    t1 = time.time()
    total = t1-t0
    
    df = pd.DataFrame(data)
    return df
    
st.title("Daraz Scraper")
search = st.text_input('Enter search term')

time.sleep(5)
p = getData(search)
time.sleep(5)
st.subheader(p)
st.subheader(" Recent Repositories")
