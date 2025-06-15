import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

st.title("💪 BMI Calculator")
st.markdown("### Enter your details below to calculate your Body Mass Index:")

# Weight input
weight = st.number_input("⚖️ Enter your weight in kg:", min_value=1.0, step=0.5)

# Height input option selector
height_unit = st.radio("Select height input unit:", ("Centimeters (cm)", "Feet & Inches"))

if height_unit == "Centimeters (cm)":
    height_cm = st.number_input("📏 Enter your height in cm:", min_value=50.0, step=0.5)
elif height_unit == "Feet & Inches":
    feet = st.number_input("Feet", min_value=0, max_value=10, step=1)
    inches = st.number_input("Inches", min_value=0, max_value=11, step=1)
    # Convert feet & inches to cm
    height_cm = (feet * 30.48) + (inches * 2.54)

if st.button("Calculate BMI"):
    if weight and height_cm:
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        st.markdown(f"### 🧮 Your BMI is: `{bmi:.2f}`")

        if bmi < 18.5:
            st.warning("🔸 You are **Underweight**. Try eating a balanced, nutritious diet.")
        elif 18.5 <= bmi <= 24.9:
            st.success("✅ You have **Normal weight**. Keep it up with healthy habits!")
        elif 25 <= bmi <= 29.9:
            st.info("⚠️ You are **Overweight**. Consider regular exercise and a healthy routine.")
        else:
            st.error("🚨 You are **Obese**. It’s best to consult a doctor or a nutritionist.")

        st.markdown("---")
        st.caption("Developed by **Samra Moinuddin** 👩‍💻 — The Creative Coder 💡")
    else:
        st.error("Please enter both weight and height.")
