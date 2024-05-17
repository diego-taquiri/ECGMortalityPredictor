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
5. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#resultados)
   - [Tabla resumen ECG](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#tabla-resumen-ecg)
   - [Tabla resumen EMG ](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#tabla-resumen-emg)
   - [Tabla resumen EEG](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#tabla-resumen-eeg)
6. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#discusi%C3%B3n)
7. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/README.md#bibliograf%C3%ADa)

### Introducción
<p align="justify"> Las señales ECG, EEG y EMG pueden ser clasificadas juntas dentro del grupo de señales bioeléctricas. Este tipo de señal describe la suma de las señales eléctricas que acompañan a una contracción mecánica de una sola célula cuando es estimulada por una corriente eléctrica, ya sea neural o externa [1].
Sin embargo, estas señales son bastante complejas asique son propensas a adquirir ruido y no linealidades mientras viajan a través de diferentes tejidos e interfaces como electrodos y circuitos de procesamiento de señales electrónicas. Por lo tanto, la detección y procesamiento de señales ECG se ha convertido en un requisito muy importante en ingeniería biomédica [2]. Por ende el diseño de diferentes tipos de filtros para aplicar en el procesamiento de estas señales es un área bastante explorada hoy en día. 
   
<p align="justify"> El término filtro se utiliza habitualmente para describir un dispositivo que discrimina, de acuerdo con algún atributo de los objetos aplicados a su entrada, lo que pasa a través. El filtrado se emplea de formas muy variadas en el procesamiento digital de señales; por ejemplo, para eliminar el ruido indeseado que pueda existir en las señales, para conformación espectral en la ecualización de canales de comunicación, en la detección de señales de radar, sonar y de comunicaciones y para realizar el análisis espectral de señales, etc. Por lo tanto, seleccionando adecuadamente los coeficientes, se puede diseñar filtros selectivos de frecuencia que dejan pasar señales con componentes de frecuencia en determinadas bandas mientras que atenúan señales que contienen frecuencias en otras bandas. Normalmente, los filtros se clasifican de acuerdo con sus características en el dominio de la frecuencia como filtros paso bajo, paso alto, paso banda, banda eliminada y paso todo [3].
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/paso.png" alt="Descripción de la imagen" width="300"><br> 
<p align="center"><b>Figura 1.</b> Módulo de las respuestas de algunos filtros discretos en el tiempo y selectivos en frecuencia [3]. <br> 

<p align="justify">Sin embargo, también es conveniente subdividir la clase de sistemas lineales invariantes en el tiempo en dos tipos: aquellos que tienen una repuesta al impulso de duración finita (FIR) y aquellos que tienen una respuesta al impulso de duración infinita (IIR). En la práctica, los filtros FIR se emplean en problemas de filtrado en los que se precisa una característica de fase dentro de la banda de paso del filtro. Si no se necesita esta característica de fase lineal, puede emplearse un filtro IIR o FIR. Por regla general, un filtro IIR tiene lóbulos secundarios más pequeños en la banda eliminada que un filtro FIR con el mismo número de parámetros. Por esta razón, si es tolerable cierta distorsión, es preferible un filtro IIR, principalmente porque su implementación precisa muy pocos parámetros, requiere menos memoria y presenta menos complejidad de cálculo [3].

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/filtro.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 2.</b> Módulo de los filtros físicamente realizables [3]. <br> 
   
<p align="justify">En este laboratorio, se abordará el diseño de filtros IIR por medio de transformación bilineal. Hay varios tipos comunes de filtros analógicos: Butterworth, que tienen bandas de paso máximamente planas en filtros del mismo orden, Chebyshev tipo I que son equivariables en la banda de paso, Chebyshev tipo II que son equivariables en la banda de parada, y filtros elípticos que son equivariables tanto en la banda de paso y la banda de parada. La versión digital de estos se puede obtener a partir de diseños analógicos a través de la transformación bilineal [4]. En comparación, para FIR, las técnicas de diseño para filtros digitales, se trabajarán con el método de ventana, el cual comienza con una respuesta de muestra unitaria deseada que luego se trunca mediante una ventana de duración finita [5]. Los distintos tipos de filtro FIR e IIR son visualizados a continuación.

<div style="text-align: center;">
      <p align="center">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/iir.png" alt="Descripción de la primera imagen" width="300">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/vent.png" alt="Descripción de la primera imagen" width="550">
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

<p align="justify"> En el caso de este trabajo, el filtrado de la señal ECG se realizó utilizando el trabajo de Basu et al para el filtrado IIR[15], y el trabajo de Kumar et al [16] para el filtrado FIR. Se utilizó un filtro Chebyshev I pasabajo de orden 4 con filtro en 40 Hz, y un filtro Kaiser con ventana de orden 56, una frecuencia de corte de 40 y un beta de 6. Debido a que el filtro pasabajos se encuentra por debajo de la frecuencia de interferencia eléctrica (60 Hz), no es necesario implementar un notch en la frecuencia.


#### EMG
<p align="justify">La señal electromiográfica de superficie que se origina en el músculo está inevitablemente contaminada por varias señales de ruido que se originan en la interfaz piel-electrodo, en la electrónica que amplifica las señales, y en fuentes externas. Los dispositivos son sustancialmente inmunes a algunos de estos ruidos, pero no al ruido de referencia y al ruido de artefacto de movimiento. Estas fuentes de ruido tienen espectros de frecuencia que contaminan la parte de baja frecuencia de espectro de frecuencia. Hay muchos factores que deben tenerse en cuenta al determinar las especificaciones de filtro adecuadas para eliminar estos artefactos; Incluyen el músculo probado y el tipo de contracción, la configuración del sensor y la fuente de ruido específica. La determinación del paso de banda es siempre un compromiso entre (a) reducir el ruido y la contaminación por artefactos, y (b) preservar la información deseada [8].

<p align="justify">Para reducir este ruido se consideraron las siguientes características en el filtrado:
   
<p align="justify">Se realizó el filtrado IIR de acuerdo a las especificaciones del trabajo realizado por Mello et al[17]. El filtro realizado fue la combinación de varios filtros de Buttersworth. Un filtro pasaalto de segundo orden con una frecuencia de corte de 10 Hz, un filtro pasabajo de 400 Hz de frecuencia de corte, y 6 filtros rechazabanda de segundo orden con bandas de rechazo cercanas las armónicas de 60 Hz hasta los 400 Hz (59-61, 119-121, 179-181, etc)[17].

<p align="justify">Por otro lado, la literatura es más vaga en lo referente a filtros FIR para EMG. Si bien se menciona el uso del filtro de ventana de Bartlett en un estudio[18], este carece de la información requerida para reproducirlo. Por tanto se utiliza el método de ventana de Hamming con los parámetros sugeridos.

<b>Diseñar un filtro FIR:</b>
- Métodos de ventana: Hamming, Blackman.
- Objetivo: Aislar la banda de frecuencia de interés que corresponde a la actividad muscular.
- Especificaciones sugeridas: Fc = 40 Hz, paso banda bajo.

<p align="justify">Como las señales EMG tienen una amplitud muy baja, es necesario amplificarlas con una ganancia de 1000x a una escala que es menos sensible al ruido y puede ser procesada adicionalmente por un convertidor analógico a digital. Para eliminar fuentes de ruido no deseadas o limitar la salida del sensor, también es útil filtrar la señal a una banda de frecuencia específica de interés que aún contiene toda la información de señales musculares como 20-450 Hz que se usa típicamente para superficie EMG. [9]

#### EEG
<p align="justify">Las fuentes de ruido también se manifiestan como frecuencias oscilantes que son captadas por el EEG. El ruido de baja frecuencia proviene de fuentes como el movimiento de la cabeza y los cables de los electrodos, y la transpiración en el cuero cabelludo. Este aparece como derivas lentas en la señal del EEG durante muchos segundos. Por el contrario, el ruido de alta frecuencia proviene de fuentes que incluyen interferencias electromagnéticas y contracciones musculares. Este parece cambios rápidos de arriba a abajo (como los dientes de una sierra) en el EEG. La frecuencia de las fuentes de ruido de alta y baja frecuencia puede superponerse con la banda de interés del EEG de 1-30 Hz, pero en general tienden a ser más bajas y más altas, respectivamente, que el EEG humano. Esto significa que al reducir la potencia de la señal en las frecuencias por encima y por debajo del rango de interés experimental, podemos reducir el ruido con un impacto mínimo en las señales de interés. [10]

<p align="justify">Para reducir este ruido se consideraron las siguientes características en el filtrado:

<p align="justify">El filtrado de EEG fue realizado de acuerdo a las conclusiones de los estudios realizados por Anshul et al para el filtro FIR [13] y Rayhan et al para el filtro IIR [14]. Para el filtro FIR se utilizó un filtro Kaiser de orden 4 y frecuencia de corte de 50 Hz, y un filtro Chebyshev tipo II de orden 4 pasabanda con frecuencias de corte de 12.5-17.5 Hz. En ambos casos se utilizó un filtrado notch de la frecuencia de 60 Hz

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
| Basal | ![Imagen de ECG](plots/2nd-try/ECG-rest-unfiltered.png) | ![Imagen de ECG](plots/2nd-try/ECG-rest-IIR.png) | ![Imagen de ECG](plots/2nd-try/ECG-rest-FIR.png) |
| Respiración | ![Imagen de ECG](plots/ecg-respiracion-cruda.png) | ![Imagen de ECG](plots/ecg-respiracion-IIR.png) | ![Imagen de ECG](plots/ecg-respiracion-FIR.png) |
| Ejercicio | ![Imagen de ECG](plots/2nd-try/ECG-exercise-unfiltered.png) | ![Imagen de ECG](plots/2nd-try/ECG-exercise-IIR.png) | ![Imagen de ECG](plots/2nd-try/ECG-exercise-FIR.png) |

#### Tabla resumen EMG 
| Estado | Señal cruda | Filtro IIR | Filtro FIR |
| ------------ | -------------- | ------------------ | ------------------ |
| Reposo | ![Imagen de EMG](plots/2nd-try/EMG-rest-unfiltered.png) | ![Imagen de EMG](plots/2nd-try/EMG-rest-IIR.png) | ![Imagen de EMG](plots/2nd-try/EMG-rest-FIR.png) |
| Flexión isotónica | ![Imagen de EMG](plots/2nd-try/EMG-flexion-unfiltered.png) | ![Imagen de EMG](plots/2nd-try/EMG-flexion-IIR.png) | ![Imagen de EMG](plots/2nd-try/EMG-flexion-FIR.png) |
| Flexión isométrica | ![Imagen de EMG](plots/2nd-try/EMG-isometric-unfiltered.png) | ![Imagen de EMG](plots/2nd-try/EMG-isometric-IIR.png) | ![Imagen de EMG](plots/2nd-try/EMG-isometric-FIR.png) |

#### Tabla resumen EEG 
| Estado | Señal cruda | Filtro IIR | Filtro FIR |
| ------------ | -------------- | ------------------ | ------------------ |
| Reposo | ![Imagen de EEG](plots/EEG-base1-o.png) | ![Imagen de EEG](plots/EEG-base1-IIR.png) | ![Imagen de EEG](plots/EEG-base1-FIR.png) |
| Apertura y cierre de ojos | ![Imagen de EEG](plots/EEG-abc-o.png) | ![Imagen de EEG](plots/EEG-abc-IIR.png) | ![Imagen de EEG](plots/EEG-abc-FIR.png) |
| Resolución de ejercicios matemáticos | ![Imagen de EEG](plots/EEG-eje-o.png) | ![Imagen de EEG](plots/EEG-eje-IIR.png) | ![Imagen de EEG](plots/EEG-eje-FIR.png) |

### Discusión
<p align="justify"><b>Filtración de ECG:</b>
<p align="justify"> En ambos casos se observa un suavizado de la señal con una desaparición del ruido de scattering que se superpone al las ondas. Diversas configuraciones de filtrado de frecuencias elevadas afectan los componentes de la señal ECG, tal y como lo describe Basu et al. Frecuencias de corte muy bajas como 20Hz  resultan en un complejo QRS irreconocible, mientras que órdenes bajos en el filtro resultan en pérdida de la señal de la onda T [15]. En ambos casos no ha sido posible eliminar el ruido que rodea a la onda P, ya que este tiene una frecuencia baja que no es eliminada por el filtro pasabaja.
<p align="justify"><b>Filtración de EMG:</b>
<p align="justify"> Debido a que las aplicaciones de la señal de EMG de superficie rara vez involucran diagnóstico de patologías musculares, para las cuales se utilizan métodos más precisos como la EMG de aguja, el filtrado de posibles artefactos ocasionados por el movimiento, interferencias de otras señales como el ECG, interferencias de línea eléctrica entre otros [12], el filtrado de frecuencias contaminantes toma un rol más importante dependiendo del uso de la sEMG, como en el caso de uso de prótesis, para la cual se requeriría filtrar de acuerdo al umbral usado.   
<p align="justify"><b>Filtración de EEG:</b>
<p align="justify">Los resultados para el EEG no fueron satisfactorios. Si bien se puede observar el resultado del filtrado en el espectro de la frecuencia,los cambios ocasionados por los filtros en la señal en el tiempo son muy variados en efectividad de acuerdo al momento evaluado. Asimismo, hubieron problemas relacionados a la interpretación. Se utilizaron señales del Ultracortex Mk IV. Los datos en el dominio del tiempo presentan amplitudes que no corresponden a los parámetros obtenidos. Si bien se intentó normalizar la data a valores conocidos (-15-15 uV), la gran variabilidad de datos no permitió obtener una respuesta estable en las señales estudiadas. Si bien en teoría el filtro IIR que es un filtro pasabanda debería resaltar las frecuencias correspondientes al patrón beta, esto no es visible en el dominio del tiempo. Una segunda dificultad concierne a la forma realizada por el estudio, en la cual no es posible determinar la zona cerebral sensada por el electrodo utilizado, por tanto tampoco es posible determinar la efectividad de la señal basados en la misma. En este caso, el filtro IIR filtra una banda de frecuencias correspondientes al ritmo beta, por lo que en teoría tras aplicar el filtro debería poder observarse una mayor nitidez de la señal filtrada en el dominio de la frecuencia.  </b>
   
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
<p align="justify">[12] M. Boyer, L. Bouyer, J.-S. Roy, and Alexandre Campeau-Lecours, “Reducing Noise, Artifacts and Interference in Single-Channel EMG Signals: A Review,” Sensors, vol. 23, no. 6, pp. 2927–2927, Mar. 2023, doi: https://doi.org/10.3390/s23062927.
<p align="justify">[13] Anshul Khatter, D. Bansal, and R. Mahajan. Performance Analysis of IIR & FIR Windowing Techniques in Electroencephalography Signal Processing, IJITEE, vol. 8, n.o 10, pp. 3568-3578, ago. 2019, doi: 10.35940/ijitee.J9771.0881019.
<p align="justify">[14] Rayhan Habib Jibon, Etu Podder, Abdullah Al-Mamun Bulbul, Ramendra Nath Bairagi, Md. Salim Ahmed, and Imtiaj Ahmmed Shohagh, “Performance analysis of IIR filter in removing PLI from EEG signal,” International Journal of Engineering & Technology, vol. 7, no. 4, pp. 5363–5367, 2018, doi: https://doi.org/10.14419/ijet.v7i4.26715.
<p align="justify">[15] S. Basu y S. Mamud, «Comparative Study on the Effect of Order and Cut off Frequency of Butterworth Low Pass Filter for Removal of Noise in ECG Signal», en 2020 IEEE 1st International Conference for Convergence in Engineering (ICCE), Kolkata, India: IEEE, sep. 2020, pp. 156-160. doi: 10.1109/ICCE50343.2020.9290646.
<p align="justify">[16] K. S. Kumar, B. Yazdanpanah and P. R. Kumar, "Removal of noise from electrocardiogram using digital FIR and IIR filters with various methods," 2015 International Conference on Communications and Signal Processing (ICCSP), Melmaruvathur, India, 2015, pp. 0157-0162, doi: 10.1109/ICCSP.2015.7322780.
<p align="justify">[17] R. G. T. Mello, L. F. Oliveira, y J. Nadal, «Digital Butterworth filter for subtracting noise from low magnitude surface electromyogram», Computer Methods and Programs in Biomedicine, vol. 87, n.º 1, pp. 28-35, jul. 2007, doi: 10.1016/j.cmpb.2007.04.004.
<p align="justify">[18] Hemant kumar and Anjana Goen (2015); Comparative Study of FIR Digital Filter for Noise Elimination in EMG Signal Int. J. of Adv. Res. 3 (Dec). 598-603] (ISSN 2320-5407). www.journalijar.com