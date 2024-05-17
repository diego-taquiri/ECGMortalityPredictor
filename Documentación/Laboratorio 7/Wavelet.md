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
<p align="justify"> Las señales ECG, EEG y EMG, conocidas colectivamente como señales bioeléctricas, representan la suma de las señales eléctricas que acompañan a las contracciones mecánicas de las células cuando son estimuladas por corrientes eléctricas, ya sean de origen neural o externo [1]. Estas señales son intrínsecamente complejas y, al viajar a través de diversos tejidos e interfaces, como electrodos y circuitos de procesamiento, son susceptibles a la adquisición de ruido y no linealidades. Por esta razón, la detección y procesamiento efectivo de señales bioeléctricas se ha convertido en un objetivo crucial dentro de la ingeniería biomédica [2]. El diseño de filtros adecuados para el procesamiento de estas señales es un campo de investigación activo y esencial para mejorar la precisión y fiabilidad del análisis de las señales ECG, EEG y EMG.

<p align="justify"> Una onda generalmente se define como una función oscilante del tiempo o del espacio, como una sinusoide. El análisis de Fourier es un análisis de ondas, el cual amplía señales o funciones en términos de sinusoides (o exponenciales complejas), lo que ha demostrado ser extremadamente valioso en matemáticas, ciencia e ingeniería, especialmente para fenómenos periódicos, invariantes en el tiempo o estacionarios. Por otro lado, una wavelet es una "onda pequeña", cuya energía se concentra en el tiempo para proporcionar una herramienta para el análisis de fenómenos transitorios, no estacionarios o que varían en el tiempo. Todavía tiene la característica de onda oscilante, pero también tiene la capacidad de permitir análisis simultáneos de tiempo y frecuencia con una base matemática flexible. [3]

<p align="justify">Las wavelets se utilizan en una expansión en serie de señales o funciones de la misma manera que una serie de Fourier usa la onda o sinusoide para representar una señal o función. Las señales son funciones de una variable continua, que a menudo representa el tiempo o la distancia. A partir de esta expansión de la serie, se desarrolla una versión de tiempo discreto, similar a la transformada discreta de Fourier, donde la señal está representada por una cadena de números que pueden ser muestras de una señal, de otra cadena de números o productos internos de una señal con algún conjunto de expansión. Finalmente, se describe brevemente la transformada wavelet continua donde tanto la señal, como la transformada, son funciones de variables continuas. Esto es análogo a la transformada de Fourier. [3]

<p align="justify">En este laboratorio, se explorarán las wavelets del procesamiento de señales, las cuales pasaron a primer plano a principios de la década de 1990 como una alternativa atractiva al procesamiento clásico de señales e imágenes basado en la transformada de Fourier [4]. Esto debido a que las expansiones y transformadas de wavelets han demostrado ser muy eficientes y efectivas en el análisis de una amplia clase de señales y fenómenos [3]. 

1. <p align="justify">El tamaño de los coeficientes de expansión de las wavelets disminuye rápidamente para una gran clase de señales. Esta propiedad se llama ser una base incondicional y es por eso que las wavelets son muy efectivas en la compresión, eliminación de ruido y detección de señales e imágenes. [3]

2. <p align="justify">La expansión wavelet permite una descripción local más precisa y una separación de las características de la señal. Un coeficiente de Fourier representa un componente que dura para siempre y, por tanto, eventos temporales deben describirse mediante una característica de fase que permita la cancelación o el refuerzo a lo largo del tiempo. Un coeficiente de expansión wavelet representa un componente que es en sí mismo local y es más fácil de interpretar. La expansión wavelet puede permitir una separación de componentes de una señal que se superponen en tanto en tiempo como en frecuencia. [3]

3. <p align="justify">Las wavelets son ajustables y adaptables. Como no hay una sola wavelet, se pueden diseñar para adaptarse a aplicaciones individuales. Son ideales para sistemas adaptativos que se ajustan solos para adaptarse a la señal. [3]

