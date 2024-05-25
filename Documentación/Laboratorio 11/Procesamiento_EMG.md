# Tratamiento de señal EMG
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro

## Tabla de contenidos
1. [Introducción](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Procesamiento_EMG.md#introducci%C3%B3n)
2. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Procesamiento_EMG.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Procesamiento_EMG.md#materiales-y-m%C3%A9todos)
5. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Procesamiento_EMG.md#resultados)
6. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Procesamiento_EMG.md#discusi%C3%B3n)
7. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Procesamiento_EMG.md#bibliograf%C3%ADa)

### Introducción
<p align="justify"> La electromiografía (EMG) se refiere a la señal eléctrica colectiva de los músculos, la cual está controlada por el sistema nervioso y se produce durante la contracción muscular. Esta representa las propiedades anatómicas y fisiológicas de los músculos; de hecho, una señal de EMG es la actividad eléctrica de las unidades motoras de un músculo, las cuales consisten en dos tipos: EMG superficial y EMG intramuscular. [1] En este laboratorio se estará trabajando con EMG superficial, el cual capta las señales mediante electrodos no invasivos y las reproduce, como en la figura 1. 

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Images/plot.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 1.</b> Señal EMG cruda [2]. <br> 

<p align="justify"> En la actualidad, se prefieren este tipo de señales para obtener información sobre el tiempo o la intensidad de la activación muscular superficial. Se consideran muy útiles como señales electrofisiológicas tanto en el campo médico como en el ingenieril. Para utilizar estas aplicaciones de manera efectiva, la adquisición precisa de la señal de EMG es un requisito previo; sin embargo, siempre que se registra una señal de EMG del músculo, varios tipos de ruidos la contaminan (equipos electrónicos y factores fisiológicos). Por lo tanto, analizar y clasificar las señales de EMG es muy difícil debido al patrón complicado de la EMG, especialmente cuando ocurre el movimiento. [1] Extraer ideas significativas de estas señales requiere la aplicación de técnicas avanzadas de reconocimiento de patrones y análisis de datos, donde la decodificación de señales de sEMG puede resumirse de la siguiente manera [2]: 

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Images/clasifica.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 2.</b> Arquitectura de clasificación de señales de sEMG. [3]. <br> 
  
#### Adquisición de señales
<p align="justify"> A pesar de las características no estacionarias de las señales de sEMG, aún pueden ser detectadas utilizando electrodos de superficie. Los electrodos suelen clasificarse según su tipo (electrodos rellenos de gel o secos) y densidad (lineales o en matriz 2D). El sensor utilizado para la adquisición de sEMG debe adherirse al teorema de Nyquist-Shannon, lo que garantiza una frecuencia de muestreo que sea al menos el doble de la frecuencia más alta de las señales de sEMG, lo que requiere una frecuencia de muestreo superior a 1000 Hz. [2]

#### Preprocesamiento
<p align="justify"> El desafío con los datos de sEMG en bruto radica en el alto nivel de ruido capturado durante la adquisición de la señal. Principalmente, existen tres tipos de ruido en las señales de sEMG: ruido inherente de los componentes electrónicos, interferencia de frecuencia de potencia del sistema eléctrico y ruido originado por los electrodos. [2] <br>
  
- <p align="justify"><b>Filtrado:</b> El filtrado es esencial para reducir los artefactos en las señales de sEMG. [2] En este laboratorio, se compararán filtros FIR, IIR y Wavelet. En algunos estudios, se utilizaron tanto un filtro pasa banda como un filtro notch para extraer las señales de sEMG, mientras que otros recomendaron un filtro Butterworth con parámetros específicos. [2] <br>

- <p align="justify"><b>Rectificación:</b> Dado que las señales de sEMG fluctúan entre valores positivos y negativos durante la contracción muscular, se abordan 2 enfoques comunes: rectificación de onda completa y de onda media, siendo la primera preferida debido a su capacidad para representar la señal de activación neural. [2] <br>

- <p align="justify"><b>Normalización:</b> Como se muestra una variabilidad significativa entre individuos, la normalización de amplitud es esencial para comparar las señales entre diferentes sujetos, eliminando la variación en el índice de grasa corporal, la edad, la fatiga, el género y factores externos. La normalización implica dividir las señales de sEMG recopiladas por un valor de referencia de sEMG en condiciones idénticas, lo que facilita las comparaciones entre sujetos. [2] <br>

- <p align="justify"><b>Segmentación:</b> Se divide los datos muestreados en segmentos, donde el tamaño de estos debe ser lo suficientemente grande como para extraer adecuadamente características de cada uno y tener una mayor precisión de clasificación, pero su longitud también debe ser pequeña para evitar cualquier retraso computacional en sistemas en tiempo real. Hay dos métodos predominantes: el método de ventanas adyacentes y el método de ventanas superpuestas. En el método adyacente, los datos se dividen en segmentos predefinidos y no superpuestos, y se extraen características de cada segmento; sin embargo, deja el procesador inactivo hasta la formación del siguiente segmento. Por otro lado, el método de ventanas superpuestas implica segmentos con solapamiento entre cada segmento y su predecesor, facilitando la extracción de características adicionales y produciendo una precisión de clasificación superior. [2]

#### Extracción de características 
<p align="justify"> Si bien los clasificadores pueden entrenarse utilizando señales en bruto preprocesadas, generalmente se logra una mejor precisión extrayendo características de estas señales. Esto no solo mejora el rendimiento del clasificador, sino que también reduce la dimensionalidad, simplificando el procesamiento y la clasificación posteriores. [2]  Hasta ahora, ningún estudio ha identificado qué tipos de características pueden expresar completamente las propiedades matemáticas de las señales de sEMG. Si se seleccionan demasiadas características, se aumentará el cálculo y la complejidad del clasificador, y la eficiencia de reconocimiento se reducirá. Si se seleccionan demasiado pocas características, la información contenida en la señal de EMG se perderá y no contribuirá a la clasificación en los pasos de identificación subsiguientes. [4] <br>
  
- <p align="justify"><b>Características en el dominio del tiempo:</b> Se evalúan en función de las variaciones de amplitud de la señal a lo largo del tiempo, eliminando la necesidad de transformaciones adicionales y beneficiándose de su simplicidad y bajos requisitos de recursos computacionales. [2] <br>

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Images/time.png" alt="Descripción de la imagen" width="600"><br> 
<p align="center"><b>Figura 3.</b> Resumen de las características en el dominio del tiempo. [2]. <br> 
  
- <p align="justify"><b>Características en el dominio de la frecuencia:</b> No pueden derivarse directamente de los datos en bruto y se obtienen aplicando la transformada de Fourier a la señal. Estas características abarcan la densidad espectral de potencia de la señal (PSD). [2] <br>

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Images/freq.png" alt="Descripción de la imagen" width="600"><br> 
<p align="center"><b>Figura 4.</b> Resumen de las características en el dominio de la frequencia [2]. <br> 

- <p align="justify"><b>Características en el dominio tiempo-frecuencia:</b> La transformada tiempo-frecuencia (TFD) combina información tanto de tiempo como de frecuencia, permitiendo la observación de diferentes componentes de frecuencia en distintos intervalos de tiempo. Esta técnica es especialmente valiosa para detectar componentes localizados, transitorios o intermitentes que pueden pasarse por alto con métodos espectrales tradicionales como la Transformada de Fourier (FFT). Se dispone de varios métodos para realizar la descomposición de señales en el plano tiempo-frecuencia, como la transformada continua de wavelet (CWT) y la transformada discreta de wavelet (DWT), así como otras técnicas como la distribución de Choi-Williams (CWD), la transformada de Fourier de tiempo corto (STFT) y la transformada de Wigner-Ville (WVT). Entre estos, la transformada de wavelet (WT) se destaca por su versatilidad, ya que no se limita a funciones sinusoidales y puede acomodar una amplia variedad de formas de onda, siempre que cumplan con ciertos criterios predefinidos. [2] <br>

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Images/tf.png" alt="Descripción de la imagen" width="500"><br> 
<p align="center"><b>Figura 5.</b> Resumen de las características en el dominio del tiempo-frequencia. [3]. <br> 
  
#### Clasificación y evaluación
<p align="justify"> Hay varios enfoques de aprendizaje automático y aprendizaje profundo para decodificar las señales de sEMG, pero que no serán abarcados este laboratorio. [2] En el campo del diagnóstico clínico y la biomedicina, el análisis de señales de EMG con metodologías potentes y avanzadas se está convirtiendo cada vez más en una herramienta necesaria para los proveedores de atención médica. [1] La posibilidad de estudiar la activación de los músculos esqueléticos, mediante el registro de los potenciales eléctricos producidos durante las contracciones musculares, es de particular relevancia en la ciencia deportiva y la medicina de rehabilitación. [5]

### Objetivos específicos de la práctica
- <p align="justify"> Adquirir una comprensión sólida de la Electromiografía (EMG) y las técnicas de procesamiento de señales relacionadas.
- <p align="justify"> Identificar y elegir el filtro más apropiado para cada señal sEMG, asegurando una reducción efectiva del ruido sin comprometer la integridad de los datos.
- <p align="justify"> Reconocer la importancia fundamental de la segmentación de señales en el análisis eficaz de la EMG y valorar su papel en la obtención de resultados precisos.
- <p align="justify"> Desarrollar competencias para extraer características relevantes de las señales de EMG en diferentes dominios para una interpretación más completa de los datos.
- <p align="justify"> Ejecutar las etapas del tratamiento de la señal EMG de manera coherente y precisa en dos señales de un mismo individuo realizando diferentes actividades, garantizando la comparabilidad y fiabilidad de los resultados obtenidos.
  
### Materiales y métodos

#### Adquisición
#### Filtrado 
#### Rectificación
#### Segmentación
#### Extracción de caracteristicas

### Resultados

### Discusión

### Bibliografía
<p align="justify"> [1] R. Chowdhury, M. Reaz, M. Ali, A. Bakar, K. Chellappan, y T. Chang, “Surface electromyography signal processing and classification techniques”, Sensors (Basel), vol. 13, núm. 9, pp. 12431–12466, 2013.
<p align="justify"> [2] A. M. Moslhi, H. H. Aly, y M. ElMessiery, “The impact of feature extraction on classification accuracy examined by employing a Signal Transformer to classify hand gestures using surface electromyography signals”, Sensors (Basel), vol. 24, núm. 4, p. 1259, 2024.
<p align="justify"> [3] S. M. S. Moctar, I. Rida, y S. Boudaoud, “Time-domain features for sEMG signal classification: A brief survey”, Hal.science. [En línea]. Disponible en: https://hal.science/hal-04199535/document.
<p align="justify"> [4] Y. Wu, X. Hu, Z. Wang, J. Wen, J. Kan, y W. Li, “Exploration of feature extraction methods and dimension for sEMG signal classification”, Appl. Sci. (Basel), vol. 9, núm. 24, p. 5343, 2019.
<p align="justify"> [5] M. A. Cavalcanti Garcia y T. M. M. Vieira, “Surface electromyography: Why, when and how to use it”, Rev. Andal. Med. Deport., vol. 4, núm. 1, pp. 17–28, 2011.
