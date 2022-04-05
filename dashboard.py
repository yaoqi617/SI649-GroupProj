import altair as alt
import pandas as pd
import streamlit as st
from altair import datum

st.set_page_config(layout="wide")
####################
## Data Preprocess #
####################
df = pd.read_csv("heart_2020_cleaned.csv")

def convert_to_int(x):
    if x == 'Yes':
        return 1
    else:
        return 0

df['HeartDisease'] = df['HeartDisease'].apply(lambda x: convert_to_int(x))
table_1 = df[['AgeCategory', 'Sex', 'Race', 'HeartDisease']].groupby(
    ['AgeCategory', 'Sex', 'Race']).count()
table_1 = table_1.rename(columns={'HeartDisease': 'total_num_people'})
table_2 = df[['AgeCategory', 'Sex', 'Race', 'HeartDisease']].groupby(
    ['AgeCategory', 'Sex', 'Race']).sum()
table_2 = table_2.rename(columns={'HeartDisease': 'num_heart_disease'})
age_group = pd.merge(table_1, table_2, on=['AgeCategory', 'Sex', 'Race'])
age_group['percentage'] = round(age_group['num_heart_disease']/age_group['total_num_people'] * 100, 1)
age_group = age_group.reset_index()

####################
### INTRODUCTION ###
####################

st.title("Key Indicators of Heart Disease")

intro_col1, intro_col2 = st.columns([1, 10])


with intro_col1:
    st.image("images/heart.jpg",
            caption="Welcome to our data visualization world",
            width=150)
with intro_col2:
    st.markdown("""
    Hello there! Did you know that heart disease is the leading cause of death in the U.S.? A lot of studies show that many factors might affect cardiovascular condition, including but not limited to personal lifestyle, demographic characteristics, and general health conditions. This app will show you how different factors impact heart disease through various charts. At the end of the app, you can use the machine learning model that we built to estimate your chance of heart disease (yes/no) in seconds!

    **Disclaimer**: Please keep in mind that all the visualizations and predicted results are not supposed to be used as any medical diagnosis! If you have any questions related to heart disease, consult a human doctor.

    **Author**: Yaoqi Liao & Hojeong Yoo ([GitHub Repo](https://github.com/yaoqi617/SI649-GroupProj))
    """)

####################
###### Viz 1 #######
####################
st.subheader('Distribution of heart disease by gender and race')

age_sex_race = alt.Chart(age_group
            ).mark_bar(
            height=25).encode(
            x=alt.X('percentage', title='Percentage of Heart Disease'),
            y=alt.Y('AgeCategory'),
            color='Race',
            column=alt.Column('Sex', title=None),
            tooltip=['Sex:N', 'Race:N', 'percentage:Q']
            ).properties(
            width=350,
            height=400)

race = list(age_group['Race'].unique())
race.insert(0, 'Not Selected')

native = alt.Chart(age_group
            ).transform_filter(alt.datum.Race=='American Indian/Alaskan Native').mark_bar(
            height=25).encode(
            x=alt.X('percentage', title='Percentage of Heart Disease'),
            y=alt.Y('AgeCategory'),
            color='Sex',
            column=alt.Column('Sex', title=None),
            tooltip=['Sex:N', 'Race:N', 'percentage:Q']
            ).properties(
            width=350,
            height=400)

asian = alt.Chart(age_group
            ).transform_filter(alt.datum.Race=='Asian').mark_bar(
            height=25).encode(
            x=alt.X('percentage', title='Percentage of Heart Disease'),
            y=alt.Y('AgeCategory'),
            color='Sex',
            column=alt.Column('Sex', title=None),
            tooltip=['Sex:N', 'Race:N', 'percentage:Q']
            ).properties(
            width=350,
            height=400)

black = alt.Chart(age_group
            ).transform_filter(alt.datum.Race=='Black').mark_bar(
            height=25).encode(
            x=alt.X('percentage', title='Percentage of Heart Disease'),
            y=alt.Y('AgeCategory'),
            color='Sex',
            column=alt.Column('Sex', title=None),
            tooltip=['Sex:N', 'Race:N', 'percentage:Q']
            ).properties(
            width=350,
            height=400)

hispanic = alt.Chart(age_group
            ).transform_filter(alt.datum.Race=='Hispanic').mark_bar(
            height=25).encode(
            x=alt.X('percentage', title='Percentage of Heart Disease'),
            y=alt.Y('AgeCategory'),
            color='Sex',
            column=alt.Column('Sex', title=None),
            tooltip=['Sex:N', 'Race:N', 'percentage:Q']
            ).properties(
            width=350,
            height=400)

other = alt.Chart(age_group
            ).transform_filter(alt.datum.Race=='Other').mark_bar(
            height=25).encode(
            x=alt.X('percentage', title='Percentage of Heart Disease'),
            y=alt.Y('AgeCategory'),
            color='Sex',
            column=alt.Column('Sex', title=None),
            tooltip=['Sex:N', 'Race:N', 'percentage:Q']
            ).properties(
            width=350,
            height=400)

white = alt.Chart(age_group
            ).transform_filter(alt.datum.Race=='White').mark_bar(
            height=25).encode(
            x=alt.X('percentage', title='Percentage of Heart Disease'),
            y=alt.Y('AgeCategory'),
            color='Sex',
            column=alt.Column('Sex', title=None),
            tooltip=['Sex:N', 'Race:N', 'percentage:Q']
            ).properties(
            width=350,
            height=400)

viz1_col1, viz1_col2 = st.columns([3, 6])

with viz1_col1:
    race_selections = st.selectbox ("Race", race, key='attribute_team')
with viz1_col2:
    if race_selections == race[0]:
        st.write(age_sex_race)
    elif race_selections == race[1]:
        st.write(native)
    elif race_selections == race[2]:
        st.write(asian)
    elif race_selections == race[3]:
        st.write(black)
    elif race_selections == race[4]:
        st.write(hispanic)
    elif race_selections == race[5]:
        st.write(other)
    elif race_selections == race[6]:
        st.write(white)