import altair as alt
import pandas as pd
from sklearn import preprocessing
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

def convert_to_bool(x):
    if x == 0:
        return 'No'
    else:
        return 'Yes'

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

table_3 = pd.read_csv("table_5.csv")


####################
### INTRODUCTION ###
####################

st.title("Key Indicators of Heart Disease")

intro_col1, intro_col2 = st.columns([2, 8])


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
    
st.subheader("A quick note about privacy")
st.markdown("""
Streamlit open-source software does not see or store any of the data you put into any app that you develop with it.
We also set the configuration setting as gathering usage stats is impossible.For more information, please visit https://streamlit.io/privacy-policy.
""")

####################
##### Raw Data #####
####################
st.subheader("Currently selected data:")

data_spacer1, data_1, data_spacer2, data_2, data_spacer3, data_3, data_spacer4, data_4, data_spacer5   = st.columns((.2, 1.6, .2, 1.6, .2, 1.6, .2, 1.6, .2))
with data_1:
    total_num_people = df.count()['HeartDisease']
    str_games = "👥 " + str(total_num_people) + " Observations"
    st.markdown(str_games)

with data_2:
    num_female = df[df['Sex']=='Female'].count()['Sex']
    female_total = "👩 " + str(num_female) + "Female"
    st.markdown(female_total)

with data_3:
    num_male = df[df['Sex']=='Male'].count()['Sex']
    female_total = "👨 " + str(num_male) + "Male"
    st.markdown(female_total)

with data_4:
    num_diseases = "🦠 " + "5 other diseases"
    st.markdown(num_diseases)


st.text('')
see_data = st.expander('You can click here to see 100 data sample 👉')
with see_data:
    st.dataframe(data=df.head(100))
st.text('')


####################
###### Viz 1 #######
####################
st.subheader('Distribution of Heart Disease by Age, Gender and Race')


def age_sex_race():
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
    return age_sex_race


def native():
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
    return native


def asian():
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
    return asian

def black():
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
    return black


def hispanic():
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
    return hispanic


def other_race():
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
    return other


def white():
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
    return white

viz1_col1, viz1_col2 = st.columns([2, 6])

race = list(age_group['Race'].unique())
race.insert(0, 'Not Selected')

with viz1_col1:
    race_selections = st.selectbox ("Race", race)

with viz1_col2:
    if race_selections == race[0]:
        st.write(age_sex_race())
    elif race_selections == race[1]:
        st.write(native())
    elif race_selections == race[2]:
        st.write(asian())
    elif race_selections == race[3]:
        st.write(black())
    elif race_selections == race[4]:
        st.write(hispanic())
    elif race_selections == race[5]:
        st.write(other_race())
    elif race_selections == race[6]:
        st.write(white())

####################
###### Viz 2 #######
####################
st.subheader('How Sleep and Weight Affect Heart Disease?')
##### Data Processing #####
multi_var = df[['HeartDisease', 'PhysicalHealth', 'MentalHealth', 'SleepTime', 'BMI', 'Sex']]

multi_var['HeartDisease'] = multi_var['HeartDisease'].apply(lambda x: convert_to_bool(x))
selector = alt.selection_single(empty='all', fields=['HeartDisease'])
color_scale = alt.Scale(domain=['Yes', 'No'], range=['#D81B60', '#1E88E5'])
alt.data_transformers.disable_max_rows()

##### General Plots #####
bmi_thres = pd.DataFrame([{"bmi_thres": 25}]) #Standard BMI
sleep_thres = pd.DataFrame([{"sleep_thres": 6}]) #Normal Sleep Hours
bmi_rule = alt.Chart(bmi_thres).mark_rule().encode(x='bmi_thres:Q')
sleep_rule = alt.Chart(sleep_thres).mark_rule().encode(x='sleep_thres:Q')

base = alt.Chart(multi_var
        ).properties(
        width=300,
        height=250
        ).add_selection(selector)

