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
<p align="justify"> El método más extendido para observar la actividad eléctrica del corazón a lo largo del tiempo es el electrocardiograma (ECG). [1] El ECG puede describir la actividad eléctrica del corazón y es una herramienta esencial para el diagnóstico de enfermedades cardiovasculares. [2] Esta es  una señal aleatoria e inestable y es significantemente diferente entre entornos e individuos. [3] Con el rápido desarrollo de técnicas de ECG portátiles e inalámbricas, la monitorización de ECG en tiempo real y de rutina está atrayendo cada vez más atención debido a la creciente popularización de la salud médica. [2]
  
<p align="justify"> Cada ciclo cardíaco (latido del corazón) se representa en el ECG como una secuencia de cinco deflexiones (el complejo PQRST), cada una de las cuales representa la actividad eléctrica durante las diferentes fases del ciclo cardíaco. [1] La onda P (indica despolarización auricular o contracción de la aurícula), el complejo QRS (indica despolarización ventricular o contracción de los ventrículos) y la onda T (indica repolarización ventricular) son los componentes principales de la forma de onda del ECG, y la detección precisa de ellos es importante para el análisis de la señal del ECG. El complejo QRS es la característica dominante de la señal del ECG y su detección precisa es una cuestión importante en muchas condiciones clínicas. [3] 

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Images/qrs.png" alt="Descripción de la imagen" width="300"><br> 
<p align="center"><b>Figura 1.</b> El complejo PQRST. [1] <br> 
  
Sin embargo,  las características del ECG empiezan con la detección del pico R, ya que todas las demás se extraen después de la ubicación de este. La detección del complejo QRS, especialmente la detección de la onda R en la señal cardíaca, es más fácil que otras partes de la señal del ECG debido a su forma estructural y alta amplitud. [4] Es fundamental su precisión para el diagnóstico de arritmias como contracción auricular prematura, taquicardia y bradicardia. Aunque la extracción eficiente del pico R sigue siendo difícil en el entorno dinámico y ruidoso debido a la morfología de la forma de onda que varía con el tiempo, es más difícil cuando la señal del ECG se ve abrumada por ruidos con frecuencia similar en la distribución de energía. [2]

<p align="justify"> Aún se necesita un desarrollo significativo debido al desafío de los efectos de ruido inesperados en la señal de ECG, como la desviación de la línea base, el movimiento y estiramiento de los electrodos, los artefactos de movimiento y el ruido muscular, que impiden que la tecnología de procesamiento automático de ECG funcione de manera efectiva. Las principales fuentes de ruido son las actividades eléctricas de los músculos y la desviación de la línea base causada por la respiración, el mal contacto de los electrodos y los equipos o dispositivos electrónicos. [2] Desafortunadamente, existen grandes desafíos para la detección automatizada porque las morfologías y amplitudes de muchos complejos QRS normales son como los complejos QRS anormales. El ruido superpuesto en la señal de ECG hace que este problema sea más grave. Además, las ondas P/T con mayor amplitud pueden interferir con la detección del complejo QRS. Por lo tanto, el primer paso de la detección del pico R es la eliminación de ruido de la señal, y luego se mejoran y detectan los complejos QRS. [3]

<p align="justify"> La variabilidad de la frecuencia cardíaca (VFC) es la evaluación de la actividad eléctrica del corazón a través de un ECG. Se observa que la frecuencia cardíaca puede ser alta o baja dependiendo de las actividades físicas, las condiciones de estrés y las emociones de los individuos. Por lo tanto, la VFC puede reconocerse como la respuesta del corazón ante cualquier tipo de estímulo para que compense las situaciones en consecuencia y, por lo tanto, su variación puede usarse como señales de alerta de enfermedades cardíacas. [5] Esta es simplemente una medida de la variación en el tiempo de la frecuencia entre una sucesión de intervalos R-R; es decir, entre cada latido del corazón. [6, 7] Esta variación está controlada por una parte primitiva del sistema nervioso llamada sistema nervioso autónomo (SNA). Este sistema funciona en segundo plano, regulando automáticamente nuestra frecuencia cardíaca, presión arterial, respiración y digestión, entre otras tareas clave. [7] 
  
