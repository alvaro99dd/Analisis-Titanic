import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np

st.set_page_config(page_title="Titanic", page_icon=":passenger_ship:",layout="wide") #configuración de la página

df = pd.read_csv("https://raw.githubusercontent.com/alvaro99dd/Analisis-Titanic/main/Recursos/titanic.csv")
df_repaired = pd.read_csv("https://raw.githubusercontent.com/alvaro99dd/Analisis-Titanic/main/Recursos/titanic_repaired.csv")

def change_page(seleccion):
    """Muestra la página en función de lo que seleccione el usuario en el sidebar"""
    match seleccion:
        case "Inicio":
            inicio()
        case "Reparación de datos":
            reparacion()
        case "Sexo y edad de los pasajeros":
            sexo_edad()
        case "Precio del billete":
            precio_billete()
        case "Clase del pasajero":
            clase_pasajero()

def inicio():
    """Muestra la pagina de inicio"""
    # Título
    st.title("Análisis de la supervivencia para con la clase social en el Titanic")
    col1, col2 = st.columns(2)
    with col1:
        # Imagen
        st.markdown("##")
        st.image("https://raw.githubusercontent.com/alvaro99dd/Analisis-Titanic/main/Recursos/imagen_Titanic.webp"
        , caption="Créditos: Getty Images" # Añado créditos
        , width=650) # Ajusto anchura
    with col2:
        # Subtitulo
        st.markdown("#####")
        st.subheader("Estudio en profundidad de las víctimas del Titanic, observando la relación entre distintas variables con respecto a la supervivencia de cada una de ellas.")
        st.subheader("En base a la información recopilada, se tratarán los siguientes puntos:")
        with st.expander(":memo:", expanded=True):
            st.markdown("##### Reparación de datos")
            st.markdown("##### Sexo y edad de los pasajeros")
            st.markdown("##### Precio del billete")
            st.markdown("##### Clase del pasajero")
    st.markdown("##")
    st.info("«*Los números tienen una historia importante que contar. Dependen de ti, para darles una voz.*» - *Stephen Few*")


def reparacion():
    """Muestra la pagina de reparacion de datos"""
    # Reparación
    st.title("Reparación y preparación de datos")
    st.subheader("Datos sin reparar")
    # Muestro el dataframe
    st.dataframe(df)
    st.divider()
    # Muestro el mapa de calor con los valores nulos
    st.subheader("Observamos qué columnas necesitan reparación de nuestro conjunto de datos")
    st.image("https://raw.githubusercontent.com/alvaro99dd/Analisis-Titanic/main/Recursos/heatmap.png")
    st.divider()
    # Muestro los datos ya reparados
    st.subheader("Aplicamos a cada columna el tratamiento necesario (si lo fuese)")
    st.dataframe([df_repaired["Age"], df_repaired["Survived"], df_repaired["MeanCurrentFare"]])

def sexo_edad():
    """Muestra la pagina de distribucion de las variables sexo y edad"""
    # Sexo y edad
    st.title("Distribución de la edad y el :blue[sexo] de los pasajeros")
    col1,col2 = st.columns(2) # Creo las columnas necesarias
    with col1:
        # Creo y muestro la distribución de la edad
        fig = px.histogram(df_repaired,range_x=[0,80], x="Age", nbins=10, text_auto=True, labels={"Age": "Edad"}, log_y=False,template="plotly_dark",width=650, histfunc="count", title="Distribución de la edad")
        fig.update_xaxes(tick0=0, dtick=5)
        st.plotly_chart(fig)
        st.text("Observamos que la gran mayoría de pasajeros oscila entre los 15 y los 35 años.")
    with col2:
        # Calculo el porcentaje de personas que sobrevivieron
        total_survived = np.round(len(df_repaired[df_repaired["Survived"] == "Si"]) * 100 / len(df["Survived"]), 2)
        men_survived = np.round(len(df_repaired[df_repaired["Survived"] == "Si"][df_repaired["Sex"] == "male"]) * 100 / len(df_repaired[df_repaired["Survived"] == "Si"]), 2)
        women_survived = np.round(len(df_repaired[df_repaired["Survived"] == "Si"][df_repaired["Sex"] == "female"]) * 100 / len(df_repaired[df_repaired["Survived"] == "Si"]), 2)
        # Creo y muestro la gráfica
        fig = px.histogram(df_repaired, x="Survived", nbins=5, text_auto=True, labels={"Survived": "Sobrevivió", "Sex": "Sexo"}, log_y=False,template="plotly_dark",color="Sex", width=750, histfunc="count", title="Nº de supervivientes según el sexo")
        st.plotly_chart(fig)
        st.text(f"El porcentaje de personas que en total sobrevivieron es de: {total_survived}% \n\rEl porcentaje de hombres que sobrevivieron es de: {men_survived}% \n\rEl porcentaje de mujeres que sobrevivieron es de: {women_survived}%", help="Calculamos los porcentajes para una mejor comparación")

