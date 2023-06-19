import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days: ',
                 min_value=1,
                 max_value=5,
                 help='Select the number of forecasted days')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))

if place:

    match option:
        case 'Temperature':
            try:
                dates, temperatures = get_data(place, days, option)
                st.subheader(f'{option} for the next {days} days in {place}')
                figure = px.line(x=dates, y=temperatures, labels={'x': 'Dates',
                                                                  'y': 'Temperatures (C)'})
                st.plotly_chart(figure)
            except KeyError:
                st.error(f'{place} is not a valid location name.')

        case 'Sky':
            image_info = {'Clouds': 'images/cloud.png',
                          'Rain': 'images/rain.png',
                          'Clear': 'images/clear.png',
                          'Snow': 'images/snow.png'}
            try:
                dates, sky = get_data(place, days, option)
                st.subheader(f'{option} for the next {days} days in {place}')
                image_paths = [image_info[i] for i in sky]
                columns = [i for i in st.columns(days)]
                dates = ["Time : " + i.split(' ')[1] for i in dates]
                date_counter = 0
                for index, col in enumerate(columns):
                    with col:
                        for image in image_paths[index * 8:(index + 1) * 8]:
                            st.image(image, width=115)
                            st.write(dates[date_counter])
                            date_counter += 1

                        st.subheader(f'Day :\t{index + 1}')
            except KeyError:
                st.error(f'{place} is not a valid location name.')



