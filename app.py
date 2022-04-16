import pandas as pd 
import streamlit as st
import time
import urllib3
import requests
import re

def getData(search):

    start_url = 'https://www.olx.com.pk/items/q-{}'.format(search)
    source = requests.get(start_url).text
    data = re.findall('" aria-label="Title">(.*)</div><div class="_52497c97"', source)
    return data
    
st.title("olx.pk Scraper")
search = st.text_input('Enter search term')

time.sleep(5)
p = getData(search)
time.sleep(5)
st.subheader(p)
st.subheader(" Recent Repositories")
