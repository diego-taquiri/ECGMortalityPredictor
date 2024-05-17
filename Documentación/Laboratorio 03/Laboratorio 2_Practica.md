# ADQUISICIÓN DE SEÑALES Y GRAFICACIÓN EN ARDUINO
Lista de participantes:  
-Mantilla M., Ana Belen  
-Valdivia E., Erick Alexander   
-Flórez T., Armando Antonio  
-Taquiri D., Diego Alejandro  
## Tabla de contenidos
1. [Uso del Generador de Señales y Osciloscopio](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/README.md#uso-del-generador-de-se%C3%B1ales-y-osciloscopio)
2. [Ploteo de las señales](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#ploteo-de-las-se%C3%B1ales)
   - [Ruido](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#ruido)
   - [Señal 1](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#se%C3%B1al-1)
   - [Señal 2](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#se%C3%B1al-2)
   - [Señal 3](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#se%C3%B1al-3)
3. [Filtro pasa altas](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/README.md#filtro-pasa-altas)
   
### Uso del Generador de Señales y Osciloscopio
<p align="justify">Se configuró el Generador de Señales para proporcionar una señal sinusoidal de 1 KHz de frecuencia, 3.3V de Amplitud y 0V de offset. Su amplitud (3.32V) y periodo (1.01ms) son mostrados a continuación:

<div style="text-align: center;">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/0001.jpg" alt="Descripción de la primera imagen" width="300">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/0002.jpg" alt="Descripción de la segunda imagen" width="300">
</div>
Figura 1. (a) Amplitud y (b) Periodo mostrados en el osciloscopio.

### Ploteo de las señales
#### Ruido
<p align="justify">Para comenzar, se llevó a cabo la medición del ruido ambiental utilizando el Arduino IoT, aplicando una tasa de sampleo de 10 Hz. Notamos que el ruido ambiental registró una forma sinusoidal. Para mejorar la calidad de la señal recogida, se incorporó un condensador como parte de un circuito de filtrado, actuando junto con la resistencia interna del ADC del Arduino para conformar un filtro tipo RC básico. Esta configuración permitió filtrar eficazmente la mayor parte del ruido ambiental, como se puede apreciar en la gráfica derecha de la Figura 2.

<div style="text-align: center;">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/01.jpg" alt="Descripción de la primera imagen" width="300">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/02.jpg" alt="Descripción de la segunda imagen" width="300">
</div>
Figura 2. Ruido del ambiente sin condensador y con condensador, respectivamente. 

#### Señal 1
<p align="justify">Posteriormente, se procedió a evaluar una señal proveniente del generador de señales, utilizando esta vez una frecuencia de muestreo de 50 Hz. Se capturó una señal limpia en el ploteo con el arduino (Figura 3). Los resultados fueron similares a los obtenidos con el ruido ambiental, el condensador filtró la señal del generador. 

<div style="text-align: center;">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/05.jpg" alt="Descripción de la primera imagen" width="300">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/10.jpg" alt="Descripción de la segunda imagen" width="300">
</div>
Figura 3. Señal 1 sin condensador y con condensador, respectivamente. <br> <br>

<p align="justify">Podemos observar que la señal del osciloscopio a 5Hz tiene un parecido con la señal ploteada sin el condensador, pero difiere bastante de la gráfica cuando el condensador es añadido. En este caso, como en los demás, se disminuyó el voltaje aplicado a 3V, ya que, al ser visualizado en el osciloscopio, observamos un aumento de este debido al ruido.<br> 

<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/ab1.jpg" alt="Descripción de la imagen" width="300"><br> 
Figura 4. Señal 1 sin condensador representada en el osciloscopio.

#### Señal 2
<p align="justify">A continuación, se analizó una segunda señal del generador, aplicando una frecuencia de muestreo de 500 Hz. La gráfica resultante reveló una señal de mayor frecuencia, y el condensador de igual manera filtró la mayoría de la señal, pero no hubo una atenuación como con la de 50Hz (Figura 5). 

<div style="text-align: center;">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/06.jpg" alt="Descripción de la primera imagen" width="300">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/07.jpg" alt="Descripción de la segunda imagen" width="300">
</div>
Figura 5. Señal 2 sin condensador y con condensador, respectivamente. <br><br>

<p align="justify">Si bien mantenemos una clara diferencia visual con la señal con condensador, ahora la señal ploteada sin condensador no coincide de igual manera con la señal obtenida en el osciloscopio. Esto se debe a que la frecuencia de muestreo determina la cantidad de puntos de datos que se toman por unidad de tiempo así que su aumento lleva a una mayor cantidad de picos, como se puede observar en la Figura 6. Para este caso, utilizamos una señal de 100Hz. <br> 

<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/ab2.jpg" alt="Descripción de la imagen" width="300"><br> 
Figura 6. Señal 2 sin condensador representada en el osciloscopio.

#### Señal 3
<p align="justify">Finalmente, se experimentó con una tercera señal del generador, ajustando la frecuencia de muestreo a 1000 Hz. 

<div style="text-align: center;">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/08.jpg" alt="Descripción de la primera imagen" width="300">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/09.jpg" alt="Descripción de la segunda imagen" width="300">
</div>
Figura 7. Señal 3 sin condensador y con condensador, respectivamente. <br><br>

<p align="justify">Se observa que la gráfica ploteada a 500Hz sin condensador vuelve a ser más similar a la gráfica obtenida en el osciloscopio, aunque esto también puede ser influenciado por el cambio de escala. Sin embargo la señal ploteada también mantiene algunos picos randomizados que pueden ser efectos del ruido, lo cual no se observaba en la señal con frecuencia de muestreo de 50 Hz.<br> 

<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/ab3.jpg" alt="Descripción de la imagen" width="300"><br> 
Figura 8. Señal 3 sin condensador representada en el osciloscopio.

### Filtro paso alto
<p align="justify">Como se mencionó previamente, la conexión realizada con el condensador de 470uF actúa como un filtro paso alto, considerando la resistencia interna del arduino. Existe una atenuación de la onda sinusoidal obtenida a partir del generador de ondas, la cual a frecuencias bajas como 1 Hz filtra completamente la señal.<br> 
<p align="justify">La frecuencia de corte se puede obtener a partir de los valores de R y C, utilizando la fórmula Fc=1/(2*π*RC). En el caso del laboratorio se utilizó un condensador de 470 uF. Si bien el datasheet del ATmega 168 menciona una resistencia asociada en los pines analógicos de 100 Mohms [1], esta no interfiere con la medición de la señal. Para el cálculo de la frecuencia de corte, asumiendo interferencia mínima de la resistencia interna, (1 ohm), se obtendría una Fc de 339 Hz, la cual disminuye a medida que se incrementa el valor de R. <br>
<p align="justify">Pese al ruido observado, el incremento de la frecuencia de la señal de entrada por encima de la frecuencia de corte máxima calculada y el subsecuente incremento de la tasa de muestreo, resultan en la aparición de la señal de entrada en la lectura del arduino. Aún así, el condensador sigue actuando como un atenuador en todos los casos. Si bien nuestras señales fueron obtenidas con ruido, es posible su interpretación gracias al circuito realizado en el protoboard y los mínimos cambios visibles del arduino. El comportamiento gráfico de este proceso se oberva en la Figura 9.<br> 

<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/Diagrama-de-filtro-RC-paso-alto.png" alt="Descripción de la imagen" width="300"><br> 
Figura 9. Filtro paso alto. [2]

### Bibliografía


<p align="justify">[1]Atmel Corporation. "ATmega168V Datasheet." ATmega168V Datasheet, November 2016. Available: https://www.onlinecomponents.com/en/datasheet/atmega16820au-49534822/<br> 
<p align="justify">[2] “Calculadora de Filtro Paso Alto”, Learningaboutelectronics.com. [En línea]. Disponible en: https://www.learningaboutelectronics.com/Articulos/Calculadora-de-filtro-paso-alto.php. <br> 