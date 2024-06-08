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

#### Picos de la onda R

Sin embargo,  las características del ECG empiezan con la detección del pico R, ya que todas las demás se extraen después de la ubicación de este. La detección del complejo QRS, especialmente la detección de la onda R en la señal cardíaca, es más fácil que otras partes de la señal del ECG debido a su forma estructural y alta amplitud. [4] Es fundamental su precisión para el diagnóstico de arritmias como contracción auricular prematura, taquicardia y bradicardia. Aunque la extracción eficiente del pico R sigue siendo difícil en el entorno dinámico y ruidoso debido a la morfología de la forma de onda que varía con el tiempo, es más difícil cuando la señal del ECG se ve abrumada por ruidos con frecuencia similar en la distribución de energía. [2]

#### Fuentes de ruido

<p align="justify"> Aún se necesita un desarrollo significativo debido al desafío de los efectos de ruido inesperados en la señal de ECG, como la desviación de la línea base, el movimiento y estiramiento de los electrodos, los artefactos de movimiento y el ruido muscular, que impiden que la tecnología de procesamiento automático de ECG funcione de manera efectiva. Las principales fuentes de ruido son las actividades eléctricas de los músculos y la desviación de la línea base causada por la respiración, el mal contacto de los electrodos y los equipos o dispositivos electrónicos. [2] Desafortunadamente, existen grandes desafíos para la detección automatizada porque las morfologías y amplitudes de muchos complejos QRS normales son como los complejos QRS anormales. El ruido superpuesto en la señal de ECG hace que este problema sea más grave. Además, las ondas P/T con mayor amplitud pueden interferir con la detección del complejo QRS. Por lo tanto, el primer paso de la detección del pico R es la eliminación de ruido de la señal, y luego se mejoran y detectan los complejos QRS. [3]

#### Variabilidad de la frecuencia cardíaca

<p align="justify"> La variabilidad de la frecuencia cardíaca (VFC) es la evaluación de la actividad eléctrica del corazón a través de un ECG. Se observa que la frecuencia cardíaca puede ser alta o baja dependiendo de las actividades físicas, las condiciones de estrés y las emociones de los individuos. Por lo tanto, la VFC puede reconocerse como la respuesta del corazón ante cualquier tipo de estímulo para que compense las situaciones en consecuencia y, por lo tanto, su variación puede usarse como señales de alerta de enfermedades cardíacas. [5] Esta es simplemente una medida de la variación en el tiempo de la frecuencia entre una sucesión de intervalos R-R; es decir, entre cada latido del corazón. [6, 7] Esta variación está controlada por una parte primitiva del sistema nervioso llamada sistema nervioso autónomo (SNA). Este sistema funciona en segundo plano, regulando automáticamente nuestra frecuencia cardíaca, presión arterial, respiración y digestión, entre otras tareas clave. [7] 
  
<p align="justify"> La modulación del SNA en el corazón se puede analizar a partir del procesamiento del ECG. Entre las diversas técnicas que se han desarrollado recientemente para esta evaluación, se ha descubierto que la HRV es una de las formas más rápidas y no invasivas, que se utiliza con mayor frecuencia para analizar los datos más reproducibles y fiables sobre la modulación autónoma de la frecuencia cardíaca. [5] Al medir la variabilidad de la frecuencia cardíaca, se pueden analizar múltiples variables. Estas variables se pueden dividir en tres dominios principales: dominio temporal, dominio de frecuencia y dominio geométrico. [6] Siendo los índices de dominio temporal de la VFC quienes cuantifican la cantidad de variabilidad en las mediciones del intervalo entre latidos, las mediciones de dominio de frecuencia las que estiman la distribución de la potencia absoluta o relativa en cuatro bandas de frecuencia y, finalmente, las mediciones no lineales quienes permiten cuantificar la imprevisibilidad de una serie temporal. [8]

### Objetivos específicos de la práctica
- <p align="justify"> Buscar y aprender acerca del procesamiento de señales ECG y la detección de picos R, así como sobre la variabilidad de la frecuencia cardíaca (HRV).
- <p align="justify"> Aplicar técnicas de filtrado para eliminar el ruido de las señales ECG adquiridas, incluyendo la desviación de la línea base, el ruido muscular y los artefactos de movimiento.
- <p align="justify"> Detectar con precisión los picos de la onda R en las señales ECG filtradas y graficarlas para visualización.
- <p align="justify"> Calcular la Variabilidad de la Frecuencia Cardíaca (HRV) a partir de los intervalos R-R obtenidos de la señal ECG y analizar los resultados obtenidos.

### Materiales y métodos
#### Dataset de señales ECG adquirirdas y filtradas

