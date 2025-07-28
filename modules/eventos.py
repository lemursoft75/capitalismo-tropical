import streamlit as st
import pandas as pd
import json
from utils import helpers

def mostrar():
    st.title("🎉 Eventos Corporativos Tropicales")
    st.subheader("Impacto narrativo, emocional y estratégico por sede")

    # 📦 Cargar eventos desde JSON
    try:
        with open("data/eventos.json", "r", encoding="utf-8") as f:
            eventos_data = json.load(f)
        df = pd.DataFrame(eventos_data)
    except FileNotFoundError:
        st.warning("No se encontró historial de eventos.")
        return

    st.markdown("### 🗓️ Eventos por Mes y Sucursal")
    eventos = df["Evento"].unique()
    for evento in eventos:
        datos = df[df["Evento"] == evento]
        sucursal = datos["Sucursal"].iloc[0]
        impacto_efi = helpers.eficiencia_promedio(datos, "ImpactoEficiencia")
        impacto_clima = helpers.eficiencia_promedio(datos, "ImpactoClima")

        st.markdown(f"**{evento}** ({sucursal})")
        st.write(f"- 📈 Impacto en eficiencia: {impacto_efi:+.2f}")
        st.write(f"- 🌤️ Impacto en clima: {impacto_clima:+.2f}")
        st.line_chart(datos.set_index("Mes")[["ImpactoEficiencia", "ImpactoClima"]])
        st.markdown("---")

    # 🎭 Frases de empleados clave involucrados
    st.subheader("🎙️ Reacciones Emocionales")
    empleados = df["Empleado"].dropna().unique()
    for nombre in empleados:
        st.caption(f"🗣️ {nombre}: *{helpers.frase_drama(nombre, 'tras el evento')}*")

    # 🌪️ Diagnóstico de clima prolongado
    st.subheader("🌡️ Evaluación emocional por sucursal")
    sucursales = df["Sucursal"].unique()
    for sucursal in sucursales:
        evaluacion = helpers.riesgo_climatico(df, sucursal)
        st.info(evaluacion)

    # 🔗 Sugerencias de fusión por crisis combinada
    fusiones = helpers.fusion_sugerida(df)
    if fusiones:
        st.subheader("🔀 Propuesta de Fusiones Temporales")
        for sugerencia in fusiones:
            st.warning(sugerencia)