def general_plot(allow_output_mutation=True):
    points = base.mark_point(filled=True, size=300
        ).encode(
        x=alt.X('mean(PhysicalHealth):Q',
                title='Avg Days/Month in Physical Discomfort',
                scale=alt.Scale(domain=[0,10])),
        y=alt.Y('mean(MentalHealth):Q',
                title='Avg Days/Month in Mental Discomfort',
                scale=alt.Scale(domain=[0,10])),
        color=alt.condition(selector,
                            'HeartDisease:N',
                            alt.value('lightgray'),
                            scale=color_scale)
        )

    sleep_hists = base.transform_joinaggregate(
        groupby=['HeartDisease'],
        total='count(HeartDisease)'
        ).transform_calculate(
        pct='1 / datum.total'
        ).mark_bar(opacity=0.5, thickness=100
        ).encode(
        x=alt.X('SleepTime',
                title='Sleep Hours',
                bin=alt.Bin(step=2),
                scale=alt.Scale(domain=[0,24])),
        y=alt.Y('sum(pct):Q',
                axis=alt.Axis(format='%'),
                title=None,
                stack=None),
        color=alt.Color('HeartDisease:N',
                        scale=color_scale),
        tooltip=[alt.Tooltip('sum(pct):Q', format='.2%')]
        ).transform_filter(selector)

    bmi_hists = base.transform_joinaggregate(
        groupby=['HeartDisease'],
        total='count(HeartDisease)'
        ).transform_calculate(
        pct='1 / datum.total'
        ).mark_bar(opacity=0.5, thickness=100
        ).encode(
        x=alt.X('BMI',
                title='BMI',
                bin=alt.Bin(step=2),
                ),
        y=alt.Y('sum(pct):Q',
                title=None,
                axis=alt.Axis(format='%'),
                stack=None),
        color=alt.Color('HeartDisease:N',
                        scale=color_scale),
        tooltip=[alt.Tooltip('sum(pct):Q', format='.2%')]
        ).transform_filter(selector)

    combined_1 = (points | (sleep_hists + sleep_rule) | (bmi_hists + bmi_rule)
        ).configure_view(strokeWidth=0
        ).configure_axis(
        labelFontSize=10,
        titleFontSize=12
        ).configure_legend(
        titleFontSize=13,
        labelFontSize=13)

    return combined_1

##### Female Plot #####
def female_plot():
    female_points = base.mark_point(
        filled=True, size=300
        ).transform_filter(
        alt.datum.Sex=='Female'
        ).encode(
        x=alt.X('mean(PhysicalHealth):Q',
                title='Avg Days/Month in Physical Discomfort',
                scale=alt.Scale(domain=[0,10])),
        y=alt.Y('mean(MentalHealth):Q',
                title='Avg Days/Month in Mental Discomfort',
                scale=alt.Scale(domain=[0,10])),
        color=alt.condition(selector,
                            'HeartDisease:N',
                            alt.value('lightgray'),
                            scale=color_scale)
        )

    female_sleep = base.mark_bar(
        opacity=0.5, thickness=100
        ).transform_filter(
        alt.datum.Sex=='Female'
        ).transform_joinaggregate(
        groupby=['HeartDisease'],
        total='count(HeartDisease)'
        ).transform_calculate(
        pct='1 / datum.total'
        ).encode(
        x=alt.X('SleepTime',
                title='Sleep Hours',
                bin=alt.Bin(step=2),
                scale=alt.Scale(domain=[0,24])),
        y=alt.Y('sum(pct):Q',
                axis=alt.Axis(format='%'),
                title=None,
                stack=None),
        color=alt.Color('HeartDisease:N',
                        scale=color_scale),
        tooltip=[alt.Tooltip('sum(pct):Q', format='.2%')]
        ).transform_filter(selector)

    female_bmi = base.mark_bar(
        opacity=0.5, thickness=100
        ).transform_filter(
        alt.datum.Sex=='Female'
        ).transform_joinaggregate(
        groupby=['HeartDisease'],
        total='count(HeartDisease)'
        ).transform_calculate(
        pct='1 / datum.total'
        ).encode(
        x=alt.X('BMI',
                title='BMI',
                bin=alt.Bin(step=2)),
        y=alt.Y('sum(pct):Q',
                title=None,
                axis=alt.Axis(format='%'),
                stack=None),
        color=alt.Color('HeartDisease:N',
                        scale=color_scale),
        tooltip=[alt.Tooltip('sum(pct):Q', format='.2%')]
        ).transform_filter(selector)

    combined_2 = (female_points | (female_sleep + sleep_rule) | (female_bmi + bmi_rule)
        ).configure_view(strokeWidth=0
        ).configure_axis(
        labelFontSize=10,
        titleFontSize=12
        ).configure_legend(
        titleFontSize=13,
        labelFontSize=13)
    return combined_2

