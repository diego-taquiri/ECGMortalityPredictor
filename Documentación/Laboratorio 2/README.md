# ADQUISICIÓN DE SEÑALES Y GRAFICACIÓN EN ARDUINO

## Tabla de contenidos
1. [Uso del Generador de Señales y Osciloscopio](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/README.md#uso-del-generador-de-se%C3%B1ales-y-osciloscopio)
2. [Ploteo de las señales](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#ploteo-de-las-se%C3%B1ales)
   - [Ruido](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#ruido)
   - [Señal 1](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#se%C3%B1al-1)
   - [Señal 2](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#se%C3%B1al-2)
   - [Señal 3](https://github.com/diego-taquiri/ISB-equipo11/tree/main/Documentaci%C3%B3n/Laboratorio%202#se%C3%B1al-3)
3. [Filtro pasa altas](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/README.md#filtro-pasa-altas)
   
### Uso del Generador de Señales y Osciloscopio
Se configuró el Generador de Señales para proporcionar una señal sinusoidal de 1 KHz de frecuencia, 3.3V de Amplitud y 0V de offset. Su amplitud (3.32V) y periodo (1.01ms) son mostrados a continuación:

<div style="text-align: center;">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/0001.jpg" alt="Descripción de la primera imagen" width="300">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%202/images%20lab%202/0002.jpg" alt="Descripción de la segunda imagen" width="300">
</div>

### Ploteo de las señales
#### Ruido
Para comenzar, se llevó a cabo la medición del ruido ambiental utilizando el Arduino IoT, aplicando una tasa de sampleo de 10 Hz. Notamos que el ruido ambiental registró una forma sinusoidal. Para mejorar la calidad de la señal recogida, se incorporó un condensador como parte de un circuito de filtrado, actuando junto con la resistencia interna del ADC del Arduino para conformar un filtro tipo RC básico. Esta configuración permitió filtrar eficazmente la mayor parte del ruido ambiental, como se puede apreciar en la gráfica derecha de la figura 3.

#### Señal 1
Posteriormente, se procedió a evaluar una señal proveniente del generador de señales, utilizando esta vez una frecuencia de muestreo de 50 Hz en el Arduino. Se capturó una señal limpia en el ploteo con el arduino (Figura 4). Los resultados fueron similares a los obtenidos con el ruido ambiental, el condensador filtró la señal del generador. 

Podemos observar que la señal del osciloscopio tiene un parecido con la señal ploteada sin el condensador pero difiere bastante de la gráfica cuando el condensador es añadido.

#### Señal 2
A continuación, se analizó una segunda señal del generador, aplicando una frecuencia de muestreo de 500 Hz. La gráfica resultante reveló una señal de mayor frecuencia, y el condensador de igual manera filtró la mayoría de la señal, pero no hubo una atenuación como la de 50Hz (Figura 6). 

Si bien mantenemos una clara diferencia visual con la señal con condensador ahora la señal ploteada sin condensador no coincide de igual manera con la señal obtenida en el osciloscopio. Esto se debe a que la frecuencia de muestreo determina la cantidad de puntos de datos que se toman por unidad de tiempo así que su aumento lleva a una mayor cantidad de picos.

#### Señal 3
Finalmente, se experimentó con una tercera señal del generador, ajustando la frecuencia de muestreo del Arduino a 1000 Hz. 

Se observa que la gráfica ploteada sin condensador vuelve a ser más similar a la gráfica obtenida en el osciloscopio, aunque esto también puede ser influenciado por el cambio de escala. Sin embargo la señal ploteada también mantiene algunos picos randomizados que pueden ser efectos del ruido lo cual no se observaba en la señal con frecuencia de muestreo de 50 Hz

### Filtro pasa altas
Como se mencionó previamente, la conexión realizada con el condensador de 470uF actúa como un filtro pasa altos, considerando la resistencia interna del arduino. 



### Bibliografía

[1] “Calculadora de Filtro Paso Alto”, Learningaboutelectronics.com. [En línea]. Disponible en: https://www.learningaboutelectronics.com/Articulos/Calculadora-de-filtro-paso-alto.php. 

