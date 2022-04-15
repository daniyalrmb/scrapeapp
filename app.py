import time
import pandas as pd
import requests
import streamlit as st
import re
import json
import urllib3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# accessing Chromedriver
def getData(search):

  list = []
  t0 = time.time()

  chrome_options = Options()
  #chrome_options.add_argument("--disable-extensions")
  chrome_options.add_argument("--disable-gpu")
  #chrome_options.add_argument("--no-sandbox") # linux only
  chrome_options.add_argument("--headless")
  # chrome_options.headless = True # also works
  driver = webdriver.Chrome(options=chrome_options)
  start_url = 'https://www.daraz.pk/catalog/?q={}&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34937MnH6tM'.format(search)
  driver.get(start_url)
  source = driver.page_source
  data = json.loads(re.search(r'window\.pageData=({.*})', source).group(1))
  for item in data['mods']['listItems']:
    list.append(item['name'])
# b'<!DOCTYPE html><html xmlns="http://www....
  driver.quit()
  t1 = time.time()

  total = t1-t0
  return list
    
st.title("Daraz Scraper")
search = st.text_input('Enter search term')

time.sleep(5)
p = getData(search)
time.sleep(5)
st.subheader(p)
st.subheader(" Recent Repositories")
