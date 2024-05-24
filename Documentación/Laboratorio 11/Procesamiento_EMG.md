# Transformada Wavelet
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro  

## Tabla de contenidos
1. [Introducción](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/Wavelet.md#introducci%C3%B3n)
2. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/Wavelet.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/Wavelet.md#materiales-y-m%C3%A9todos)
5. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/Wavelet.md#resultados)
   - [Tabla resumen ECG](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/Wavelet.md#tabla-resumen-ecg)
   - [Tabla resumen EMG ](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/Wavelet.md#tabla-resumen-emg)
   - [Tabla resumen EEG](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/Wavelet.md#tabla-resumen-ecg)
6. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/Wavelet.md#discusi%C3%B3n)
7. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/Wavelet.md#bibliograf%C3%ADa)

### Introducción
<p align="justify"> Las señales ECG, EEG y EMG, conocidas colectivamente como señales bioeléctricas, representan la suma de las señales eléctricas que acompañan a las contracciones mecánicas de las células cuando son estimuladas por corrientes eléctricas, ya sean de origen neural o externo [1]. Estas señales son intrínsecamente complejas y, al viajar a través de diversos tejidos e interfaces, como electrodos y circuitos de procesamiento, son susceptibles a la adquisición de ruido y no linealidades. Por esta razón, la detección y procesamiento efectivo de señales bioeléctricas se ha convertido en un objetivo crucial dentro de la ingeniería biomédica [2]. El diseño de filtros adecuados para el procesamiento de estas señales es un campo de investigación activo y esencial para mejorar la precisión y fiabilidad del análisis de las señales ECG, EEG y EMG.

<p align="justify"> Una onda generalmente se define como una función oscilante del tiempo o del espacio, como una sinusoide. El análisis de Fourier es un análisis de ondas, el cual amplía señales o funciones en términos de sinusoides (o exponenciales complejas), lo que ha demostrado ser extremadamente valioso en matemáticas, ciencia e ingeniería, especialmente para fenómenos periódicos, invariantes en el tiempo o estacionarios. Por otro lado, una wavelet es una "onda pequeña", cuya energía se concentra en el tiempo para proporcionar una herramienta para el análisis de fenómenos transitorios, no estacionarios o que varían en el tiempo. Todavía tiene la característica de onda oscilante, pero también tiene la capacidad de permitir análisis simultáneos de tiempo y frecuencia con una base matemática flexible. [3] Hay varias familias de wavelets que han demostrado ser especialmente útiles, como Haar, Daubechies, Biorthogonal, Coiflets, Symlets, Morlet, Mexican Hat, Meyer, etc. [4]

<div style="text-align: center;">
      <p align="center">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/images/sine.png" alt="Descripción de la primera imagen" width="300">
    <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2009/images/wavelet.png" alt="Descripción de la primera imagen" width="330">
</div>
<p align="center"><b>Figura 1.</b> Una onda y una wavelet: (a) Onda seno y (b) Wavelet ψD20 de Daubechies [3]. <br> 
      
<p align="justify">Las wavelets se utilizan en una expansión en serie de señales o funciones de la misma manera que una serie de Fourier usa la onda o sinusoide para representar una señal o función. Las señales son funciones de una variable continua, que a menudo representa el tiempo o la distancia. A partir de esta expansión de la serie, se desarrolla una versión de tiempo discreto, similar a la transformada discreta de Fourier, donde la señal está representada por una cadena de números que pueden ser muestras de una señal, de otra cadena de números o productos internos de una señal con algún conjunto de expansión. Finalmente, se describe brevemente la transformada wavelet continua donde tanto la señal, como la transformada, son funciones de variables continuas. Esto es análogo a la transformada de Fourier. [3]

<p align="justify">En este laboratorio, se explorarán las wavelets del procesamiento de señales, las cuales pasaron a primer plano a principios de la década de 1990 como una alternativa atractiva al procesamiento clásico de señales e imágenes basado en la transformada de Fourier [5]. Esto debido a que las expansiones y transformadas de wavelets han demostrado ser muy eficientes y efectivas en el análisis de una amplia clase de señales y fenómenos [3]. 

1. <p align="justify">El tamaño de los coeficientes de expansión de las wavelets disminuye rápidamente para una gran clase de señales. Esta propiedad se llama base incondicional y es por eso que las wavelets son muy efectivas en la compresión, eliminación de ruido y detección de señales e imágenes. [3]

2. <p align="justify">La expansión wavelet permite una descripción local más precisa y una separación de las características de la señal. Un coeficiente de Fourier representa un componente que dura para siempre y, por tanto, eventos temporales deben describirse mediante una característica de fase que permita la cancelación o el refuerzo a lo largo del tiempo. Un coeficiente de expansión wavelet representa un componente que es en sí mismo local y es más fácil de interpretar. La expansión wavelet puede permitir una separación de componentes de una señal que se superponen en tanto en tiempo como en frecuencia. [3]

3. <p align="justify">Las wavelets son ajustables y adaptables. Como no hay una sola wavelet, se pueden diseñar para adaptarse a aplicaciones individuales. Son ideales para sistemas adaptativos que se ajustan solos para adaptarse a la señal. [3]

4. <p align="justify">La generación de wavelets y el cálculo de la transformada de wavelets discreta se adaptan bien a la computadora digital. No se utiliza cálculo, no hay derivadas ni integrales, solo operaciones de multiplicación y suma que son básicas para un sistema digital computadora. [3]

<p align="justify">Finalmente, se ha demostrado que el umbral de los coeficientes wavelet tiene una propiedad de reducción de ruido casi óptima para muchas clases de señales [6]. Los métodos actuales utilizan la transformada wavelet discreta (DWT) para procesar una señal, aplicando un umbral que elimina coeficientes por debajo de cierto valor y luego realizando la inversa de la DWT. Este proceso es eficaz para eliminar ruido y lograr alta compresión debido a la capacidad de concentración de las wavelets. En comparación, el procesamiento tradicional basado en Fourier busca minimizar la superposición de señales y ruido en el dominio de frecuencia mediante filtrado lineal. Las wavelets permiten elegir bases que reducen la superposición en el dominio tiempo-frecuencia. Hay un nuevo método no lineal que se centra en la diferencia de amplitud en lugar de la ubicación espectral, permitiendo recortar, umbralizar y reducir la amplitud para separar señales o eliminar ruido. Las propiedades de localización de las wavelets son especialmente efectivas para estos métodos, mejorando también la compresión, otro proceso no lineal. [3]

<p align="justify"> Una emocionante aplicación del procesamiento de señales basado en wavelets se encuentra en el procesamiento de señales e imágenes médicas y biomédicas, donde las aplicaciones de eliminación de ruido, compresión y detección son todas importantes, especialmente si se trata de dimensiones superiores. [3]

### Objetivos específicos de la práctica
- Familiarizarse con los conceptos básicos y la teoría detrás de las wavelets, incluyendo su definición, propiedades y diferencias clave respecto a la transformada de Fourier.
- Comparar la eficiencia y efectividad de las wavelets con la transformada de Fourier en el análisis de señales ECG, EEG y EMG.
- Aplicar técnicas de wavelets para el procesamiento de señales específicas de ECG, EEG y EMG, enfocándose en la eliminación de ruido y la detección de características importantes.
- Diseñar y probar filtros adaptativos basados en wavelets que puedan ajustarse a las características específicas de las señales bioeléctricas para mejorar su análisis y procesamiento.

### Materiales y métodos

#### ECG

<p align="justify">La señal ECG utilizada en este trabajo fue adquirida mediante un dispositivo BITalino, utilizando el canal 2 para la recolección de datos. La frecuencia de muestreo fue de 1000 Hz y el BITalino realiza la cuantización de la señal a 10 bits. Inicialmente, la cuantización de 10 bits cubre un rango de 0 a 3.3 mV [7]. Para convertir la señal cruda de bits a milivoltios y centrarla, se utilizó la siguiente relación de conversión:

```python
data_mV = (data[:, 5] * volt_range / (2 ** bits - 1)) - media(data_mV)
```

<p align="justify">Esta conversión permitió adecuar la señal para el posterior procesamiento.

<p align="justify">La metodología utilizada para el filtrado de la señal ECG usando wavelet se basa en la implementación propuesta por Alfaouri y Daqrouq en su artículo "ECG signal denoising by wavelet transform thresholding" [8]. En este estudio, se destaca la importancia del uso de la transformada wavelet para la eliminación de ruido en señales ECG no estacionarias. Los autores proponen un método de umbralización de coeficientes wavelet para la mejora de la relación señal-ruido y que preserva las características morfológicas de la señal ECG. <br>

<p align="justify">Siguiendo la implentación del artículo, se utilizó la aplicación de wavelets Daubechies 4 (db4) y un umbral suave para la eliminación de ruido. A continuación, se detallan los pasos seguidos en la metodología:<br>

<p align="justify">1. <b>Descomposición de la señal</b>: La señal ECG fue descompuesta utilizando la función `pywt.wavedec` con wavelets db4 hasta un nivel de descomposición de 5. Esta función descompone la señal original en un conjunto de coeficientes de aproximación y detalle, que representan las diferentes frecuencias presentes en la señal.

 ```python
    coeffs = pywt.wavedec(y_1, 'db4', level=5)
 ```

<p align="justify">2. <b>Cálculo de umbrales</b>: Se calculó un umbral adaptativo para cada nivel de detalle utilizando la desviación estándar de la señal y los coeficientes de detalle. El umbral \(T\) para cada nivel se calculó usando la siguiente fórmula:

<p align="center">
<img src="./plots/images/ecg-equation.png" alt="ECG Equation" width="200">
<p align="center"><b>Figura 2.</b> Fórmula para el cálculo de los umbrales. <br> 

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
<p align="justify">En el paper "Arm EMG Wavelet-Based Denoising System" [9] se describe un sistema para la eliminación de ruido en señales EMG utilizando técnicas de transformada wavelet. Aquí está la traducción de la explicación y el análisis de cada parte del código Python proporcionado:

   - Función de base wavelet: Los autores usaron la wavelet Daubechies de orden 4 (db4). La elección de la wavelet es crucial porque afecta la eficiencia en la reducción de ruido y la preservación de las características de la señal.

   - Nivel de descomposición: La señal EMG fue descompuesta hasta el nivel 10. Este nivel de descomposición asegura que tanto el ruido de alta frecuencia como los artefactos de baja frecuencia puedan ser efectivamente aislados de la verdadera señal EMG.

   - Algoritmo de selección de umbral: Utilizaron un enfoque heurístico para la umbralización. Esto significa que los umbrales no son fijos, sino que se determinan dinámicamente en función de las características de la señal en cada nivel de descomposición.

   - Reescalado del umbral: El método heurístico de umbralización se acopla con un método de reescalado de umbral universal ('sln'), que ajusta los umbrales basándose en el nivel de ruido dentro de la señal.

Análisis del Código

<p align="justify">1. Función de Denoising con Wavelet:</b>

```python
def wavelet_denoise(signal, wavelet='db4', level=10):
```
<p align="justify">Se define una función wavelet_denoise que toma una señal, el tipo de wavelet y el nivel de descomposición como parámetros.

<p align="justify">2. Descomposición de la Señal:</b>

```python
coeffs = pywt.wavedec(signal, wavelet, level=level)
```
<p align="justify">La señal se descompone en sus coeficientes wavelet utilizando la función wavedec de la librería pywt.

<p align="justify">3. Estimación del Umbral de Ruido:</b>

```python
sigma = np.median(np.abs(coeffs[-level])) / 0.6745
uthresh = sigma * np.sqrt(2 * np.log(len(signal))) * threshold_scaling_factor
```
<p align="justify">Se calcula el umbral de ruido usando la mediana de los coeficientes de detalle de mayor nivel. Este cálculo está basado en la estimación robusta de la desviación estándar.

<p align="justify">4. Umbralización de los Coeficientes:</b>

```python
denoised_coeffs = [pywt.threshold(c, uthresh, mode='soft') for c in coeffs]
```
<p align="justify">Se aplica la umbralización suave a cada conjunto de coeficientes wavelet, reduciendo así el ruido.

<p align="justify">5. Reconstrucción de la Señal:</b>

```python
denoised_signal = pywt.waverec(denoised_coeffs, wavelet)
```
<p align="justify">La señal se reconstruye a partir de los coeficientes umbralizados utilizando la función waverec.

#### EEG
<p align="justify">Para el filtrado de señal EEG, se utilizó la señal de EEG tomada mediante BITalino en tres instancias, reposo, apertura y cierre de ojos, y resolución mental de ejercicios matemáticos. El filtrado de la señal se realizó utilizando los criterios mencionados por Zikov et al.[10] Se utilizó una función Coiflet 3 con 5 niveles de descomposición y un método de hard thresholding solo aplicado en los tres primeros niveles, es decir a frecuencias menores de 16 Hz, el cual utiliza un umbral de ruido o threshold determinado por la siguiente ecuación: <br>
<p align="justify"> Tk=media(Hk)+2*std(Hk)
<p align="justify">Donde <br>
   - Hk denota los coeficientes del wavelet para cada escala k de descomposición 
<p align="justify">Adicionalmente la señal fue filtrada a 60 Hz.para evitar ruidos provenientes de la interferencia de corriente alterna.

<p align="justify">El código resultante fue el que sigue.

<p align="justify">1. Cálculo de umbral de ruido:</b>

```python
def calculate_thresholds(coeffs):
    thresholds = [np.mean(np.abs(coeff)) + 2 * np.std(np.abs(coeff)) for coeff in coeffs[1:]]  
    return thresholds
```
<p align="justify">Cálculo del umbral o threshold de acuerdo a lo especificado en el trabajo de Zikov.

<p align="justify">2. Thresholding de los coeficientes wavelet:</b>

```python
def apply_threshold(coeffs, thresholds, max_level):
    denoised_coeffs = [coeffs[0]]  
    for i, coeff in enumerate(coeffs[1:]):
        if i < max_level:  
            threshold = thresholds[i]
            denoised_coeff = pywt.threshold(coeff, threshold, mode='hard')
        else:
            denoised_coeff = coeff  
        denoised_coeffs.append(denoised_coeff)
    return denoised_coeffs
```
<p align="justify">Los coeficientes de Coiflet 3 se modifican utilizando el threshold calculado solo hasta el nivel máximo que en este caso es el tercer coeficiente de detalle y hard thresholding en los coeficientes umbralizados. 

<p align="justify">3. Estimación del Umbral de Ruido:</b>

```python
sigma = np.median(np.abs(coeffs[-level])) / 0.6745
uthresh = sigma * np.sqrt(2 * np.log(len(signal))) * threshold_scaling_factor
```
<p align="justify">Se calcula el umbral de ruido usando la mediana de los coeficientes de detalle de mayor nivel. Este cálculo está basado en la estimación robusta de la desviación estándar.

<p align="justify">4. Umbralización de los Coeficientes:</b>

```python
    coeffs = pywt.swt(data_mV_notched, wavelet, level=levels, start_level=0)
    thresholds = calculate_thresholds(coeffs)
    denoised_coeffs = apply_threshold(coeffs, thresholds, max_threshold_level)
    denoised_signal = pywt.iswt(denoised_coeffs, wavelet)
```
<p align="justify">Se descompone y reconstruye la señal mediante transformada de Wavelet estacionaria y su respectiva inversa.

### Resultados
#### Tabla resumen ECG 
| Campo        | Señal cruda                                                   | Señal + Wavelet                                                    |
|--------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Basal        | ![Imagen de ECG](plots/ecg-reposo-cruda.png)       | ![Imagen de ECG](plots/ecg-reposo-wavelet.png)              |
| Respiración  | ![Imagen de ECG](plots/ecg-respiracion-cruda.png)             | ![Imagen de ECG](plots/ecg-respiracion-wavelet.png)               |
| Ejercicio    | ![Imagen de ECG](plots/ecg-ejercicio-cruda.png)   | ![Imagen de ECG](plots/ecg-ejercicio-wavelet.png)          |


#### Tabla resumen EMG 
| Campo        | Señal cruda                                                   | Señal + Wavelet                                                    |
|--------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Reposo        |  ![Imagen de EMG](plots/emg.reposo.png)        |   ![Imagen de EMG](plots/emg.reposo.filtrado.png)               |
| Flexión isotónica  |     ![Imagen de EMG](plots/emg.contrafuerza.png)           |   ![Imagen de EMG](plots/emg.contrafuerza.filtrado.png)             |
| Flexión isométrica    |    ![Imagen de EMG](plots/emg.fuerza.isometrica.png)   |  ![Imagen de EMG](plots/emg.fuerza.isometrica.filtrada.png)       |

#### Tabla resumen EEG 
| Campo        | Señal cruda                                                   | Señal + Wavelet                                                    |
|--------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Reposo        |![Imagen de EEG](plots/rest_original.png)         |![Imagen de EEG](plots/rest_wavelet.png)                |
| Apertura y cierre de ojos  |![Imagen de EEG](plots/o_close_original.png)               |![Imagen de EEG](plots/o_close_wavelet.png)                |
| Resolución de ejercicios matemáticos    |![Imagen de EEG](plots/math_original.png)     | ![Imagen de EEG](plots/math_wavelet.png)          |

#### Tabla espectrogramas EEG
Se utiliza una tabla de espectrograma en el caso de EEG para poder evaluar el efecto de la transformada wavelet estacionaria en las frecuencias de interés.

| Campo        | Señal cruda                                                   | Señal + Wavelet                                                    |
|--------------|---------------------------------------------------------------|---------------------------------------------------------------|
| Reposo        |![Imagen de EEG](plots/spect_rest_original.png)         |![Imagen de EEG](plots/spect_rest_wavelet.png)                |
| Apertura y cierre de ojos  |![Imagen de EEG](plots/spect_o_original.png)               |![Imagen de EEG](plots/spect_o_wavelet.png)                |
| Resolución de ejercicios matemáticos    |![Imagen de EEG](plots/spect_math_original.png)     | ![Imagen de EEG](plots/spect_math_wavelet.png)          |

### Discusión
<p align="justify"><b>Filtración de ECG:</b>
<p align="justify"> El filtrado de señales electrocardiográficas (ECG) mediante la transformada wavelet Daubechies 4 (db4) con umbral suave adaptativo ha mostrado mejoras significativas en la calidad de las señales. Esto se debe a que este tipo de filtrado ha demostrado ser eficaz en la eliminación de varios tipos de ruido que afectan las señales ECG, por ejemplo ruido de alta frecuencia, artefactos musculares y ruido de línea base [11]. Según Chatterjee et al. (2020), la aplicación de la transformada wavelet es particularmente efectiva para eliminar el ruido aditivo gaussiano blanco, artefactos musculares y ruido de interferencia de línea eléctrica, entre otros tipos de ruido compuesto​​. La señal ECG cruda, cuando se procesa con la transformada wavelet, muestra una reducción notable del ruido de alta frecuencia. Además, preserva las características morfológicas esenciales de la señal ECG, como el complejo QRS y las ondas P [11]. La técnica de wavelet Daubechies 4 con umbral suave adaptativo mantiene estas características como se observa en los resultados.

En nuestro estudio, utilizamos los siguientes valores de umbral para el filtrado wavelet: 0.49, 0.71, 1.18, 2.12 y 4.39. Estos umbrales fueron calculados en base a la desviación estándar de los coeficientes de la señal de entrada y una constante C. A diferencia del estudio de Alfaouri y Daqrouq [8], donde los umbrales varían entre 1 y 100, e incluso hasta 400, debido a una mayor desviación estándar de las señales utilizadas, nuestros umbrales son más bajos debido a la desviación estándar de nuestras señales (aproximadamente de 1 a 5). Además, seleccionamos una constante C de 0.01, a diferencia de su valor de 5, para evitar la pérdida de características morfológicas importantes de la señal. Esta adaptación fue necesaria debido a las diferencias en el nivel de ruido y las características de las señales capturadas, que en nuestro caso presentan mayor ruido por se capturadas por un dispositivo de bajo costo, el BITalino​​.

<p align="justify"><b>Filtración de EMG:</b>
<p align="justify"> El código que hemos desarrollado para la filtración de señales EMG utiliza la transformada wavelet para descomponer la señal en diferentes niveles de detalle y aplicar umbrales que reducen el ruido. El método wavelet-based descrito en el paper implica varios pasos clave. Primero, la señal EMG se descompone en varios niveles utilizando una transformada wavelet discreta (DWT), empleando wavelets como Daubechies (db4) debido a su eficacia en la detección de características musculares. Luego, se calcula un umbral para cada nivel de descomposición basado en el ruido presente en los coeficientes wavelet, determinado utilizando la desviación estándar del ruido y un factor multiplicativo para ajustar la rigurosidad de la filtración. Estos coeficientes wavelet se umbralizan mediante umbralización suave (soft thresholding) para reducir el ruido mientras se preservan las características importantes de la señal, ajustando el umbral multiplicando la estimación del ruido por un factor determinado. Finalmente, los coeficientes umbralizados se recomponen para formar la señal denoised, recuperando así una versión filtrada de la señal original. 
<p align="justify">Al aplicar este método a nuestras señales EMG, observamos resultados alentadores. La señal en reposo muestra una eliminación efectiva del ruido, transformándose en una línea horizontal, lo que confirma la eficacia del método. La señal con fuerza isométrica y la señal con contrafuerza también experimentan una reducción significativa del ruido sin alterar la estructura principal de la señal, lo que permite una mejor visualización de los picos y valles que representan las contracciones y relajaciones musculares. Ajustes adicionales en los parámetros del filtro, como el nivel de descomposición y el factor de umbralización, pueden optimizar aún más los resultados para diferentes tipos de señales y necesidades específicas de análisis. Estos resultados coinciden con otros estudios con metodos similares que utilizan umbrales, por ejemplo en el paper "Discrete wavelet transform based processing of embroidered textile-electrode electromyography signal acquired with load and pressure effect" [12] donde se demuestran la eficacia de las técnicas de umbralización de ondas para eliminar el ruido de las señales de sEMG y sugieren la elección correcta de la familia de ondas y el método de umbralización para mejores aplicaciones de eliminación de ruido.
<p align="justify"><b>Filtración de EEG:</b>
<p align="justify">Se puede observar un suavizado de la señal eletroencefalográfica como resultado del filtro de wavelet con las características planteadas. Como se puede apreciar en las imágenes de las señales de salida, tras utilizar la transformada de wavelet, la forma de la onda no considera las espículas que son influencia de frecuencias mayores en el espectro, el cual es visible a amplitudes bajas pero se pierde a amplitudes mayores, como las que se observan en la señal de apertura y cierre de ojos tratada con la transformada que contiene oscilaciones cuyo suavizado es menos notorio. El suavizado de la señal puede apreciarse de mejor forma en un espectrograma, donde se aprecia que las frecuencias por encima de los 50Hz se reducen en amplitud si están por debajo de un umbral de poder. Esto se correlaciona con la señal tratada con la transformada wavelet, la cual atenua más levemente porciones de la señal con amplitudes elevadas. Los resultados del trabajo de Zikov[10] muestran un suavizado de la imagen similar con la excepción de la atenuación de mesetas, las cuales se atenúan en gran manera dejando intactas las frecuencias menores. Las oscilaciones evaluadas en la instancia de apertura y cierre de ojos son demasiado pronunciadas para determinar la presencia de mesetas comparables al trabajo de Zikov. En los resultados obtenidos, la señal de entrada muestra oscilaciones muy pronunciadas en amplitud, lo cual podría afectar la capacidad de la transformada estacionaria de Wavelet de suavizar las mismas. 
<p align="justify">La literatura indica tres orígenes fisiológicos de ruido en las señales EEG. Los movimientos de ojo ocasionan un cambio en el campo eléctrico que rodea los mismos mediante la formación de dipolos en la retina y movimientos de las pestañas, generando potenciales en el cuero cabelludo [13]. Su espectro se sobrelapa con las ondas alfa del EEG en tareas mentales, y debido a su mayor amplitud, pueden llegar a suprimirlas [14].  Las señales electromiográficas son un ruido común en mediciones de ondas beta y gamma, y debido a su amplitud ocluyen la señal EEG a partir de los 20 Hz, siendo esta oclusión mayor a partir de los 50Hz. [15]. En el caso del trabajo de Zikov et al, este está enfocado en eliminar los artefactos causados por el movimiento de ojos, los que se presentan en un rango de frecuencias de 0-7 Hz mediante el filtrado de frecuencias menores. No obstante dependiendo de la zona estudiada, otros tipos de ruido pueden ser más prevalentes. La atenuación del ruido de la señal EEG debe considerar no solo el lugar sino las frecuencias de interés, puesto que los métodos de filtrado trabajan principalmente en el dominio de la frecuencia, y diversas fuentes de ruido pueden ser más o menos prevalentes dependiendo del lugar estudiado. Ese es el caso con este estudio, el cual evaluó señales EEG correspondientes a las áreas frontales Fp1 y Fp2, las cuales debido a su posición, tienen mayor contaminación por señales provenientes del movimiento de los ojos. Un análisis más completo de EEG, requeriría diversos tipos de filtros considerando el posicionamiento de los electrodos, el tipo de montaje y las características del paciente.   

### Bibliografía
<p align="justify">[1]  Martinek R, Ladrova M, Sidikova M, Jaros R, Behbehani K, Kahankova R, Kawala-Sterniuk A. Advanced Bioelectrical Signal Processing Methods: Past, Present and Future Approach-Part I: Cardiac Signals. Sensors (Basel). 2021 Jul 30;21(15):5186. doi: 10.3390/s21155186. PMID: 34372424; PMCID: PMC8346990. 
<p align="justify">[2] Adimulam, M. K., & Srinivas, M. . (2016). Modeling of EXG (ECG, EMG and EEG) non-idealities using MATLAB. 2016 9th International Congress on Image and Signal Processing, BioMedical Engineering and Informatics (CISP-BMEI). doi:10.1109/cisp-bmei.2016.7852968
<p align="justify">[3] C. S. Burrus, R. A. Gopinath, y H. Guo, Introduction to wavelets and wavelet transforms: A primer. Upper Saddle River, NJ, Estados Unidos de América: Pearson, 1997.
<p align="justify">[4] “Introduction to Wavelet Families - MATLAB & Simulink - MathWorks América Latina”, Mathworks.com. [En línea]. Disponible en: https://la.mathworks.com/help/wavelet/gs/introduction-to-the-wavelet-families.html.
<p align="justify">[5] “Wavelets: Multiscale edge detection and image denoising”, en Embedded Image Processing on the TMS320C6000TM DSP, Boston, MA: Springer US, 2005, pp. 281–378.
<p align="justify">[6] D. L. Donoho, “De-noising by soft-thresholding”, IEEE Trans. Inf. Theory, vol. 41, núm. 3, pp. 613–627, 1995.
<p align="justify">[7] PLUX – Wireless Biosignals, S.A., "Electrocardiography (ECG) Sensor Data Sheet," Rev. B, 2020. [Online]. Available: https://bitalino.com/storage/uploads/media/revolution-ecg-sensor-datasheet-revb-1.pdf. 
<p align="justify">[8] M. Alfaouri and K. Daqrouq, "ECG signal denoising by wavelet transform thresholding," American Journal of Applied Sciences, vol. 5, no. 3, pp. 276-281, 2008. doi: 10.3844/ajassp.2008.276.281.
<p align="justify">[9] Gradolewski, D., Tojza, P.M., Jaworski, J., Ambroziak, D., Redlarski, G., Krawczuk, M. (2015). Arm EMG Wavelet-Based Denoising System. In: Awrejcewicz, J., Szewczyk, R., Trojnacki, M., Kaliczyńska, M. (eds) Mechatronics - Ideas for Industrial Application. Advances in Intelligent Systems and Computing, vol 317. Springer, Cham. https://doi.org/10.1007/978-3-319-10990-9_26
<p align="justify">[10] T. Zikov, S. Bibian, G. A. Dumont, M. Huzmezan and C. R. Ries, "A wavelet based de-noising technique for ocular artifact correction of the electroencephalogram," Proceedings of the Second Joint 24th Annual Conference and the Annual Fall Meeting of the Biomedical Engineering Society] [Engineering in Medicine and Biology, Houston, TX, USA, 2002, pp. 98-105 vol.1, doi: 10.1109/IEMBS.2002.1134407.
<p align="justify">[11] S. Chatterjee, R. S. Thakur, R. N. Yadav, L. Gupta, y D. K. Raghuvanshi, "Review of noise removal techniques in ECG signals," IET Signal Processing, vol. 14, no. 9, pp. 569-590, 2020. doi: 10.1049/iet-spr.2020.0104.
<p align="justify">[12] Belay, Bulcha & Dawud, Ahmed & Malengier, B. & Sitek, Wojciech & Gemechu, Wendimu & Krishnamoorthy, Janarthanan & Van Langenhove, Lieva. (2024). Discrete wavelet transform based processing of embroidered textile-electrode electromyography signal acquired with load and pressure effect. Journal of Industrial Textiles. 54. 10.1177/15280837241232449. 
<p align="justify">[13] R. J. Croft and R. J. Barry, “Removal of ocular artifact from the EEG: a review,” Neurophysiologie clinique, vol. 30, no. 1, pp. 5–19, Feb. 2000, doi: https://doi.org/10.1016/s0987-7053(00)00055-1.
<p align="justify">[14] S. Zahan, "Removing EOG artifacts from EEG signal using noise-assisted multivariate empirical mode decomposition," 2016 2nd International Conference on Electrical, Computer & Telecommunication Engineering (ICECTE), Rajshahi, Bangladesh, 2016, pp. 1-5, doi: 10.1109/ICECTE.2016.7879634.
<p align="justify">[15] K. J. Pope et al., “Managing electromyogram contamination in scalp recordings: An approach identifying reliable beta and gamma EEG features of psychoses or other disorders,” Brain and behavior, vol. 12, no. 9, Aug. 2022, doi: https://doi.org/10.1002/brb3.2721.