##### Male Plot #####

def male_plot():
    male_points = base.mark_point(
        filled=True, size=300
        ).transform_filter(
        alt.datum.Sex=='Male').encode(
        x=alt.X('mean(PhysicalHealth):Q',
                title='Avg Days/Month in Physical Discomfort',
                scale=alt.Scale(domain=[0,10])),
        y=alt.Y('mean(MentalHealth):Q',
                title='Avg Days/Month in Mental Discomfort',
                scale=alt.Scale(domain=[0,10])),
                color=alt.condition(selector,
                                    'HeartDisease:N',
                                    alt.value('lightgray'),
                                    scale=color_scale)
                )

    male_sleep = base.mark_bar(
        opacity=0.5, thickness=100
        ).transform_filter(
        alt.datum.Sex=='Male'
        ).transform_joinaggregate(
        groupby=['HeartDisease'],
        total='count(HeartDisease)'
        ).transform_calculate(
        pct='1 / datum.total'
        ).encode(
        x=alt.X('SleepTime',
                title='Sleep Hours',
                bin=alt.Bin(step=2),
                scale=alt.Scale(domain=[0,24])),
        y=alt.Y('sum(pct):Q',
                axis=alt.Axis(format='%'),
                title=None,
                stack=None),
        color=alt.Color('HeartDisease:N',
                        scale=color_scale),
        tooltip=[alt.Tooltip('sum(pct):Q', format='.2%')]
        ).transform_filter(selector)

    male_bmi = base.mark_bar(
        opacity=0.5, thickness=100
        ).transform_filter(
        alt.datum.Sex=='Male'
        ).transform_joinaggregate(
        groupby=['HeartDisease'],
        total='count(HeartDisease)'
        ).transform_calculate(
        pct='1 / datum.total'
        ).encode(
        x=alt.X('BMI',
                title='BMI',
                bin=alt.Bin(step=5)),
        y=alt.Y('sum(pct):Q',
                title=None,
                axis=alt.Axis(format='%'),
                stack=None),
        color=alt.Color('HeartDisease:N',
                        scale=color_scale),
        tooltip=[alt.Tooltip('sum(pct):Q', format='.2%')]
        ).transform_filter(selector)

    combined_3 = (male_points | (male_sleep + sleep_rule) | (male_bmi + bmi_rule)
        ).configure_view(strokeWidth=0
        ).configure_axis(
        labelFontSize=10,
        titleFontSize=12
        ).configure_legend(
        titleFontSize=13,
        labelFontSize=13)
    return combined_3

##### Implement Viz 2 in Streamlit #####
viz2_col1, viz2_col2 = st.columns([1, 7])

gender = list(multi_var['Sex'].unique())
gender.insert(0, 'Not Selected')

with viz2_col1:
    sex_selections = st.selectbox("Gender", gender)

with viz2_col2:
    if sex_selections == gender[0]:
        st.write(general_plot())
    elif sex_selections == gender[1]:
        st.write(female_plot())
    elif sex_selections == gender[2]:
        st.write(male_plot())

####################
###### Viz 3 #######
####################
st.subheader('How Are the Underlying Diseases Related to Heart Disease?')

other_diseases = df[['HeartDisease', 'Stroke', 'Diabetic', 'Asthma', 'KidneyDisease', 'SkinCancer']]
ls_diseases = ['Stroke', 'Diabetic', 'Asthma', 'KidneyDisease', 'SkinCancer']

for dis in ls_diseases:
    other_diseases[dis] = other_diseases[dis].apply(lambda x: convert_to_int(x))

num_heart_disease = other_diseases['HeartDisease'].value_counts()
other_diseases = other_diseases.groupby(['HeartDisease']).sum()
other_diseases['Num_HeartDisease'] = num_heart_disease

for dis in ls_diseases:
    other_diseases[dis] = other_diseases[dis] / other_diseases['Num_HeartDisease']