4. <p align="justify">La generación de wavelets y el cálculo de la transformada de wavelets discreta se adaptan bien a la computadora digital. No se utiliza cálculo, no hay derivadas ni integrales, solo operaciones de multiplicación y suma que son básicas para un sistema digital computadora. [3]

<p align="justify">Finalmente, se ha demostrado que el umbral de los coeficientes wavelet tiene una propiedad de reducción de ruido casi óptima para muchas clases de señales [5]. Los métodos actuales utilizan la transformada wavelet discreta (DWT) para procesar una señal, aplicando un umbral que elimina coeficientes por debajo de cierto valor y luego realizando la inversa de la DWT. Este proceso es eficaz para eliminar ruido y lograr alta compresión debido a la capacidad de concentración de las wavelets. En comparación, el procesamiento tradicional basado en Fourier busca minimizar la superposición de señales y ruido en el dominio de frecuencia mediante filtrado lineal. Las wavelets permiten elegir bases que reducen la superposición en el dominio tiempo-frecuencia. El nuevo método no lineal se centra en la diferencia de amplitud en lugar de la ubicación espectral, permitiendo recortar, umbralizar y reducir la amplitud para separar señales o eliminar ruido. Las propiedades de localización de las wavelets son especialmente efectivas para estos métodos, mejorando también la compresión, otro proceso no lineal. [3]

<p align="justify"> Una emocionante aplicación del procesamiento de señales basado en wavelets se encuentra en el procesamiento de señales e imágenes médicas y biomédicas, donde las aplicaciones de eliminación de ruido, compresión y detección son todas importantes, especialmente si se trata de dimensiones superiores. [3]

### Objetivos específicos de la práctica
- Familiarizarse con los conceptos básicos y la teoría detrás de las wavelets, incluyendo su definición, propiedades y diferencias clave respecto a la transformada de Fourier.
- Comparar la eficiencia y efectividad de las wavelets con la transformada de Fourier en el análisis de señales ECG, EEG y EMG.
- Aplicar técnicas de wavelets para el procesamiento de señales específicas de ECG, EEG y EMG, enfocándose en la eliminación de ruido y la detección de características importantes.
- Diseñar y probar filtros adaptativos basados en wavelets que puedan ajustarse a las características específicas de las señales bioeléctricas para mejorar su análisis y procesamiento.

### Materiales y métodos

#### ECG

<p align="justify">La señal ECG utilizada en este trabajo fue adquirida mediante un dispositivo BITalino, utilizando el canal 2 para la recolección de datos. La frecuencia de muestreo fue de 1000 Hz y el BITalino realiza la cuantización de la señal a 10 bits. Inicialmente, la cuantización de 10 bits cubre un rango de 0 a 3.3 mV [6]. Para convertir la señal cruda de bits a milivoltios y centrarla, se utilizó la siguiente relación de conversión:

```python
data_mV = (data[:, 5] * volt_range / (2 ** bits - 1)) - media(data_mV)
```

<p align="justify">Esta conversión permitió adecuar la señal para el posterior procesamiento.

<p align="justify">La metodología utilizada para el filtrado de la señal ECG usando wavelet se basa en la implementación propuesta por Alfaouri y Daqrouq en su artículo "ECG signal denoising by wavelet transform thresholding" [7]. En este estudio, se destaca la importancia del uso de la transformada wavelet para la eliminación de ruido en señales ECG no estacionarias. Los autores proponen un método de umbralización de coeficientes wavelet para la mejora de la relación señal-ruido y que preserva las características morfológicas de la señal ECG. <br>

<p align="justify">Siguiendo la implentación del artículo, se utilizó la aplicación de wavelets Daubechies 4 (db4) y un umbral suave para la eliminación de ruido. A continuación, se detallan los pasos seguidos en la metodología:<br>

