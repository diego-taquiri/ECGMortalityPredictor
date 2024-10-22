# Tratamiento de señal EEG
Lista de participantes:  
- Mantilla M., Ana Belen  
- Valdivia E., Erick Alexander   
- Flórez T., Armando Antonio  
- Taquiri D., Diego Alejandro

## Tabla de contenidos
1. [Introducción](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#introducci%C3%B3n)
2. [Objetivos específicos de la práctica](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#objetivos-espec%C3%ADficos-de-la-pr%C3%A1ctica)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#materiales-y-m%C3%A9todos)
5. [Resultados](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#resultados)
6. [Discusión](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#discusi%C3%B3n)
7. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/Procesamiento_EEG.md#bibliograf%C3%ADa)

### Introducción
<p align="justify"> La electroencefalografía (EEG) es un método de imagenología cerebral no invasivo en el que se colocan electrodos sobre el cuero cabelludo para registrar la actividad eléctrica del cerebro. Este proceso permite a los investigadores medir y estudiar las señales eléctricas generadas por el cerebro, proporcionando así información crucial sobre su funcionamiento. Esta técnica es fundamental para identificar trastornos neurológicos diversos y para investigar procesos cognitivos como la percepción, la atención y la memoria. [1] Existen cinco ondas cerebrales principales que se distinguen por sus diferentes rangos de frecuencia. Estas bandas de frecuencia, de bajas a altas respectivamente, se denominan alpha (α), theta (θ), beta (β), delta (δ) y gamma (γ). [2]

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/images/rythms.png" alt="Descripción de la imagen" width="400"><br> 
<p align="center"><b>Figura 1.</b> Ritmos cerebrales dominantes típicos. La onda delta se observa en bebés y adultos durante el sueño, la onda theta en niños y adultos durante el sueño, la onda alfa se detecta en la región occipital del cerebro cuando no hay atención, y la onda beta aparece frontal y parietalmente con baja amplitud. [2] <br> 
  
<p align="justify"> Para identificar y analizar de manera precisa las señales de EEG, es necesario tener un profundo conocimiento de sus propiedades complejas y teóricas, así como realizar la extracción de características relevantes. Sin embargo, las señales de EEG presentan desafíos significativos debido a sus características únicas. Estos desafíos incluyen la susceptibilidad al ruido, su naturaleza no lineal y la falta de conformidad con una distribución normal, además de factores individuales como la edad, la psicología y el entorno. Las propiedades distintivas de las señales de EEG representan un desafío para extraer información relevante sobre tareas específicas directamente de ellas. Por lo tanto, es crucial desarrollar diversas metodologías para el análisis de estas señales e investigar técnicas de aprendizaje automático para mejorar la comprensión de las señales de EEG. [1]

<p align="justify"> En general, el procesamiento de señales EEG tiene como objetivo traducir las señales EEG crudas en la clase de estas señales. Esta traducción generalmente se logra utilizando un enfoque de reconocimiento de patrones, cuyos pasos se pueden observar en la siguiente imagen. [3]

<p align="center">
<img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2013/images/processing.png" alt="Descripción de la imagen" width="500"><br> 
<p align="center"><b>Figura 2.</b> El análisis de señales EEG implica cuatro etapas: adquisición, eliminación de ruido, ingeniería de características y clasificación. [1] <br> 
  
<p align="justify"> La adquisición de la señal se suele realizar según ha sido estipulado por La Federación Internacional de Sociedades de Electroencefalografía y Neurofisiología Clínica, quien ha recomendado un ajuste convencional de electrodos (también llamado 10-20) para 21 electrodos (excluyendo los electrodos de lóbulo de la oreja). [2] Para iniciar con el tratamiento, después de la adquisición, se realiza un pipeline de filtrado y preprocesamiento (normalización y alineación), el cual es un conjunto de métodos aplicados a grabaciones crudas de EEG, destinados a preparar las señales para un análisis posterior y más específico. Puede incluir varios pasos en los que existen diferentes opciones, donde la selección de los algoritmos y herramientas "más apropiados" no es directa. [4] Esto es importante debido a lo siguiente [5]:
  
1. <p align="justify"> Las señales recogidas desde el cuero cabelludo no necesariamente son una representación precisa de las señales que provienen del cerebro.
2. <p align="justify"> Los datos de EEG contienen mucho ruido que puede ocultar señales de EEG más débiles.
3. <p align="justify"> Artefactos como parpadeos o movimientos musculares pueden contaminar los datos y distorsionar la imagen.
4. <p align="justify"> Queremos separar las señales neurales relevantes de la actividad aleatoria que ocurre durante las grabaciones de EEG.

<p align="justify"> Seguido a ello se tienen 2 pasos principales [3]:
  
- <p align="justify"> Extracción de características: Tiene como objetivo describir las señales EEG mediante idealmente unos pocos valores relevantes llamados "características", las cuales deben capturar la información incrustada en las señales EEG que es relevante para describir los estados mentales a identificar, mientras se rechaza el ruido y otra información no relevante. Todas las características extraídas generalmente se organizan en un vector conocido como vector de características.
  
- <p align="justify"> Clasificación: Asigna una clase a un conjunto de características extraído de las señales, la cual corresponde al tipo de investigación identificado. Este paso también puede ser denominado "traducción de características" y a sus algoritmos se les conoce como "clasificadores".

<p align="justify"> Las señales EEG pueden ser procesadas en dominios de tiempo, frecuencia o espaciales, ofreciendo medios multidimensionales para interpretar las actividades cerebrales. Además de proporcionar información invaluable, las señales EEG tienen la ventaja de capturar patrones neurales complejos a alta velocidad. Como método confiable, portátil y no invasivo para medir la actividad eléctrica en el cerebro, el EEG es una metodología central para la investigación asequible y práctica, así como una herramienta prometedora en la atención clínica. [6]

### Objetivos específicos de la práctica
- <p align="justify">Aplicar técnicas avanzadas de filtrado para reducir el ruido y eliminar artefactos en las señales EEG, asegurando que la señal esté limpia y lista para un análisis más detallado.
- <p align="justify">Normalizar y alinear las señales EEG durante el preprocesamiento para garantizar la consistencia y comparabilidad entre las sesiones o sujetos, preparando las señales para una extracción eficaz de características.
- <p align="justify">Implementar métodos de extracción de características utilizando análisis Wavelet (continuo o discreto) para identificar las características más informativas y relevantes de las señales EEG que pueden estar relacionadas con estados mentales específicos o respuestas cognitivas.
- <p align="justify">Desarrollar y aplicar técnicas de feature engineering para optimizar las características extraídas, mejorando así la precisión y eficacia de los modelos de machine learning utilizados en la clasificación de patrones de actividad cerebral.
- <p align="justify">Explorar el uso de MNE-Python para integrar y analizar datos desde múltiples dominios (tiempo, frecuencia, espacio), facilitando una comprensión holística de las dinámicas cerebrales.

### Materiales y métodos
<p align="justify"> El laboratorio se enfoca en el análisis avanzado de datos neurofisiológicos humanos utilizando herramientas modernas y metodologías innovadoras. En particular, utilizamos el paquete de código abierto en Python conocido como MNE-Python. Esta herramienta permite explorar, visualizar y analizar una variedad de datos neurofisiológicos, incluyendo MEG, EEG, sEEG, ECoG, NIRS, entre otros. [7] MNE-Python no solo facilita la manipulación y procesamiento de grandes volúmenes de datos, sino que también ofrece herramientas robustas para la extracción de características, el análisis espectral y la clasificación de patrones. El objetivo de esta herramienta es implementar y proporcionar un conjunto de algoritmos que permitan a los usuarios ensamblar flujos completos de análisis de datos que abarquen la mayoría de las fases del procesamiento de datos M/EEG. [8]

#### Adquisición de datos
Para la adquisición de datos EEG, se utilizó la Siena Scalp EEG Database de PhysioNet, que contiene registros de 14 pacientes (9 hombres, 5 mujeres, edades 20-71) con epilepsia. Las señales se obtuvieron utilizando amplificadores EB Neuro y Natus Quantum LTM, con electrodos de copa reutilizables siguiendo el sistema internacional 10-20, y un total de 32 canales EEG con una frecuencia de muestreo de 512 Hz. Los datos, organizados en formato EDF, incluyen episodios epilépticos clasificados según los criterios de la Liga Internacional Contra la Epilepsia y se almacenan en carpetas individuales para cada paciente. Además, los registros incluyen señales de EKG y detalles sobre la lateralización de los episodios. Los pacientes dieron su consentimiento informado y la aprobación ética fue otorgada por la Universidad de Siena [9].

#### Preprocesamiento

Para el preprocesamiento de los datos EEG, seleccionamos el archivo correspondiente al primer paciente (PN00-1.edf). Este archivo contiene un episodio de epilepsia que recortamos para analizar específicamente la señal de interés. Recortamos la señal para tomar solo el episodio epiléptico que dura 1 minuto y 10 segundos.

```python
# Define the path to your .edf file
edf_file_path = 'PN00-1.edf'  # Replace with the actual file name if it's in the same directory

# Load the EDF file
raw = mne.io.read_raw_edf(edf_file_path, preload=True)

# Crop the raw data to take only the epilepsy episode
raw.crop(tmin=1143, tmax=1213)
```

Luego, seleccionamos solo los canales EEG, excluyendo cualquier canal marcado como "malo". También renombramos los canales según el sistema estándar 10-20 para asegurar la consistencia y compatibilidad con las herramientas de análisis EEG.

Para la digitalización, agregamos las coordenadas espaciales a cada electrodo utilizando el montaje estándar 10-20, lo que es crucial para los análisis espaciales posteriores. Además, excluimos ciertos canales que no son relevantes para el análisis EEG, como aquellos utilizados para monitoreo cardíaco y otros propósitos auxiliares.

```python
# Drop non-brain channels which are not used in EEG brain signal analysis
raw.drop_channels(['ECG', 'SPO2', 'HR', '1', '2', 'MK'])

# Define a standard montage (10-20 system)
montage = mne.channels.make_standard_montage('standard_1020')
```

#### Filtrado

Para mejorar la calidad de las señales EEG, se realizó un proceso de filtrado y eliminación de artefactos. Inicialmente, se aplicaron filtros notch para eliminar el ruido de la línea de alimentación a 50 Hz y sus armónicos, mejorando la precisión del análisis posterior.
```python

# Apply notch filter to remove power line noise at 50 Hz
raw.notch_filter(freqs=50.0, notch_widths=1.0)

# Apply notch filter to remove power line noise at 150.0 Hz
raw.notch_filter(freqs=150.0, notch_widths=1.0)
```
Posteriormente, se aplicó un filtro pasa-altas con una frecuencia de corte de 1 Hz para eliminar componentes de baja frecuencia.


```python
# ICA works best with a highpass filter applied
raw.filter(l_freq=1.0, h_freq=None)
```

Posteriormente, se empleó un Análisis de Componentes Independientes (ICA) utilizando 10 componentes. Este número de componentes fue ajustado de acuerdo al número de canales disponibles, que son 32.

```python
ica = mne.preprocessing.ICA(
    n_components=10, method="picard", max_iter="auto", random_state=97
)
ica.fit(raw)
```
Para identificar manualmente los artefactos, se plotearon las propiedades de las componentes ICA seleccionadas. Inicialmente, se visualizaron las componentes para identificar señales sospechosas de ser artefactos, como las señales musculares.

```python
idx = [0, 1, 2, 4, 9]
ica.plot_properties(raw, picks=idx, log_scale=True)

artifacts_idx = [3,5,6,7,8]
ica.plot_properties(raw, picks=artifacts_idx, log_scale=True)
```
Adicionalmente, se utilizó un algoritmo automático para detectar artefactos musculares. Los índices de las componentes ICA identificadas automáticamente como artefactos fueron comparados con los manualmente seleccionados.

```python
muscle_idx_auto, scores = ica.find_bads_muscle(raw)
ica.plot_scores(scores, exclude=muscle_idx_auto)
print(
    f"Manually found muscle artifact ICA components:      {artifacts_idx}\n"
    f"Automatically found muscle artifact ICA components: {muscle_idx_auto}"
)
```
Una vez identificados los artefactos, se aplicó el ICA para eliminar estos componentes y reconstruir la señal EEG.
```python
ica.apply(raw)
ica.plot_overlay(raw, exclude=artifacts_idx)
```
Finalmente, se compararon las señales originales y filtradas para verificar la efectividad de la eliminación de artefactos, asegurando que la señal reconstruida estuviera libre de las interferencias detectadas.

#### Feature extraction-Kurtosis y Entropía
A traves del proceso de extracción de propiedades, se busca obtener las variables de kurtosis y entropia. Desde la perspectiva del procesamiento estadístico de señales, los datos de EEG son tan irregulares que pueden considerarse como señales casi gaussianas, mientras que los de los pacientes con condiciones cerebrales son tan regulares que pueden considerarse como señales significativamente gaussianas. Por lo tanto, las señales de EEG pueden evaluarse en términos de su nivel de "gaussianidad", que se cuantifica mediante su valor de Kurtosis (una medida de la no gaussianidad). Cuanto menor sea el valor absoluto de la curtosis, más cercana será la señal a una distribución gaussiana, y viceversa [10]. Por otro lado, la entropía es una medida de la dispersión de los datos. Los datos con una distribución de probabilidad amplia y plana tendrán una entropía alta. Por otro lado, los datos con una distribución estrecha y con un pico tendrán una entropía baja. Aplicado al EEG, la entropía es el descriptor estadístico de la variabilidad dentro de la señal EEG. [11]
Para realizar la extracción de estas caracteristicas de la señal filtrada se siguen los siguientes pasos: 

- Segmentación de Datos en Épocas:
```python
epoch_length = 1  # en segundos
epoch_samples = int(epoch_length * fs)

def segment_data(data, epoch_samples):
    n_samples = data.shape[0]
    n_epochs = n_samples // epoch_samples
    return data[:n_epochs * epoch_samples].reshape(n_epochs, epoch_samples)

channel_epochs = segment_data(channel_data, epoch_samples)
```
Aquí se define la longitud de cada época (epoch_length) en segundos y se calcula el número de muestras por época (epoch_samples) utilizando la frecuencia de muestreo (fs). La función segment_data divide los datos del canal EEG (channel_data) en épocas de longitud epoch_samples, creando así la matriz channel_epochs donde cada fila representa una época y cada columna las muestras de esa época.

- Cálculo de Kurtosis y Entropía:
```python
kurtosis_features = np.zeros(channel_epochs.shape[0])
entropy_features = np.zeros(channel_epochs.shape[0])

for i in range(channel_epochs.shape[0]):
    kurtosis_features[i] = kurtosis(channel_epochs[i])
    epoch_normalized = (channel_epochs[i] - np.min(channel_epochs[i])) / (np.max(channel_epochs[i]) - np.min(channel_epochs[i]))
    hist, _ = np.histogram(epoch_normalized, bins='auto', density=True)
    prob_density = hist / np.sum(hist)
    entropy_features[i] = scipy_entropy(prob_density)
```
Se proporciona una explicación detallada del procesamiento de datos EEG desde un archivo EDF ("PN00-1.edf"), donde se calcula la curtosis y la entropía para el primer canal, seguido de la representación gráfica de estas características. Se comienza importando las librerías necesarias: pyedflib para leer archivos EDF, numpy para operaciones matemáticas y manejo de matrices, scipy.stats para funciones estadísticas como kurtosis y entropy, y matplotlib.pyplot para la visualización de datos. Luego, se carga el archivo EDF especificado, se obtienen el número de canales y la frecuencia de muestreo, y se lee y almacena los datos del primer canal. Posteriormente, se segmentan estos datos en épocas de un segundo de longitud. Para cada época, se calcula la curtosis y la entropía: la curtosis evalúa la "gaussianidad" de la señal EEG, mientras que la entropía describe la variabilidad dentro de la misma. 

- Graficación de Características:
```python
def plot_features(features, feature_name):
    plt.figure(figsize=(15, 5))
    plt.plot(features)
    plt.title(f'{feature_name} across epochs for the first channel')
    plt.xlabel('Epoch')
    plt.ylabel(feature_name)
    plt.show()

plot_features(kurtosis_features, 'Kurtosis')
plot_features(entropy_features, 'Entropy')
```
La función plot_features se define para crear gráficos de línea que representan las características (curtosis o entropía) a lo largo de las épocas. Se utiliza matplotlib.pyplot para visualizar los datos. Primero se grafican las características de la curtosis y luego las características de la entropía para el primer canal.

#### Feature extraction-Power Spectral Density (PSD)
La obtención de Densidad Espectral de Poder o PSD se obtuvo mediante el análisis de la transformada de Fourier en tiempo corto o STFT, y la determinación de un espectrograma a partir de los índices en tiempo y frecuencia y la segmentación en ventanas tal y como se describe en el trabajo de Zabidi et al. [12] Python ofrece herramientas para realizar este análisis en la forma de la función Spectrogram, previa conversión a rango de decibeles. El código utilizado es, por tanto, el siguiente a partir de la señal filtrada. 

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram, periodogram, welch, iirnotch, filtfilt

    plt.figure(figsize=(12, 10))
    frequencies, times, spectrogram_orig = spectrogram(signal  , fs= sampling_frequency)
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_orig), shading='gouraud', cmap='jet', vmin=-200, vmax=0)
    plt.title('Espectrograma de señal EEG original')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Frecuencia (Hz)')
    plt.colorbar(label='Densidad Espectral de Poder (dB)')
    plt.tight_layout()
```

### Resultados
<p align="center">
<img src="./images/raw-data.png" alt="Ploteo de la señal EEG cruda" width="700"><br>
<p align="center"><b>Figura 3.</b> Ploteo de la señal de electroencefalograma (EEG) cruda del paciente, mostrando la extracción del episodio de epilepsia a través de los 29 canales.</p>

<p align="center">
<img src="./images/ica-components.png" alt="Ploteo de los componentes ICA de la señal EEG" width="700"><br>
<p align="center"><b>Figura 4.</b> Ploteo de los 10 componentes ICA (Análisis de Componentes Independientes) de la señal EEG del paciente, mostrando el resultado del filtrado de la señal.</p>

<p align="center">
<img src="./images/ica000.png" alt="Ploteo del ICA 0" width="700"><br>
<p align="center"><b>Figura 5.</b> Ploteo del componente ICA 0 de la señal EEG. </p>

<p align="center">
<img src="./images/ica006.png" alt="Ploteo del ICA 6" width="700"><br>
<p align="center"><b>Figura 6.</b> Ploteo del componente ICA 6 de la señal EEG. Artefacto liminado mediante el análisis ICA.</p>

<p align="center">
<img src="./images/artifacts.png" alt="Identificación de artefactos manuales y automáticos" width="700"><br>
<p align="center"><b>Figura 7.</b> Identificación de artefactos en la señal EEG. Los artefactos identificados automáticamente como de músculo son los componentes 6, 7 y 9.</p>

<p align="center">
<img src="./images/signal-before-after-cleaning.png" alt="Señal EEG antes y después de la limpieza" width="700"><br>
<p align="center"><b>Figura 8.</b> Reconstrucción de la señal EEG antes (en rojo) y después (en negro) de la limpieza. La señal después de la limpieza muestra la eliminación de los componentes ICA reconocidos como artefactos</p>

<p align="center">
<img src="./images/eeg-kurtosis.png" alt="Kurtosis de la señal EEG" width="700"><br>
<p align="center"><b>Figura 9.</b> Kurtosis de la señal EEG

<p align="center">
<img src="./images/eeg-entropy.png" alt="Entropia de la señal EEG" width="700"><br>
<p align="center"><b>Figura 10.</b> Entropia de la señal EEG

<p align="center">
<img src="./images/PSD.jpeg" alt="Espectrograma de señal" width="700"><br>
<p align="center"><b>Figura 11.</b> PSD de señal EEG visualizado mediante espectrograma.
  

### Discusión
<p align="justify"> Se realizó un análisis detallado de los componentes ICA obtenidos a partir de la señal EEG del paciente. El componente ICA 0 exhibe un patrón focalizado en el hemisferio derecho, lo cual sugiere una actividad neuronal específica relacionada con la lateralización hemisférica derecha en el contexto de la epilepsia. Este hallazgo es consistente con la literatura que indica una asociación entre la actividad focalizada y los eventos epilépticos en el hemisferio derecho. 
<p align="justify"> Por otro lado, el componente ICA 6 se identificó como un artefacto significativo que fue correctamente eliminado mediante el análisis ICA. Este artefacto probablemente estaba relacionado con interferencias musculares u otros artefactos no cerebrales que afectan la señal EEG. La eliminación eficaz de este componente ha mejorado notablemente la calidad de la señal, permitiendo una interpretación más precisa y confiable de la actividad cerebral subyacente. Durante el proceso de análisis, se identificaron automáticamente varios artefactos, incluidos los componentes 6, 7 y 9, que se asociaron con actividad muscular. Además, se realizaron identificaciones manuales adicionales de otros artefactos presentes en la señal EEG. Este enfoque combinado de detección automática y manual aseguró una limpieza exhaustiva de la señal, suavizando contaminaciones que pudieran distorsionar la interpretación de los datos. La comparación entre la señal EEG vista en la figura 8, antes (en rojo) y después (en negro) de la limpieza muestra claramente los beneficios del análisis ICA en la eliminación de artefactos. La señal post-limpieza exhibe una reducción significativa en la interferencia de artefactos, resultando en una señal más acorde a la actividad cerebral evaluada. 
<p align="justify"> Debido a que se está utilizando señales EEG de pacientes con epilepsia, se deben tener consideraciones particulares referentes a las manifestaciones de la enfermedad. Estas pueden tener un componente muscular debido a las contracciones en convulsiones tónico clónicas[13], variabilidad cardiaca notable en crisis convulsivas [14] y movimientos bruscos del ojo en el caso de nistagmo [15]. El análisis de ICA,en este trabajo se ha utilizado para aislar las señales EEG de ruidos ocasionados por señales fisiológicas, las cuales ofuscan la señal buscada, ya que en condiciones patológicas, tienen una presencia mayor y más errática en las crisis del paciente con epilepsia. Asimismo, estas manifestaciones permiten ofrecer indicios sobre el pronóstico de la enfermedad a partir de la gravedad de las mismas. Su valor diagnóstico hace que no sea conveniente eliminarlas mediante métodos tradicionales, razón por la que ICA es ideal para aislar dichas señales en lugar de eliminarlas, si se deseara realizar el análisis de todos los componentes de la señal. Si bien no es muy usado, asimismo ICA puede ser usado como herramienta predictiva [16].
<p align="justify"> Los estudios como el de Harpale[16] y Kannathal[11] muestran que  pacientes con epilepsia pueden exhibir cambios significativos en los valores de kurtosis y entropía en comparación con individuos sanos. La kurtosis, como medida de la "gaussianidad" de la señal EEG, tiende a ser más alta en pacientes con epilepsia. Esto sugiere una mayor concentración de eventos neuronales específicos, como picos de actividad relacionados con descargas epileptiformes o actividad sincrónica anormal dentro de las redes neuronales afectadas. Por otro lado, la entropía, que describe la complejidad y la irregularidad de la señal, puede mostrar variaciones. En algunos estudios, se ha observado que la entropía puede ser menor en pacientes con epilepsia en comparación con individuos sanos. Esto puede reflejar una menor variabilidad o una organización más rígida de la actividad neuronal, posiblemente debido a la presencia de actividad epileptiforme que podría reducir la aleatoriedad y la complejidad temporal de la señal EEG. Estos cambios en kurtosis y entropía pueden ser indicativos de alteraciones en la dinámica neuronal y la organización funcional del cerebro en pacientes con epilepsia. La mayor kurtosis podría ser un marcador de eventos epileptiformes distintivos, mientras que la menor entropía podría sugerir una reducción en la variabilidad de la actividad neuronal normal [17]. Estas características pueden ser utilizadas no solo para diagnosticar la epilepsia, sino también para monitorear la respuesta al tratamiento y evaluar el pronóstico de los pacientes.
<p align="justify"> Las crisis convulsivas, debido a su naturaleza transitoria y errática hacen que evaluar el EEG del paciente no pueda darse únicamente en la detección de ondas en el dominio de la frecuencia y basado en la ubicación de los electrodos. Se necesita un componente de tiempo en la evaluación por lo que la visualización mediante un espectrograma del PSD del paciente permite evaluar los periodos de tiempo correspondientes a convulsiones. Como se puede observar en la figura 11, esto resulta de gran utilidad para detectar eventos de interés, los cuales resaltan en el estudio y son fácilmente delimitables. Trabajos como el de Liu et al [18] han planteado aprovechar las características de la señal para generar modelos predictivos, lo cual resultaría de gran utilidad en futuro tratamiento de la enfermedad. 


### Bibliografía
<p align="justify"> [1] A. Chaddad, Y. Wu, R. Kateb, y A. Bouridane, “Electroencephalography signal processing: A comprehensive review and analysis of methods and techniques”, Sensors (Basel), vol. 23, núm. 14, p. 6434, 2023.
<p align="justify"> [2] S. Sanei y J. A. Chambers, EEG signal processing. Wiley, 2007.
<p align="justify"> [3] F. Lotte, “A tutorial on EEG signal-processing techniques for mental-state recognition in brain–computer interfaces”, en Guide to Brain-Computer Music Interfacing, London: Springer London, 2014, pp. 133–161.
<p align="justify"> [4] S. Coelli et al., “Selecting methods for a modular EEG pre-processing pipeline: An objective comparison”, Biomed. Signal Process. Control, vol. 90, núm. 105830, p. 105830, 2024.
<p align="justify"> [5] “Introduction to EEG-preprocessing”, Github.io. [En línea]. Disponible en: https://g0rella.github.io/gorella_mwn/preprocessing_eeg.html.
<p align="justify"> [6] Y. Tran, EEG signal processing for biomedical applications. MDPI, 2023.
<p align="justify"> [7] E. Larson et al., MNE-Python. Zenodo, 2024.
<p align="justify"> [8] A. Gramfort, “MEG and EEG data analysis with MNE-Python”, Front. Neurosci., vol. 7, 2013.
<p align="justify"> [9] Detti P. Siena Scalp EEG Database (version 1.0.0). PhysioNet. 2020. Available from: https://doi.org/10.13026/5d4a-j060.
<p align="justify"> [10] Wang, G., Shepherd, S. J., Beggs, C. B., Rao, N., & Zhang, Y. (2015). The use of kurtosis de-noising for EEG analysis of patients suffering from Alzheimer’s disease. Bio-Medical Materials and Engineering, 26(s1), S1135–S1148. doi:10.3233/bme-151410 
<p align="justify"> [11] Kannathal, N., Choo, M. L., Acharya, U. R., & Sadasivan, P. K. (2005). Entropies for detection of epilepsy in EEG. Computer Methods and Programs in Biomedicine, 80(3), 187–194. doi:10.1016/j.cmpb.2005.06.012 
<p align="justify"> [12] A. Zabidi, W. Mansor, Y. K. Lee and C. W. N. F. Che Wan Fadzal, "Short-time Fourier Transform analysis of EEG signal generated during imagined writing," 2012 International Conference on System Engineering and Technology (ICSET), Bandung, Indonesia, 2012, pp. 1-4, doi: 10.1109/ICSEngT.2012.6339284.
<p align="justify"> [13] S. T. Sarmast, Abba Musa Abdullahi, and N. Jahan, “Current Classification of Seizures and Epilepsies: Scope, Limitations and Recommendations for Future Action,” Curēus, Sep. 2020, doi: https://doi.org/10.7759/cureus.10549.
<p align="justify"> [14] G. Costagliola, A. Orsini, M. Coll, R. Brugada, P. Parisi, and P. Striano, “The brain–heart interaction in epilepsy: implications for diagnosis, therapy, and SUDEP prevention,” Annals of clinical and translational neurology, vol. 8, no. 7, pp. 1557–1568, May 2021, doi: https://doi.org/10.1002/acn3.51382.
<p align="justify"> [15] K.-S. Kim, Young Hyo Kim, Y. Hwang, B. Kang, Dong Hyun Kim, and Young Se Kwon, “Epileptic Nystagmus and Vertigo Associated with Bilateral Temporal and Frontal Lobe Epilepsy,” Clinical and experimental otorhinolaryngology, vol. 6, no. 4, pp. 259–259, Jan. 2013, doi: https://doi.org/10.3342/ceo.2013.6.4.259.
<p align="justify"> [16] V. K. Harpale y V. K. Bairagi, «Significance of Independent Component Analysis (ICA) for Epileptic Seizure Detection Using EEG Signals», en Proceedings of the International Conference on Data Engineering and Communication Technology, vol. 469, S. C. Satapathy, V. Bhateja, y A. Joshi, Eds., en Advances in Intelligent Systems and Computing, vol. 469. , Singapore: Springer Singapore, 2017, pp. 829-838. doi: 10.1007/978-981-10-1678-3_80.
<p align="justify"> [17]‌ Rosas, Georgina & Santillán Guzmán, Alina. (2017). Detección de Eventos Epilépticos de Ausencia usando Cálculos Estadísticos. 
<p align="justify"> [18]‌ S. Liu, J. Wang, S. Li and L. Cai, "Epileptic Seizure Detection and Prediction in EEGs Using Power Spectra Density Parameterization," in IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 3884-3894, 2023, doi: 10.1109/TNSRE.2023.3317093.