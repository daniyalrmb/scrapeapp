import pandas as pd 
import streamlit as st
import time
import urllib3
import requests
import re

def getData(search, pages):

    #start_url = 'https://www.olx.com.pk/items/q-{}'.format(search)
    start_url = 'https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20220416075355&SearchText={}&spm=a2g0o.home.1000002.0'.format(search)
    source = requests.get(start_url).content
    data = re.findall('"storeName":"(.*?)","storeId":', str(source))
    #source = requests.get(start_url).text
    #data = re.findall('" aria-label="Title">(.*)</div><div class="_52497c97"', source)
    dat = []
    
    for i in range(1, pages):
        sec_url = 'https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText=lamp&ltype=wholesale&SortType=default&page={}'.format(i)
        source = requests.get(sec_url).content
        dat.append(re.findall('"storeName":"(.*?)","storeId":', str(source)))

    flat_list = [item for sublist in dat for item in sublist]
    data = data + flat_list
    df = pd.DataFrame(data, columns =['Stores'])
    
    return df
    
st.title("olx.pk Scraper")
search = st.text_input('Enter search term')
pages = st.number_input(label = 'Enter number of pages here', min_value=0, format = %i)

time.sleep(5)
p = getData(search, pages)
time.sleep(5)
st.dataframe(p)
st.subheader(" Recent Repositories")
