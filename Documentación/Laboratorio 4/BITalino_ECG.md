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
<b>Figura 4.</b> Secuencia de parada cardíaca. [2] <br> 

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
    <td>Texto</td>
  </tr>
</table>
</div>
<p align="center"><b>Tabla 2.</b> Videos mostrando las conexiones electrodos-cuerpo y la señal ploteada en OpenSignals de la simulación de un paro cardíaco. <br> 

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
<p align="justify">Durante la respiración normal, se ve una variación rítmica en el ECG debido a la influencia del sistema nervioso autónomo en el corazón. Esto se manifiesta como un aumento en la frecuencia cardíaca durante la inhalación y una disminución durante la exhalación. <br> 
<p align="justify"><b>Ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER (5 segundos):</b>
<p align="justify">Durante la inhalación, es probable que veas un ligero aumento en la frecuencia cardíaca debido a la activación del sistema nervioso simpático, que prepara al cuerpo para la absorción de oxígeno. Durante la exhalación, es probable que la frecuencia cardíaca disminuya ligeramente a medida que el sistema nervioso parasimpático predomina, facilitando la relajación. Esta variabilidad en la frecuencia cardíaca es un indicador de un sistema nervioso autónomo saludable y una función cardiovascular adecuada. [3] <br> 
<p align="justify"><b>Fase inicial antes del entrenamiento - frecuencia cardíaca:</b>
<p align="justify">La frecuencia cardíaca en reposo puede variar significativamente entre personas y se ve influenciada por factores como la edad, el nivel de condición física, el estado emocional y la salud cardiovascular general. Una frecuencia cardíaca en reposo más baja generalmente se asocia con una mejor condición física y una función cardiovascular más eficiente.[4] <br> 
<p align="justify"><b>Fase inicial después del entrenamiento - frecuencia cardíaca:</b>
<p align="justify">Durante el ejercicio intenso como los burpees, se ve un aumento sustancial en la frecuencia cardíaca y posiblemente en la amplitud y la forma de las ondas del ECG. Este aumento en la frecuencia cardíaca es una respuesta fisiológica normal al aumento de la demanda de oxígeno y energía durante el ejercicio. Además, es posible observar cambios en la forma de onda del ECG debido al estrés físico inducido por el ejercicio, como una mayor variabilidad en el intervalo RR (intervalo entre latidos). [5] Después del ejercicio, esperarías ver una disminución gradual en la frecuencia cardíaca a medida que el cuerpo se recupera del esfuerzo. Durante esta fase, es posible que también observes una disminución en la variabilidad de la frecuencia cardíaca a medida que el sistema nervioso autónomo regresa a un estado de equilibrio. <br> 
<p align="justify"><b>Ciclo de INHALACIÓN-MANTENER-EXHALACIÓN-MANTENER (10 segundos):</b>
<p align="justify">Un ciclo de respiración más prolongado puede tener efectos más pronunciados en la variabilidad del ritmo cardíaco. Durante la fase de inhalación profunda, es probable que veas un aumento en la frecuencia cardíaca debido a la activación del sistema nervioso simpático y la mayor demanda de oxígeno. Durante la fase de exhalación prolongada, es probable que observes una disminución en la frecuencia cardíaca a medida que el sistema nervioso parasimpático predomina y el cuerpo se relaja aún más. <br> 
<p align="justify"><b>Simulación de un paro cardíaco:</b> 
<p align="justify">Durante la simulación de paro cardíaco, vemos patrones anormales en el ECG que indican una función cardíaca comprometida. El ProSim4 genera 4 pulsos distintivos para representar un paro cardiaco, el CVP, la taquicardia ventricular, la fibrilacion ventricular severa y finalmente la asistolia:
   <li>Fase de CVP (Compresión Ventricular Prematura):
      En esta fase, se observan irregularidades en el trazado del ECG que sugieren la presencia de contracciones prematuras de los ventrículos. Estas                    contracciones pueden ocurrir fuera del ritmo cardíaco normal y podrían indicar una disfunción eléctrica del corazón. [6]
   <li>Fase de Taquicardia Ventricular:
      Durante la taquicardia ventricular, se ve un patrón de onda en el ECG que indica una rápida y descoordinada actividad eléctrica en los ventrículos.                Esto se manifestaría como una serie de complejos ventriculares amplios y rápidos en el trazado del ECG. Este tipo de arritmia puede llevar a una fibrilacion       auricular, lo cual coincide con la siguiente fase que tiene programada el ProSim . [7]
   <li>Fase de Fibrilación Auricular Severa:
      La fibrilación auricular severa se caracteriza por la presencia de ondas irregulares y caóticas en el ECG, que reflejan una actividad eléctrica                    desorganizada en las aurículas. Esto se traduce en una ausencia de contracciones auriculares efectivas y puede resultar en una disminución significativa           del gasto cardíaco y la perfusión de órganos vitales. [8]
   <li>Fase de Asistolia:
      La asistolia se define como la ausencia total de actividad eléctrica en el corazón, lo que resulta en una línea plana en el trazado del ECG. Esta fase             representa una emergencia médica grave y requiere intervención inmediata, como la administración de RCP y desfibrilación y en la mayoria de casos como este        implica la muerte del paciente. [9]
      
