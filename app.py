from selenium import webdriver
import time
import pandas as pd
import requests
import streamlit as st
import bs4 as BeautifulSoup
import re
import json
import urllib3

# accessing Chromedriver
def getData(search):
    p=[]
    URL = 'https://www.daraz.pk/catalog/?q={}&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34937MnH6tM'.format(search)
    html_doc = requests.get(URL).text
    data = json.loads(re.search(r'window\.pageData=({.*})', html_doc).group(1))
    for item in data['mods']['listItems']:
        p.append(item['name'])
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
