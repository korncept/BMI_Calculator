import streamlit as st

st.set_page_config(page_title="Cornell's BMI Calculator", page_icon="💪")

st.title("💪 Cornell's BMI Calculator")
st.markdown("Find out your Body Mass Index in seconds!")

st.divider()

user_height = st.number_input("What is your height in metres?", min_value=0.5, max_value=3.0, value=1.70, step=0.01, format="%.2f")
st.write(f"Your height is **{user_height} metres**. Okay!")

user_weight = st.number_input("What do you weigh in kilograms?", min_value=1.0, max_value=300.0, value=70.0, step=0.1, format="%.1f")
st.write(f"Your weight is **{user_weight} kilograms**. Cool!")

st.divider()

if st.button("Calculate my BMI 🚀"):
    bmi = user_weight / (user_height ** 2)
    st.success(f"**Your Body Mass Index is: {round(bmi, 2)}**")

    if user_height < 1.70:
        st.info(f"You are really short for someone that is {user_height} metres tall, hehehe! 😄")
    elif user_height == 1.70:
        st.info(f"You are basically just average height for someone that is {user_height} metres tall, not bad! 😊")
    else:
        st.info(f"You are also quite tall for someone that is {user_height} metres tall, hehehe! 😄")

    st.divider()
    st.markdown("### What does your BMI mean?")
    if bmi < 18.5:
        st.warning("⚠️ Underweight (BMI below 18.5)")
    elif 18.5 <= bmi < 25.0:
        st.success("✅ Normal weight (BMI 18.5 – 24.9)")
    elif 25.0 <= bmi < 30.0:
        st.warning("⚠️ Overweight (BMI 25.0 – 29.9)")
    else:
        st.error("❗ Obese (BMI 30.0 and above)")
