import streamlit as st

st.title("HISTIDINA")
st.sidebar.title("Menú de navegación")
st.sidebar.header("Secciones disponibles")

# Opciones en la barra lateral
opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Información básica", "Funciones biológicas", "Propiedades químicas"]
)
# Contenido dinámico basado en la selección
if opcion == "Información básica":
    st.header("Información básica sobre la Histidina")
    st.write("""La histidina (His, H) es un aminoácido que se utiliza para la síntesis de proteínas. Es una molécula hidrofílica, por lo que generalmente está orientada hacia la parte externa de las estructuras proteicas cuando estas se encuentran en un medio líquido.""")
    st.image("https://th.bing.com/th/id/OIP.a1VjRkDwAYHh2KAOjC9NEQHaFj?w=226&h=180&c=7&r=0&o=5&pid=1.7")
    st.write("""La histidina cumple funciones fisiológicas muy importantes en el ser humano, como formar parte de los centros activos de muchas enzimas, participar en el crecimiento, en el sistema inmunitario y en la formación de la mielina en las fibras nerviosas, entre otras.""")
    st.write("""La biosíntesis de la histidina es un proceso complejo que sucede principalmente en el hígado y que requiere de 9 a 11 pasos enzimáticos. Su degradación se produce en el hígado y la piel y pasa por la formación de glutamato, siguiendo luego diferentes vías.

Muchos alimentos son ricos en histidina, como las proteínas animales (carne y productos lácteos), y las proteínas vegetales. Estos aportan gran parte de los requerimientos diarios de histidina que el cuerpo necesita para funcionar correctamente.

El déficit o el exceso de histidina ocasionado por problemas hereditarios metabólicos o de transporte, o la falla dietética en la ingesta, se relacionan con algunos problemas importantes que afectan la salud en niños y en adultos. El consumo suficiente de histidina permite mantener una vida sana y saludable en la mayor parte de los casos.""")
    st.image("""https://draxe.com/wp-content/uploads/2019/06/histidine-header-768x350.jpg""")
