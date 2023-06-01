import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
from datetime import datetime, timedelta
import plotly.graph_objects as go
from skimage import data
#from streamlit_extras.let_it_rain import rain

# read csv from a github repo
#df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")



df = pd.read_csv("measurements.csv")

st.set_page_config(
    page_title = 'Solaredge SenseConnect LIVE',
    page_icon = '✅',
    layout = 'wide'
    
)

# Display an image from disk
image_path = "SolarEdge_logo_header_new_0.jpg"
title1, title2, title3 = st.columns(3)

with title1:
    st.write('')
with title2:
    st.image(image_path, caption='', width = 400)
    st.title("SenseConnect LIVE")
with title3:
    st.write('')

#set_background_color("#EB3434")  # Set background color to AliceBlue
# dashboard title



# Adjust the font of a st.metric component
st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 60px;
}
</style>
""",
    unsafe_allow_html=True,
)

# Adjust the font of a st.metric component
st.markdown(
    """
<style>
[data-testid="stMetricLabel"] {
    font-size: 30px;
}
</style>
""",
    unsafe_allow_html=True,
)

#job_filter = st.selectbox("Select the Job", pd.unique(df['job']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

#df = df[df['job']==job_filter]

# near real-time / live feed simulation 

while(True):
#while True: 
    df = pd.read_csv("measurements.csv").tail(200)
    #df['age_new'] = df['age'] * np.random.choice(range(1,5))
    #df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

    # Take last measurement raw
    #data_in = df.head(1)

    # creating KPIs 
    power = df['Power'].iloc[-1]
    voltage = df['Vout'].iloc[-1]
    temperature = df['thermistor'].iloc[-1]
    temperature_prev = df['thermistor'].iloc[-2]
    timestamp = df['Time'].iloc[-1]
    sense_connect = df['Is_CTM'].iloc[-1]
    timestamp_formated = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    print(timestamp)
    print(power)
    print(voltage)
    print(sense_connect)
    #count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
    
    #balance = np.mean(df['balance_new'])
    


    with placeholder.container():
        # create three columns
        #st.write('1 + 1 = ', 2)
        kpi1, kpi2, kpi3 = st.columns(3)
        sense_connect_column = st.columns(1)
        
        
        if sense_connect:
            st.error('SenseConnect event Detected')
        else:
            st.info('Monitoring Optimizer Output Connector Temperature...')

                
        

        graph_column1, graph_column2, graph_column3 = st.columns(3)
        #kpi1, kpi2 = st.columns(2)
        #column3, column4 = st.columns(2)
        # fill in those three columns with respective metrics or KPIs 

        kpi1.metric(label="Optimizer Power", value=f"{round(power)} W")
        kpi2.metric(label="Optimizer Voltage", value= f"{int(voltage)} V")
        kpi3.metric(label="Connector Temperature", value= f"{round(temperature)} °C", delta= f"{round(temperature) - round(temperature_prev)} °C", delta_color="inverse")

        # create two columns for charts 

        #fig_col1, fig_col2, fig_col3 = st.columns(3)
        with graph_column1:
            #st.markdown("### Optimizer Output Power")
            fig = px.line(data_frame = df, y = 'Power', x = 'Time')
            fig.update_xaxes(range=[timestamp_formated - timedelta(seconds=90) , timestamp_formated  + timedelta(seconds=30)])
            fig.update_yaxes(range=[0, 300])
            st.write(fig)
            #img = data.astronaut()
            #fig4 = px.imshow(img, binary_format="jpeg", binary_compression_level=0)
            #fig4.update_layout(coloraxis_showscale=False)
            #fig4.update_xaxes(showticklabels=False)
            #fig4.update_yaxes(showticklabels=False)
            #st.write(fig4)
        with graph_column2:
            #st.markdown("### Optimizer Output Voltage")
            fig2 = px.line(data_frame = df, y = 'Vout', x = 'Time')
            fig2.update_xaxes(range=[timestamp_formated - timedelta(seconds=30) , timestamp_formated  + timedelta(seconds=90)])
            fig2.update_yaxes(range=[0, 50])
            st.write(fig2)
        with graph_column3:
            #st.markdown("### MC4 Connector Temperature")
            fig3 = px.line(data_frame = df, y = 'thermistor', x = 'Time')
            fig3.update_xaxes(range=[timestamp_formated - timedelta(seconds=30) , timestamp_formated  + timedelta(seconds=90)])
            fig2.update_yaxes(range=[0, 160])
            st.write(fig3)
        #st.markdown("### Detailed Data View")
        #st.dataframe(df)

        

        #rain(
        #    emoji="🎈",
        #    font_size=54,
        #    falling_speed=5,
        #    animation_length="infinite",
        #)

        time.sleep(1)
    #placeholder.empty()