other_diseases = other_diseases.reset_index()
other_diseases.drop(['Num_HeartDisease'], axis=1, inplace=True)
other_diseases = other_diseases.set_index('HeartDisease', append=False).unstack('HeartDisease')
other_diseases = pd.DataFrame(other_diseases)
other_diseases = other_diseases.reset_index()
other_diseases = other_diseases.rename(columns={'level_0': 'other_diseases', 0: 'percentage'})
other_diseases['HeartDisease'] = other_diseases['HeartDisease'].apply(lambda x: convert_to_bool(x))

def diseases():
    diseases = alt.Chart(other_diseases).mark_bar(
        cornerRadiusTopLeft=3,
        cornerRadiusTopRight=3
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q',
                axis=alt.Axis(format='%', grid=False)
            ),
        color='other_diseases',
        tooltip=['other_diseases:N', alt.Tooltip('percentage:Q', format='.2%')]
        ).properties(
        width=450,
        height=500
        ).configure_view(strokeWidth=0
        ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
        ).configure_legend(
        titleFontSize=13,
        labelFontSize=13)
    return diseases

##### ASTHMA #####
def asthma():
    asthma = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='Asthma').mark_bar(
        cornerRadiusTopLeft=3,
        cornerRadiusTopRight=3
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q',
                axis=None,
                scale=alt.Scale(domain=(0,0.35))),
        tooltip=['other_diseases:N', alt.Tooltip('percentage:Q', format='.2%')]
        ).properties(
        width=450,
        height=500)
    asthma_annot = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='Asthma'
        ).mark_text(
        baseline='middle',
        dx=2,
        dy=-8,
        fontSize=14
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q', axis=None),
        text=alt.Text('percentage:Q',format='.2%'))
    asthma_viz = (asthma+asthma_annot).configure_view(
        strokeWidth=0
        ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
        )
    return asthma_viz

##### DIABETIC #####
def diabetic():
    diabetic = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='Diabetic').mark_bar(
        cornerRadiusTopLeft=3,
        cornerRadiusTopRight=3
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q',
                axis=None,
                scale=alt.Scale(domain=(0,0.35))),
        tooltip=['other_diseases:N', alt.Tooltip('percentage:Q', format='.2%')]
        ).properties(
        width=450,
        height=500)
    diabetic_annot = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='Diabetic'
        ).mark_text(
        baseline='middle',
        dx=2,
        dy=-8,
        fontSize=14
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q', axis=None),
        text=alt.Text('percentage:Q',format='.2%'))
    diabetic_viz = (diabetic+diabetic_annot).configure_view(
        strokeWidth=0
        ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
        )
    return diabetic_viz

##### KIDNEY #####
def kidney_disease():
    kidney_disease = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='KidneyDisease').mark_bar(
        cornerRadiusTopLeft=3,
        cornerRadiusTopRight=3
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q',
                axis=None,
                scale=alt.Scale(domain=(0,0.35))),
        tooltip=['other_diseases:N', alt.Tooltip('percentage:Q', format='.2%')]
        ).properties(
        width=450,
        height=500)
    kidney_annot = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='KidneyDisease'
        ).mark_text(
        baseline='middle',
        dx=2,
        dy=-8,
        fontSize=14
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q', axis=None),
        text=alt.Text('percentage:Q',format='.2%'))
    kidney_viz = (kidney_disease+kidney_annot).configure_view(
        strokeWidth=0
        ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
        )
    return kidney_viz

##### SKIN CANCER #####
def skin_cancer():
    skin_cancer = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='SkinCancer').mark_bar(
        cornerRadiusTopLeft=3,
        cornerRadiusTopRight=3,
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q',
                axis=None,
                scale=alt.Scale(domain=(0,0.35))),
        tooltip=['other_diseases:N', alt.Tooltip('percentage:Q', format='.2%')]
        ).properties(
        width=450,
        height=500)
    skin_annot = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='SkinCancer'
        ).mark_text(
        baseline='middle',
        dx=2,
        dy=-8,
        fontSize=14
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q', axis=None),
        text=alt.Text('percentage:Q',format='.2%'))
    skin_viz = (skin_cancer+skin_annot).configure_view(
        strokeWidth=0
        ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
        )
    return skin_viz