### Bibliografía 
<p align="justify">[1] BITalino (r)evolution Home Guide. PLUX-Wireless Biosignals, S A. Lisbon Portugal 2020. Disponible en: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf
<p align="justify">[2] Users Manual, “Vital Signs Simulator”, Flukebiomedical.com. [En línea]. Disponible en: https://www.flukebiomedical.com/sites/default/files/resources/Pro4____umeng0300.pdf.
<p align="justify">[3] “Cómo el cuerpo controla la respiración”. NHLBI, NIH. Accedido el 20 de abril de 2024. [En línea]. Disponible: https://www.nhlbi.nih.gov/es/salud/pulmones/controles-respiratorios-del-cuerpo
<p align="justify">[4] E. Laskowski. “Dos maneras fáciles y precisas de medir tu frecuencia cardíaca”. Mayo Clinic. Accedido el 20 de abril de 2024. [En línea]. Disponible: https://www.mayoclinic.org/es/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979#:~:text=Generalmente,%20una%20frecuencia%20cardíaca%20más,a%2040%20latidos%20por%20minuto.
<p align="justify">[5] D. Anderson. “Real-time ECG for objective stress level measurement”. Diva Portal. Accedido el 20 de abril de 2024. [En línea]. Disponible: https://www.diva-portal.org/smash/get/diva2:1119950/FULLTEXT01.pdf
<p align="justify">[6] S. Sánchez-Morago. “CONTRACCIONES VENTRICULARES PREMATURAS : ¿SON TODAS IGUALES?” SEEUE - Sociedad Española de Enfermería de Urgencias y Emergencias. Accedido el 20 de abril de 2024. [En línea]. Disponible: https://www.enfermeriadeurgencias.com/ciber/PRIMERA_EPOCA/2006/octubre/contraccionesventriculares.htm
<p align="justify">[7] B. Benito y M. Josephson. “Taquicardia ventricular en la enfermedad coronaria | Revista Española de Cardiología”. Revista Española de Cardiología. Accedido el 20 de abril de 2024. [En línea]. Disponible: https://www.revespcardiol.org/es-taquicardia-ventricular-enfermedad-coronaria-articulo-S0300893212003284
<p align="justify">[8] M. Cardenas. “Fibrilación auricular”. Scielo. Accedido el 20 de abril de 2024. [En línea]. Disponible: https://www.scielo.org.mx/scielo.php?script=sci_arttext&amp;pid=S1405-99402007000600003
<p align="justify">[9] M. Bravo. “ACLS/ Asistolía – AESP”. Síntesis de Conocimientos. Accedido el 20 de abril de 2024. [En línea]. Disponible: https://sintesis.med.uchile.cl/revision/r-de-urgencias/14186-acls-asistolia-aesp
