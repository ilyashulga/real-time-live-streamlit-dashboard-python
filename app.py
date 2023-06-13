import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
from datetime import datetime, timedelta
import plotly.graph_objects as go
import random
#from streamlit_extras.let_it_rain import rain

#import streamlit_extras.let_it_rain as rain

# read csv from a github repo
#df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

def create_parameter_panel():
    st.sidebar.subheader("Parameters")
    # Add input fields for your parameters
    #parameter1 = st.sidebar.text_input("Parameter 1", "")
    opt_string_count = st.sidebar.slider("Number of oprimizers in string", 7, 28, 13)
    #parameter2 = st.sidebar.slider("Parameter 2", 0, 100, 50)
    #parameter3 = st.sidebar.selectbox("Parameter 3", ["Option 1", "Option 2", "Option 3"])

    return opt_string_count

triggered = 0
PATH = "C:\\Users\\lab-opt\\Documents\\Tests\\InterSolar\\measurements.csv"

df = pd.read_csv(PATH)

st.set_page_config(
    page_title = 'Sense Connect - LIVE Demo ',
    page_icon = '🌡️',
    layout = 'wide'
    
)

# Display an image from disk
image_path = "SolarEdge_logo_header_new_0.jpg"
title1, title2, title3 = st.columns(3)

with title1:
    st.write('')
with title2:
    
    st.markdown(""" <style> .big-font2 {font-family: "Times New Roman", Times, serif; text-align: center; font-size:60px; color: black;  } </style> """, unsafe_allow_html=True) 
    st.markdown('<p class="big-font2">Sense Connect - LIVE Demo</p>', unsafe_allow_html=True)
    #st.title("SenseConnect LIVE")
with title3:
    # Adjust the font of a st.metric component
    st.image(image_path, caption='', width = 400)
    st.write('')



# Add CSS styling to align the image to the right
st.markdown(
    """
<style>
[data-testid="stImage"] {
    display: block;
    margin-left: auto;
    margin-right: 50;
}
</style>
""",
    unsafe_allow_html=True,
)

#set_background_color("#EB3434")  # Set background color to AliceBlue
# dashboard title



# Adjust the font of a st.metric component
st.markdown(
    """
<style>
[data-testid="stMetricValue"] > div {
    font-size: 60px;
    text-align: center;
}
</style>
""",
    unsafe_allow_html=True,
)

# Adjust the font of a st.metric component
st.markdown(
    """
<style>
[data-testid="stMetricLabel"] > div {
    font-size: 30px;
    text-align: center;
}
</style>
""",
    unsafe_allow_html=True,
)

# Adjust the font of a st.metric component
st.markdown(
    """
<style>
[data-testid="stMetricDelta"] {
    font-size: 30px;
    text-align: center;
}
</style>
""",
    unsafe_allow_html=True,
)

#job_filter = st.selectbox("Select the Job", pd.unique(df['job']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

# Create the side panel
opt_in_string = create_parameter_panel()
#df = df[df['job']==job_filter]

# near real-time / live feed simulation 