La señal ECG utilizada en este trabajo fue adquirida mediante un dispositivo BITalino. se realizó el preprocesamiento de la señal tal como lo menciona el trabajo de Masomenos et al[1]. Se empleó un filtro pasabandas de fase cero con frecuencias de corte entre 0.5 Hz y 43 Hz, seguido de un suavizado de la señal de salida mediante un filtro de promedio móvil.

La identificación de los picos de las ondas R se llevó a cabo utilizando un algoritmo derivado del algoritmo Pan Tompkins, también referido en el mismo trabajo. Este algoritmo atenúa las ondas T y P, dejando prominente el pico de la onda R. La señal característica se calcula de la siguiente forma: 
f[n]=1.3⋅grad1+1.1⋅grad2f[n] = 1.3 \cdot \text{grad1} + 1.1 \cdot \text{grad2}f[n]=1.3⋅grad1+1.1⋅grad2 
donde:
•	f[n]f[n]f[n] es la señal resultante o señal característica.
•	grad1\text{grad1}grad1 es la primera derivada de la señal filtrada.
•	grad2\text{grad2}grad2 es la segunda derivada de la señal filtrada.
Se utilizó la función find_peaks de la biblioteca scipy de Python para identificar los picos en la señal característica. Para evitar que el algoritmo considere picos mínimos por error, se estableció una altura mínima de 0.02 mV para el reconocimiento de picos.

Descripción de código:
- Diseño del Filtro FIR: para diseñar el filtro FIR se utilizó el método `firwin` con un total de 101 coeficientes (`numtaps`). Este filtro se configuró como un filtro de paso banda con cortes bajos y altos definidos por `low_cutoff` y `high_cutoff` respectivamente.

```python
numtaps = 101  # Número de coeficientes en el filtro
b = firwin(numtaps, [low_cutoff, high_cutoff], pass_zero=False)
```

- Aplicación del Filtro Digital de Fase Cero: El filtro de fase cero digital de paso banda se aplicó a la señal utilizando la función `filtfilt` para minimizar cualquier desfase introducido por el filtrado.

```python
filtered_signal = filtfilt(b, 1, data_mV)
```

- Diseño del Filtro de Promedio Móvil. Para suavizar la señal filtrada, se diseñó un filtro de promedio móvil con un tamaño de ventana de 5 muestras.

```python
window_size = 5  # Tamaño de la ventana para el filtro de promedio móvil
moving_avg_filter = np.ones(window_size) / window_size
```

- Cálculo de la Primera Derivada: Se calculó la primera derivada de la señal suavizada para resaltar los cambios en la pendiente. Se añadió un cero al final de la señal derivada para mantener la longitud original de la señal.

```python
first_derivative = np.diff(smoothed_signal, n=1)
first_derivative = np.append(first_derivative, 0)
```

- Cálculo de la Segunda Derivada: Para resaltar los cambios en la aceleración de la señal, se calculó la segunda derivada. Se añadieron dos ceros al final de la señal derivada para mantener la wxw original.

```python
second_derivative = np.diff(smoothed_signal, n=2)
second_derivative = np.append(second_derivative, [0, 0])
```
- Combinación de las Derivadas: Las derivadas calculadas se combinaron para formar la señal de características. La primera derivada se ponderó por un factor de 1.3 y la segunda derivada por un factor de 1.1 para obtener la señal final de características.

```python
feature_signal = 1.3 * first_derivative + 1.1 * second_derivative
```
#### Picos de la onda R
<p align="justify">Las ondas R en un electrocardiograma (ECG) indican el proceso de activación de la pared ventricular libre y representan la despolarización de los ventrículos en un contexto clínico. Existen numerosas investigaciones médicas que han documentado el análisis de la morfología de la onda R en ECGs tomados a diferentes ritmos cardíacos. Un ejemplo significativo es la progresión deficiente de la onda R (PRWP), un hallazgo crucial en el ECG que puede relacionarse con diversas afecciones cardíacas, las cuales conllevan riesgos de mortalidad relevantes para el director médico. PRWP describe la incapacidad de la onda R para aumentar gradualmente desde las derivaciones V1 hasta V6, algo comúnmente observado en el infarto de miocardio anterior típico, el bloqueo de rama izquierda, la hipertrofia ventricular tanto derecha como izquierda, el síndrome de Wolff-Parkinson-White, entre otros.[9] 

Para identificar los picos R (máximos) en la señal característica, se utilizó la función `find_peaks` de la biblioteca `scipy.signal`. Se asumió una distancia mínima de 0.4 segundos entre los picos R, correspondiente a una distancia de `fs/2.5` muestras, donde `fs` es la frecuencia de muestreo de la señal ECG.

