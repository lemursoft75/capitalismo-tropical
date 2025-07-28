import streamlit as st
import pandas as pd

def mostrar():
    st.title("📋 Reportes de Recursos Humanos")
    st.subheader("Analiza el rendimiento histórico de tus empleados tropicales")

    try:
        df = pd.read_csv("data/empleados.csv")
    except FileNotFoundError:
        st.warning("No se encontró historial de empleados.")
        return

    st.markdown("### 👤 Resumen por empleado")
    empleados = df["Nombre"].unique()
    for nombre in empleados:
        datos = df[df["Nombre"] == nombre]
        eficiencia_media = datos["Eficiencia"].mean()
        antiguedad = len(datos["Mes"].unique())
        emoji = "🌟" if eficiencia_media >= 0.85 else "⚠️" if eficiencia_media < 0.75 else "🙂"

        st.markdown(f"**{nombre}** ({datos.iloc[0]['Rol']}) {emoji}")
        st.write(f"- 🧮 Eficiencia promedio: {eficiencia_media*100:.1f}%")
        st.write(f"- ⏳ Antigüedad: {antiguedad} meses registrados")
        st.line_chart(datos.set_index("Mes")["Eficiencia"])

        if eficiencia_media < 0.7:
            st.error("🚨 Rendimiento bajo sostenido. Considera capacitación o reemplazo.")
        st.markdown("---")

    st.subheader("🌤️ Clima Laboral Histórico")
    df_mes = df.groupby("Mes")["Eficiencia"].mean().reset_index()
    st.line_chart(df_mes.set_index("Mes"))