while(True):
#while True: 
    df = pd.read_csv(PATH).tail(200)
    #df['age_new'] = df['age'] * np.random.choice(range(1,5))
    #df['balance_new'] = df['balance'] * np.random.choice(range(1,5))

    # Take last measurement raw
    #data_in = df.head(1)

    # creating KPIs 
    power = float(df['Power'].iloc[-1])
    voltage = float(df['Vout'].iloc[-1])
    v_in = float(df['Vin'].iloc[-1])
    temperature = float(df['thermistor'].iloc[-1])
    temperature_prev = float(df['thermistor'].iloc[-2])
    timestamp = df['Time'].iloc[-1]
    sense_connect = int(df['Is_CTM'].iloc[-1])
    timestamp_formated = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    print(timestamp)
    print(power)
    print(voltage)
    print(v_in)
    print(sense_connect)
    #count_married = int(df[(df["marital"]=='married')]['marital'].count() + np.random.choice(range(1,30)))
    
    #balance = np.mean(df['balance_new'])
    


    with placeholder.container():
        # create three columns
        #st.write('1 + 1 = ', 2)
        if sense_connect:
            #st.header(':red[SenseConnect event Detected!]')
            st.markdown(""" <style> .big-font { text-align: center; background-color: red; font-size:42px; color: white; !important; } </style> """, unsafe_allow_html=True) 
            st.markdown('<p class="big-font">SenseConnect event Detected!!!</p>', unsafe_allow_html=True)
            #st.balloons()    
            #st.write('SenseConnect event Detected!')
        else:
            st.markdown(""" <style> .big-font { text-align: center ;font-size:42px; color: white; background-color: grey;} </style> """, unsafe_allow_html=True) 
            st.markdown('<p class="big-font">Monitoring power optimizer output connector temperature...</p>', unsafe_allow_html=True)
            #st.write('Monitoring Optimizer Output Connector Temperature...')
        
        st.write('')
        st.write('')
        st.write('')
        kpi6, kpi5, kpi4, kpi2, kpi1, kpi3  = st.columns(6)
        #sense_connect_column = st.columns(1)

        #st.markdown(
        #    """
        #    <style>
        #    [data-testid="stMarkdownContainerValue"] {
        #        font-size: 50px;
        #    }
        #    </style>
        #    """,
        #    unsafe_allow_html=True
        #    ) # This don't work




        #error = st.alert("This is error alert.", title="Error", type="error", icon="🚨")
        
        #if sense_connect:
        #    error.open()
        #else:
        #    error.close()
        

        graph_column1, graph_column2, graph_column3 = st.columns(3)

        #kpi1, kpi2 = st.columns(2)
        #column3, column4 = st.columns(2)
        # fill in those three columns with respective metrics or KPIs
        st.markdown(""" <style> .big-metric { text-align: center ;font-size:30px; color: black; background-color: white;} </style> """, unsafe_allow_html=True)
        kpi6.markdown('<p class="big-metric">String Power</p>', unsafe_allow_html=True)
        kpi6.metric(label='String Power', value=f"{round(power*opt_in_string*random.uniform(0.99, 1.01))} W", label_visibility="hidden")
        kpi5.markdown('<p class="big-metric">String Voltage</p>', unsafe_allow_html=True)
        kpi5.metric(label="String Voltage", value=f"{round(voltage*opt_in_string*random.uniform(0.99, 1.01), 2)} V", label_visibility="hidden")
        kpi1.markdown('<p class="big-metric">Optimizer Power</p>', unsafe_allow_html=True)
        kpi1.metric(label="Optimizer Power", value=f"{round(power, 2)} W", label_visibility="hidden")
        kpi2.markdown('<p class="big-metric">Optimizer Voltage</p>', unsafe_allow_html=True)
        kpi2.metric(label="Optimizer Voltage", value= f"{round(voltage*random.uniform(0.999, 1.001), 2)} V", label_visibility="hidden")
        kpi4.markdown('<p class="big-metric">PV Voltage</p>', unsafe_allow_html=True)
        kpi4.metric(label="PV Voltage", value= f"{round(v_in*random.uniform(0.999, 1.001), 2)} V", label_visibility="hidden")
        kpi3.markdown('<p class="big-metric">Connector Temperature</p>', unsafe_allow_html=True)
        kpi3.metric(label="Connector Temperature", value= f"{round(temperature, 2)} °C", delta= f"{round(temperature - temperature_prev, 2)} °C", delta_color="inverse", label_visibility="hidden")

        # create two columns for charts 
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        #fig_col1, fig_col2, fig_col3 = st.columns(3)
        with graph_column1:
            #st.markdown("### Optimizer Output Power")
            st.markdown(""" <style> .big-font3 { text-align: center ;font-size:32px; color: black; background-color: white;} </style> """, unsafe_allow_html=True)
            st.markdown('<p class="big-font3">Power Optimizer Power</p>', unsafe_allow_html=True)
            fig = px.line(data_frame = df, y = 'Power', x = 'Time')
            fig.update_xaxes(range=[timestamp_formated - timedelta(seconds=90) , timestamp_formated  + timedelta(seconds=30)], title=dict(text='', font=dict(
                size=32
                )
            ))
            fig.update_yaxes(range=[0, 400], title=dict(text='Optimizer Power (W)', font=dict(
                size=28
                )
            ))
            fig.update_layout(
                yaxis = dict(
                tickfont = dict(size=20)))
            fig.update_layout(
                xaxis = dict(
                tickfont = dict(size=20)))
            st.write(fig)
            #img = data.astronaut()
            #fig4 = px.imshow(img, binary_format="jpeg", binary_compression_level=0)
            #fig4.update_layout(coloraxis_showscale=False)
            #fig4.update_xaxes(showticklabels=False)
            #fig4.update_yaxes(showticklabels=False)
            #st.write(fig4)
        with graph_column2:
            st.markdown('<p class="big-font3">Power Optimizer Voltage</p>', unsafe_allow_html=True)
            fig2 = px.line(data_frame = df, y = 'Vout', x = 'Time')
            fig2.update_xaxes(range=[timestamp_formated - timedelta(seconds=90) , timestamp_formated  + timedelta(seconds=30)], title=dict(text='Time', font=dict(
                size=32
                )
            ))
            fig2.update_yaxes(range=[0, 38], title=dict(text='Optimizer Voltage (V)', font=dict(
                size=28
                )
            ))
            fig2.update_layout(
                yaxis = dict(
                tickfont = dict(size=20)))
            fig2.update_layout(
                xaxis = dict(
                tickfont = dict(size=20)))
            st.write(fig2)
        with graph_column3:
            st.markdown('<p class="big-font3">Connector temperature</p>', unsafe_allow_html=True)
            fig3 = px.line(data_frame = df, y = 'thermistor', x = 'Time')
            fig3.add_hline(y=90, line_color="red")
            fig3.add_hrect(y0=90, y1=140, line_width=0, fillcolor="red", opacity=0.1)
            fig3.add_hrect(y0=0, y1=40, line_width=0, fillcolor="green", opacity=0.1)
            fig3.update_xaxes(range=[timestamp_formated - timedelta(seconds=90) , timestamp_formated  + timedelta(seconds=30)], title=dict(text='', font=dict(
                size=32
                )
            ))
            fig3.update_yaxes(range=[0, 140], title=dict(text='Connector Temperature (°C)', font=dict(
                size=26
                )
            ))
            fig3.update_layout(
                yaxis = dict(
                tickfont = dict(size=20)))
            fig3.update_layout(
                xaxis = dict(
                tickfont = dict(size=20)))
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
    #if sense_connect:
        #st.balloons()
            #st.header(':red[SenseConnect event Detected!]')
    #        rain(
    #                emoji="🌡️",
    #                font_size=54,
    #                falling_speed=5,
    #                animation_length=1,
    #            )
    #placeholder.empty()


