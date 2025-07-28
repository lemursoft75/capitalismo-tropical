# modules/negocio.py

import streamlit as st
from config import NEGOCIOS, EMOJIS

def mostrar():
    st.title("🛍️ Elige tu negocio")
    st.subheader("Cada opción tiene riesgos y oportunidades únicas")

    negocio_seleccionado = st.selectbox(
        "📦 Tipos de negocio disponibles:",
        options=list(NEGOCIOS.keys()),
        format_func=lambda x: f"{NEGOCIOS[x]['emoji']} {x.capitalize()}"
    )

    negocio = NEGOCIOS[negocio_seleccionado]

    st.markdown("---")
    st.markdown(f"### {negocio['emoji']} Detalles del negocio seleccionado")
    st.markdown(f"💰 **Costo inicial:** ${negocio['costo_inicial']} MXN")
    st.markdown(f"📉 **Gasto mensual:** ${negocio['gasto_mensual']} MXN")
    st.markdown(f"📈 **Ganancia promedio:** ${negocio['ganancia_media']} MXN")
    st.markdown("🔍 Piensa bien: no hay marcha atrás una vez arrancas...")

    if st.button("🚀 Lanzar negocio"):
        st.success(f"¡Tu negocio de {negocio_seleccionado.capitalize()} ha sido lanzado! Prepárate para tomar decisiones.")