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

<p align="justify"> En la actualidad, se prefieren este tipo de señales para obtener información sobre el tiempo o la intensidad de la activación muscular superficial. Se consideran muy útiles como señales electrofisiológicas tanto en el campo médico como en el ingenieril. Para utilizar estas aplicaciones de manera efectiva, la adquisición precisa de la señal de EMG es un requisito previo; sin embargo, siempre que se registra una señal de EMG del músculo, varios tipos de ruidos la contaminan (equipos electrónicos y factores fisiológicos). Por lo tanto, analizar y clasificar las señales de EMG es muy difícil debido al patrón complicado de la EMG, especialmente cuando ocurre el movimiento. [1] Extraer ideas significativas de estas señales requiere la aplicación de técnicas avanzadas de reconocimiento de patrones y análisis de datos similares a las utilizadas en el análisis de datos. Estudios recientes sobre la decodificación de señales de sEMG revelaron que estos estudios siguen enfoques similares, que pueden resumirse de la siguiente manera [2]: 

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Images/clasifica.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 2.</b> Arquitectura de clasificación de señales de sEMG. [3]. <br> 
  
#### Adquisición de señales
<p align="justify"> A pesar de las características no estacionarias de las señales de sEMG, aún pueden ser detectadas utilizando electrodos de superficie. Los electrodos suelen clasificarse según su tipo (electrodos rellenos de gel o secos) y densidad (lineales o en matriz 2D). El sensor utilizado para la adquisición de sEMG debe adherirse al teorema de Nyquist-Shannon, lo que garantiza una frecuencia de muestreo que sea al menos el doble de la frecuencia más alta de las señales de sEMG, lo que requiere una frecuencia de muestreo superior a 1000 Hz. [2]

#### Preprocesamiento
<p align="justify"> El desafío con los datos de sEMG en bruto radica en el alto nivel de ruido capturado durante la adquisición de la señal, lo que requiere un procesamiento exhaustivo para una decodificación precisa de la señal. Principalmente, existen tres tipos de ruido en las señales de sEMG: (1) ruido inherente de los componentes electrónicos, (2) interferencia de frecuencia de potencia del sistema eléctrico y (3) ruido originado por los electrodos. El preprocesamiento abarca varios pasos clave, que incluyen  [2]: <br>
- Filtrado: El filtrado es esencial para reducir los artefactos en las señales de sEMG. En algunos estudios, se utilizaron tanto un filtro pasa banda como un filtro notch para extraer las señales de sEMG, mientras que otros recomendaron un filtro Butterworth con parámetros específicos.<br>
- Rectificación: Dado que las señales de sEMG fluctúan entre -5 y 5 mV durante la contracción muscular, la rectificación es un paso de preprocesamiento crítico que aborda la parte negativa de la señal. Dos enfoques comunes son la rectificación de onda completa y la rectificación de onda media, siendo la rectificación de onda completa generalmente preferida debido a su capacidad para representar la señal de activación neural.<br>
- Normalización: Dado que las señales de sEMG muestran una variabilidad significativa entre individuos, la normalización de amplitud es esencial para comparar las señales entre diferentes sujetos. La normalización implica dividir las señales de sEMG recopiladas por un valor de referencia de sEMG en condiciones idénticas, lo que facilita las comparaciones entre sujetos y mejora la eficiencia computacional. Varios factores contribuyen a la variabilidad de las señales de sEMG entre individuos, como el índice de grasa corporal, la edad, la fatiga, el género y factores externos como la interferencia de la línea eléctrica y la colocación de los electrodos.<br>
- Segmentación: La segmentación divide los datos muestreados en segmentos para la extracción de características posterior. El tamaño de los segmentos debe ser lo suficientemente grande como para extraer adecuadamente características de cada segmento y tener una mayor precisión de clasificación, pero la longitud de estos segmentos también debe ser pequeña para evitar cualquier retraso computacional en sistemas en tiempo real. Hay dos métodos predominantes para segmentar las señales de sEMG: el método de ventanas adyacentes y el método de ventanas superpuestas. En el método adyacente, los datos se dividen en segmentos predefinidos y no superpuestos, y se extraen características de cada segmento. Sin embargo, esta técnica tiene la desventaja de dejar el procesador inactivo hasta la formación del siguiente segmento. Por otro lado, el método de ventanas superpuestas implica segmentos con solapamiento entre cada segmento y su predecesor, facilitando la extracción de características adicionales. La investigación ha demostrado que las ventanas superpuestas tienden a producir una precisión de clasificación superior.

#### Extracción de características 
<p align="justify"> Si bien los clasificadores pueden entrenarse utilizando señales en bruto preprocesadas, generalmente se logra una mejor precisión extrayendo características de estas señales antes del entrenamiento del modelo. La extracción de características no solo mejora el rendimiento del clasificador, sino que también reduce la dimensionalidad, simplificando el procesamiento y la clasificación posteriores. Las características pueden clasificarse en tres categorías: <br>
- Características en el dominio del tiempo: Se evalúan en función de las variaciones de amplitud de la señal a lo largo del tiempo, eliminando la necesidad de transformaciones adicionales y beneficiándose de su simplicidad y bajos requisitos de recursos computacionales. <br>
- Características en el dominio de la frecuencia: No pueden derivarse directamente de los datos en bruto y se obtienen aplicando la transformada de Fourier a la señal. Estas características abarcan la densidad espectral de potencia de la señal (PSD). <br>
- Características en el dominio tiempo-frecuencia: Combina información de tiempo y frecuencia, lo que permite la observación de diferentes componentes de frecuencia en diversos intervalos de tiempo. TFD resulta especialmente valioso para capturar componentes localizados, transitorios o intermitentes que a menudo son pasados por alto por métodos solo espectrales como la FFT. Se dispone de varios métodos, como la transformada continua de wavelet (CWT) y la transformada discreta de wavelet (DWT), para la descomposición de señales en el plano tiempo-frecuencia, cada uno ofreciendo ventajas únicas. Existen una variedad de técnicas disponibles para la descomposición de señales en el dominio tiempo-frecuencia, como la distribución de Choi-Williams (CWD), la transformada de Fourier de tiempo corto (STFT), la transformada de Wigner-Ville (WVT) y la CWT. Dentro del ámbito de las características en el dominio tiempo-frecuencia, un enfoque notablemente efectivo es la transformada de wavelet (WT). La WT comprende principalmente dos métodos distintos: la CWT y la DWT. A diferencia de la STFT, la WT no se limita únicamente a funciones sinusoidales; acomoda una amplia variedad de formas de onda, siempre y cuando cumplan con criterios predefinidos. <br>
  
#### Clasificación y evaluación
Hay varios enfoques de aprendizaje automático y aprendizaje profundo para decodificar las señales de sEMG, pero que no serán abarcados este laboratorio. 

En el campo del diagnóstico clínico y la biomedicina, el análisis de señales de EMG con metodologías potentes y avanzadas se está convirtiendo cada vez más en una herramienta necesaria para los proveedores de atención médica. [1]

### Objetivos específicos de la práctica


### Materiales y métodos

#### Filtrado 
#### Segmentación
#### Extracción de caracteristicas

### Resultados

### Discusión

### Bibliografía
