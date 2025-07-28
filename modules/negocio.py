import streamlit as st
import json
from datetime import datetime

# 🧾 Cargar negocios desde JSON
try:
    with open("data/negocios.json", "r", encoding="utf-8") as f:
        NEGOCIOS_LISTA = json.load(f)
    NEGOCIOS = {neg["nombre"]: neg for neg in NEGOCIOS_LISTA}
except Exception as e:
    st.error("❌ No se pudo cargar el catálogo de negocios.")
    st.stop()

def mostrar():
    st.title("🛍️ Elige tu negocio")
    st.subheader("Cada opción tiene riesgos y oportunidades únicas")

    if not NEGOCIOS:
        st.warning("🪫 No hay negocios registrados. Agrega al menos uno en el archivo `negocios.json`.")
        return

    negocio_seleccionado = st.selectbox(
        "📦 Tipos de negocio disponibles:",
        options=list(NEGOCIOS.keys()),
        format_func=lambda x: f"{NEGOCIOS[x]['emoji']} {x.capitalize()}",
        index=0
    )

    if negocio_seleccionado is None:
        st.info("Selecciona un negocio para ver los detalles.")
        return

    negocio = NEGOCIOS[negocio_seleccionado]

    st.markdown("---")
    st.markdown(f"### {negocio['emoji']} Detalles del negocio seleccionado")
    st.markdown(f"💰 **Costo inicial:** ${negocio['costo_inicial']:,} MXN")
    st.markdown(f"📉 **Gasto mensual:** ${negocio['gasto_mensual']:,} MXN")
    st.markdown(f"📈 **Ganancia promedio:** ${negocio['ganancia_media']:,} MXN")
    st.markdown("🔍 Piensa bien: no hay marcha atrás una vez arrancas...")

    # 🚀 Lanzar negocio y registrar en historial
    if st.button("🚀 Lanzar negocio"):
        st.success(f"¡Tu negocio de {negocio_seleccionado.capitalize()} ha sido lanzado! Prepárate para tomar decisiones.")

        nuevo_lanzamiento = {
            "nombre": negocio_seleccionado,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "emoji": negocio["emoji"],
            "costo_inicial": negocio["costo_inicial"],
            "gasto_mensual": negocio["gasto_mensual"],
            "ganancia_media": negocio["ganancia_media"]
        }

        try:
            with open("data/historial_negocios.json", "r", encoding="utf-8") as f:
                historial = json.load(f)
        except:
            historial = []

        historial.append(nuevo_lanzamiento)

        with open("data/historial_negocios.json", "w", encoding="utf-8") as f:
            json.dump(historial, f, indent=4, ensure_ascii=False)

        st.toast("🎯 Lanzamiento registrado en el historial.")