##### STROKE #####
def stroke():
    stroke = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='Stroke').mark_bar(
        cornerRadiusTopLeft=3,
        cornerRadiusTopRight=3,
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q',
                axis=None,
                scale=alt.Scale(domain=(0,0.35))),
        tooltip=['other_diseases:N', alt.Tooltip('percentage:Q', format='.2%')]
        ).properties(
        width=450,
        height=500)
    stroke_annot = alt.Chart(other_diseases
        ).transform_filter(
        alt.datum.other_diseases=='Stroke'
        ).mark_text(
        baseline='middle',
        dx=2,
        dy=-8,
        fontSize=14
        ).encode(
        x=alt.X('HeartDisease:N', axis=alt.Axis(grid=False)),
        y=alt.Y('percentage:Q', axis=None),
        text=alt.Text('percentage:Q',format='.2%'))
    stroke_viz = (stroke+stroke_annot).configure_view(
        strokeWidth=0
        ).configure_axis(
        labelFontSize=14,
        titleFontSize=16
        )
    return stroke_viz

##### Implement Viz 3 in Streamlit #####
viz3_col1, viz3_col2 = st.columns([3, 6])

underlying = list(other_diseases['other_diseases'].unique())
underlying.insert(0, 'Not Selected')

with viz3_col1:
    dis_selections = st.selectbox("Underlying Diseases", underlying)

with viz3_col2:
    if dis_selections == underlying[0]:
        st.write(diseases())
    elif dis_selections == underlying[1]:
        stroke_desc = """
                    <p style="font-size: 18px;">
                    Among patients with heart disease, 16.03% also suffer from stroke.</p>
                    <p style="font-size: 18px;">
                    Compared to people without heart disease,
                    patients with heart disease had about 6.1 times more strokes.</p>"""
        st.markdown(stroke_desc, unsafe_allow_html=True)
        st.write(stroke())
    elif dis_selections == underlying[2]:
        diabete_desc = """
                    <p style="font-size: 18px;">
                    Among patients with heart disease, 32.72% also suffer from diabetes.</p>
                    <p style="font-size: 18px;">
                    Compared to people without heart disease,
                    patients with heart disease had about 3 times more diabetes.</p>"""
        st.markdown(diabete_desc, unsafe_allow_html=True)
        st.write(diabetic())
    elif dis_selections == underlying[3]:
        asthma_desc = """
                    <p style="font-size: 18px;">
                    Among patients with heart disease, 18.02% also suffer from asthma.</p>
                    <p style="font-size: 18px;">
                    Compared to people without heart disease,
                    patients with heart disease had about 1.4 times more asthma.</p>"""
        st.markdown(asthma_desc, unsafe_allow_html=True)
        st.write(asthma())
    elif dis_selections == underlying[4]:
        kidney_desc = """<p style="font-size: 18px;">
                    Among patients with heart disease, 12.62% also suffer from kidney disease.</p>
                    <p style="font-size: 18px;">
                    Compared to people without heart disease,
                    patients with heart disease had about 4.4 times more kidney disease.</p>"""
        st.markdown(kidney_desc, unsafe_allow_html=True)
        st.write(kidney_disease())
    elif dis_selections == underlying[5]:
        kidney_desc = """<p style="font-size: 18px;">
                    Among patients with heart disease, 18.19% also suffer from skin cancer.</p>
                    <p style="font-size: 18px;">
                    Compared to people without heart disease,
                    patients with heart disease had about 2.1 times more skin cancer.</p>"""
        st.markdown(kidney_desc, unsafe_allow_html=True)
        st.write(skin_cancer())


####################
###### Viz 4 #######
####################
st.subheader('Does Smoking/Drinking habits and BMI change the risk of Heart Disease?')
bmi_desc = """<p style="font-size: 18px;">First, let's calculate your BMI.</p>"""
st.markdown(bmi_desc, unsafe_allow_html=True)
userWeight = int(st.text_input('What is your weight? (lbs)', 190))
userHeight = float(st.text_input('What is your height? (ft)', 5.6))
ft_to_m = userHeight/3.28084
bmi = round((userWeight/2.20462)/(ft_to_m*ft_to_m),2)
weight_status=None
if bmi <= 18.5 :
    weight_status = 'underweight'
elif 18.5<bmi<=24.9 :
    weight_status = 'normal'
elif 25<bmi<=29.9 :
    weight_status = 'overweight'
else:
    weight_status = 'obese'

