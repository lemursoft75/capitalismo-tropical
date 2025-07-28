import streamlit as st
import pandas as pd
import json
import random
import pyttsx3
from datetime import datetime

def calcular_impuestos(utilidad, tasa_isr=30.0, tasa_iva=16.0):
    isr = utilidad * (tasa_isr / 100)
    iva = utilidad * (tasa_iva / 100)
    return isr, iva

def guardar_historial(mes, utilidad):
    nuevo = {"Mes": mes, "Utilidad": utilidad}
    try:
        with open("data/historial.json", "r", encoding="utf-8") as f:
            historial = json.load(f)
    except:
        historial = []

    historial.append(nuevo)

    with open("data/historial.json", "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=4, ensure_ascii=False)

def mostrar_historial():
    try:
        with open("data/historial.json", "r", encoding="utf-8") as f:
            historial = json.load(f)
        df = pd.DataFrame(historial)
        st.subheader("📈 Historial de Utilidades")
        st.line_chart(df.set_index("Mes"))
        return df
    except:
        st.info("Aún no hay historial guardado.")
        return pd.DataFrame()

def generar_resumen_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def mostrar():
    st.title("💰 Finanzas Capitalismo Tropical")
    st.header("🏢 Rendimiento por Sucursal")

    sucursales = st.multiselect("Selecciona sucursales operativas", ["Mérida", "CDMX", "París", "Tokio"])
    rendimiento = {}
    utilidad_total = 0

    for suc in sucursales:
        ingresos = st.number_input(f"🟢 Ingresos en {suc}", min_value=0.0, format="%.2f", key=f"ingresos_{suc}")
        gastos = st.number_input(f"🔴 Gastos en {suc}", min_value=0.0, format="%.2f", key=f"gastos_{suc}")
        utilidad = ingresos - gastos
        rendimiento[suc] = utilidad
        utilidad_total += utilidad
        emoji = "😎" if utilidad > 0 else "🔥"
        st.metric(f"Utilidad en {suc} {emoji}", f"${utilidad:,.2f}")

    st.markdown("---")
    st.subheader("🧾 Impuestos")
    isr, iva = calcular_impuestos(utilidad_total)
    utilidad_final = utilidad_total - isr - iva
    st.warning(f"ISR: ${isr:,.2f} | IVA: ${iva:,.2f}")
    st.success(f"💵 Utilidad después de impuestos: ${utilidad_final:,.2f}")

    st.markdown("---")
    st.subheader("📅 Proyección Anual")
    df_historial = mostrar_historial()
    if not df_historial.empty:
        promedio_mensual = df_historial["Utilidad"].mean()
        proyeccion = promedio_mensual * 12
        st.info(f"📊 Proyección anual basada en historial: ${proyeccion:,.2f}")

    st.markdown("---")
    st.subheader("🔊 Narrador Financiero")
    if st.button("Activar resumen por voz"):
        resumen = f"Este mes has ganado {utilidad_final:,.2f} pesos después de impuestos, operando en {len(sucursales)} sucursales. Tu héroe financiero se llama tú."
        generar_resumen_voz(resumen)
        st.success("Resumen vocal activado")

    if st.button("📌 Guardar utilidad del mes"):
        mes_actual = datetime.now().strftime("%b-%Y")
        guardar_historial(mes_actual, utilidad_final)
        st.success(f"✅ Utilidad guardada para {mes_actual}")