import pandas as pd 
import streamlit as st
import time
import urllib3
import requests
import re
from st_aggrid import AgGrid

def getData(search, pages):
    
    start_url = 'https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20220416075355&SearchText={}&spm=a2g0o.home.1000002.0'.format(search)
    source = requests.get(start_url).content
    data = re.findall('"storeName":"(.*?)","storeId":', str(source))
    namedata = re.findall('":{"displayTitle":"(.*?)","shortTitle":', str(source))
    pricedata = re.findall('formatted_price":"PKR (.*?)","csp"', str(source))
    pricedata = [int(float(j).replace('PKR','') for j in pricedata]
    iddata = re.findall('"productId":(.*?),"store":{', str(source))


    dat = []
    namedat = []
    pricedat = []
    iddat = []
    
    for i in range(1,pages):
        sec_url = 'https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText={}&ltype=wholesale&SortType=default&page={}'.format(search, i)
        source = requests.get(sec_url).content
        dat.append(re.findall('"storeName":"(.*?)","storeId":', str(source)))
        namedat.append(re.findall('":{"displayTitle":"(.*?)","shortTitle":', str(source)))
        pricedat.append(re.findall('formatted_price":"PKR (.*?)","csp"', str(source)))
        iddat.append(re.findall('"productId":(.*?),"store":{', str(source)))


    flat_list = [item for sublist in dat for item in sublist]
    name_list = [item for sublist in namedat for item in sublist]
    price_list = [item for sublist in pricedat for item in sublist]
    price_list = [int(float(j)).replace('PKR','') for j in price_list]
    id_list = [item for sublist in iddat for item in sublist]

    data = data + flat_list
    namedata = namedata + name_list
    pricedata = pricedata + price_list
    iddata = iddata + id_list
    iddata = ['https://www.aliexpress.com/item/'+j+'.html' for j in iddata]

    df = pd.DataFrame(
        {'Stores': data,
        'Names': namedata
        })
    
    df['Price'] = pd.Series(pricedata)
    df['ProductID'] = pd.Series(iddata)
    
    return df

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


st.title("aliexpress scraper")
search = st.text_input('Enter search term')
pages = st.number_input('Enter number of pages here', min_value=1, max_value=10, value=5, step=1)
time.sleep(1)
p = getData(search, pages)
csv = convert_df(p)
st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
time.sleep(1)

#AgGrid(p, height=500, fit_columns_on_grid_load=True, enable_enterprise_modules=True)
st.dataframe(p)