bmi_str = f"""<style>p.a {{font: bold 23px Courier; color: Green;}}</style><p class="a">{bmi}</p>"""
weight_str = f"""<style>p.a {{font: bold 23px Courier; color: Green;}}</style><p class="a">{weight_status}</p>"""
st.write('Your BMI is : ')
st.markdown(bmi_str, unsafe_allow_html=True)
st.write('Based on your BMI, your weight status is : ')
st.markdown(weight_str, unsafe_allow_html=True)

smoking_str = """<p style="font-size: 18px; color"Green";>Smoking is a major cause of cardiovascular disease (CVD) and causes approximately one of every four deaths from CVD, 
    according to the 2014 Surgeon General’s Report on smoking and health. Chemicals in cigarette smoke cause the cells that line blood vessels to become swollen and inflamed. <br />
    This can narrow the blood vessels and can lead to many cardiovascular conditions.<br />
    <br />

    </p>"""
st.markdown(smoking_str, unsafe_allow_html=True)


bmi_labels = ['underweight', 'normal', 'overweight', 'obese']
smdr_labels = ['smoking only', 'smoking & drinking', 'drinking only', 'none']

selection=alt.selection_single(encodings=['y'], on="mouseover", clear="mouseout")
opacity = alt.condition(selection, alt.value(1.0), alt.value(0.4))

def lifestyle_viz():
    heatmap = alt.Chart(
        table_3, 
        width=450, height=300, 
        title='Percentage of Heart Disease by BMI and Smoking/Drinking'
        ).mark_rect().encode(
        x = alt.X("BMI label:N", sort=bmi_labels, axis=alt.Axis(labelAngle=15)),
        y = alt.Y("smdr:N", sort=smdr_labels, title=None),
        color = alt.Color('perc_sb:Q', scale=alt.Scale(scheme='lightmulti'), title="%"),
        opacity=opacity
        )
    text = heatmap.mark_text(
        align='center', baseline='middle'
        ).encode(
        text = alt.Text('perc_sb:Q', format='0.2f'),
        color = (alt.value('black'))
        )
    chart1 = (heatmap +text)

    bar1 = alt.Chart(
        table_3, 
        width=450, height=120, 
        title='Percentage of Heart Disease by BMI range'
        ).mark_bar().transform_joinaggregate(
        groupby=['BMI label']
        ).encode(
        x = alt.X('mean(perc_b):Q', axis=alt.Axis(format="0.0%"), title=None),
        y = alt.Y('BMI label:N', title=None, sort=['underweight', 'normal', 'overweight', 'obese']),
        color = alt.Color('mean(perc_b):Q', scale=alt.Scale(scheme='lightmulti')),
        tooltip = alt.Tooltip('perc_b:Q', format="0.0%"),
        opacity = opacity
        ).add_selection(selection)

    bar2 = alt.Chart(
        table_3, 
        width=450, height=120, 
        title='Percentage of Heart Disease by Smoking/Drinking'
        ).mark_bar().transform_joinaggregate(
        groupby=['smdr']
        ).encode(
        x = alt.X('mean(perc_s):Q', axis=alt.Axis(format="0.0%"), title=None),
        y = alt.Y('smdr:N', title=None, sort=['smoking only', 'smoking & drinking', 'drinking only', 'none']),
        color = alt.Color('mean(perc_s):Q', scale=alt.Scale(scheme='lightmulti'), legend=None),
        tooltip = alt.Tooltip('perc_s:Q', format="0.0%"),
        opacity = opacity
        ).add_selection(selection)

    chart2 = alt.vconcat(bar2, bar1).resolve_scale(x='shared')
    viz4 = (chart2 | chart1).resolve_scale(color='independent')

    return viz4

st.write(lifestyle_viz())

####################
######Drinking######
####################
st.subheader('Drinking and Heart Condition?')
drinking_comment = """<p style="font-size: 18px;">Moderate drinking -- one drink a day for women and two for men -- appears to protect some people against heart disease. <br />
    However, Doctors are not sure if those healthy effects come from the alcohol or from other good lifestyle choices that light drinkers make. 
    So if you don’t drink already, your heart is not a reason to start. A healthy diet and regular exercise provide many of the same good effects that are tied to alcohol.
    </p>"""
st.markdown(drinking_comment, unsafe_allow_html=True)
st.markdown("""[Source: WebMD](https://www.webmd.com/heart-disease/heart-disease-alcohol-your-heart)""")

