import streamlit as st
import pandas as pd
import numpy as np
import requests
import config
import datetime as dt
from iex import IEXStock

st.title("HAB LABS")
st.write("Display analytics, run models and automate data processes")

option = st.sidebar.selectbox("Please Choose Your Dashboard", ('Start Here','API: Stock Info', 'Machinel Learning','Web App'))

st.header(option)


if option == 'API: Stock Info':
    symbol = st.sidebar.text_input("Symbol", value="NFLX")
    st.header("Asset: "+ symbol)
    
    

    screen =st.sidebar.selectbox("View",("Overview", "Price Data", "Social Media Mentions"))
    st.title(screen)
    st.subheader("Put your favorite stock ticker in the sidebar!")
    
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
        
    if screen == "Social Media Mentions":
    
        #symbol = st.sidebar.text_input("Symbol", value='NFLX', max_chars=5)
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


        


if option == "Start Here":
    
    st.header("Explore this dashboard to learn more about our services")
    st.subheader("1)We can connect to an external API to fetch data so that you can view it effortlessly. Check out the 'API' option to see this might work for you.")
    st.subheader("2)You might also use these dashboards to display data analytics and machine learning. Check out the 'Machine Learning' option to see how this might work for you")
    

  
        
if option == "Machine Learning":
    model =st.sidebar.selectbox("Model",("Prediction", "Classification"))
    st.header("You are currently viewing the ", model, "model.")
    if model =="Prediction":
        st.subheader("machine learning ", model, "project info goes here")
        
    if model =="Classification":
        st.subheader("machine learning ", model, "project info goes here")
        
if option == "Web App":
    st.header("Custom Web Apps")
    st.write("These web apps can also be useful for operational activities - such as a team capturing data")
    team_member = st.text_input("Team member name:  ")
    info = st.text_input("Information goes here:   ")
    if st.button("click"):
        st.write("The following data has been added to the database, thank you.")
        st.write(team_member)
        st.write(info)
    
        
    
    

