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
<p align="justify"> La electromiografía (EMG) se refiere a la señal eléctrica colectiva de los músculos, la cual está controlada por el sistema nervioso y se produce durante la contracción muscular [1]. Esta representa las propiedades anatómicas y fisiológicas de los músculos; de hecho, una señal de EMG es la actividad eléctrica de las unidades motoras de un músculo, las cuales consisten en dos tipos: EMG superficial y EMG intramuscular [2]. En este laboratorio se estará trabajando con EMG superficial, el cual capta las señales mediante electrodos no invasivos y las reproduce, como en la figura 1. 

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2011/Images/plot.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 1.</b> Señal EMG cruda [3]. <br> 

<p align="justify"> En la actualidad, se prefieren este tipo de señales para obtener información sobre el tiempo o la intensidad de la activación muscular superficial. Se consideran muy útiles como señales electrofisiológicas tanto en el campo médico como en el ingenieril. Para utilizar estas aplicaciones de manera efectiva, la adquisición precisa de la señal de EMG es un requisito previo; sin embargo, siempre que se registra una señal de EMG del músculo, varios tipos de ruidos la contaminan (equipos electrónicos y factores fisiológicos). Por lo tanto, analizar y clasificar las señales de EMG es muy difícil debido al patrón complicado de la EMG, especialmente cuando ocurre el movimiento. [1]

<p align="justify"> Otro de los principales desafíos relacionados con las señales de sEMG es su tendencia al sobreajuste, especialmente al cambiar entre diferentes individuos. Cuando los clasificadores entrenados con datos de una persona se aplican a un nuevo usuario, su rendimiento suele ser apenas mejor que el azar. Varios factores contribuyen a la variabilidad de las señales de sEMG entre individuos, como el índice de grasa corporal, la edad, la fatiga, el género y factores externos como la interferencia de la línea eléctrica y la colocación de los electrodos. Por lo tanto, para decodificar eficazmente las señales de sEMG se requiere el uso de algoritmos avanzados de detección, filtrado, procesamiento y clasificación. [3]

<p align="justify">  Las señales de EMG, por su naturaleza, exhiben información compleja y altamente variable. Extraer ideas significativas de estas señales requiere la aplicación de técnicas avanzadas de reconocimiento de patrones y análisis de datos similares a las utilizadas en el análisis de datos. Estudios recientes sobre la decodificación de señales de sEMG revelaron que estos estudios siguen enfoques similares, que pueden resumirse de la siguiente manera [3]: 
  
#### Adquisición de señales
<p align="justify"> A pesar de las características no estacionarias de las señales de sEMG, aún pueden ser detectadas utilizando electrodos de superficie. Los electrodos suelen clasificarse según su tipo (electrodos rellenos de gel o secos) y densidad (lineales o en matriz 2D). El sensor utilizado para la adquisición de sEMG debe adherirse al teorema de Nyquist-Shannon, lo que garantiza una frecuencia de muestreo que sea al menos el doble de la frecuencia más alta de las señales de sEMG, lo que requiere una frecuencia de muestreo superior a 1000 Hz. [3]

#### Preprocesamiento
<p align="justify"> El desafío con los datos de sEMG en bruto radica en el alto nivel de ruido capturado durante la adquisición de la señal, lo que requiere un procesamiento exhaustivo para una decodificación precisa de la señal. Principalmente, existen tres tipos de ruido en las señales de sEMG: (1) ruido inherente de los componentes electrónicos, (2) interferencia de frecuencia de potencia del sistema eléctrico y (3) ruido originado por los electrodos. El preprocesamiento abarca varios pasos clave, que incluyen  [3]: 
- Filtrado
- Rectificación
- Normalización
- Segmentación.

#### Extracción de características 

  
#### Clasificación y evaluación

En el campo del diagnóstico clínico y la biomedicina, el análisis de señales de EMG con metodologías potentes y avanzadas se está convirtiendo cada vez más en una herramienta necesaria para los proveedores de atención médica. [1]

### Objetivos específicos de la práctica


### Materiales y métodos

#### Filtrado 
#### Segmentación
#### Extracción de caracteristicas

### Resultados

### Discusión

### Bibliografía
