# modules/inicio.py

import streamlit as st

def mostrar():
    st.title("🌴 Capitalismo Tropical")
    st.subheader("💸 Capital inicial: $50,000 MXN")
    st.markdown("Elige cómo quieres comenzar tu aventura:")

    opcion = st.radio("Opciones:", [
        "Invertir solo",
        "Buscar socio",
        "Solicitar préstamo"
    ])

    st.markdown(f"Elegiste: **{opcion}**")
    if st.button("👉 Comenzar"):
        st.success("¡Listo para elegir tu tipo de negocio!")