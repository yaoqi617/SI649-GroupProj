####################
##### Predict  #####
####################
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

df = pd.read_csv("heart_2020_cleaned.csv")
def convert_to_int(x):
    if x == 'Yes':
        return 1
    else:
        return 0

df['HeartDisease'] = df['HeartDisease'].apply(lambda x: convert_to_int(x))

X_train, x_test, y_train, y_test = train_test_split(df.drop('HeartDisease',axis=1),
                                                        df['HeartDisease'], test_size=0.30,
                                                        random_state=101)

num_pip = Pipeline([
        ("scaler", StandardScaler())
    ])
categorical_pip = Pipeline([("cat_encoder", OneHotEncoder(sparse=False))])
categorical_attr = ["Smoking", "AlcoholDrinking", "Stroke", "DiffWalking", 
            "Sex", "AgeCategory", "Race", "Diabetic", "PhysicalActivity", 
            "GenHealth", "Asthma", "KidneyDisease", "SkinCancer"]
num_attr = ["BMI", "PhysicalHealth", "MentalHealth", "SleepTime"]

preprocess_pipeline = ColumnTransformer([
        ("num", num_pip, num_attr),
        ("cat", categorical_pip, categorical_attr)
    ])

X = preprocess_pipeline.fit_transform(
    X_train[num_attr + categorical_attr])

y = y_train

oversample = SMOTE()
X_oversample, y_oversample = oversample.fit_resample(X, y)
logmodel = LogisticRegression()
logmodel.fit(X_oversample, y_oversample)

filename = 'finalized_model.pkl'
pickle.dump(logmodel, open(filename, 'wb'))
