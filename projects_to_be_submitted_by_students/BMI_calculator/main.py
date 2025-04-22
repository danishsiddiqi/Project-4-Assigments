import streamlit as st


st.title("BMI CALCULATOR")


weight = st.number_input("Enter your weight in kg.")
height = st.number_input("Enter your height in cm.")
final_height =height ** 2
if st.button("Calculate BMI"):
    
        bmi = weight / final_height
        st.success(f"Your BMI is {bmi:.2f}")
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
        st.error("Please enter valid weight and height values.")
