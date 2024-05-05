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
<p align="justify"> El término filtro se utiliza habitualmente para describir un dispositivo que discrimina, de acuerdo con algún atributo de los objetos aplicados a su entrada, lo que pasa a través. El filtrado se emplea de formas muy variadas en el procesamiento digital de señales; por ejemplo, para eliminar el ruido indeseado que pueda existir en las señales deseadas, para conformación espectral en la ecualización de canales de comunicación, en la detección de señales de radar, sonar y de comunicaciones y para realizar el análisis espectral de señales, etc. Por tanto, seleccionando adecuadamente los coeficientes, se puede diseñar filtros selectivos de frecuencia que dejan pasar señales con componentes de frecuencia en determinadas bandas mientras que atenúan señales que contienen frecuencias en otras bandas. Normalmente, los filtros se clasifican de acuerdo con sus características en el dominio de la frecuencia como filtros paso bajo, paso alto, paso banda, banda eliminada y paso todo. [1]
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/paso.png" alt="Descripción de la imagen" width="300"><br> 
<p align="center"><b>Figura 1.</b> Módulo de las respuestas de algunos filtros discretos en el tiempo y selectivos en frecuencia [1]. <br> 

<p align="justify">Sin embargo, también es conveniente subdividir la clase de sistemas lineales invariantes en el tiempo en dos tipos: aquellos que tienen una repuesta al impulso de duración finita (FIR, finite-duration impulse response) y aquellos que tienen una respuesta al impulso de duración infinita (IIR, infinite-duration impulse response). En la práctica, los filtros FIR se emplean en problemas de filtrado en los que se precisa una característica de fase dentro de la banda de paso del filtro. Si no se necesita esta característica de fase lineal, puede emplearse un filtro IIR o FIR. Por regla general, un filtro IIR tiene lóbulos secundarios más pequeños en la banda eliminada que un filtro FIR con el mismo número de parámetros. Por esta razón, si es tolerable cierta distorsión, es preferible un filtro IIR, principalmente porque su implementación precisa muy pocos parámetros, requiere menos memoria y presenta menos complejidad de cálculo [1].

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/filtro.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 1.</b> Módulo de los filtros físicamente realizables [1]. <br> 
   
<p align="justify">En este laboratorio, se abordará el diseño de filtros IIR por medio de transformación bilineal. Hay varios tipos comunes de filtros analógicos: Butterworth, que tienen bandas de paso máximamente planas en filtros del mismo orden, Chebyshev tipo I que son equivariables en la banda de paso, Chebyshev tipo II que son equivariables en la banda de parada, y filtros elípticos que son equivariables tanto en la banda de paso y la banda de parada. La versión digital de estos se puede obtener a partir de diseños analógicos a través de la transformación bilineal [2]. En comparación, las técnicas de diseño para filtros digitales, en este laboratorio se trabajará con el método de ventana, el cual comienza con una respuesta de muestra unitaria deseada que luego se trunca mediante una ventana de duración finita [3]. Los distintos tipos de filtro FIR e IIR son visualizados a continuación.
   
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/ventana.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 1.</b> Formas de varias funciones de ventana [1]. <br> 
      
### Objetivos específicos de la práctica
- Diseñar filtros FIR e IIR con los datasets de los laboratorios anteriores.
- Filtrar de manera óptima las frecuencias altas de las señales de ECG que corresponden a ruido.
- Filtrar las señales EMG para eliminar ruido y artefactos, y aislar la actividad muscular efectiva.
- Preprocesar señales EEG para reducir el ruido y extraer características de interés como ondas cerebrales específicas.

### Materiales y métodos
#### ECG
#### EMG
#### EEG
<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%206/images/Screenshot%202024-05-04%20192312.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 1.</b> Bandas de frecuencia de EEG, ocurrencia y tareas para activar la potencia de la banda. <br> 
   
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
### Bibliografía
<p align="justify">[1]  Martinek R, Ladrova M, Sidikova M, Jaros R, Behbehani K, Kahankova R, Kawala-Sterniuk A. Advanced Bioelectrical Signal Processing Methods: Past, Present and Future Approach-Part I: Cardiac Signals. Sensors (Basel). 2021 Jul 30;21(15):5186. doi: 10.3390/s21155186. PMID: 34372424; PMCID: PMC8346990. 
<p align="justify">[2] Adimulam, M. K., & Srinivas, M. . (2016). Modeling of EXG (ECG, EMG and EEG) non-idealities using MATLAB. 2016 9th International Congress on Image and Signal Processing, BioMedical Engineering and Informatics (CISP-BMEI). doi:10.1109/cisp-bmei.2016.7852968
