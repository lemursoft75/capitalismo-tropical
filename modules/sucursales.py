import streamlit as st
import pandas as pd
import json

def mostrar():
    st.title("🏢 Reporte de Sucursales")
    st.subheader("Comparativa mensual entre sucursales tropicales")

    # 📦 Carga datos principales desde JSON
    try:
        with open("data/sucursales.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
    except Exception:
        st.warning("No se encontró historial de sucursales.")
        return

    if df.empty:
        st.info("⚠️ El archivo `sucursales.json` está vacío.")
        return

    sucursales = df["Sucursal"].unique()

    # 📊 Rendimiento general
    st.markdown("### 📊 Rendimiento General")
    rendimiento = df.groupby("Sucursal")["Eficiencia"].mean().reset_index()
    st.bar_chart(rendimiento.set_index("Sucursal"))

    # 🌦️ Clima laboral por sucursal
    st.markdown("---")
    st.subheader("🌦️ Clima Laboral por Sucursal")
    clima = df.groupby(["Sucursal", "Mes"])["Clima"].mean().reset_index()
    for sucursal in sucursales:
        st.markdown(f"#### {sucursal}")
        datos = clima[clima["Sucursal"] == sucursal]
        st.line_chart(datos.set_index("Mes")["Clima"])

        media = datos["Clima"].mean()
        if media < 0.6:
            st.error("🥶 Clima laboral bajo. Considera intervención interna.")
        elif media > 0.85:
            st.success("☀️ Excelente ambiente, ideal para expandir funciones.")
        else:
            st.info("🌤️ Clima estable. Observa tendencias.")

        st.markdown("---")

    # 🚀 Sugerencias de expansión
    try:
        with open("data/lideres.json", "r", encoding="utf-8") as f:
            lideres_data = json.load(f)
        df_lideres = pd.DataFrame(lideres_data)
        sugerencias_expansion(df, df_lideres)
    except:
        st.warning("No se pudo cargar info de líderes.")

    # 🔄 Relevo de liderazgo
    try:
        with open("data/lideres_hist.json", "r", encoding="utf-8") as f:
            hist_data = json.load(f)
        df_lideres_hist = pd.DataFrame(hist_data)
        relevo_liderazgo(df_lideres_hist)
    except:
        st.warning("No se pudo analizar historial de líderes.")

    # 👥 Transferencias
    sugerir_transferencias(df)

# 🚀 Sugerencias de expansión
def sugerencias_expansion(df, df_lideres):
    st.subheader("🚀 Sugerencias de Expansión")

    recientes = df[df["Mes"].isin(sorted(df["Mes"].unique())[-3:])]
    clima_por_sucursal = recientes.groupby("Sucursal")["Clima"].mean()
    eficiencia_lideres = df_lideres.groupby("Sucursal")["Eficiencia"].mean()

    recomendaciones = []
    for sucursal in clima_por_sucursal.index:
        clima = clima_por_sucursal[sucursal]
        eficiencia = eficiencia_lideres.get(sucursal, None)
        if clima > 0.85 and eficiencia and eficiencia > 0.8:
            recomendaciones.append((sucursal, clima, eficiencia))

    if recomendaciones:
        for s, c, e in recomendaciones:
            st.success(f"✅ {s} está lista para expandir: Clima {c:.2f}, Liderazgo {e:.2f}")
    else:
        st.info("🔍 Ninguna sucursal cumple todos los criterios de expansión por ahora.")

# 🔄 Relevos de liderazgo
def relevo_liderazgo(df_lideres_hist):
    st.subheader("🔄 Relevos de Liderazgo")

    recientes = df_lideres_hist[df_lideres_hist["Mes"].isin(sorted(df_lideres_hist["Mes"].unique())[-3:])]
    promedio_por_lider = recientes.groupby(["Sucursal", "Nombre"])["Eficiencia"].mean().reset_index()

    for _, row in promedio_por_lider.iterrows():
        if row["Eficiencia"] < 0.75:
            st.warning(f"⚠️ {row['Nombre']} en {row['Sucursal']} tiene bajo rendimiento ({row['Eficiencia']:.2f}). Considera apoyo o relevo.")

# 👥 Transferencias
def sugerir_transferencias(df):
    st.subheader("🚚 Sugerencias de Transferencias")

    clima_reciente = df[df["Mes"] == sorted(df["Mes"].unique())[-1]]
    clima_medio = clima_reciente.groupby("Sucursal")["Clima"].mean()
    cargas = df.groupby("Sucursal")["Eficiencia"].count()

    bajas = clima_medio[clima_medio < 0.65].index
    altas = clima_medio[clima_medio > 0.85].index

    if len(bajas) and len(altas):
        for destino in altas:
            st.success(f"📦 Considera reubicar personal a {destino} desde: {', '.join(bajas)}")
    else:
        st.info("📍 No hay condiciones claras para transferencias en este momento.")