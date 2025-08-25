import streamlit as st
from joblib import load
import numpy as np

dTmodel = load('decision_tree_model.joblib')

subscription_type = st.selectbox(
    "Select Subscription Type",
    options=[0, 1, 2],
    format_func=lambda x: {0: "Basic", 1: "Standard", 2: "Premium"}[x]
)

monthly_fee = st.selectbox(
    "Select Monthly Fee",
    options=[1, 2, 3],
    format_func=lambda x: {1: "$8.99", 2: "$13.99", 3: "$17.99"}[x]
)

number_of_profiles = st.selectbox(
    "Select Number of Profiles",
    options=list(range(1, 6))  # 1 到 5
)

watch_hours = st.number_input("Enter total watch hours", min_value=0.0, step=1.0)
last_login_days = st.number_input("Enter days since last login", min_value=0, step=1)
avg_watch_time_per_day = st.number_input("Enter avg watch time per day", min_value=0, step=1)

if st.button("Predict Churn"):
    import numpy as np
    from joblib import load
    
    dTmodel = load("decision_tree_model.joblib")
    
    input_array = np.array([[
        subscription_type,
        watch_hours,
        last_login_days,
        monthly_fee,
        number_of_profiles,
        avg_watch_time_per_day
    ]])
    
    predicted_churn = dTmodel.predict(input_array)[0]
    predicted_output = "Retain" if predicted_churn == 0 else "Churn"
    
    st.success(f"Predicted Churn: {predicted_output}")