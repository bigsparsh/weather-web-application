import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days: ',
                 min_value=1,
                 max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

dates = ['2023-06-12', '2023-07-12', '2023-08-12']
temperatures = [20, 12, 23]

figure = px.line(x=dates, y=temperatures, labels={'x': 'Dates',
                                                  'y': 'Temperatures (C)'})
st.plotly_chart(figure)
