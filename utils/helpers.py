import pandas as pd
import random

# 🎯 Eficiencia promedio sobre cualquier columna
def eficiencia_promedio(df, columna="Eficiencia"):
    return df[columna].mean()

# 📆 Últimos N meses únicos
def ultimos_meses(df, columna="Mes", cantidad=3):
    return sorted(df[columna].unique())[-cantidad:]

# 🌦️ Clasificador de clima
def evaluar_clima(valor):
    if valor < 0.6:
        return "🥶 Bajo"
    elif valor > 0.85:
        return "☀️ Excelente"
    else:
        return "🌤️ Estable"

# 🎭 Frases de drama organizacional
def frase_drama(nombre, contexto="su traslado"):
    frases = [
        f"{nombre} ha declarado: '¡No dejaré {contexto} sin luchar!'",
        f"{nombre} renunció diciendo: 'Prefiero irme antes que dejar mi tierra.'",
        f"{nombre} rechazó el cambio: 'París no entiende mi ritmo tropical.'",
        f"{nombre} dijo: '¿Acaso soy una caja que pueden mover sin preguntar?'",
        f"{nombre} firmó su carta de renuncia: 'Mi lealtad está con {contexto}.'"
    ]
    return random.choice(frases)

# 💼 Evaluación de riesgo por clima prolongado
def riesgo_climatico(df, sucursal):
    if "Clima" not in df.columns:
        return f"⚠️ No se encontró la columna 'Clima' para evaluar emocionalmente {sucursal}."

    clima = df[df["Sucursal"] == sucursal]
    recientes = clima[clima["Mes"].isin(ultimos_meses(clima))]

    if recientes.empty:
        return f"⚠️ No hay datos recientes para evaluar el clima en {sucursal}."

    media = eficiencia_promedio(recientes, "Clima")
    if media < 0.55:
        return f"🌪️ Riesgo alto de fuga emocional en {sucursal}"
    elif media < 0.65:
        return f"😬 Riesgo moderado de desgaste cultural en {sucursal}"
    return f"🌿 Clima tolerable en {sucursal}"

# 🔗 Sugerir fusión temporal de sucursales en crisis
def fusion_sugerida(df):
    columnas_necesarias = ["Clima", "Eficiencia"]
    faltantes = [col for col in columnas_necesarias if col not in df.columns]

    if faltantes:
        return [f"⚠️ No se encontraron las columnas requeridas: {', '.join(faltantes)}"]

    resumen = df.groupby("Sucursal")[["Clima", "Eficiencia"]].mean()
    crisis = resumen[(resumen["Clima"] < 0.6) & (resumen["Eficiencia"] < 0.75)].index.tolist()

    fusiones = []
    if len(crisis) >= 2:
        for i in range(len(crisis)):
            for j in range(i + 1, len(crisis)):
                fusiones.append(f"🔀 Fusionar temporalmente {crisis[i]} y {crisis[j]} hasta mejora interna.")
    return fusiones