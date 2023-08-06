import streamlit as st
import pandas as pd  
import plotly.express as px 
st.subheader('By Solomon Kibon')

st.title('Churn Modelling Analysis')
st.write('This app analyzes Churn_Modelling dataset and displays various visualizations')
#load dataset
def load_data():
    df = pd.read_csv('Churn_Modelling.csv')
    df['Churn']=df['Exited']
    return df
df=load_data()
#display data
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(df)
## Calculate overall churn rate
if st.checkbox('Show overall churn rate'):
    overall_churn_rate = df['Churn'].mean()
    st.subheader('overall churn rate')
    st.write(f'Overall Churn Rate:  {overall_churn_rate:.2f}')
## Churn rate by age group
if st.checkbox('Show Churn rate by age group'):
    age_churn_rate = df.groupby('Age')['Churn'].mean()
    age_churn_rate=age_churn_rate.sort_values()
    st.subheader('Churn rate by Age group')
    st.write(age_churn_rate)

# Plot churn rate by gender
fig=px.bar(df,x='Gender', y='Churn',title='Bar plot of Churn rate by Gender')
st.plotly_chart(fig)
#Churn rate by age group
fig=px.bar(df,x='Age', y='Churn',title='Bar plot of Churn rate by Age')
st.plotly_chart(fig)
# Compare behavior of churned and retained customers (e.g., CreditScore, Balance, etc.)
fig=px.bar(df,x='Churn', y='CreditScore', title='CreditScore Distribution - Churn vs. Retained')
st.plotly_chart(fig)

fig=px.bar(df,x='Churn', y='Balance', title='Balance Distribution - Churn vs. Retained')
st.plotly_chart(fig)

#correlation matrix
correlation_matrix=df.corr(numeric_only=True)
fig=px.imshow(correlation_matrix, title='Correlation Matrix')
st.plotly_chart(fig)