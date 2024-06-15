# Tratamiento de señal EEG
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro

## Tabla de contenidos
1. [Introducción](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#introducci%C3%B3n)
2. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#materiales-y-m%C3%A9todos)
5. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#resultados)
6. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#discusi%C3%B3n)
7. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#bibliograf%C3%ADa)

### Introducción
<p align="justify"> La electroencefalografía (EEG) es un método de imagenología cerebral no invasivo en el que se colocan electrodos sobre el cuero cabelludo para registrar la actividad eléctrica del cerebro. Este proceso permite a los investigadores medir y estudiar las señales eléctricas generadas por el cerebro, proporcionando así información crucial sobre su funcionamiento. Esta técnica es fundamental para identificar trastornos neurológicos diversos y para investigar procesos cognitivos como la percepción, la atención y la memoria. [1] Existen cinco ondas cerebrales principales que se distinguen por sus diferentes rangos de frecuencia. Estas bandas de frecuencia, de bajas a altas respectivamente, se denominan alpha (α), theta (θ), beta (β), delta (δ) y gamma (γ). [2]

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/images/rythms.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 1.</b> Ritmos cerebrales dominantes típicos. La onda delta se observa en bebés y adultos durante el sueño, la onda theta en niños y adultos durante el sueño, la onda alfa se detecta en la región occipital del cerebro cuando no hay atención, y la onda beta aparece frontal y parietalmente con baja amplitud. [2] <br> 
  
<p align="justify"> Para identificar y analizar de manera precisa las señales de EEG, es necesario tener un profundo conocimiento de sus propiedades complejas y teóricas, así como realizar la extracción de características relevantes. Sin embargo, las señales de EEG presentan desafíos significativos debido a sus características únicas. Estos desafíos incluyen la susceptibilidad al ruido, su naturaleza no lineal y la falta de conformidad con una distribución normal, además de factores individuales como la edad, la psicología y el entorno. Las propiedades distintivas de las señales de EEG representan un desafío para extraer información relevante sobre tareas específicas directamente de ellas. Por lo tanto, es crucial desarrollar diversas metodologías para el análisis de estas señales e investigar técnicas de aprendizaje automático para mejorar la comprensión de las señales de EEG. [1]

<p align="justify"> En general, el procesamiento de señales EEG tiene como objetivo traducir las señales EEG crudas en la clase de estas señales. Esta traducción generalmente se logra utilizando un enfoque de reconocimiento de patrones, cuyos pasos se pueden observar en la siguiente imagen. [3]

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/images/processing.png" alt="Descripción de la imagen" width="500"><br> 
<p align="center"><b>Figura 2.</b> El análisis de señales EEG implica cuatro etapas: adquisición, eliminación de ruido, ingeniería de características y clasificación. [1] <br> 
  
<p align="justify"> La adquisición de la señal se suele realizar según ha sido estipulado por La Federación Internacional de Sociedades de Electroencefalografía y Neurofisiología Clínica, quien ha recomendado un ajuste convencional de electrodos (también llamado 10-20) para 21 electrodos (excluyendo los electrodos de lóbulo de la oreja). [2] Para iniciar con el tratamiento, después de la adquisición, se realiza un pipeline de preprocesamiento, el cual es un conjunto de métodos aplicados a grabaciones crudas de EEG, destinados a preparar las señales para un análisis posterior y más específico. Puede incluir varios pasos en los que existen diferentes opciones, donde la selección de los algoritmos y herramientas "más apropiados" no es directa. [4] Esto es importante debido a lo siguiente [5]:
  
1. <p align="justify"> Las señales recogidas desde el cuero cabelludo no necesariamente son una representación precisa de las señales que provienen del cerebro.
2. <p align="justify"> Los datos de EEG contienen mucho ruido que puede ocultar señales de EEG más débiles.
3. <p align="justify"> Artefactos como parpadeos o movimientos musculares pueden contaminar los datos y distorsionar la imagen.
4. <p align="justify"> Queremos separar las señales neurales relevantes de la actividad aleatoria que ocurre durante las grabaciones de EEG.

<p align="justify"> Seguido a ello se tienen 2 pasos principales [3]:
  
- <p align="justify"> Extracción de características: Tiene como objetivo describir las señales EEG mediante idealmente unos pocos valores relevantes llamados "características", las cuales deben capturar la información incrustada en las señales EEG que es relevante para describir los estados mentales a identificar, mientras se rechaza el ruido y otra información no relevante. Todas las características extraídas generalmente se organizan en un vector conocido como vector de características.
  
- <p align="justify"> Clasificación: Asigna una clase a un conjunto de características extraído de las señales, la cual corresponde al tipo de investigación identificado. Este paso también puede ser denominado "traducción de características" y a sus algoritmos se les conoce como "clasificadores".

<p align="justify"> Las señales EEG pueden ser procesadas en dominios de tiempo, frecuencia o espaciales, ofreciendo medios multidimensionales para interpretar las actividades cerebrales. Además de proporcionar información invaluable, las señales EEG tienen la ventaja de capturar patrones neurales complejos a alta velocidad. Como método confiable, portátil y no invasivo para medir la actividad eléctrica en el cerebro, el EEG es una metodología central para la investigación asequible y práctica, así como una herramienta prometedora en la atención clínica. [6]

### Objetivos específicos de la práctica

### Materiales y métodos
#### Filtrado
#### Preprocesamiento
#### Feature extraction
#### Feature engineering

### Resultados

### Discusión

### Bibliografía
<p align="justify"> [1] A. Chaddad, Y. Wu, R. Kateb, y A. Bouridane, “Electroencephalography signal processing: A comprehensive review and analysis of methods and techniques”, Sensors (Basel), vol. 23, núm. 14, p. 6434, 2023.
<p align="justify"> [2] S. Sanei y J. A. Chambers, EEG signal processing. Wiley, 2007.
<p align="justify"> [3] F. Lotte, “A tutorial on EEG signal-processing techniques for mental-state recognition in brain–computer interfaces”, en Guide to Brain-Computer Music Interfacing, London: Springer London, 2014, pp. 133–161.
<p align="justify"> [4] S. Coelli et al., “Selecting methods for a modular EEG pre-processing pipeline: An objective comparison”, Biomed. Signal Process. Control, vol. 90, núm. 105830, p. 105830, 2024.
<p align="justify"> [5] “Introduction to EEG-preprocessing”, Github.io. [En línea]. Disponible en: https://g0rella.github.io/gorella_mwn/preprocessing_eeg.html.
<p align="justify"> [6] Y. Tran, EEG signal processing for biomedical applications. MDPI, 2023.