####################
##### Sidebar  #####
####################

st.subheader('Overall probabilty of Heart Disease based on your personal condition')
side_desc = """<p style="font-size: 18px;">Press "predict" on the bottom of the sidebar after you select your health condition.</p>"""
st.markdown(side_desc, unsafe_allow_html=True)

def user_select_features():
    race = st.sidebar.selectbox("Race", options=(race for race in df['Race'].unique()))
    sex = st.sidebar.selectbox("Sex", options=(sex for sex in df['Sex'].unique()))
    age_cat = st.sidebar.selectbox("Age category", options=(age for age in df['AgeCategory'].unique()))
    bmi_cat = st.sidebar.number_input('Enter your BMI: ', 12, 95)
    sleep_time = st.sidebar.number_input("How many hours on average do you sleep?", 0, 24, 7)
    gen_health = st.sidebar.selectbox("How can you define your general health?",
                                        options=(health for health in df['GenHealth'].unique()))
    phys_health = st.sidebar.number_input("For how many days during the past 30 days was"
                                            " your physical health not good?", 0, 30, 0)
    ment_health = st.sidebar.number_input("For how many days during the past 30 days was"
                                            " your mental health not good?", 0, 30, 0)
    phys_act = st.sidebar.selectbox("Have you played any sports (running, biking, etc.)"
                                    " in the past month?", options=("No", "Yes"))
    smoking = st.sidebar.selectbox("Have you smoked at least 100 cigarettes in"
                                    " your entire life (approx. 5 packs)?)",
                                    options=("No", "Yes"))
    alcohol_drink = st.sidebar.selectbox("Do you have more than 14 drinks of alcohol (men)"
                                            " or more than 7 (women) in a week?", options=("No", "Yes"))
    stroke = st.sidebar.selectbox("Did you have a stroke?", options=("No", "Yes"))
    diff_walk = st.sidebar.selectbox("Do you have serious difficulty walking"
                                        " or climbing stairs?", options=("No", "Yes"))
    diabetic = st.sidebar.selectbox("Have you ever had diabetes?",
                                    options=(diabetic for diabetic in df['Diabetic'].unique()))
    asthma = st.sidebar.selectbox("Do you have asthma?", options=("No", "Yes"))
    kid_dis = st.sidebar.selectbox("Do you have kidney disease?", options=("No", "Yes"))
    skin_canc = st.sidebar.selectbox("Do you have skin cancer?", options=("No", "Yes"))

    features = pd.DataFrame({
                "BMI": [bmi_cat],
                "PhysicalHealth": [phys_health],
                "MentalHealth": [ment_health],
                "SleepTime": [sleep_time],
                "Smoking": [smoking],
                "AlcoholDrinking": [alcohol_drink],
                "Stroke": [stroke],
                "DiffWalking": [diff_walk],
                "Sex": [sex],
                "AgeCategory": [age_cat],
                "Race": [race],
                "Diabetic": [diabetic],
                "PhysicalActivity": [phys_act],
                "GenHealth": [gen_health],
                "Asthma": [asthma],
                "KidneyDisease": [kid_dis],
                "SkinCancer": [skin_canc]
            })
    return features

st.sidebar.title("Let's predict your probability of getting heart disease")
st.sidebar.markdown("Select conditions below and we will give you the probability")
st.sidebar.image("images/heart_side.jpeg", width=100)
input_df = user_select_features()
submit = st.sidebar.button("Predict")

####################
##### Predict  #####
####################
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import pickle
MODEL_FILEPATH = "finalized_model.pkl"
PIPE_FILEPATH = "pipeline.pkl"

preprocess_pipeline = pickle.load(open(PIPE_FILEPATH, 'rb'))

logmodel = pickle.load(open(MODEL_FILEPATH, "rb"))

if submit:
    trans_input_df = preprocess_pipeline.transform(input_df)
    prediction = logmodel.predict(trans_input_df)
    prediction_prob = logmodel.predict_proba(trans_input_df)
    if prediction == 0:
        st.info(f"""**The probability that you'll have heart disease is 
        {round(prediction_prob[0][1] * 100, 2)}%. You are healthy!**""")
    else:
        st.info(f"""**The probability that you will have heart disease is 
        {round(prediction_prob[0][1] * 100, 2)}%. It sounds like you are not healthy.**""")
