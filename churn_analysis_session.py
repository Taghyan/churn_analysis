
import  streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('Churn_Modelling.csv')

st.title('Churn Analysis')

tab1, tab2 = st.tabs(['Descriptive Statistics', 'Charts'])

num = df.describe()
cat = df.describe(include= 'O')

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('Numerical descriptive Data')
        st.dataframe(num)
    with col3:
        st.subheader('Categorical descriptive Data')
        st.dataframe(cat)
with tab2:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        Filter = st.sidebar.selectbox('Select Country', df['Geography'].unique())
        filtered_data = df[df['Geography'] == Filter]

    st.header('Pie Chart')
    fig = px.pie(filtered_data, names='Exited', title='Exited')
    st.plotly_chart(fig, use_container_width=True)
    
    st.header('Bar Chart')
    fig = filtered_data.groupby(['Geography', 'Gender'])['Exited'].sum().reset_index()
    fig = px.bar(fig, 'Geography', 'Exited', color= 'Gender', barmode= 'group', labels={'Geography':'Country'}, title= 'Num. of Exited/Country' ,color_discrete_sequence=px.colors.qualitative.D3)
    st.plotly_chart(fig, use_container_width=True)

    with col4:
        st.header('Scatter Plot')
        fig = px.scatter(filtered_data, x='Age', y='Balance', color='Exited')
        st.plotly_chart(fig, use_container_width=True)

        st.header('Heatmap Chart')
        fig = px.imshow(filtered_data.select_dtypes(exclude= 'O').corr().round(2), aspect= 'auto' ,text_auto= True)
        st.plotly_chart(fig, use_container_width=True)
