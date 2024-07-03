# Repositorio del Equipo 11 - Introducción a Señales Biomédicas 
<p align="justify">
¡Hola a todos y bienvenidos al repositorio del Equipo 11 de Introducción a Señales Biomédicas 2024-1!

<p align="justify">
Es un placer darles la bienvenida a este espacio donde compartiremos y colaboraremos en el desarrollo de nuestro proyecto. Como equipo, estamos emocionados de trabajar juntos en la exploración y análisis de señales biomédicas, ¡y esperamos lograr resultados increíbles!

# Tabla de contenidos
- [Temática del proyecto](#Temática-del-proyecto)
- [Contenido del curso](#Contenido-del-curso)
- [Docentes del curso](#Docentes-del-curso)
- [Participantes](#Participantes)

### Temática del proyecto
#### Alerta temprana de ECG para pacientes con chagas: Implementación de TinyML para áreas de bajos recursos del Perú.
###### Early ECG warning for chagas patients: Implementation of TinyML for low-resource areas in Peru.

##### Resumen
<p align="justify"> Este proyecto tiene como objetivo desarrollar un sistema de alerta temprana basado en electrocardiografía (ECG) para la detección de pacientes de alto riesgo de mortalidad por la enfermedad de Chagas en Perú. Utiliza técnicas avanzadas de procesamiento de señales y aprendizaje automático, específicamente Tiny Machine Learning (TinyML), para identificar patrones específicos en las señales cardíacas de los pacientes con Chagas de manera eficiente y a bajo costo, facilitando su implementación en zonas de bajos recursos.

##### Motivación
<p align="justify">Las enfermedades cardiovasculares son la principal causa de muerte a nivel mundial, y en Perú representan la segunda causa de defunción. La enfermedad de Chagas, conocida localmente como Chirimacha, es una enfermedad parasitaria desatendida que afecta a millones de personas en América Latina, incluyendo Perú. Esta enfermedad puede provocar miocardiopatía chagásica, una de las principales causas de miocardiopatía no isquémica en la región.

<p align="justify">El Dr. José Ercilla, vicepresidente de la Sociedad Peruana de Cardiología (Sopechard), destaca el desafío futuro que representan estas enfermedades, especialmente ante el aumento significativo de la población mayor de 50 años proyectado para el año 2050. La migración de poblaciones rurales hacia centros urbanos ha incrementado la relevancia de esta enfermedad en áreas donde el vector no ha sido detectado previamente.

<p align="justify">Con este proyecto, buscamos implementar una solución tecnológica accesible y eficiente que permita la detección temprana de problemas cardíacos en pacientes con Chagas, mejorando así su calidad de vida y reduciendo la mortalidad asociada a esta enfermedad. La implementación de TinyML en dispositivos portátiles y de bajo costo puede transformar el monitoreo de salud en comunidades de bajos recursos, haciendo posible una atención médica más oportuna y precisa.

##### Principales hallazgos
- <p align="justify">El modelo XGBoost mostró una capacidad predictiva razonable con un R-cuadrado de 0.61.
- <p align="justify">La media del error cuadrático (MSE) fue de 0.38, indicando una precisión aceptable.
- <p align="justify">La media del error absoluto (MAE) fue de 0.51, reflejando la precisión en las predicciones.
- <p align="justify">El modelo fue implementado en un Arduino Nano BLE 33, demostrando viabilidad para entornos con recursos limitados.
- <p align="justify">Se redujo el número de derivaciones de ECG de 12 a una, haciendo el sistema más accesible y económico.
- <p align="justify">Se integró una etapa de extracción de características (skewness, entropy) para mejorar la capacidad del modelo de extraer y utilizar información de la señal.
- <p align="justify">Las predicciones del modelo sobre señales de ECG de sujetos sanos mostraron resultados comparables a los ECGs de pacientes sobrevivientes en el dataset.
- <p align="justify">Las métricas de evaluación sugieren que el modelo tiene un buen potencial, aunque hay margen para mejoras adicionales en su precisión y generalización.

##### Informe
- [Enlace de paperswithcode](https://paperswithcode.com/paper/early-ecg-warning-for-chagas-patients)
  
### Contenido del curso
- [Ver PDF del Sílabo en Google Docs Viewer](https://docs.google.com/viewer?url=https://github.com/diego-taquiri/ISB-equipo11/raw/main/Documentaci%C3%B3n/Laboratorio%2001/S%C3%ADlabo.pdf&embedded=true)

### Docentes del curso
#### PROFESORES DEL CURSO E INVITADOS

| Grado o Título | Nombre    | Apellidos             | Condición   | Correo electrónico         |
| -------------- | --------- | --------------------- | ----------- | -------------------------- |
| Magister       | U. Lewis  | De la Cruz Rodríguez  | Contratado  | [umbert.de.la.cruz@upch.pe](mailto:umbert.de.la.cruz@upch.pe) |
| Magister       | Moisés    | Meza Rodríguez        | Contratado  | [moises.meza@upch.pe](mailto:moises.meza@upch.pe) |

#### JEFES DE PRÁCTICA

| Grado o Título | Nombre    | Apellidos             | Condición   | Correo electrónico         |
| -------------- | --------- | --------------------- | ----------- | -------------------------- |
| Ingeniería     | Julissa E.| Venancio Huerta       | Contratado  | [julissa.venancio@upch.pe](mailto:julissa.venancio@upch.pe) |
| Licenciado     | José A.   | Cáceres del Águila    | Contratado  | [jose.caceres.d@upch.pe](mailto:jose.caceres.d@upch.pe) |

### Participantes
| Imagen                                                                                           | Grado                            | Nombre y Apellido        | Condición   | Correo electrónico                            |
|-------------------------------------------------------------------------------------------------|----------------------------------|--------------------------|-------------|-----------------------------------------------|
| <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2001/diego.jpeg" alt="Diego" width="100"/> | Estudiante de Biología           | Diego Taquiri            | Colaborador | [diego.taquiri@upch.pe](mailto:diego.taquiri@upch.pe)  |
| <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2001/Armando.jpeg" alt="Armando" width="100"/> | Estudiante de Ingeniería Biomédica | Armando Flórez           | Colaborador | [armando.florez@upch.pe](mailto:armando.florez@upch.pe)  |
| <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2001/ana.jpg" alt="Ana Belen" width="100"/>   | Estudiante de Ingeniería Biomédica | Ana Belen Mantilla       | Colaborador | [ana.mantilla@upch.pe](mailto:ana.mantilla@upch.pe)    |
| <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2001/Erick.jpg" alt="Erick" width="100"/>  | Estudiante de Ingeniería Biomédica | Erick Valdivia           | Colaborador | [erick.valdivia@upch.pe](mailto:erick.valdivia@upch.pe) |

<p align="justify"> ¡Gracias por visitar nuestro repositorio y por ser parte de nuestro viaje hacia el conocimiento y la innovación en señales biomédicas!
