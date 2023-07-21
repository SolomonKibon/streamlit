import streamlit as st
st.title('Hello,streamlit')
st.write('This is my first streamlit app')

st.write('Displaying an image')
st.image('Sg9 _sti.jpg',caption='Image caption',use_column_width=True)

st.write('choose a number')
number=st.slider('Number',min_value=1,max_value=100,value=50)
st.write(f'you chose:{number}')
#button
if st.button('Click me!'):
    st.write('You clicked the button')
#slider
slider_value = st.slider("Select a value:", min_value=0, max_value=100, value=50)
st.write(f"Selected value: {slider_value}")   
#checkbox
checkbox_value=st.checkbox('show content')
if checkbox_value:
    st.write('content displayed')
#text input
import streamlit as st
name=st.text_input('Enter your name:','Type here')
st.write(f'Hello,{name}!')
#text area
feedback=st.text_area('Your feedback:')
st.write(f'Thank you for your feedback: {feedback}')
#number input
age=st.number_input('Enter your age:',min_value=0,max_value=120,value=23,step=2)
st.write(f'Your age is: {age}')
#date input
date=st.date_input('Select a date:', None)
st.write(f'selected date: {date}')
#time input
import datetime
time=st.time_input('select a time:',datetime.time(12,00))
st.write(f'selected time is: {time}')
#current time
import datetime
time=st.time_input('select a time:',None)
st.write(f'current time: {time}')
#selectbox
options=['option 1','option 2','option 3']
choice=st.selectbox('choose an option:',options)
st.write(f'You chose:{choice}')
#multiselect
options=['option 1','option 2','option 3']
selections=st.multiselect('choose multiple selections:',options)
st.write(f"you chose: {','.join(selections)}")
#radio button/same as selectbox ina a different way
options=['option 1','option 2','option 3']
choice=st.radio('choose an option:',options)
st.write(f'You chose:{choice}')
#file uploader
uploaded_file=st.file_uploader('choose a file to upload',type=["csv", "txt", "xlsx"])
if uploaded_file is not None:
    st.write(f'File uploaded: {uploaded_file.name}')

#Download
import streamlit as st
import pandas as pd 
import io
       # Create a sample DataFrame
data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
df = pd.DataFrame(data)
        # Display the DataFrame
st.dataframe(df)
# Download the DataFrame as a CSV file
# Create a StringIO object to hold the CSV data
csv_buffer = io.StringIO()
# Write the contents of the DataFrame to the StringIO object in CSV format
# The index column is excluded from the output by passing index=False
df.to_csv(csv_buffer, index=False)
# Get the contents of the StringIO object as a string
csv_data = csv_buffer.getvalue()
st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="sample_data.csv",
    mime="text/csv")

   #Basic Data Processing and Visualization
#Uploading data files (CSV, Excel, etc.)
import streamlit as st
uploaded_file = st.file_uploader("Upload a CSV or Excel file:", type=["csv", "xlsx"])
import pandas as pd
#Data manipulation with Pandas
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data:")
    st.dataframe(df)
#Data visualization with Matplotlib and Plotly
import matplotlib.pyplot as plt
st.write("Bar chart:")

plt.bar(df['Column1'], df['Column2'])
plt.xlabel('Column1')
plt.ylabel('Column2')
st.pyplot(plt)

import plotly.express as px
st.write("Scatter plot:")
fig = px.scatter(df, x='Column1', y='Column2', hover_name='Column1')
st.plotly_chart(fig)

   #Layout options
#Columns
import streamlit as st

col1, col2, col3 = st.columns(3)

col1.write("Column 1")
col2.write("Column 2")
col3.write("Column 3")
#sidebars
import streamlit as st

st.write("Main content")
st.sidebar.write("Sidebar content")
#expanders
import streamlit as st

with st.expander("Section 1"):
    st.write("Content for Section 1")

with st.expander("Section 2"):
    st.write("Content for Section 2")

#progress bars
import streamlit as st
import time

progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.1)
#spinners
import streamlit as st
import time

with st.spinner("Please wait..."):
    time.sleep(5)
st.write("Task completed.")
