# Tratamiento de señal ECG
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro

## Tabla de contenidos
1. [Introducción](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Procesamiento_ECG.md#introducci%C3%B3n)
2. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Procesamiento_ECG.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Procesamiento_ECG.md#materiales-y-m%C3%A9todos)
5. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Procesamiento_ECG.md#resultados)
6. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Procesamiento_ECG.md#discusi%C3%B3n)
7. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Procesamiento_ECG.md#bibliograf%C3%ADa)

### Introducción
<p align="justify"> El electrocardiograma (ECG) puede describir la actividad eléctrica del corazón y es una herramienta esencial para el diagnóstico de enfermedades cardiovasculares. [1] Esta es  una señal aleatoria e inestable y es significantemente diferente entre entornos e individuos. [2] Con el rápido desarrollo de técnicas de ECG portátiles e inalámbricas, la monitorización de ECG en tiempo real y de rutina está atrayendo cada vez más atención debido a la creciente popularización de la salud médica. [1]

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Images/qrs.png" alt="Descripción de la imagen" width="300"><br> 
<p align="center"><b>Figura 1.</b> La forma de onda principal en una señal de ECG. Onda P: indica despolarización auricular o contracción de la aurícula; complejo QRS: indica despolarización ventricular o contracción de los ventrículos; onda T: indica repolarización ventricular. [2] <br> 
  
<p align="justify"> La onda P, el complejo QRS y la onda T son los componentes principales de la forma de onda del ECG, y la detección precisa de ellos es importante para el análisis de la señal del ECG. El complejo QRS es la característica dominante de la señal del ECG y su detección precisa es una cuestión importante en muchas condiciones clínicas. [2] Sin embargo,  las características del ECG empiezan con la detección del pico R, ya que todas las demás se extraen después de la ubicación de este. Su detección precisa es fundamental para el diagnóstico de arritmias como contracción auricular prematura, taquicardia y bradicardia. Sin embargo, la extracción eficiente del pico R sigue siendo difícil en el entorno dinámico y ruidoso debido a la morfología de la forma de onda que varía con el tiempo. Esto sería más difícil cuando la señal del ECG se ve abrumada por ruidos con frecuencia similar en la distribución de energía. [1]

<p align="justify"> Aún se necesita un desarrollo significativo debido al desafío de los efectos de ruido inesperados en la señal de ECG, como la desviación de la línea base, el movimiento y estiramiento de los electrodos, los artefactos de movimiento y el ruido muscular, que impiden que la tecnología de procesamiento automático de ECG funcione de manera efectiva. Las principales fuentes de ruido son las actividades eléctricas de los músculos y la desviación de la línea base causada por la respiración, el mal contacto de los electrodos y los equipos o dispositivos electrónicos. [1] Desafortunadamente, existen grandes desafíos para la detección automatizada porque las morfologías y amplitudes de muchos complejos QRS normales son como los complejos QRS anormales. El ruido superpuesto en la señal de ECG hace que este problema sea más grave. Además, las ondas P/T con mayor amplitud pueden interferir con la detección del complejo QRS. Por lo tanto, el primer paso de la detección del pico R es la eliminación de ruido de la señal, y luego se mejoran y detectan los complejos QRS. [2]

### Objetivos específicos de la práctica

### Materiales y métodos
#### Dataset de señales ECG adquirirdas y filtradas
#### Picos de la onda R
#### HRV 

### Resultados
#### Picos de la onda R
#### HRV 

### Discusión
#### Picos de la onda R
#### HRV 

### Bibliografía
[1] Q. Qin, J. Li, Y. Yue, y C. Liu, “An adaptive and time-efficient ECG R-peak detection algorithm”, J. Healthc. Eng., vol. 2017, pp. 1–14, 2017.
