import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
from datetime import datetime, timedelta

# read csv from a github repo
#df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

df = pd.read_csv("measurements.csv")

st.set_page_config(
    page_title = 'Solaredge SenseConnect LIVE',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("SenseConnect LIVE")

# top-level filters 

#job_filter = st.selectbox("Select the Job", pd.unique(df['job']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

#df = df[df['job']==job_filter]

# near real-time / live feed simulation 

for seconds in range(200):
#while True: 
    df = pd.read_csv("measurements.csv").tail(200)
    #df['age_new'] = df['age'] * np.random.choice(range(1,5))
    #df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

    # Take last measurement raw
    #data_in = df.head(1)

    # creating KPIs 
    power = df['Power (W)'].iloc[-1]
    voltage = df['Voltage (V)'].iloc[-1]
    temperature = df['Temperature (C)'].iloc[-1]
    temperature_prev = df['Temperature (C)'].iloc[-2]
    timestamp = df['Timestamp'].iloc[-1]
    timestamp_formated = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    print(timestamp)
    print(power)
    print(voltage)
    #count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
    
    #balance = np.mean(df['balance_new'])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)
        #kpi1, kpi2 = st.columns(2)
        
        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="Power", value=f"{round(power)} W")
        kpi2.metric(label="Voltage", value= f"{int(voltage)} V")
        kpi3.metric(label="Connector Temperature", value= f"{round(temperature)} °C", delta= f"{round(temperature) - round(temperature_prev)} °C", delta_color="inverse")

        # create two columns for charts 

        fig_col1, fig_col2, fig_col3 = st.columns(3)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.line(data_frame = df, y = 'Power (W)', x = 'Timestamp')
            fig.update_xaxes(range=[timestamp_formated - timedelta(seconds=30) , timestamp_formated  + timedelta(seconds=90)])
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.line(data_frame = df, y = 'Voltage (V)', x = 'Timestamp')
            fig2.update_xaxes(range=[timestamp_formated - timedelta(seconds=30) , timestamp_formated  + timedelta(seconds=90)])
            st.write(fig2)
        with fig_col3:
            st.markdown("### Third Chart")
            fig3 = px.line(data_frame = df, y = 'Temperature (C)', x = 'Timestamp')
            fig3.update_xaxes(range=[timestamp_formated - timedelta(seconds=30) , timestamp_formated  + timedelta(seconds=90)])
            st.write(fig3)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(0.5)
    #placeholder.empty()


