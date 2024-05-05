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
<p align="justify">El término filtro se utiliza habitualmente para describir un dispositivo que discrimina, de acuerdo con algún atributo de los objetos aplicados a su entrada, lo que pasa a través. El filtrado se emplea de formas muy variadas en el procesamiento digital de señales; por ejemplo, para eliminar el ruido indeseado que pueda existir en las señales deseadas, para conformación espectral en la ecualización de canales de comunicación, en la detección de señales de radar, sonar y de comunicaciones y para realizar el análisis espectral de señales, etc. Por tanto, seleccionando adecuadamente los coeficientes, se puede diseñar filtros selectivos de frecuencia que dejan pasar señales con componentes de frecuencia en determinadas bandas mientras que atenúan señales que contienen frecuencias en otras bandas. [1]
   
   
   
   Los métodos de diseño de filtros analógicos tienen una larga historia y se han desarrollado una variedad de elegantes procedimientos de diseño.

La invariancia de impulso y la transformación bilineal representan las dos principales técnicas analíticas para el diseño de filtros digitales a través de la transformación de diseños analógicos. En este laboratorio, se abordará el diseño de filtros IIR por medio de transformación bilineal. Esta transformación tiene la ventaja de que asigna todo el eje jQ en el plano s en una revolución alrededor del círculo unitario en el plano z. El alias está ahí por lo tanto eliminado, pero en contraste con la invariancia de impulso, se introduce distorsión en el eje de frecuencia no lineal. Hay varios tipos comunes de filtros analógicos: Butterworth, que tienen bandas de paso máximamente planas en filtros del mismo orden, Chebyshev tipo I que son equivariables en la banda de paso, Chebyshev tipo II que son equivariables en la banda de parada, y filtros elípticos que son equivariables tanto en la banda de paso y la banda de parada. La versión digital de estos se puede obtener a partir de diseños analógicos a través de la transformación bilineal. [1] En comparación, las técnicas de diseño para filtros digitales FIR generalmente se llevan a cabo directamente en el dominio del tiempo discreto. Hay tres técnicas de diseño principales, las cuales incluyen el método de la ventana, el método de muestreo de frecuencia y el diseño algorítmico de filtros óptimos. En este laboratorio se trabajará con el método de ventana, el cual comienza con una respuesta de muestra unitaria deseada que luego se trunca mediante una ventana de duración finita. [2]
   
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

