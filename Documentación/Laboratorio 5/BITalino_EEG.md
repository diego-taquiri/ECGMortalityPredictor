# Uso de BITalino para EEG
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro  

## Tabla de contenidos
1. [Introducción](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_EEG.md#introducci%C3%B3n)
2. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_EEG.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_EEG.md#materiales-y-m%C3%A9todos)
4. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_EEG.md#resultados)
   - [Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_EEG.md#videos-mostrando-las-conexiones-electrodos-cuerpo-y-la-se%C3%B1al-ploteada)
   - [Archivo de los datos de la señal ploteada](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_EEG.md#archivo-de-los-datos-de-la-se%C3%B1al-ploteada)
   - [Ploteo de las señales en Python](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_EEG.md#ploteo-de-las-se%C3%B1ales-en-python)
5. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_EEG.md#discusi%C3%B3n)
6. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_EEG.md#bibliograf%C3%ADa)

### Introducción
El EEG es una señal compleja, cuyas propiedades estadísticas dependen tanto del tiempo como del espacio. En cuanto a las características temporales, es esencial tener en cuenta que las señales de EEG están en constante cambio. [1]
El EEG registra la actividad eléctrica generada por las neuronas cerebrales, en forma de diferencias de potencial entre electrodos posicionados sobre el cuero cabelludo. Esta actividad es digitalizada, amplificada (en un adulto sano típicamente oscila entre 20-100 μV), filtrada para eliminar o reducir el ruido (generalmente de 0.3 a 70 Hz), y se muestra como formas de onda con morfologías y frecuencias variables. La interpretación de estas formas de onda generalmente se realiza mediante inspección visual, pero también puede llevarse a cabo mediante análisis cuantitativo de la frecuencia, amplitud, distribución topográfica, correlación cruzada y reactividad; estos análisis permiten una evaluación objetiva de la actividad cerebral. [2] 


### Objetivos específicos de la práctica
- Adquirir señales biomédicas de EEG.
- Hacer una correcta configuración del BiTalino y del UltraCortex.
- Extraer la información de las señales EEG de los softwares OpenSignals (r)evolution y OpenBCI GUI.
- Comprender el cambio de señal desencadenado por cambios de actividad neuronal.

### Materiales y métodos
<p align="justify">Se realizó la medición de EEG de acuerdo a las instrucciones de la guía experimental de BITalino sobre bioseñales. [3] La medición se realizó utilizando un cable de electrodo de tres derivaciones conectado al terminal del BITalino correspondiente a EEG (Figura 1). <br>
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/Images/bitalino.jpg" alt="Descripción de la imagen" width="300"><br> 
<p align="center"><b>Figura 1.</b> Conexiones de los cables del electrodo en el BITalino. <br> 

<p align="justify"> Una posible configuración del sensor de EEG BITalino es la de medición bipolar, la cual contiene dos electrodos de medición (IN + e IN-) y uno de referencia que debe ser conectado de manera adicional en una zona ósea. Siguiendo el sistema internacional 10-20, , el cual es el estándar aceptado internacionalmente para la colocación de electrodos en el contexto del EEG, se colocaron los dos electrodos de medición en FP1 con una distancia predefinida por los broches del sensor; mientras que el electrodo de referencia se colocó en una región neutra. [3] Las posiciones pueden observarse en la figura 2. <br> 

<div style="text-align: center;">
      <p align="center">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/Images/posicion1.png" alt="Descripción de la primera imagen" width="300" height="270">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/Images/colocacion.jpg" alt="Descripción de la primera imagen" width="300" height="270">
</div>
<p align="center"><b>Figura 2.</b> (a) Sistema internacional 10-20 para la (b) colocación de electrodos para la configuración de medición bipolar: electrodos de medición (IN + e IN-) y de referencia. [3] <br> 

<p align="justify">El protocolo seguido para evaluar el cambio de señal desencadenado por cambios de actividad neuronal fue el siguiente: <br>

<ol>
  <li>Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal, sin movimientos oculares/ojos cerrados) durante 30 segundos. </li>
  <li>Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos. </li>
  <li>Registrar otra fase de referencia de 30 segundos. </li>
  <li>Escuchar una serie de ejercicios matemáticos y resolver cada uno de ellos mentalmente enfocando la mirada en un punto específico para evitar artefactos. [4] </li>
</ol>

<p align="justify">Adicionalmente, siguiendo el sistema 10-20, también se incorporó el análisis de la actividad neuronal desde un UltraCortex Mark IV. Las imágenes a continuación indican las ubicaciones predeterminadas de 10 a 20 electrodos que espera la interfaz gráfica de usuario de OpenBCI. Utilizando el kit de investigación y desarrollo de 16 canales OpenBCI, los nodos azules indicaron las 8 ubicaciones predeterminadas (canales 1-8) de la placa Cyton; mientras que los rojos indicaron las de los canales 9-16. [5]

<p align="justify">Como puede observarse en la figura 3, algunos componentes no fueron conectados debido al mal estado con el que fue entregado el dispositivo. Asimismo, se incorporaron los dos electrodos de clip para la oreja, los cuales sirven como referencia y polarización (tierra con rechazo de ruido de modo común). [5]

<div style="text-align: center;">
      <p align="center">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/Images/tablar.png" alt="Descripción de la primera imagen" width="300" height="325">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/Images/ultracortex.jpg" alt="Descripción de la primera imagen" width="300" height="325">
</div>
<p align="center"><b>Figura 3.</b> Colocación del Ultracortex Mark IV siguiendo el sistema 10-20. [5] <br> 

<p align="justify">Realizando los cambios respectivos mediante el ajuste de los resortes al tamaño de la cabeza, se logró que el UltraCortex esté ubicado de modo que el nodo central posterior esté aproximadamente a la misma distancia, por encima del inion, que el nodo central frontal, el cual está por encima del puente de la nariz. [5]

<p align="justify">A continuación, se muestra una captura de pantalla de cómo se ve la GUI con el OpenBCI Cyton + Ultracortex (16 canales) conectado.<br>

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/Images/senal.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 4.</b> GUI con el OpenBCI Cyton + Ultracortex (16 canales). <br> 

### Resultados
#### Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada
- <p align="justify">Protocolo seguido para evaluar el cambio de actividad neuronal en OpenSignals. 

| Protocolo | Línea Base | Ciclo de ojos abiertos-cerrados | Fase de referencia | Ejercicios matemáticos |
| --------- | ---------- | ------------------------------ | ------------------ | ---------------------- |
| Conexiones electrodos-cuerpo | <p align="center"><a href="https://youtu.be/Aakm-yAOVgY"><img src="https://img.youtube.com/vi/Aakm-yAOVgY/0.jpg" alt="Miniatura del video" width="350"></a></p> | <p align="center"><a href="https://youtu.be/pgSb1oMOQ-0"><img src="https://img.youtube.com/vi/pgSb1oMOQ-0/0.jpg" alt="Miniatura del video" width="350"></a></p> | <p align="center"><a href="https://youtu.be/Bp8uORbIjmg"><img src="https://img.youtube.com/vi/Bp8uORbIjmg/0.jpg" alt="Miniatura del video" width="350"></a></p> | <p align="center"><a href="https://youtu.be/8Rho--2nGmg"><img src="https://img.youtube.com/vi/8Rho--2nGmg/0.jpg" alt="Miniatura del video" width="350"></a></p> |
| Señal ploteada en OpenSignals | Texto | Texto | Texto | Texto |
<p align="center"><b>Tabla 1.</b> Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenSignals del protocolo. <br> 

- <p align="justify">Protocolo seguido para evaluar el cambio de actividad neuronal en OpenBCI. 
   
| Protocolo | Línea Base | Ciclo de ojos abiertos-cerrados | Fase de referencia | Ejercicios matemáticos |
| :--------: | :--------: | :-----------------------------: | :----------------: | :--------------------: |
| Señal ploteada en OpenBCI | <p align="center"><a href="https://youtu.be/XvO9Swg0UOs"><img src="https://img.youtube.com/vi/XvO9Swg0UOs/0.jpg" alt="Miniatura del video" width="200"></a></p> | <p align="center"><a href="https://youtu.be/5O7GbBteY9w"><img src="https://img.youtube.com/vi/5O7GbBteY9w/0.jpg" alt="Miniatura del video" width="200"></a></p> | <p align="center"><a href="https://youtu.be/g9LNPO2JDDc"><img src="https://img.youtube.com/vi/g9LNPO2JDDc/0.jpg" alt="Miniatura del video" width="200"></a></p> | <p align="center"><a href="https://youtu.be/p1FOJwmLAsk"><img src="https://img.youtube.com/vi/p1FOJwmLAsk/0.jpg" alt="Miniatura del video" width="200"></a></p> |
<p align="center"><b>Tabla 2.</b> Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenBCI del protocolo. <br> 

#### Archivo de los datos de la señal ploteada
- [ECG raw data OpenSignals](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%205/Raw%20data/Raw%20Data%20Bitalino)
- [ECG raw data OpenBCI](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%205/Raw%20data/Raw%20Data%20UltraCortex)

#### Ploteo de las señales en Python
- <p align="justify">Protocolo seguido para evaluar el cambio de actividad neuronal en OpenSignals. 

<p align="center"><b>Tabla 3.</b> Ploteo del protocolo usando BITalino en Python. <br> 

- <p align="justify">Protocolo seguido para evaluar el cambio de actividad neuronal en OpenBCI. 

<p align="center"><b>Tabla 4.</b> Ploteo del protocolo usando UltraCortex en Python. <br> 

### Discusión

<p align="justify"><b>Línea Base - Respiración normal:</b>

<p align="justify"><b>Ciclo de OJOS ABIERTOS - OJOS CERRADOS:</b>

<p align="justify"><b>Fase de referencia:</b>

<p align="justify"><b>Ejercicios matemáticos:</b>
      
### Bibliografía 
<p align="justify">[1] Schomer, Donald L., and others, 'C44EEG Analysis: Theory and Practice', in Donald L. Schomer, and Fernando H. Lopes da Silva (eds), Niedermeyer's Electroencephalography: Basic Principles, Clinical Applications, and Related Fields, 7 edn (New York, 2017; online edn, Oxford Academic, 1 Nov. 2017), https://doi.org/10.1093/med/9780190228484.003.0044
<p align="justify">[2] Sewell L, Abbas A, Kane N. Introduction to interpretation of the EEG in intensive care. BJA Educ. 2019 Mar;19(3):74-82. doi: 10.1016/j.bjae.2018.11.002. Epub 2018 Dec 17. PMID: 33456874; PMCID: PMC7808102.
<p align="justify">[3] EXPERIMENTAL GUIDES TO MEET y L. Y. Biosignals, “BITalino (r)evolution Lab Guide”, Pluxbiosignals.com. [En línea]. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf
<p align="justify">[4] J. Molina del Río, M. A. Guevara, M. Hernández González, R. M. Hidalgo Aguirre, y M. A. Cruz Aguilar, “EEG correlation during the solving of simple and complex logical–mathematical problems”, Cogn. Affect. Behav. Neurosci., vol. 19, núm. 4, pp. 1036–1046, 2019.
<p align="justify">[5] “Ultracortex Mark IV”, Openbci.com, 2016. [En línea]. Disponible en: https://docs.openbci.com/AddOns/Headwear/MarkIV/
