import streamlit as st

# Page title
st.title("💰 Tax Calculator for my baby")

# User inputs
client_name = st.text_input("Add your Name")
precio = st.number_input("add your salary ($)", min_value=0.0, value=0.0)
impuesto = st.slider("Tax (%)", 0, 100, 21)

# Calculation
precio_final = precio * (1 - impuesto / 100)

# Output
if client_name:
    st.success(
        f"Hello **{client_name}**! Your salary after tax is **${precio_final:.2f}**, so your are poor again."
    )
else:
    st.info(
        f"Your salary after tax is **${precio_final:.2f}**, so your are poor again."
    )