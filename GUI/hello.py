import streamlit as st
import joblib 

model = joblib.load("RandomForest.pkl")
col1, col2, col3 = st.columns([1, 1, 1])  # 

with col1:
    st.write("")
    st.image("C:\\Users\\Dell\\Downloads\\food2.png", width=150)

with col2:
    st.image("C:\\Users\\Dell\\Downloads\\balanced_diet.png", width=150)

with col3:
    st.write("")
    st.image("C:\\Users\\Dell\\Downloads\\food1.png", width=150)

st.title("HealthyMe – Obesity Predictor")
#dataset=['Weight','Height','Age','family_history_with_overweight','FAVC','FAF','TUE']
age = st.number_input("write your age", min_value=1, max_value=100, step=1)
Weight=st.number_input("weight(KG)",min_value=30.0,max_value=200.0,value=70.0)
Height=st.number_input("height(m)",min_value=1.0,max_value=2.5,value=1.70)
FAVC = st.radio("are you frequently consumes high-calorie foods", ["Yes", "No"])
FAF = st.slider("Physical activity frequency", 0, 3, 1)
TUE=st.slider("Time spent using technology", 0,3,1)

input_data = [[age,Weight,Height,FAVC,FAF,TUE]]
if st.button("predict"):
    prediction = model.predict(input_data)
    st.success(f"result {prediction[0]}")
