import streamlit as st

# Inicializamos el contador en la memoria
if "clics" not in st.session_state:
    st.session_state.clics = 0

def sumar_clic():
    st.session_state.clics += 1

st.markdown("## Tengo un mensaje para ti...")
st.write("") # Espacio en blanco

# Lógica de posiciones
if st.session_state.clics == 0:
    st.button("Haz clic aquí para leerlo", on_click=sumar_clic)

elif st.session_state.clics == 1:
    col1, col2, col3 = st.columns(3)
    with col2:  # Lo movemos al centro
        st.button("Pícale otra vez", on_click=sumar_clic)

elif st.session_state.clics == 2:
    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:  # Lo movemos hasta la extrema derecha
        st.button("Casi", on_click=sumar_clic)

elif st.session_state.clics >= 3:
    st.success("Hola pau, suerte en tu clase ")
    st.balloons()
    
    st.divider()
    if st.button("Reiniciar"):
        st.session_state.clics = 0
        st.rerun()