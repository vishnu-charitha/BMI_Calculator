import streamlit as st

# Page config
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚕️",
    layout="centered"
)

# Title
st.title("⚕️ BMI Calculator")
st.write("Calculate your Body Mass Index (BMI)")

st.divider()

# Inputs
name = st.text_input("Enter your name")

weight = st.number_input(
    "Enter your weight (kg)",
    min_value=1.0,
    max_value=300.0,
    step=0.1
)

height = st.number_input(
    "Enter your height in meters (Example: 1.70)",
    min_value=0.5,
    max_value=3.0,
    step=0.01,
    help="Example: 170 cm = 1.70 meters"
)

# Button
if st.button("Calculate BMI"):

    bmi = weight / (height ** 2)

    # Category & suggestion
    if bmi < 18.5:
        category = "Underweight"
        suggestion = "Eat nutritious food and maintain a healthy diet."

    elif bmi < 25:
        category = "Normal Weight"
        suggestion = "Great! Maintain your healthy lifestyle."

    elif bmi < 30:
        category = "Overweight"
        suggestion = "Exercise regularly and eat healthy food."

    else:
        category = "Obese"
        suggestion = "Consult a healthcare expert and focus on fitness."

    # Result
    st.success(f"{name}'s BMI: {bmi:.2f}")

    st.subheader("Result")
    st.write(f"**Category:** {category}")
    st.write(f"**Suggestion:** {suggestion}")

    st.subheader("BMI Level")
    st.progress(min(int(bmi), 100))

    st.info("BMI is only a general health indicator.")