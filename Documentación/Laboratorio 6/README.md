# Filtros FIR e IIR
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro  

## Tabla de contenidos
1. [Introducción](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#introducci%C3%B3n)
2. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#materiales-y-m%C3%A9todos)
4. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#resultados)
   - [Tabla resumen ECG](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#tabla-resumen-ecg)
   - [Tabla resumen EMG ](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#tabla-resumen-emg)
   - [Tabla resumen EEG](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#tabla-resumen-eeg)
5. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#discusi%C3%B3n)
6. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#bibliograf%C3%ADa)

### Introducción
<p align="justify"> Las señales ECG, EEG y EMG pueden ser clasificadas juntas dentro del grupo de señales bioeléctricas. Este tipo de señal describe la suma de las señales eléctricas que acompañan a una contracción mecánica de una sola célula cuando es estimulada por una corriente eléctrica, ya sea neural o externa [1].
Sin embargo, estas señales son bastante complejas asique son propensas a adquirir ruido y no linealidades mientras viajan a través de diferentes tejidos e interfaces como electrodos y circuitos de procesamiento de señales electrónicas. Por lo tanto, la detección y procesamiento de señales ECG se ha convertido en un requisito muy importante en ingeniería biomédica [2]. Por ende el diseño de diferentes tipos de filtros para aplicar en el procesamiento de estas señales es un área bastante explorada hoy en día. 
   
<p align="justify"> El término filtro se utiliza habitualmente para describir un dispositivo que discrimina, de acuerdo con algún atributo de los objetos aplicados a su entrada, lo que pasa a través. El filtrado se emplea de formas muy variadas en el procesamiento digital de señales; por ejemplo, para eliminar el ruido indeseado que pueda existir en las señales deseadas, para conformación espectral en la ecualización de canales de comunicación, en la detección de señales de radar, sonar y de comunicaciones y para realizar el análisis espectral de señales, etc. Por tanto, seleccionando adecuadamente los coeficientes, se puede diseñar filtros selectivos de frecuencia que dejan pasar señales con componentes de frecuencia en determinadas bandas mientras que atenúan señales que contienen frecuencias en otras bandas. Normalmente, los filtros se clasifican de acuerdo con sus características en el dominio de la frecuencia como filtros paso bajo, paso alto, paso banda, banda eliminada y paso todo. [3]
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/paso.png" alt="Descripción de la imagen" width="300"><br> 
<p align="center"><b>Figura 1.</b> Módulo de las respuestas de algunos filtros discretos en el tiempo y selectivos en frecuencia [3]. <br> 

<p align="justify">Sin embargo, también es conveniente subdividir la clase de sistemas lineales invariantes en el tiempo en dos tipos: aquellos que tienen una repuesta al impulso de duración finita (FIR, finite-duration impulse response) y aquellos que tienen una respuesta al impulso de duración infinita (IIR, infinite-duration impulse response). En la práctica, los filtros FIR se emplean en problemas de filtrado en los que se precisa una característica de fase dentro de la banda de paso del filtro. Si no se necesita esta característica de fase lineal, puede emplearse un filtro IIR o FIR. Por regla general, un filtro IIR tiene lóbulos secundarios más pequeños en la banda eliminada que un filtro FIR con el mismo número de parámetros. Por esta razón, si es tolerable cierta distorsión, es preferible un filtro IIR, principalmente porque su implementación precisa muy pocos parámetros, requiere menos memoria y presenta menos complejidad de cálculo [3].

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/filtro.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 2.</b> Módulo de los filtros físicamente realizables [3]. <br> 
   
<p align="justify">En este laboratorio, se abordará el diseño de filtros IIR por medio de transformación bilineal. Hay varios tipos comunes de filtros analógicos: Butterworth, que tienen bandas de paso máximamente planas en filtros del mismo orden, Chebyshev tipo I que son equivariables en la banda de paso, Chebyshev tipo II que son equivariables en la banda de parada, y filtros elípticos que son equivariables tanto en la banda de paso y la banda de parada. La versión digital de estos se puede obtener a partir de diseños analógicos a través de la transformación bilineal [4]. En comparación, para FIR, las técnicas de diseño para filtros digitales, se trabajarán con el método de ventana, el cual comienza con una respuesta de muestra unitaria deseada que luego se trunca mediante una ventana de duración finita [5]. Los distintos tipos de filtro FIR e IIR son visualizados a continuación.

<div style="text-align: center;">
      <p align="center">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/iir.png" alt="Descripción de la primera imagen" width="300">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/vent.png" alt="Descripción de la primera imagen" width="525">
</div>
<p align="center"><b>Figura 3.</b> (a) Módulo de las respuestas de los filtros de Bessel y Butterworth de orden N = 4 y (b) formas de varias funciones de ventana [3]. <br> 
      
### Objetivos específicos de la práctica
- Diseñar filtros FIR e IIR con los datasets de los laboratorios anteriores.
- Filtrar de manera óptima las frecuencias altas de las señales de ECG que corresponden a ruido.
- Filtrar las señales EMG para eliminar ruido y artefactos, y aislar la actividad muscular efectiva.
- Preprocesar señales EEG para reducir el ruido y extraer características de interés como ondas cerebrales específicas.

### Materiales y métodos
#### ECG
<p align="justify">La contaminación de una señal de ECG proviene de diversas fuentes dentro y fuera del cuerpo de los pacientes. Las señales eléctricas de otros músculos además del corazón, así como la respiración, la tos y otros tipos de movimiento, pueden crear artefactos. El ruido también puede deberse a conexiones eléctricas deficientes si los electrodos no se colocan correctamente sobre el paciente. Además, los cables de ECG son antenas eficaces que captan fácilmente fuentes de ruido eléctrico del entorno inmediato, incluidas luces fluorescentes, teléfonos móviles o dispositivos con Bluetooth. Todas estas cosas pueden crear una lectura de ECG borrosa [6].

<p align="justify">Adicionalmente, es indispensable saber que la definición de filtros de muesca, los cuales combinan filtros de paso alto y bajo para crear una pequeña región de frecuencias que se eliminarán. Para los ECG, el objetivo principal es eliminar el ruido de 50 Hz o 60 Hz dado que el ruido de la red eléctrica se sitúa en la zona de interés. El equipo de ECG ya tiene cierta capacidad para rechazar el ruido de la red incluso sin un filtro, por lo que, dependiendo de la cantidad de ruido de CA en el ambiente, es posible que no se requiera este filtro [7].

<p align="justify">Para reducir este ruido se consideraron las siguientes características en el filtrado:

<b>Diseñar un filtro IIR:</b>
- Opciones de filtro: Bessel, Butterworth, Chebyshev, Eliptico.
- Especificaciones sugeridas: Fc = 60 Hz, Wp = 188 rad/s, Ws = 300 rad/s.
  
<b>Diseñar un filtro FIR:</b>
- Métodos de ventana: Hanning, Hamming, Bartlett, rectangular o Blackman.
- Especificaciones sugeridas: Fc = 40 Hz, paso banda bajo.

<b>Características del filtro: </b>
- Fc = 20 hz
- Wp = 94 rad/s
- Ws = 157 rad/s

<p align="justify">Afortunadamente, existen varios tipos de filtros que puede utilizar para mitigar esta interferencia. Las frecuencias de ECG suelen estar en el rango de 0,5 a 150 Hz, y los filtros diseñados para eliminar el ruido fuera de ese rango (en el extremo alto o bajo) son relativamente sencillos. El proceso se vuelve más complicado cuando la interferencia se superpone con el rango de frecuencia del ECG [6]. Para diferentes propósitos (monitorización, cuidados intensivos, diagnóstico, ambulatorio, monitorización del segmento ST, etc.) el equilibrio cambia, por lo que terminamos con una gama de filtros ajustados para obtener el mejor equilibrio. Algunos ejemplos comunes de filtros de ECG son: Diagnóstico: 0,05 Hz ~ 150 Hz; Monitorización ambulatoria de pacientes: 0,67 Hz ~ 40 Hz; Segmento ST: 0,05 Hz ~; y Músculo, ruido ESU: ~ 15 Hz [7].

#### EMG
<p align="justify">La señal electromiográfica de superficie (sEMG) que se origina en el músculo está inevitablemente contaminada por varias señales de ruido o artefactos que se originan en la interfaz piel-electrodo, en la electrónica que amplifica las señales, y en fuentes externas. La tecnología moderna es sustancialmente inmune a algunos de estos ruidos, pero no al ruido de referencia y al ruido de artefacto de movimiento. Estas fuentes de ruido tienen espectros de frecuencia que contaminan la parte de baja frecuencia de espectro de frecuencia. Hay muchos factores que deben tenerse en cuenta al determinar las especificaciones de filtro adecuadas para eliminar estos artefactos; Incluyen el músculo probado y el tipo de contracción, la configuración del sensor y la fuente de ruido específica. La determinación del paso de banda es siempre un compromiso entre (a) reducir el ruido y la contaminación por artefactos, y (b) preservar la información deseada [8].

<p align="justify">Para reducir este ruido se consideraron las siguientes características en el filtrado:
   
<b>Diseñar un filtro IIR:</b>
- Opciones de filtro: Bessel, Butterworth, Chebyshev, Eliptico.
- Objetivo: Eliminar frecuencias altas que correspondan a ruido eléctrico y artefactos de movimiento.
- Especificaciones sugeridas: Fc = 60 Hz, Wp = 188 rad/s, Ws = 300 rad/s.
  
<b>Diseñar un filtro FIR:</b>
- Métodos de ventana: Hamming, Blackman.
- Objetivo: Aislar la banda de frecuencia de interés que corresponde a la actividad muscular.
- Especificaciones sugeridas: Fc = 40 Hz, paso banda bajo.

<p align="justify">Como las señales EMG tienen una amplitud muy baja (nivel de milivoltios), es necesario amplificarlas con una ganancia de 1000x a una escala que es menos sensible al ruido y puede ser procesada adicionalmente por un convertidor analógico a digital (ADC). Para eliminar fuentes de ruido no deseadas o limitar la salida del sensor, también es útil filtrar la señal a una banda de frecuencia específica de interés que aún contiene toda la información de señales musculares como 20-450 Hz que se usa típicamente para superficie EMG. [9]

#### EEG
<p align="justify">Las fuentes de ruido también se manifiestan como frecuencias oscilantes que son captadas por el EEG. El ruido de baja frecuencia proviene de fuentes como el movimiento de la cabeza y los cables de los electrodos, y la transpiración en el cuero cabelludo. Este aparece como derivas lentas en la señal del EEG durante muchos segundos. Por el contrario, el ruido de alta frecuencia proviene de fuentes que incluyen interferencias electromagnéticas y contracciones musculares. Este parece cambios rápidos de arriba a abajo (como los dientes de una sierra) en el EEG. La frecuencia de las fuentes de ruido de alta y baja frecuencia puede superponerse con la banda de interés del EEG de 1-30 Hz, pero en general tienden a ser más bajas y más altas, respectivamente, que el EEG humano. Esto significa que al reducir la potencia de la señal en las frecuencias por encima y por debajo del rango de interés experimental, podemos reducir el ruido con un impacto mínimo en las señales de interés. [10]

<p align="justify">Para reducir este ruido se consideraron las siguientes características en el filtrado:

<b>Diseñar un filtro IIR:</b>
- Opciones de filtro: Bessel, Butterworth, Chebyshev, Eliptico.
- Objetivo: Suprimir la interferencia de frecuencia alta y artefactos.
- Especificaciones sugeridas: Fc = 30 Hz, Wp = 94 rad/s, Ws = 157 rad/s.

<b>Diseñar un filtro FIR:</b>
- Métodos de ventana: Hanning, Bartlett.
- Objetivo: Extraer bandas de frecuencia específicas (alfa, beta, etc.).
- Especificaciones sugeridas: Fc = 12 Hz, paso banda para ondas alfa.

<p align="justify">Cinco subbandas de frecuencia definen las frecuencias de la señal EEG que se pueden medir desde el cerebro, siendo gamma la más rápida y delta de las frecuencias más lentas [11]. 
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/Screenshot%202024-05-04%20192312.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 4.</b> Bandas de frecuencia de EEG, ocurrencia y tareas para activar la potencia de la banda [11]. <br> 

<p align="justify"><b>Banda delta:</b> Oscila en frecuencias de 0 a 4 Hz y están presentes en diferentes fases del sueño [11].

<p align="justify"><b>Banda theta:</b> Varían en frecuencias de 4 a 8 Hz y se originan en el tálamo y son más fuertes en el lado derecho del cerebro. Las ondas theta están asociadas con el área frontal del cerebro y se correlacionan con tareas metálicas e indican una mayor potencia de banda con mayor dificultad de la tarea, aunque se puede medir en todas las áreas de la corteza y se relaciona con la región del cerebro transportador [11].

<p align="justify"><b>Banda alfa:</b> Varían en frecuencias de 8 a 12 Hz y reflejan funciones correlacionadas con la memoria, la motricidad y los sentidos. Un aumento de la potencia de la banda alfa puede ser provocado por la relajación en estado de vigilia cuando los ojos están cerrados. En comparación, las ondas alfa se suprimen al abrir los ojos y al realizar actividad física o mental [11].

<p align="justify"><b>Banda beta:</b> Oscilan entre 12 y 25 Hz y se generan en las regiones posterior y frontal. Se correlacionan con el pensamiento activo y concentración. A mayor concentración, las oscilaciones beta se disparan en una frecuencia más rápida [11].

<p align="justify"><b>Banda gamma:</b> Frecuencias superiores a 25 Hz. El origen y el reflejo de estas oscilaciones no es notablemente claro [11].

### Resultados
#### Tabla resumen ECG 
| Campo | Señal cruda | Filtro IIR | Filtro FIR |
| --------- | ---------- | ------------------------------ | ---------------------- |
| Basal | ![Imagen de EEG](plots/ecg-reposo-cruda.png) | ![Imagen de EEG](plots/ecg-reposo-IIR.png) | ![Imagen de EEG](plots/ecg-reposo-FIR.png) |
 Respiración | ![Imagen de EEG](plots/ecg-respiracion-cruda.png) | ![Imagen de EEG](plots/ecg-respiracion-IIR.png) | ![Imagen de EEG](plots/ecg-respiracion-FIR.png) |
| Ejercicio | ![Imagen de EEG](plots/ecg-ejercicio-cruda.png) | ![Imagen de EEG](plots/ecg-ejercicio-IIR.png) | ![Imagen de EEG](plots/ecg-ejercicio-FIR.png) |

#### Tabla resumen EMG 
| Estado | Señal cruda | Filtro IIR | Filtro FIR |
| ------------ | -------------- | ------------------ | ------------------ |
| Reposo | ![Imagen de EMG](plots/emg-reposo-cruda.png) | ![Imagen de EMG](plots/emg-reposo-IIR.png) | ![Imagen de EMG](plots/emg-reposo-FIR.png) |
| Contracción leve | ![Imagen de EMG](plots/emg-contraccion-leve-cruda.png) | ![Imagen de EMG](plots/emg-contraccion-leve-IIR.png) | ![Imagen de EMG](plots/emg-contraccion-leve-FIR.png) |
| Contracción fuerte | ![Imagen de EMG](plots/emg-contraccion-fuerte-cruda.png) | ![Imagen de EMG](plots/emg-contraccion-fuerte-IIR.png) | ![Imagen de EMG](plots/emg-contraccion-fuerte-FIR.png) |

#### Tabla resumen EEG 
### Discusión
<p align="justify"><b>Filtración de ECG:</b>
<p align="justify"><b>Filtración de EMG:</b>
<p align="justify">A traves de los resultados obtenidos por el filtro FIR de ventana Hamming y el filtro IIR de metodo Butterworth, podemos observar que el filtro FIR proporciona resultados más entendibles con menos ruido y picos más pronunciados. Este resultado coincide con el estudio realizado por Liu, S. [12], el cual hizo uso de los mismos tipos de filtros en señales EMG y encontro que el SNR o Signal to Noise Ratio es mayor en los filtros FIR ademas de mostrar un tiempo de ejecución mucho menor. Estos parametros son indicadores de una mejor filtración de señal.
<p align="justify"><b>Filtración de EEG:</b>
   
### Bibliografía
<p align="justify">[1]  Martinek R, Ladrova M, Sidikova M, Jaros R, Behbehani K, Kahankova R, Kawala-Sterniuk A. Advanced Bioelectrical Signal Processing Methods: Past, Present and Future Approach-Part I: Cardiac Signals. Sensors (Basel). 2021 Jul 30;21(15):5186. doi: 10.3390/s21155186. PMID: 34372424; PMCID: PMC8346990. 
<p align="justify">[2] Adimulam, M. K., & Srinivas, M. . (2016). Modeling of EXG (ECG, EMG and EEG) non-idealities using MATLAB. 2016 9th International Congress on Image and Signal Processing, BioMedical Engineering and Informatics (CISP-BMEI). doi:10.1109/cisp-bmei.2016.7852968
<p align="justify">[3] J. G. Proakis y D. G. Manolakis, Tratamiento digital de señales. Old Tappan, NJ, Estados Unidos de América: Prentice Hall, 2007.
<p align="justify">[4] “DT Filter Design: IIR Filters”, Mit.edu, 2006. [En línea]. Disponible en: https://ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/51e3beff8c8ce2289ba292fcdb0040f4_lec08.pdf.
<p align="justify">[5] A. V. Oppenheim, “Design of FIR digital filters”, Mit.edu, 2011. [En línea]. Disponible en: https://ocw.mit.edu/courses/res-6-008-digital-signal-processing-spring-2011/aea8444ff81fdeed9c2b66dccebbce47_MITRES_6_008S11_lec17.pdf.
<p align="justify">[6] GE HealthCare, “A guide to ECG signal filtering”, Gehealthcare.com. [En línea]. Disponible en: https://www.gehealthcare.com/insights/article/a-guide-to-ecg-signal-filtering.
<p align="justify">[7] P. Selvey, “ECG filters”, MEDTEQ, 27-feb-2017. [En línea]. Disponible en: https://www.medteq.net/article/2017/4/1/ecg-filters.
<p align="justify">[8] C. J. De Luca, L. Donald Gilmore, M. Kuznetsov, y S. H. Roy, “Filtering the surface EMG signal: Movement artifact and baseline noise contamination”, J. Biomech., vol. 43, núm. 8, pp. 1573–1579, 2010.
<p align="justify">[9] EXPERIMENTAL GUIDES TO MEET y L. Y. Biosignals, “BITalino (r)evolution Lab Guide”, Pluxbiosignals.com. [En línea]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf. [Consultado: 05-may-2024].
<p align="justify">[10] “Filtering EEG data — neural data science in python”, Neuraldatascience.io. [En línea]. Disponible en: https://neuraldatascience.io/7-eeg/erp_filtering.html.
<p align="justify">[11] EXPERIMENTAL GUIDES TO MEET y L. Y. Biosignals, “BITalino (r)evolution Lab Guide”, Pluxbiosignals.com. [En línea]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf. [Consultado: 05-may-2024].
<p align="justify">[12] Liu, S., Sabrina, N., & Hardson, H. (2023). Comparison of FIR and IIR Filters for Audio Signal Noise Reduction. Ultima Computing : Jurnal Sistem Komputer, 15(1), 19-24. https://doi.org/https://doi.org/10.31937/sk.v15i1.3171
