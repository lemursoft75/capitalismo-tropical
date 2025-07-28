import streamlit as st
from modules import inicio, negocio, finanzas, empleados, reportes_rrhh, sucursales, eventos  # ← agrega eventos


with open("assets/estilo.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Configuración de la página
st.set_page_config(page_title="Capitalismo Tropical", page_icon="🌴", layout="centered")

# Sidebar para navegación
opcion = st.sidebar.radio(
    "Ir a:",
    ("Inicio", "Mi Negocio", "Finanzas", "Empleados", "Reportes RRHH", "Sucursales", "Eventos")  # ← agrega Eventos
)

# Renderizado condicional por pantalla
if opcion == "Inicio":
    inicio.mostrar()
elif opcion == "Mi Negocio":
    negocio.mostrar()
elif opcion == "Finanzas":
    finanzas.mostrar()
elif opcion == "Empleados":
    empleados.mostrar()
elif opcion == "Reportes RRHH":
    reportes_rrhh.mostrar()
elif opcion == "Sucursales":
    sucursales.mostrar()
elif opcion == "Eventos":
    eventos.mostrar()
else:
    st.warning("Pantalla no encontrada.")

# Pie de página divertido
st.markdown("---")
st.caption("Creado por Javier con ayuda de Copilot 🧠✨ | Capitalismo Tropical®")