<p align="justify">1. <b>Descomposición de la señal</b>: La señal ECG fue descompuesta utilizando la función `pywt.wavedec` con wavelets db4 hasta un nivel de descomposición de 5. Esta función descompone la señal original en un conjunto de coeficientes de aproximación y detalle, que representan las diferentes frecuencias presentes en la señal.

 ```python
    coeffs = pywt.wavedec(y_1, 'db4', level=5)
 ```

<p align="justify">2. <b>Cálculo de umbrales</b>: Se calculó un umbral adaptativo para cada nivel de detalle utilizando la desviación estándar de la señal y los coeficientes de detalle. El umbral \(T\) para cada nivel se calculó usando la siguiente fórmula:

<p align="center">
<img src="./plots/images/ecg-equation.png" alt="ECG Equation" width="200">
<p align="center"><b>Figura 1.</b> Fórmula para el cálculo de los umbrales. <br> 

<p align="justify">Donde \(C\) es una constante (0.01 en nuestro caso, elegida experimentalmente para nuestras señales), \(\sigma_{Vs}\) es la desviación estándar de la señal original, \(\sigma_{dj}\) es la desviación estándar de los coeficientes de detalle en cada nivel, y \(n\) es el número de muestras de la señal. j representa el número de niveles (en nuestro caso hasta 5 niveles), donde \(d_j\) son los coeficientes de detalle y \(n\) es el número de muestras para cada señal.

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

<p align="justify">3. <b>Aplicación de umbrales suaves</b>: Los coeficientes de detalle fueron umbralizados utilizando el umbral suave (`soft thresholding`). Este proceso reduce los coeficientes menores al umbral, manteniendo la estructura general de la señal pero eliminando el ruido. Se utilizó la función `pywt.threshold` para aplicar este umbral.

   ```python
    def soft_threshold(coeffs, T_values):
        thresholded_coeffs = coeffs.copy()
        for i in range(1, len(coeffs)):
            thresholded_coeffs[i] = pywt.threshold(coeffs[i], T_values[i-1], mode='soft')
        return thresholded_coeffs

    thresholded_coeffs = soft_threshold(coeffs, T_values)
   ```

<p align="justify">4. <b>Reconstrucción de la señal</b>: Finalmente, la señal fue reconstruida a partir de los coeficientes umbralizados utilizando la función `pywt.waverec`, obteniendo una señal denoised y filtrada.

   ```python
    y_denoised = pywt.waverec(thresholded_coeffs, 'db4')
   ```

#### EMG

#### EEG
<p align="justify">Para el filtrado de señal EEG, se utilizó la señal de EEG tomada mediante BITalino en tres instancias, reposo, apertura y cierre de ojos, y resolución mental de ejercicios matemáticos. El filtrado de la señal se realizó utilizando los criterios mencionados por Mamun et al.[ Md. Mamun, M. Al-Kadi, y Mohd. Marufuzzaman, «Effectiveness of Wavelet Denoising on Electroencephalogram Signals», Journal of Applied Research and Technology, vol. 11, n.o 1, pp. 156-160, feb. 2013, doi: 10.1016/S1665-6423(13)71524-4.] Se utilizó una función Wavelet Daubechies8 (db8) con 4 niveles de descomposición, el cual utiliza un umbral de ruido o threshold determinado por la siguiente ecuación: <br>

<p align="justify">Donde <br>
   - La desviación media absoluta(delta_mad) es la media de los valores absolutos de los coeficientes de wavelet entre 0.6745 (estimador de la desviación estándar para ruido blanco gaussiano).<br>
   - N es el número de muestras de la señal.

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
<p align="justify"> Easadas
<p align="justify"><b>Filtración de EMG:</b>
<p align="justify"> sdada
<p align="justify"><b>Filtración de EEG:</b>
<p align="justify">Se puede observar un suavizado de la señal eletroencefalográfica como resultado del filtro de wavelet con las características planteadas. Como se puede apreciar en las imágenes de las señales de salida, tras utilizar la transformada de wavelet, la forma de la onda no considera las espículas que son influencia de frecuencias mayores en el espectro.   Debido a que la señal EEG carece de un patrón identificable en el dominio del tiempo, el suavizado de la señal puede apreciarse de mejor forma en un espectrograma, donde se aprecia que las frecuencias por encima de los 50Hz se han visto reducidas en amplitud. <br>

