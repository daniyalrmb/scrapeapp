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

  
   
    URL = 'https://www.daraz.pk/catalog/?q={}&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34937MnH6tM'.format(search)

    html_doc = requests.get(URL).text
    return html_doc
    
st.title("Daraz Scraper")
search = st.text_input('Enter search term')

time.sleep(5)
p = getData(search)
time.sleep(5)
st.subheader(p)
st.subheader(" Recent Repositories")