```python
from scipy.signal import find_peaks

# Encontrar los picos R (máximos) en la señal característica
peaks, _ = find_peaks(feature_signal, distance=fs/2.5)  # Asumiendo una distancia mínima de 0.4 segundos entre picos R
```
#### HRV 
La variabilidad de la frecuencia cardíaca (HRV) representa las fluctuaciones en los intervalos RR entre latidos, las cuales se deben a la interacción continua entre las dos ramas del sistema nervioso autónomo. Aunque el nodo sinusal, que actúa como el marcapasos principal del corazón, tiene una actividad intrínseca, diversos estímulos internos y externos que afectan el equilibrio entre el tono simpático y el tono vagal pueden influir en la frecuencia cardíaca básica. Los cambios en la frecuencia cardíaca pueden producirse como respuesta al estrés mental o físico, enfermedades cardíacas o de otro tipo, o tratamientos médicos tanto farmacológicos como invasivos. Se ha comprobado que un desequilibrio en el sistema nervioso autónomo, caracterizado por un aumento del tono simpático y una disminución del tono vagal, está relacionado con un mayor riesgo de mortalidad cardíaca. Por lo tanto, la HRV se ha convertido en una herramienta crucial y ampliamente reconocida para identificar a los pacientes con riesgo de muerte cardiovascular.[10] Para evaluar la HRV, existen variso tipos de variables que pueden ser usadas. Estas métricas incluyen SDNN, SDRR, SDANN, índice SDNN, RMSSD, NN50, pNN50, HR Max − HR Min, el índice triangular HRV (HTI) y la interpolación triangular del histograma de intervalo NN. [11] RMSSD es el parámetro más comunmente utilizado para medir el HRV y es igual a la raíz cuadrada de la suma de todas las diferencias entre intervalos R-R sucesivos y es indicativo de actividad parasimpática. [12] La siguiente formula puede ser utilizada para calcular el RMSSD: 
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Images/rmssd-formula (1).jpg" alt="Descripción de la imagen" width="300"><br> 
<p align="center"><b>Figura 1.</b> Formula de RMSSD [15] <br> 