<p align="justify"> La modulación del SNA en el corazón se puede analizar a partir del procesamiento del ECG. Entre las diversas técnicas que se han desarrollado recientemente para esta evaluación, se ha descubierto que la HRV es una de las formas más rápidas y no invasivas, que se utiliza con mayor frecuencia para analizar los datos más reproducibles y fiables sobre la modulación autónoma de la frecuencia cardíaca. [5] Al medir la variabilidad de la frecuencia cardíaca, se pueden analizar múltiples variables. Estas variables se pueden dividir en tres dominios principales: dominio temporal, dominio de frecuencia y dominio geométrico. [6] Siendo los índices de dominio temporal de la VFC quienes cuantifican la cantidad de variabilidad en las mediciones del intervalo entre latidos, las mediciones de dominio de frecuencia las que estiman la distribución de la potencia absoluta o relativa en cuatro bandas de frecuencia y, finalmente, las mediciones no lineales quienes permiten cuantificar la imprevisibilidad de una serie temporal. [8]

### Objetivos específicos de la práctica
- <p align="justify"> Buscar y aprender acerca del procesamiento de señales ECG y la detección de picos R, así como sobre la variabilidad de la frecuencia cardíaca (HRV).
- <p align="justify"> Aplicar técnicas de filtrado para eliminar el ruido de las señales ECG adquiridas, incluyendo la desviación de la línea base, el ruido muscular y los artefactos de movimiento.
- <p align="justify"> Detectar con precisión los picos de la onda R en las señales ECG filtradas y graficarlas para visualización.
- <p align="justify"> Calcular la Variabilidad de la Frecuencia Cardíaca (HRV) a partir de los intervalos R-R obtenidos de la señal ECG y analizar los resultados obtenidos.

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
<p align="justify"> [1] E. B. Mazomenos, T. Chen, A. Acharyya, A. Bhattacharya, J. Rosengarten, y K. Maharatna, “A Time-Domain Morphology and Gradient based algorithm for ECG feature extraction”, en 2012 IEEE International Conference on Industrial Technology, 2012, pp. 117–122.
<p align="justify"> [2] Q. Qin, J. Li, Y. Yue, y C. Liu, “An adaptive and time-efficient ECG R-peak detection algorithm”, J. Healthc. Eng., vol. 2017, pp. 1–14, 2017.
<p align="justify"> [3] L. Wu, X. Xie, y Y. Wang, “ECG enhancement and R-peak detection based on window variability”, Healthcare (Basel), vol. 9, núm. 2, p. 227, 2021.
<p align="justify"> [4] H. Rabbani, M. Parsa Mahjoob, E. Farahabadi, y A. Farahabadi, “R peak detection in electrocardiogram signal based on an optimal combination of wavelet transform, Hilbert transform, and adaptive thresholding”, Journal of Medical Signals and Sensors, vol. 1, núm. 2, p. 91, 2011.
<p align="justify"> [5] R. Tiwari, R. Kumar, S. Malik, T. Raj, y P. Kumar, “Analysis of heart rate variability and implication of different factors on heart rate variability”, Curr. Cardiol. Rev., vol. 17, núm. 5, 2021.
<p align="justify"> [6] J. E. Peabody, R. Ryznar, M. T. Ziesmann, y L. Gillman, “A systematic review of heart rate variability as a measure of stress in medical professionals”, Cureus, 2023.
<p align="justify"> [7] H. E. LeWine, “Heart rate variability: How it might indicate well-being”, Harvard Health, 03-abr-2024. [En línea]. Disponible en: https://www.health.harvard.edu/blog/heart-rate-variability-new-way-track-well-2017112212789.
<p align="justify"> [8] F. Shaffer y J. P. Ginsberg, “An overview of heart rate variability metrics and norms”, Front. Public Health, vol. 5, 2017.
