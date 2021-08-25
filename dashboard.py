import streamlit as st
import pandas as pd
import numpy as np
import requests
import config
from iex import IEXStock
import datetime as dt

st.title("Your Information Portal")
st.write("Display analytics, run models and automate data processes")

option = st.sidebar.selectbox("Please Choose Your Dashboard", ('Example Option - Start Here','Stock Info', 'Social Media Mentions'))

st.header(option)


if option == 'Stock Info':
    symbol = st.sidebar.text_input("Symbol", value="NFLX")
    st.header("Asset: "+ symbol)
    
    

    screen =st.sidebar.selectbox("View",("Overview", "Price Data"))
    st.title(screen)
    st.subheader("Put your favorite stock ticket in the sidebar!")
    
    if screen == "Overview":
        stock = IEXStock(config.IEX_API_TOKEN, symbol)
        ##logo = stock.get_logo()

        #company_info = stock.get_company_info()

        url = f"https://cloud.iexapis.com/stable/stock/{symbol}/logo?token={config.IEX_API_TOKEN}"
        p = requests.get(url)
        logo = p.json()
        st.subheader("Check out the side bar for more options under 'view'!")
        

        col1, col2 = st.columns([1,1])

        url = f"https://cloud.iexapis.com/stable/stock/{symbol}/company?token={config.IEX_API_TOKEN}"
        p = requests.get(url)
        response_json = p.json()
       #st.write(response_json)

        with col1:
            st.image(logo['url'])
            st.subheader("Description")
            st.write(response_json['description'])

        
        with col2:
            st.subheader(response_json['companyName'])
            st.write("Industry: " + response_json['industry'])
            st.write("CEO: "+ response_json['CEO'])
            st.write("Country: "+ response_json['country'])
            st.subheader("Website")
            st.write(response_json['website'])


    if screen == "Price Data":
        st.subheader("This is live data coming to you from another database. We do this using API's and can connect multiple API's for you, bringing everything you need to one place!")
        st.image(f"https://charts2.finviz.com/chart.ashx?t={symbol}")
        url = f"https://cloud.iexapis.com/stable/stock/{symbol}/stats?token={config.IEX_API_TOKEN}"
        m = requests.get(url)
        data = m.json()
        st.write("Market Cap: ",data['marketcap'] )
        st.write("52 week high: ", data['week52high'])
        st.write("52 week low: ", data['week52low'])
        st.write("Shares outstanding: ",data['sharesOutstanding'])
        st.write("200 day moving average: ", data['day200MovingAvg'])
        st.write("50 day moving average: ", data['day50MovingAvg'])
        st.write("P/E ratio: ", data['peRatio'])
        st.write("Beta: ", data['beta'])
        st.write("Next earnings:  ", data['nextEarningsDate'])
        st.write("Next dividend: ", data['nextDividendDate'])
        st.write("Dividend yield: ", data['dividendYield'])
        
if option == "Social Media Mentions":
    
    symbol = st.sidebar.text_input("Symbol", value='NFLX', max_chars=5)
    #st.subheader('stocktwits')
    #gets most recent mentions of symbol
    #st.image(f"https://charts2.finviz.com/chart.ashx?t={symbol}")
    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
    data = r.json()
    st.subheader("Connect to social platforms and retrieve the data available. Below are posts from 'Stocktwits' mentioning the selected stock in the sidebar")

    #printing body, datetime and person of mention
    for message in data['messages']:
        st.write(message['body'])
        st.write(message['created_at'])
        st.write(message['user']['username'])
        st.image(message['user']['avatar_url'])

if option == "Example Option - Start Here":

    st.header("This is an example")
    st.write("We can connect to an external API and pull the data here so that you can view it effortlessly.")
    st.write("You might use also use these dashboards to display data analytics and monthly reports. We can automate this process to retrieve live data, to add it to your database if its not already there, and to rerun a model with the new data.")
    st.subheader("1) To explore how this might look, select a dashboard from the sidebar.")
    st.subheader("2) These can also be used for customised web applications for your business, such as the example below.")
    

    st.header("Custom Web Apps")
    st.write("These web apps can also be useful for operational activities - such as a team capturing data")
    team_member = st.text_input("Team member name:  ")
    info = st.text_input("Information goes here:   ")
    if st.button("click"):
        st.write("The following data has been added to the database, thank you.")
        st.write(team_member)
        st.write(info)

