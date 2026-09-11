import streamlit as st
import random

# Inicializamos el contador en la memoria
if "clics" not in st.session_state:
    st.session_state.clics = 0

def sumar_clic():
    st.session_state.clics += 1

st.markdown("## Tengo un mensaje para ti...")

# Lista de frases burlonas para el botón
textos_boton = [
    "Haz clic aquí para leerlo",
    "Pícale otra vez",
    "¡Casi!",
    "otra vez",
    "Tu puedes"
]

# Si aún no llega a 5 clics, el botón salta
if st.session_state.clics < 5:
    
    # 1. Movimiento vertical drástico 
    saltos_verticales = random.randint(15, 15)
    st.markdown(f"{'<br>' * saltos_verticales}", unsafe_allow_html=True)
    
    # 2. Movimiento horizontal 
    columnas = st.columns(15)
    columna_elegida = random.choice(columnas)
    

    texto_actual = textos_boton[st.session_state.clics]
    
    with columna_elegida:
        st.button(texto_actual, on_click=sumar_clic)

else:
    st.success("Hola pau, suerte en tu clase ")
    st.balloons()
    
    st.divider()
    if st.button("Reiniciar"):
        st.session_state.clics = 0
        st.rerun()