<p align="justify">La literatura indica tres orígenes fisiológicos de ruido en las señales EEG. Los movimientos de ojo ocasionan un cambio en el campo eléctrico que rodea los mismos mediante la formación de dipolos en la retina y movimientos de las pestañas, generando potenciales en el cuero cabelludo [R. J. Croft and R. J. Barry, “Removal of ocular artifact from the EEG: a review,” Neurophysiologie clinique, vol. 30, no. 1, pp. 5–19, Feb. 2000, doi: https://doi.org/10.1016/s0987-7053(00)00055-1.]. Su espectro se sobrelapa con las ondas alfa del EEG en tareas mentales, y debido a su mayor amplitud, pueden llegar a suprimirlas [S. Zahan, "Removing EOG artifacts from EEG signal using noise-assisted multivariate empirical mode decomposition," 2016 2nd International Conference on Electrical, Computer & Telecommunication Engineering (ICECTE), Rajshahi, Bangladesh, 2016, pp. 1-5, doi: 10.1109/ICECTE.2016.7879634.].  Las señales electromiográficas son un ruido común en mediciones de ondas beta y gamma, y debido a su amplitud ocluyen la señal EEG a partir de los 20 Hz, siendo esta oclusión mayor a partir de los 50Hz. [K. J. Pope et al., “Managing electromyogram contamination in scalp recordings: An approach identifying reliable beta and gamma EEG features of psychoses or other disorders,” Brain and behavior, vol. 12, no. 9, Aug. 2022, doi: https://doi.org/10.1002/brb3.2721.] 

### Bibliografía
<p align="justify">[1]  Martinek R, Ladrova M, Sidikova M, Jaros R, Behbehani K, Kahankova R, Kawala-Sterniuk A. Advanced Bioelectrical Signal Processing Methods: Past, Present and Future Approach-Part I: Cardiac Signals. Sensors (Basel). 2021 Jul 30;21(15):5186. doi: 10.3390/s21155186. PMID: 34372424; PMCID: PMC8346990. 
<p align="justify">[2] Adimulam, M. K., & Srinivas, M. . (2016). Modeling of EXG (ECG, EMG and EEG) non-idealities using MATLAB. 2016 9th International Congress on Image and Signal Processing, BioMedical Engineering and Informatics (CISP-BMEI). doi:10.1109/cisp-bmei.2016.7852968
<p align="justify">[3] C. S. Burrus, R. A. Gopinath, y H. Guo, Introduction to wavelets and wavelet transforms: A primer. Upper Saddle River, NJ, Estados Unidos de América: Pearson, 1997.
<p align="justify">[4] “Wavelets: Multiscale edge detection and image denoising”, en Embedded Image Processing on the TMS320C6000TM DSP, Boston, MA: Springer US, 2005, pp. 281–378.
<p align="justify">[5] D. L. Donoho, “De-noising by soft-thresholding”, IEEE Trans. Inf. Theory, vol. 41, núm. 3, pp. 613–627, 1995.
<p align="justify">[6] PLUX – Wireless Biosignals, S.A., "Electrocardiography (ECG) Sensor Data Sheet," Rev. B, 2020. [Online]. Available: https://bitalino.com/storage/uploads/media/revolution-ecg-sensor-datasheet-revb-1.pdf. 
<p align="justify">[7] M. Alfaouri and K. Daqrouq, "ECG signal denoising by wavelet transform thresholding," American Journal of Applied Sciences, vol. 5, no. 3, pp. 276-281, 2008. doi: 10.3844/ajassp.2008.276.281.
