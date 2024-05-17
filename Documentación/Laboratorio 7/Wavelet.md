# Transformada Wavelet
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro  

## Tabla de contenidos
1. [Introducción](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%207/Wavelet.md#introducci%C3%B3n)
2. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%207/Wavelet.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%207/Wavelet.md#materiales-y-m%C3%A9todos)
5. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%207/Wavelet.md#resultados)
   - [Tabla resumen ECG](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%207/Wavelet.md#tabla-resumen-ecg)
   - [Tabla resumen EMG ](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%207/Wavelet.md#tabla-resumen-emg)
   - [Tabla resumen EEG](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%207/Wavelet.md#tabla-resumen-ecg)
6. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%207/Wavelet.md#discusi%C3%B3n)
7. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%207/Wavelet.md#bibliograf%C3%ADa)

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

#### Filtrado de ECG usando Wavelet

La señal ECG utilizada en este trabajo fue adquirida mediante un dispositivo BITalino, utilizando el canal 2 para la recolección de datos. La frecuencia de muestreo fue de 1000 Hz y el BITalino realiza la cuantización de la señal a 10 bits. Inicialmente, la cuantización de 10 bits cubre un rango de 0 a 3.3 mV [1]. Para convertir la señal cruda de bits a milivoltios y centrarla, se utilizó la siguiente relación de conversión:

```python
data_mV = (data[:, 5] * volt_range / (2 ** bits - 1)) - media(data_mV)
```

Esta conversión permitió adecuar la señal para el posterior procesamiento.

La metodología utilizada para el filtrado de la señal ECG usando wavelet se basa en la implementación propuesta por Alfaouri y Daqrouq en su artículo "ECG signal denoising by wavelet transform thresholding" [2]. En este estudio, se destaca la importancia del uso de la transformada wavelet para la eliminación de ruido en señales ECG no estacionarias. Los autores proponen un método de umbralización de coeficientes wavelet para la mejora de la relación señal-ruido y que preserva las características morfológicas de la señal ECG. 

Siguiendo la implentación del artículo, se utilizó la aplicación de wavelets Daubechies 4 (db4) y un umbral suave para la eliminación de ruido. A continuación, se detallan los pasos seguidos en la metodología:

1. **Descomposición de la señal**: La señal ECG fue descompuesta utilizando la función `pywt.wavedec` con wavelets db4 hasta un nivel de descomposición de 5. Esta función descompone la señal original en un conjunto de coeficientes de aproximación y detalle, que representan las diferentes frecuencias presentes en la señal.

    ```python
    coeffs = pywt.wavedec(y_1, 'db4', level=5)
    ```

2. **Cálculo de umbrales**: Se calculó un umbral adaptativo para cada nivel de detalle utilizando la desviación estándar de la señal y los coeficientes de detalle. El umbral \(T\) para cada nivel se calculó usando la siguiente fórmula:

<div style="text-align: center;">
    <img src="./plots/images/ecg-equation.png" alt="ECG Equation" width="200">
</div>

   donde \(C\) es una constante (0.01 en nuestro caso, elegida experimentalmente para nuestras señales), \(\sigma_{Vs}\) es la desviación estándar de la señal original, \(\sigma_{dj}\) es la desviación estándar de los coeficientes de detalle en cada nivel, y \(n\) es el número de muestras de la señal. j representa el número de niveles (en nuestro caso hasta 5 niveles), donde \(d_j\) son los coeficientes de detalle y \(n\) es el número de muestras para cada señal.



```python
    def calculate_T(coeffs, n, C):
        sigma_Vs = np.std(y_1)
        dj = [coeffs[i] for i in range(1, len(coeffs))]
        sigma_dj = [np.std(d) for d in dj]
        T = [C * np.sqrt((sigma_Vs / sigma) * n) for sigma in sigma_dj]
        return T

    n = len(y_1)
    T_values = calculate_T(coeffs, n, C)
```

3. **Aplicación de umbrales suaves**: Los coeficientes de detalle fueron umbralizados utilizando el umbral suave (`soft thresholding`). Este proceso reduce los coeficientes menores al umbral, manteniendo la estructura general de la señal pero eliminando el ruido. Se utilizó la función `pywt.threshold` para aplicar este umbral.

    ```python
    def soft_threshold(coeffs, T_values):
        thresholded_coeffs = coeffs.copy()
        for i in range(1, len(coeffs)):
            thresholded_coeffs[i] = pywt.threshold(coeffs[i], T_values[i-1], mode='soft')
        return thresholded_coeffs

    thresholded_coeffs = soft_threshold(coeffs, T_values)
    ```

4. **Reconstrucción de la señal**: Finalmente, la señal fue reconstruida a partir de los coeficientes umbralizados utilizando la función `pywt.waverec`, obteniendo una señal denoised y filtrada.

    ```python
    y_denoised = pywt.waverec(thresholded_coeffs, 'db4')
    ```

Esta metodología permitió reducir el ruido presente en la señal ECG de manera efectiva.

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
<p align="justify">Para el filtrado de señal EEG, se utilizó la señal de EEG tomada mediante BITalino en tres instancias, reposo, apertura y cierre de ojos, y resolución mental de ejercicios matemáticos. El filtrado de la señal se realizó utilizando los criterios mencionados por Mamun et al.[ Md. Mamun, M. Al-Kadi, y Mohd. Marufuzzaman, «Effectiveness of Wavelet Denoising on Electroencephalogram Signals», Journal of Applied Research and Technology, vol. 11, n.o 1, pp. 156-160, feb. 2013, doi: 10.1016/S1665-6423(13)71524-4.] Se utilizó una función Wavelet Daubechies8 (db8) con 4 niveles de descomposición, el cual utiliza un umbral de ruido o threshold determinado por la siguiente ecuación:


Donde:
-La desviación media absoluta(delta_mad) es la media de los valores absolutos de los coeficientes de wavelet entre 0.6745 (estimador de la desviación estándar para ruido blanco gaussiano)
-N es el número de muestras de la señal.



### Resultados
#### Tabla resumen ECG 
| Campo        | Señal cruda                                                   | Señal + Wavelet                                                    |
|--------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Basal        | ![Imagen de ECG](plots/ecg-reposo-cruda.png)       | ![Imagen de ECG](plots/ecg-reposo-wavelet.png)              |
| Respiración  | ![Imagen de ECG](plots/ecg-respiracion-cruda.png)             | ![Imagen de ECG](plots/ecg-respiracion-wavelet.png)               |
| Ejercicio    | ![Imagen de ECG](plots/ecg-ejercicio-cruda.png)   | ![Imagen de ECG](plots/ecg-ejercicio-wavelet.png)          |


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
<p align="justify">Se puede observar un suavizado de la señal eletroencefalográfica como resultado del filtro de wavelet con las características planteadas. Como se puede apreciar en las imágenes de las señales de salida, tras utilizar la transformada de wavelet, la forma de la onda no considera las espículas que son influencia de frecuencias mayores en el espectro.   Debido a que la señal EEG carece de un patrón identificable en el dominio del tiempo, el suavizado de la señal puede apreciarse de mejor forma en un espectrograma, donde se aprecia que las frecuencias por encima de los 50Hz se han visto reducidas en amplitud.

<p align="justify">La literatura indica tres orígenes fisiológicos de ruido en las señales EEG. Los movimientos de ojo ocasionan un cambio en el campo eléctrico que rodea los mismos mediante la formación de dipolos en la retina y movimientos de las pestañas, generando potenciales en el cuero cabelludo [R. J. Croft and R. J. Barry, “Removal of ocular artifact from the EEG: a review,” Neurophysiologie clinique, vol. 30, no. 1, pp. 5–19, Feb. 2000, doi: https://doi.org/10.1016/s0987-7053(00)00055-1.]. Su espectro se sobrelapa con las ondas alfa del EEG en tareas mentales, y debido a su mayor amplitud, pueden llegar a suprimirlas [S. Zahan, "Removing EOG artifacts from EEG signal using noise-assisted multivariate empirical mode decomposition," 2016 2nd International Conference on Electrical, Computer & Telecommunication Engineering (ICECTE), Rajshahi, Bangladesh, 2016, pp. 1-5, doi: 10.1109/ICECTE.2016.7879634.].  Las señales electromiográficas son un ruido común en mediciones de ondas beta y gamma, y debido a su amplitud ocluyen la señal EEG a partir de los 20 Hz, siendo esta oclusión mayor a partir de los 50Hz. [K. J. Pope et al., “Managing electromyogram contamination in scalp recordings: An approach identifying reliable beta and gamma EEG features of psychoses or other disorders,” Brain and behavior, vol. 12, no. 9, Aug. 2022, doi: https://doi.org/10.1002/brb3.2721.] 

### Bibliografía

[1] PLUX – Wireless Biosignals, S.A., "Electrocardiography (ECG) Sensor Data Sheet," Rev. B, 2020. [Online]. Available: https://bitalino.com/storage/uploads/media/revolution-ecg-sensor-datasheet-revb-1.pdf. 

[2] M. Alfaouri and K. Daqrouq, "ECG signal denoising by wavelet transform thresholding," American Journal of Applied Sciences, vol. 5, no. 3, pp. 276-281, 2008. doi: 10.3844/ajassp.2008.276.281.





