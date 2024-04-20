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
4. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#bibliograf%C3%ADa)

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
<p align="center"><b>Figura 2.</b> Colocación de electrodos para la derivación I: IN+ (rojo) e IN-(negro) en las muñecas y REF (blanco) en la cresta ilíaca. [1] <br> <br> 

<p align="justify">El protocolo seguido para evaluar el latido del corazón en vivo con electrocardiografía fue el de la guía experimental de BITalino [1]: <br>
<ol>
  <li>Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal) durante 30 segundos.</li>
  <li>Repetir un ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER tres veces, manteniendo la respiración y fases de reposo durante cinco segundos.</li>
  <li> Registrar otra fase inicial de 30 segundos.</li>
  <li> Realizar 10 burpees y observa tu frecuencia cardíaca antes y después del entrenamiento.</li>
  <li> Registrar otra fase inicial de 30 segundos.</li>
  <li> Realizar una inhalación larga (~10 segundos) seguida de contener la respiración durante varios segundos (~10 segundos).</li>
</ol>

Adicionalmente, se incorporó la simulación de un paro cardíaco haciendo uso del ProSim 4 - Vital signs simulator. Como puede observarse en la figura 3, hubo una equivocación en la colocación de los electrodos, ya que 
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/fluke.jpg" alt="Descripción de la imagen" width="300"><br> 
<b>Figura 3.</b> Conexiones de los cables del electrodo en el Fluke. <br> 

### Resultados
- <p align="justify"><b>Respiración normal:</b>
- <p align="justify"><b>Ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER:</b>
- <p align="justify"><b>Respiración normal:</b>
- <p align="justify"><b>Frecuencia cardíaca antes y después del entrenamiento:</b>
- <p align="justify"><b>Respiración normal:</b>
- <p align="justify"><b>Ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER largo:</b>
- <p align="justify"><b>Simulación de un paro cardíaco:</b>

#### Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenSignals
- <p align="justify">Protocolo seguido para evaluar el latido del corazón en vivo con electrocardiografía.
- <p align="justify">Simulación de un paro cardíaco.

#### Archivo de los datos de la señal ploteada
#### Ploteo de las señales en Python

### Bibliografía 
<p align="justify">[1] BITalino (r)evolution Home Guide. PLUX-Wireless Biosignals, S A. Lisbon Portugal 2020. Available at: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf
