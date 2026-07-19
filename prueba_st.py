import streamlit as st

# Frontend: user inputs
precio = st.number_input("Base price:")
impuesto = st.slider("Tax (%)", 0, 100, 21)

# Backend: processing
precio_final = precio * (1 + impuesto / 100)

# Frontend: displaying the output
st.write(f"💰 Final price with tax: {precio_final:.2f}")