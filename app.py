import streamlit as st
from modules import inicio, negocio, finanzas  # Ahora también incluimos finanzas

with open("assets/estilo.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Configuración de la página
st.set_page_config(page_title="Capitalismo Tropical", page_icon="🌴", layout="centered")

# Sidebar para navegación
st.sidebar.title("📚 Menú de Navegación")
opcion = st.sidebar.radio(
    "Ir a:",
    ("Inicio", "Mi Negocio", "Finanzas")  # ← Aquí se agrega "Finanzas"
)

# Renderizado condicional por pantalla
if opcion == "Inicio":
    inicio.mostrar()
elif opcion == "Mi Negocio":
    negocio.mostrar()
elif opcion == "Finanzas":
    finanzas.mostrar()
else:
    st.warning("Pantalla no encontrada.")

# Pie de página divertido
st.markdown("---")
st.caption("Creado por Javier con ayuda de Copilot 🧠✨ | Capitalismo Tropical®")