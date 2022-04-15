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

    
    
    headers = { 'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
    'cache-control':'no-cache',
    'dnt':'1',
    'pragma':'no-cache',
    'referer':'https',
    'sec-fetch-mode':'no-cors',
    'sec-fetch-site':'cross-site',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }

    URL = 'https://www.daraz.pk/catalog/?q={}&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34937MnH6tM'.format(search)

    html_doc = requests.get(URL)
    html_doc = html_doc.content
    return html_doc
    
st.title("Daraz Scraper")
search = st.text_input('Enter search term')

time.sleep(5)
p = getData(search)
time.sleep(5)
st.subheader(p)
re.search(r'window\.pageData=({.*})', p)
st.subheader(" Recent Repositories")