def precio_billete():
    """Muestra la pagina de relacion entre el coste de los billetes y la supervivencia"""
    # Precio en relacion a la supervivencia
    st.title("Relación del :green[precio] del billete con la :red[supervivencia] de los pasajeros")
    # Gráfico boxplot para ver la relación del precio con la supervivencia
    fig = px.box(df_repaired, hover_name="Name", notched=True, x="MeanCurrentFare", log_x=True, boxmode="group", color="Survived", color_discrete_map={"Si": "#86a96f", "No": "#ac3547"}, labels={"Survived": "Sobrevivió", "MeanCurrentFare": "Precio del billete"}, template="plotly_dark", title="Relación precio billete/supervivencia")
    st.plotly_chart(fig)
    # Muestro el precio mínimo y máximo del billete
    st.subheader(f"El precio máximo del billete es: " + str(df_repaired["MeanCurrentFare"].max()) + "€")
    st.subheader(f"El precio mínimo del billete es: "+ str(df_repaired[df_repaired["MeanCurrentFare"] > 0]["MeanCurrentFare"].min()) + "€")
    st.info("Calculamos el precio máximo y mínimo del billete para una mejor comparación", icon="ℹ️")
    # Creo un dataframe auxiliar que contiene los datos de los apellidos duplicados
    df_aux = df_repaired[df_repaired["LastName"].duplicated(keep=False)]
    st.divider() # Separo las secciones
    # Muestro el título y dejo un espacio blanco usando markdown
    st.title(f"¿Y las familias...?")
    st.markdown("##")
    # Muestro el gráfico scatter que relaciona la edad de los miembros de cada familia con su supervivencia
    fig = px.scatter(df_aux, x="LastName", y="Age", color='Survived', template="plotly_dark"
        ,labels={"LastName": "Apellidos", "Age": "Edad", "Survived": "Sobrevivió", "Pclass": "Clase del pasajero"}
        ,size="Age"
        ,color_discrete_map={"Si": "#86a96f", "No": "#ac3547"}
        ,hover_name=df_aux["Name"]
        ,hover_data=["Pclass"]
        )
    fig.update_layout(title=dict(text="Familias afectadas", font=dict(size=40, family="Courier", color="white")))
    st.plotly_chart(fig)

