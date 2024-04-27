# Uso de BITalino para ECG
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro  

## Tabla de contenidos
1. [Introducción](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/BITalino_ECG.md#introducci%C3%B3n)
2. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#materiales-y-m%C3%A9todos)
4. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#resultados)
   - [Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenSignals](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#videos-mostrando-las-conexiones-electrodos-cuerpo-y-la-se%C3%B1al-ploteada-en-opensignals)
   - [Archivo de los datos de la señal ploteada](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#archivo-de-los-datos-de-la-se%C3%B1al-ploteada)
   - [Ploteo de las señales en Python](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#ploteo-de-las-se%C3%B1ales-en-python)
5. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#discusi%C3%B3n)
6. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/BITalino_ECG.md#bibliograf%C3%ADa)

### Introducción

### Objetivos específicos de la práctica
- Adquirir señales biomédicas de ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales ECG del software OpenSignals (r)evolution.

### Materiales y métodos
<p align="justify">Se realizó la medición de EEG de acuerdo a las instrucciones de la guía experimental de BITalino sobre bioseñales. [2] La medición se realizó utilizando un cable de electrodo de tres derivaciones conectado al terminal del BITalino correspondiente a EEG (Figura 1). <br>
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%205/Images/bitalino.jpg" alt="Descripción de la imagen" width="300"><br> 
<b>Figura 1.</b> Conexiones de los cables del electrodo en el BITalino. <br> 

<p align="justify"> Una posible configuración del sensor de ECG BITalino para Einthoven Lead I es posicionando los electrodos positivo y negativo en las muñecas, mientras que el de referencia sobre la cresta ilíaca. [2] Las posiciones pueden observarse en la figura 2. <br> 

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/position.jpg" alt="Descripción de la imagen" width="300"><br> 
<p align="center"><b>Figura 2.</b> Colocación de electrodos para la derivación I: IN+ (rojo) e IN-(negro) en las muñecas y REF (blanco) en la cresta ilíaca. [2] <br> 

<p align="justify">El protocolo seguido para evaluar el latido del corazón en vivo con electrocardiografía fue el de la guía experimental de BITalino [21]: <br>
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
<b>Figura 4.</b> Secuencia de parada cardíaca. [3] <br> 

Asimismo, se puede observar lo descrito en esta tabla en el mismo FLUKE (Figura 5). Esta simulación fue posteriormente visualizada en el OpenSignals a través del BITalino.

<div style="text-align: center;">
      <p align="center">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/step1.jpg" alt="Descripción de la primera imagen" width="200">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/step2.jpg" alt="Descripción de la primera imagen" width="200">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/step3.jpg" alt="Descripción de la primera imagen" width="200">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%204/images/step4.jpg" alt="Descripción de la primera imagen" width="200">
</div>
<p align="center"><b>Figura 5.</b> Secuencia de parada cardíaca: (a) CVP, (b) Taquicardia ventricular, (c) Fibrilación ventricular severa y (d) Asistolia. <br> 

### Resultados
#### Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenSignals
- <p align="justify">Protocolo seguido para evaluar el latido del corazón en vivo con electrocardiografía.

| Protocolo | Conexiones electrodos-cuerpo | Señal ploteada en OpenSignals |
| --------- | --------- | --------- |
| Respiración normal| <p align="center"><a href="https://youtu.be/8PnidbbtLkQ"><img src="https://img.youtube.com/vi/8PnidbbtLkQ/0.jpg" alt="Miniatura del video" width="350"></a></p> | Texto     |
| Ciclo de INHALACIÓN-EXHALACIÓN largo| <p align="center"><a href="https://youtu.be/u8qXzgWzAVI"><img src="https://img.youtube.com/vi/u8qXzgWzAVI/0.jpg" alt="Miniatura del video" width="350"></a></p> | Texto     |
| Fase inicial de 30 segundos| <p align="center"><a href="https://youtu.be/9TthaNQQPNw"><img src="https://img.youtube.com/vi/9TthaNQQPNw/0.jpg" alt="Miniatura del video" width="350"></a></p> | Texto     |
| 10 burpees| <p align="center"><a href="https://youtu.be/GUYjouPUTFM"><img src="https://img.youtube.com/vi/GUYjouPUTFM/0.jpg" alt="Miniatura del video" width="350"></a></p> | Texto     |
| Fase inicial de 30 segundos después de los burpees| <p align="center"><a href="https://youtu.be/IL7Me2n_vhA"><img src="https://img.youtube.com/vi/IL7Me2n_vhA/0.jpg" alt="Miniatura del video" width="350"></a> | Texto     |
| Ciclo de INHALACIÓN-EXHALACIÓN largo| <p align="center"><a href="https://youtu.be/av1N9T9M1a4"><img src="https://img.youtube.com/vi/av1N9T9M1a4/0.jpg" alt="Miniatura del video" width="350"></a></p> | Texto     |
<p align="center"><b>Tabla 1.</b> Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenSignals del protocolo. <br> 

- <p align="justify">Simulación de un paro cardíaco.

<div align="center">
<table>
  <tr>
    <th>Protocolo</th>
    <th>Conexiones electrodos-cuerpo</th>
    <th>Señal ploteada en OpenSignals</th>
  </tr>
  <tr>
    <td>Simulación de un paro cardíaco</td>
    <td align="center"><a href="https://www.youtube.com/watch?v=9JaGJ30xAS8"><img src="https://img.youtube.com/vi/9JaGJ30xAS8/0.jpg" alt="Miniatura del video" width="350"></a></td>
    <iframe width="560" height="315" src="https://www.youtube.com/watch?v=9JaGJ30xAS8" frameborder="0" allowfullscreen></iframe>
    <td>Texto</td>
  </tr>
</table>
</div>

#### Archivo de los datos de la señal ploteada
- [ECG raw data](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%204/ecg_raw_data)

#### Ploteo de las señales en Python
- <p align="justify">Protocolo seguido para evaluar el latido del corazón en vivo con electrocardiografía.
<div>
    <table style="width:100%;">
        <tr>
            <th>Reposo</th>
        </tr>
        <tr>
            <td><img src="plots/ecg-reposo.png" style="width:100%;"></td>
        </tr>
        <tr>
            <th>Respiración</th>
        </tr>
        <tr>
            <td><img src="plots/ecg-respiracion.png" style="width:100%;"></td>
        </tr>
        <tr>
            <th>Ejercicio</th>
        </tr>
        <tr>
            <td><img src="plots/ecg-ejericicio.png" style="width:100%;"></td>
        </tr>
    </table>
</div>
<p align="center"><b>Tabla 3.</b> Ploteo del protocolo en Python. <br> 

- <p align="justify">Simulación de un paro cardíaco.
<div>
    <table style="width:100%;">
        <tr>
            <th style="width:50%;">CVP</th>
            <th style="width:50%;">Taquicardia ventricular</th>
        </tr>
        <tr>
            <td><img src="plots/ecg-paro_cardiaco-1.png" style="width:100%;"></td>
            <td><img src="plots/ecg-paro_cardiaco-2.png" style="width:100%;"></td>
        </tr>
        <tr>
            <th style="width:50%;">Fibrilación ventricular severa</th>
            <th style="width:50%;">Asistolia</th>
        </tr>
        <tr>
            <td><img src="plots/ecg-paro_cardiaco-3.png" style="width:100%;"></td>
            <td><img src="plots/ecg-paro_cardiaco-4.png" style="width:100%;"></td>
        </tr>
    </table>
</div>
<p align="center"><b>Tabla 4.</b> Ploteo de la simulación de un paro cardíaco en Python. <br> 

### Discusión
<p align="justify"><b>Respiración normal:</b>
<p align="justify">Durante la respiración normal, se ve una variación rítmica en el ECG debido a la influencia del sistema nervioso autónomo en el corazón. Esto se manifiesta como un aumento en la frecuencia cardíaca durante la inhalación y una disminución durante la exhalación. Pese al ruido es posible identificar características de la onda de ECG que permiten observar su ritmicidad. Los picos elevados del complejo QRS y una elevación posterior que puede corresponder a la onda T pero es irregular debido al ruido.  <br> 
<p align="justify"><b>Ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER (5 segundos):</b>
<p align="justify">El proceso de inhalar, mantener el aire inspirado y exhalar es conocido como maniobra de Valsalva. La respuesta del ECG a la ejecución de la maniobra se manifiesta como una bradicardia compensatoria al incremento de la presión intratorácica en la inspiración, una taquicardia transitoria ocasionada por inhibición vagal y estimulación simpática en el esfuerzo de mantener inspiración y una bradicardia refleja al incremento de presión arterial en la espiración [4]. En la toma de la muestra en este periodo se puede observar un periodo central en el cual los picos del complejo QRS se encuentran más próximos rodeado de periodos en los que los picos están espaciados. Estos cambios son dificiles de cuantificar debido a la incertidumbre de la onda debido al ruido. [3] <br> 
<p align="justify"><b>Fase inicial antes del entrenamiento - frecuencia cardíaca:</b>
<p align="justify">La frecuencia cardíaca en reposo puede variar significativamente entre personas y se ve influenciada por factores como la edad, el nivel de condición física, el estado emocional y la salud cardiovascular general. Una frecuencia cardíaca en reposo más baja generalmente se asocia con una mejor condición física y una función cardiovascular más eficiente.[5] <br> 
<p align="justify"><b>Fase inicial después del entrenamiento - frecuencia cardíaca:</b>
<p align="justify">Durante el ejercicio intenso como los burpees, se ve un aumento sustancial en la frecuencia cardíaca y posiblemente en la amplitud y la forma de las ondas del ECG. Este aumento en la frecuencia cardíaca es una respuesta fisiológica normal al aumento de la demanda de oxígeno y energía durante el ejercicio. La literatura describe los cambios de la onda del ECG tras el ejercicio. Hay uan disminución del periodo entre la onda P y el complejo QRS, una ligera disminución de la amplitud de la onda R y un aumento de la onda S, particularmente visibles a frecuencias cardiacas elevadas y solo visible con ciertas derivaciones. [6] Existe una disminución en la variabilidad de la frecuencia cardíaca a medida que el sistema nervioso autónomo regresa a un estado de equilibrio. En el examen se aprecia el acercamiento de los picos R correspondientes a taquicardia, al igual que la visualización más clara de las ondas P y T. Otras características como las mencionadas previamente no se pueden apreciar. Cabe añadir que esta medición fue realizada después del ejercicio y no durante el mismo. <br> 
<p align="justify"><b>Ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER (10 segundos):</b>
<p align="justify">Un ciclo de respiración más prolongado puede tener efectos más pronunciados en la variabilidad del ritmo cardíaco. Durante la fase de inhalación profunda, es probable que veas un aumento en la frecuencia cardíaca debido a la activación del sistema nervioso simpático y la mayor demanda de oxígeno. Durante la fase de exhalación prolongada, es probable que observes una disminución en la frecuencia cardíaca a medida que el sistema nervioso parasimpático predomina y el cuerpo se relaja aún más. <br> 
<p align="justify"><b>Simulación de un paro cardíaco:</b> 
<p align="justify">Durante la simulación de paro cardíaco, vemos patrones anormales en el ECG que indican una función cardíaca comprometida. El ProSim4 genera 4 pulsos distintivos para representar un paro cardiaco, las CVP, la taquicardia ventricular, la fibrilacion ventricular severa y finalmente la asistolia:
   <li>Contracciones Ventriculares Prematuras (CVP):
      En esta fase, se observan irregularidades en el trazado del ECG que sugieren la presencia de contracciones prematuras de los ventrículos ocasionados por un daño en el nódulo sinoatrial. En el ECG se observan como un complejo QRS más ancho, un incremento de los intervalos RR y una desaparición de la onda P. [7] Esto se puede apreciar en el modelo del simulador, en el cual se pueden observar complejos QRS deformes y en ocasiones una onda P que cabalga al complejo QRS.
   <li>Taquicardia Ventricular:
      Durante la taquicardia ventricular, se ve un patrón de onda en el ECG que indica una rápida y descoordinada actividad eléctrica en los ventrículos. Esto se manifiesta como una serie de complejos QRS amplios y rápidos en el trazado del ECG.[8] En el simulador esto se observa como complejos QRS anchos, de menor amplitud y con una onda T que cabalga a la onda S. No se aprecia la onda P. 
   <li>Fibrilación Ventricular Severa:
      La fibrilación ventricular se caracteriza por la presencia de ondas irregulares y caóticas en el ECG, ocasionada por un remodelamiento eléctrico del corazón ocasionado por eventos cardiacos previos, que lleva a una repolarización insuficiente y subsecuente automaticidad ectópica. Esto se traduce en una ausencia de contracciones efectivas y puede resultar en una disminución significativa del gasto cardíaco y la perfusión de órganos vitales. [9] Esto es visible en el ECG simulado. No se puede apreciar ningun tipo de onda, el ECG aparece completamente errático, sin ningun tipo de periodicidad.
   <li>Asistolia:
      La asistolia se define como la ausencia total de actividad eléctrica en el corazón, lo que resulta en una línea plana en el trazado del ECG. Esta fase  representa hasta el 40-50% de causas de muerte súbita en adultos a nivel mundial y es secundario a daño estructural del miocardio. requiere intervención inmediata, como la administración de RCP y desfibrilación y en la mayoria de casos como este implica la muerte del paciente. [10] En el ECG observado se aprecia una linea plana, con cierto ruido leve pero sin ninguna de las características de la onda de ECG.
      
### Bibliografía 
<p align="justify">[1] M. AlGhatrif y J. Lindsay, «A brief review: history to understand fundamentals of electrocardiography», Journal of Community Hospital Internal Medicine Perspectives, vol. 2, n.o 1, p. 14383, ene. 2012, doi: 10.3402/jchimp.v2i1.14383.
<p align="justify">[2] BITalino (r)evolution Home Guide. PLUX-Wireless Biosignals, S A. Lisbon Portugal 2020. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf
<p align="justify">[3] Users Manual, “Vital Signs Simulator”, Flukebiomedical.com. [En línea]. Disponible en: https://www.flukebiomedical.com/sites/default/files/resources/Pro4____umeng0300.pdf.
<p align="justify">[4] S. Hosseini y M. Jamshir, «Valsalva maneuver and strain-related ECG changes», Res Cardiovasc Med, vol. 4, n.º 4, p. 8, 2015, doi: 10.5812/cardiovascmed.28136.
<p align="justify">[5] F. S. Martinelli et al., “Heart rate variability in athletes and nonathletes at rest and during head-up tilt,” Brazilian Journal of Medical and Biological Research, vol. 38, no. 4, pp. 639–647, Apr. 2005, doi: https://doi.org/10.1590/s0100-879x2005000400019.‌
<p align="justify">[6] J. Deckers, R. Vinke, J. Vos, and Maarten Simoons, “Changes in the electrocardiographic response to exercise in healthy women.,” Heart, vol. 64, no. 6, pp. 376–380, Dec. 1990, doi: https://doi.org/10.1136/hrt.64.6.376.‌
<p align="justify">[7] S. Sánchez-Morago. “CONTRACCIONES VENTRICULARES PREMATURAS : ¿SON TODAS IGUALES?” SEEUE - Sociedad Española de Enfermería de Urgencias y Emergencias. Accedido el 20 de abril de 2024. [En línea]. Disponible: https://www.enfermeriadeurgencias.com/ciber/PRIMERA_EPOCA/2006/octubre/contraccionesventriculares.htm
<p align="justify">[8] B. Benito y M. Josephson. “Taquicardia ventricular en la enfermedad coronaria | Revista Española de Cardiología”. Revista Española de Cardiología. Accedido el 20 de abril de 2024. [En línea]. Disponible: https://www.revespcardiol.org/es-taquicardia-ventricular-enfermedad-coronaria-articulo-S0300893212003284
<p align="justify">[9] Zoltán Szabó, Dóra Ujvárosy, Tamás Ötvös, V. Sebestyén, and P. P. Nánási, “Handling of Ventricular Fibrillation in the Emergency Setting,” Frontiers in pharmacology, vol. 10, Jan. 2020, doi: https://doi.org/10.3389/fphar.2019.01640.
<p align="justify">[10] H. Rodríguez-Reyes, Mayela Muñoz-Gutiérrez, and J. L. Salas-Pacheco, “Current behavior of sudden cardiac arrest and sudden death,” Deleted Journal, vol. 90, no. 2, Sep. 2020, doi: https://doi.org/10.24875/acme.m20000114.