### Resultados

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Plots/rest.png" <br>
<p align="center"><b>Figura 2.</b> Evaluación de onda de ECG reposo <br> 
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Plots/activity.png" <br>
<p align="center"><b>Figura 3.</b> Evaluación de onda de ECG actividad <br> 
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2012/Plots/artificial_2.png" <br> 
<p align="center"><b>Figura 4.</b> Evaluación de onda de ECG Fibrilación ventricular (simulación <br> 

RMSSD:
-Reposo: 167.27 ms
-Actividad: 42.81 ms


### Discusión
Se realizó el filtrado y extracción de características de la señal, obteniéndose el RMSSD para los estados de reposo y actividad. Adicionalmente se realizó el filtrado de la señal muestra de ECG de paro cardiaco para probar la robustez del algoritmo. Se observa que si bien el filtrado planteado permite observar a simple vista el complejo QRS y la onda T, la onda P resulta más difícil de identificar debido al ruido y a la presencia de oscilaciones de amplitud similar. No obstante, esto no resultó siendo un obstáculo para identificar el pico de la onda R mediante el algoritmo en ritmos cardiacos regulares. Se identificaron los puntos en el tiempo correspondientes a los picos de onda R, obteniéndose el RMSSD en cada caso. En la onda de ECG de paciente en reposo no obstante se puede apreciar claramente una variabilidad que sale de los límites descritos en la literatura, la cual en este caso puede explicarse por la presencia de ruido ocasionado por movimiento y otros factores cuya contaminación no habría sido completamente filtrada por el filtro propuesto.  En la onda de simulación, si bien es posible identificar los picos en los patrones de ECG regulares, en la completa falta de periodicidad correspondiente a la fibrilación ventricular severa, ubicar un complejo QRS bien definido resulta imposible. Correspondientemente, las ondas R también resultan imposibles de identificar.
<p align="justify"> Para conocer el estado del HRV utlizamos el RMSSD, calculandolo se encontro un valor de aproximadamente 42.8 ms. Este resultado se encuentra en el rango normal para una persona entre 20 a 29 años, el cual es entre  24-62 ms [14]. En un estudio por el European Journal of Preventive Cardiology se encontro que una media para hombres entre 20 y 24 años es de 57.3 ms, lo que coincide con la persona analizada.  
Si bien no se ha podido evaluar por falta de datos correspondientes, los datos patológicos del ECG llevan a pensar que, si bien el ECG se comporta de manera apropiada con ritmos regulares, patologías tales como las arritmias podrían resultar en una reducción de la efectividad del algoritmo. El RMSSD, asimismo es dependiente de la ubicación de una onda R definida, por lo cual su efectividad está relacionada a la forma de las oscilaciones en el ritmo cardiaco.

### Bibliografía
<p align="justify"> [1] E. B. Mazomenos, T. Chen, A. Acharyya, A. Bhattacharya, J. Rosengarten, y K. Maharatna, “A Time-Domain Morphology and Gradient based algorithm for ECG feature extraction”, en 2012 IEEE International Conference on Industrial Technology, 2012, pp. 117–122.
<p align="justify"> [2] Q. Qin, J. Li, Y. Yue, y C. Liu, “An adaptive and time-efficient ECG R-peak detection algorithm”, J. Healthc. Eng., vol. 2017, pp. 1–14, 2017.
<p align="justify"> [3] L. Wu, X. Xie, y Y. Wang, “ECG enhancement and R-peak detection based on window variability”, Healthcare (Basel), vol. 9, núm. 2, p. 227, 2021.
<p align="justify"> [4] H. Rabbani, M. Parsa Mahjoob, E. Farahabadi, y A. Farahabadi, “R peak detection in electrocardiogram signal based on an optimal combination of wavelet transform, Hilbert transform, and adaptive thresholding”, Journal of Medical Signals and Sensors, vol. 1, núm. 2, p. 91, 2011.
<p align="justify"> [5] R. Tiwari, R. Kumar, S. Malik, T. Raj, y P. Kumar, “Analysis of heart rate variability and implication of different factors on heart rate variability”, Curr. Cardiol. Rev., vol. 17, núm. 5, 2021.
<p align="justify"> [6] J. E. Peabody, R. Ryznar, M. T. Ziesmann, y L. Gillman, “A systematic review of heart rate variability as a measure of stress in medical professionals”, Cureus, 2023.
<p align="justify"> [7] H. E. LeWine, “Heart rate variability: How it might indicate well-being”, Harvard Health, 03-abr-2024. [En línea]. Disponible en: https://www.health.harvard.edu/blog/heart-rate-variability-new-way-track-well-2017112212789.
<p align="justify"> [8] F. Shaffer y J. P. Ginsberg, “An overview of heart rate variability metrics and norms”, Front. Public Health, vol. 5, 2017.
<p align="justify"> [9] Zhan P, Li T, Shi J, Wang G, Wang B, Liu H, Wang W. R-Wave Singularity: A New Morphological Approach to the Analysis of Cardiac Electrical Dyssynchrony. Front Physiol. 2020 Dec 22;11:599838. doi: 10.3389/fphys.2020.599838. PMID: 33414723; PMCID: PMC7783454.
<p align="justify"> [10] Iwona Cygankiewicz, Wojciech Zareba, Chapter 31 - Heart rate variability, Editor(s): Ruud M. Buijs, Dick F. Swaab, Handbook of Clinical Neurology, Elsevier, Volume 117, 2013, Pages 379-393, ISSN 0072-9752, ISBN 9780444534910, https://doi.org/10.1016/B978-0-444-53491-0.00031-6.
<p align="justify"> [11] Shaffer F, Ginsberg JP. An Overview of Heart Rate Variability Metrics and Norms. Front Public Health. 2017 Sep 28;5:258. doi: 10.3389/fpubh.2017.00258. PMID: 29034226; PMCID: PMC5624990.
<p align="justify"> [12] Vintila, A.1; Horumba, M.1; Cristea, G.2; Iordachescu, I.1; Tudorica, S.4; Tudorica, C.1; Vintila, V.3; Ciomag, R.2; Isacoff, D.1. HEART RATE VARIABILITY IN A COHORT OF HYPERTENSIVE PATIENTS - A CLOSER LOOK AT RMSSD. Journal of Hypertension 37():p e192, July 2019. | DOI: 10.1097/01.hjh.0000572476.43951.a0
<p align="justify"> [13] RMSSD for HRV Analysis | BIOPAC. (s.f.). BIOPAC Systems, Inc. https://www.biopac.com/application/ecg-cardiology/advanced-feature/rmssd-for-hrv-analysis/
<p align="justify"> [14] What is Heart Rate Variability? (s.f.). Rupa Health. https://www.rupahealth.com/post/what-is-heart-rate-variability#:~:text=While%20there%20is%20a%20normal,women,%20it%20is%20around%2037.
<p align="justify"> [15] Tegegne, Bale & Man, Tengfei & Roon, Arie & Snieder, Harold & Riese, Harriëtte. (2019). Reference values of heart rate variability from 10-second resting electrocardiograms: the Lifelines Cohort Study. European Journal of Preventive Cardiology. 27. 204748731987256. 10.1177/2047487319872567. 
