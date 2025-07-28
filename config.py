# config.py

# Capital inicial del jugador
CAPITAL_INICIAL = 50000  # En MXN

# Opciones de inicio
MODOS_INICIO = {
    "solo": {
        "descripcion": "Dueño absoluto, todo riesgo y toda ganancia.",
        "capital": CAPITAL_INICIAL,
        "riesgo": "alto"
    },
    "socio": {
        "descripcion": "Un socio aporta $25,000, pero comparte decisiones clave.",
        "capital": CAPITAL_INICIAL + 25000,
        "riesgo": "medio"
    },
    "prestamo": {
        "descripcion": "Recibes $100,000 con intereses del 5% mensual. Riesgo de embargo.",
        "capital": CAPITAL_INICIAL + 100000,
        "interes_mensual": 0.05,
        "riesgo": "alto"
    }
}

# Tipos de negocio y su configuración inicial
NEGOCIOS = {
    "cafeteria": {
        "emoji": "☕",
        "costo_inicial": 30000,
        "gasto_mensual": 10000,
        "ganancia_media": 15000
    },
    "taller": {
        "emoji": "🔧",
        "costo_inicial": 40000,
        "gasto_mensual": 12000,
        "ganancia_media": 18000
    },
    "papeleria": {
        "emoji": "📚",
        "costo_inicial": 20000,
        "gasto_mensual": 8000,
        "ganancia_media": 12000
    },
    "videojuegos": {
        "emoji": "🎮",
        "costo_inicial": 35000,
        "gasto_mensual": 11000,
        "ganancia_media": 16000
    }
}

# Estilos de colores (pueden usarse con st.markdown + HTML si decides aplicar CSS)
COLORES = {
    "fondo": "#F5F5DC",
    "texto": "#1D3557",
    "exito": "#2A9D8F",
    "error": "#E76F51",
    "neutro": "#F4A261"
}

# Emojis reutilizables
EMOJIS = {
    "dinero": "💵",
    "empleado": "🧑‍💼",
    "evento": "⚠️",
    "sucursal": "🏬",
    "crecimiento": "📈"
}