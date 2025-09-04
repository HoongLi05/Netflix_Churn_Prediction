import streamlit as st
from joblib import load
import numpy as np

dTmodel = load('decisionTree_model.joblib')

# --- Title ---
st.title("🎬 Netflix Churn Prediction")

subscription_type = st.selectbox(
    "Select Subscription Type",
    options=[1, 2, 3],
    format_func=lambda x: {1: "Basic", 2: "Standard", 3: "Premium"}[x],
)

# Automatically map monthly fee based on subscription type
fee_mapping = {1: 8.99, 2: 13.99, 3: 17.99}
monthly_fee = fee_mapping[subscription_type]

# Display the monthly fee (read-only)
st.write(f"Monthly Fee: ${monthly_fee}")

number_of_profiles = st.selectbox(
    "Select Number of Profiles",
    options=list(range(1, 6))
)

# number_of_profiles = st.number_input("Enter number of profiles", min_value=1, max_value=5, step=1)

watch_hours = st.number_input("Enter total watch hours", min_value=0.0, step=1.0)
last_login_days = st.number_input("Enter days since last login", min_value=0, step=1)
avg_watch_time_per_day = st.number_input(
    "Enter avg watch time per day (hours)", 
    min_value=0.0, 
    step=0.1
)

has_error = False

if watch_hours != 0 and avg_watch_time_per_day == 0:
    st.error("⚠️ Average watch time per day cannot be 0 if total watch hours is not 0.")
    has_error = True

elif avg_watch_time_per_day > watch_hours:
    st.error("⚠️ Average watch time per day cannot be greater than total watch hours.")
    has_error = True

else:
    st.success("✅ Input values look valid!")

# --- Disable Predict button if error exists ---
predict_btn = st.button("Predict Churn", disabled=has_error)

if predict_btn:
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