def clase_pasajero():
    """Muestra la pagina que relaciona la clase del pasajero con su supervivencia"""
    st.title("Relación entre la :green[clase] del pasajero y su :red[supervivencia]")
    col1, col2 = st.columns(2) # Creo las columnas necesarias
    with col1:
        st.subheader("Comprobamos que el :green[precio] del billete está directamente relacionado con la :green[clase] del pasajero")
        # Muestro el histograma
        fig = px.histogram(df_repaired, x="Pclass",y="MeanCurrentFare",labels={"Pclass": "Clase del pasajero", "MeanCurrentFare": "Billete"}
                , text_auto=True, nbins=5
                , log_y=False,template="plotly_dark",color="Pclass", color_discrete_map={1:"#4b2991", 2:"#ea4f88", 3:"#EDD9A3"}
                , width=675
                , histfunc="avg"
                , title="Clase del pasajero en relación al precio del billete")
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig)
        # Calculo y muestro el porcentaje total de personas que hay por cada clase de pasajero
        pClass1 = np.round(len(df_repaired[df_repaired["Pclass"] == 1]) * 100 / len(df), 2)
        pClass2 = np.round(len(df_repaired[df_repaired["Pclass"] == 2]) * 100 / len(df), 2)
        pClass3 = np.round(len(df_repaired[df_repaired["Pclass"] == 3]) * 100 / len(df), 2)
        st.text(f"El porcentaje total de personas según su clase de pasajero es: \n- Clase 1: {pClass1}%\n- Clase 2: {pClass2}%\n- Clase 3: {pClass3}%")
    with col2:
        # Dejo varios espacios en blanco para que la imagen se ajuste bien
        st.markdown("#")
        st.markdown("#####")
        # Muestro la imagen
        st.image("https://raw.githubusercontent.com/alvaro99dd/Analisis-Titanic/main/Recursos/clases_titanic.jpg", caption=["Menús de primera, segunda y tercera clase que se sirvieron el último día de navegación del Titanic. Créditos: rafaelcastillejo.com"])
    # Divido las secciones
    st.divider()
    st.subheader("Relación entre el :blue[sexo], la :green[clase] del pasajero y su :red[supervivencia]")
    # Muestro la gráfica de categorías paralelas para relacionar sexo, clase y supervivencia.
    fig = px.parallel_categories(df_repaired, dimensions=["Pclass", "Sex", "Survived"]
        , range_color=[1, 3], color="Pclass"
        , template="plotly_dark", color_continuous_scale=px.colors.sequential.Agsunset)
    fig.update(layout_coloraxis_showscale=False)
    fig.update_traces(dimensions=[{"categoryorder": "category ascending"} for _ in df["Pclass"].value_counts()])
    st.plotly_chart(fig)
    # Calculamos el porcentaje de personas que sobrevivieron según el Pclass
    pClass1 = np.round(len(df_repaired[df_repaired["Pclass"] == 1][df_repaired["Survived"] == "Si"]) * 100 / len(df_repaired[df_repaired["Pclass"] == 1]), 2)
    pClass2 = np.round(len(df_repaired[df_repaired["Pclass"] == 2][df_repaired["Survived"] == "Si"]) * 100 / len(df_repaired[df_repaired["Pclass"] == 2]), 2)
    pClass3 = np.round(len(df_repaired[df_repaired["Pclass"] == 3][df_repaired["Survived"] == "Si"]) * 100 / len(df_repaired[df_repaired["Pclass"] == 3]), 2)
    st.text(f"El porcentaje de personas que sobrevivieron según su clase de pasajero es: \n- Clase 1: {pClass1}%\n- Clase 2: {pClass2}%\n- Clase 3: {pClass3}%")
    # Calculamos el porcentaje de personas que NO sobrevivieron según el Pclass
    pClass1 = np.round(len(df_repaired[df_repaired["Pclass"] == 1][df_repaired["Survived"] == "No"]) * 100 / len(df_repaired[df_repaired["Pclass"] == 1]), 2)
    pClass2 = np.round(len(df_repaired[df_repaired["Pclass"] == 2][df_repaired["Survived"] == "No"]) * 100 / len(df_repaired[df_repaired["Pclass"] == 2]), 2)
    pClass3 = np.round(len(df_repaired[df_repaired["Pclass"] == 3][df_repaired["Survived"] == "No"]) * 100 / len(df_repaired[df_repaired["Pclass"] == 3]), 2)
    st.text(f"El porcentaje de personas que no sobrevivieron según su clase de pasajero es: \n- Clase 1: {pClass1}%\n- Clase 2: {pClass2}%\n- Clase 3: {pClass3}%")

#Sidebar
st.sidebar.title("Secciones")
opcion = st.sidebar.selectbox("Secciones", ["Inicio", "Reparación de datos", "Sexo y edad de los pasajeros", "Precio del billete", "Clase del pasajero"], label_visibility="hidden")
# st.sidebar.radio("a",["Inicio", "Reparación de datos", "Sexo y edad de los pasajeros", "Precio del billete", "Clase del pasajero"], label_visibility="hidden" )
change_page(opcion) # Mostrar la opción seleccionada