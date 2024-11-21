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
elif opcion == "Funciones biológicas":
   st.header("Funciones biologicas de la Histidina")
   st.write("""La histidina cumple varias funciones biológicas esenciales en el cuerpo humano debido a su estructura química única, que incluye un anillo imidazol capaz de participar en diversas reacciones químicas. Aquí están sus principales funciones:""")
   st.image("https://www.mismumi.com/wp-content/uploads/histidina-aminoacido-funcion-336x205.jpg")
   st.write("""1. Regulación del pH 
El anillo imidazol de la histidina tiene un pKa cercano al pH fisiológico (~6.0), lo que le permite actuar como un regulador en los cambios de pH.  

 2. Precursor de la histamina
La histidina es el precursor de la histamina, una amina biológicamente activa con funciones importantes:  
- Sistema inmunológico: La histamina es liberada durante las reacciones alérgicas y juega un papel clave en la respuesta inflamatoria.  
- Sistema nervioso: Actúa como neurotransmisor en el cerebro.

3. Participación en reacciones enzimáticas
El grupo imidazol de la histidina es fundamental en muchas enzimas:  
- Actúa como donador o receptor de protones en reacciones catalíticas.  

 4. Unión y transporte de metales
La histidina es crucial en la unión de iones metálicos:  
- Hemoglobina y mioglobina: Participa en la unión del oxígeno a través de la interacción con el grupo hemo.
- Forma complejos con otros metales como el zinc, el cobre y el hierro, esenciales para funciones enzimáticas y estructurales.

5. Rol en la estabilidad estructural de proteínas
Contribuye a la formación de:  
- Puentes de hidrógeno y enlaces no covalentes que estabilizan la estructura tridimensional de las proteínas.  
Es importante en proteínas como la colágena y en mecanismos de unión molecular.

 6.Producción de energía
En el metabolismo, la histidina puede ser degradada en el ciclo de los ácidos tricarboxílicos (ciclo de Krebs):  
- Se convierte en ácido glutámico y luego en α-cetoglutarato, un intermediario clave en la producción de energía celular.

7.Impulso nervioso y neurotransmisión  
- Como precursor de la histamina, tiene un rol en la transmisión sináptica en el cerebro, regulando el ciclo sueño-vigilia y la memoria.  
- También influye en procesos relacionados con la modulación de la excitabilidad neuronal.

8. Rol en el sistema inmunológico  
- Participa en la maduración y función de los glóbulos blancos.  
- Es esencial para la síntesis de proteínas involucradas en la respuesta inmune, como las inmunoglobulinas.""")
   
