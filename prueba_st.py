import streamlit as st

# Page title
st.title("💰 Tax Calculator Dashboard")

# User inputs
client_name = st.text_input("Client Name")
precio = st.number_input("Base Price ($)", min_value=0.0, value=0.0)
impuesto = st.slider("Tax (%)", 0, 100, 21)

# Calculation
precio_final = precio * (1 + impuesto / 100)

# Output
if client_name:
    st.success(
        f"Hello **{client_name}**! The final price including tax is **${precio_final:.2f}**."
    )
else:
    st.info(
        f"The final price including tax is **${precio_final:.2f}**."
    )