# Analisis Titanic
![Alt text](https://github.com/alvaro99dd/Analisis-Titanic/blob/main/Recursos/imagen_Titanic.webp "Heatmap de valores nulos")
Investigación y análisis sobre el conjunto de datos de Titanic
Haz click [aquí](https://alvaro99dd-analisis-titanic-titanic-app-jseks4.streamlit.app/) para acceder a la app.

## Descripción
Ejercicio realizado durante la bootcamp de Upgrade Hub. Con un dataset que contiene distintas víctimas del Titanic,
revisar las distintas relaciones entre variables y obtener ideas interesantes que posteriormente fueron expuestas.

## Dataset
![Alt text](https://github.com/alvaro99dd/Analisis-Titanic/blob/main/Recursos/dataset.png)
Tras investigar el conjunto de datos, llegué a la siguiente conclusión:
* PassengerId: identificador único del pasajero.
* Survived: si el pasajero sobrevivió al naufragio, codificada como 0 (no) y 1 (si).
* Pclass: clase a la que pertenecía el pasajero: 1, 2 o 3.
* Name: nombre del pasajero.
* Sex: sexo del pasajero.
* Age: edad del pasajero.
* SibSp: número de hermanos, hermanas, hermanastros o hermanastras en el barco
* Parch: número de padres e hijos en el barco.
* Ticket: identificador del billete.
* Fare: precio pagado por el billete.
* Cabin: identificador del camarote asignado al pasajero.
* Embarked: puerto en el que embarcó el pasajero.

### Reparación de datos
![Alt text](https://github.com/alvaro99dd/Analisis-Titanic/blob/main/Recursos/heatmap.png "Heatmap de valores nulos")

Se puede observar que hay una gran cantidad de valores nulos. La columna Cabin he decidido ignorarla ya que para mi investigación no me resultaba útil,
así que puse todos mis esfuerzos en la columna Age. Reparé sus datos usando el algoritmo KNN para evitar que la distribución se viera altamente afectada.

## Investigación
Decidí enfocar mi investigación alrededor de la relación entre la supervivencia de los pasajeros y su estatus social y económico, además de su sexo.

### Conclusiones
Tras realizar la investigación, se puede ver una clara tendencia a salvar a personas cuyo billete fue más caro, es decir, personas que se encontraban
en primera o segunda clase. Pese a que los pasajeros en tercera clase eran los más habituales, fueron también los que menos sobrevivieron. Esta diferencia
se puede ver incluso en las mujeres, que pese a sobrevivir mucho más que los hombres, en tercera clase hubo una enorme cantidad de ellas que no lo consiguieron.