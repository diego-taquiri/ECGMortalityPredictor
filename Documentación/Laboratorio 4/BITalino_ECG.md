# Uso de BITalino para ECG
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro  

## Tabla de contenidos
1. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
2. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#materiales-y-m%C3%A9todos)
3. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#resultados)
   - [Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenSignals](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#videos-mostrando-las-conexiones-electrodos-cuerpo-y-la-se%C3%B1al-ploteada-en-opensignals)
   - [Archivo de los datos de la señal ploteada](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#archivo-de-los-datos-de-la-se%C3%B1al-ploteada)
   - [Ploteo de las señales en Python](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#ploteo-de-las-se%C3%B1ales-en-python)
4. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#discusi%C3%B3n)
5. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#bibliograf%C3%ADa)

### Objetivos específicos de la práctica
- Adquirir señales biomédicas de ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales ECG del software OpenSignals (r)evolution.

### Materiales y métodos
<p align="justify">Se realizó la medición de ECG de acuerdo a las instrucciones de la guía experimental de BITalino sobre electromiografía. [1] La medición se realizó utilizando un cable de electrodo de tres derivaciones conectado al terminal del BITalino correspondiente a ECG (Figura 1). <br>
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/BITalino.jpg" alt="Descripción de la imagen" width="300"><br> 
<b>Figura 1.</b> Conexiones de los cables del electrodo en el BITalino. <br> 

<p align="justify"> Una posible configuración del sensor de ECG BITalino para Einthoven Lead I es posicionando los electrodos positivo y negativo en las muñecas, mientras que el de referencia sobre la cresta ilíaca. [1] Las posiciones pueden observarse en la figura 2. <br> 

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/position.jpg" alt="Descripción de la imagen" width="300"><br> 
<p align="center"><b>Figura 2.</b> Colocación de electrodos para la derivación I: IN+ (rojo) e IN-(negro) en las muñecas y REF (blanco) en la cresta ilíaca. [1] <br> 

<p align="justify">El protocolo seguido para evaluar el latido del corazón en vivo con electrocardiografía fue el de la guía experimental de BITalino [1]: <br>
<ol>
  <li>Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal) durante 30 segundos.</li>
  <li>Repetir un ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER tres veces, manteniendo la respiración y fases de reposo durante cinco segundos.</li>
  <li> Registrar otra fase inicial de 30 segundos.</li>
  <li> Realizar 10 burpees y observa tu frecuencia cardíaca antes y después del entrenamiento.</li>
  <li> Registrar otra fase inicial de 30 segundos.</li>
  <li> Realizar una inhalación larga (~10 segundos) seguida de contener la respiración durante varios segundos (~10 segundos).</li>
</ol>

Adicionalmente, se incorporó la simulación de un paro cardíaco haciendo uso del ProSim 4 - Vital signs simulator. Como puede observarse en la figura 3, hubo una equivocación en la colocación de los electrodos, lo cual podría afectar la calidad de la señal registrada y la interpretación de los datos. 
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/fluke.jpg" alt="Descripción de la imagen" width="400"><br> 
<b>Figura 3.</b> Conexiones de los cables del electrodo en el FLUKE. <br> 

Siendo las autosecuencias una serie de pasos que cambian la salida del producto automáticamente, se tiene la siguiente tabla que representa los 5 pasos antes de producirse un paro cardíaco. [2]

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/heartf.png" alt="Descripción de la imagen" width="400"><br> 
<b>Figura 4.</b>Secuencia de parada cardíaca. [2] <br> 

Asimismo, se puede observar lo descrito en esta tabla en el mismo FLUKE (Figura 5). Esta simulación fue posteriormente visualizada en el OpenSignals a través del BITalino.

<div style="text-align: center;">
      <p align="center">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/step1.jpg" alt="Descripción de la primera imagen" width="200">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/step2.jpg" alt="Descripción de la primera imagen" width="200">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/step3.jpg" alt="Descripción de la primera imagen" width="200">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/step4.jpg" alt="Descripción de la primera imagen" width="200">
</div>
<p align="center"><b>Figura 5.</b> Secuencia de parada cardíaca: (a)CVP, (b) Taquicardia ventricular, (c) Fibrilación ventricular severa y (d) Asistolia. <br> 

### Resultados
#### Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenSignals
- <p align="justify">Protocolo seguido para evaluar el latido del corazón en vivo con electrocardiografía.
- <p align="justify">Simulación de un paro cardíaco.

#### Archivo de los datos de la señal ploteada
#### Ploteo de las señales en Python

### Discusión
- <p align="justify"><b>Respiración normal:</b>
- <p align="justify"><b>Ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER:</b>
- <p align="justify"><b>Respiración normal:</b>
- <p align="justify"><b>Frecuencia cardíaca antes y después del entrenamiento:</b>
- <p align="justify"><b>Respiración normal:</b>
- <p align="justify"><b>Ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER largo:</b>
- <p align="justify"><b>Simulación de un paro cardíaco:</b> 

### Bibliografía 
<p align="justify">[1] BITalino (r)evolution Home Guide. PLUX-Wireless Biosignals, S A. Lisbon Portugal 2020. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf
<p align="justify">[2] Users Manual, “Vital Signs Simulator”, Flukebiomedical.com. [En línea]. Disponible en: https://www.flukebiomedical.com/sites/default/files/resources/Pro4____umeng0300.pdf.
