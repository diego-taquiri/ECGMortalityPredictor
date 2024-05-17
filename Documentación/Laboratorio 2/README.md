# Fibrilación Auricular

### Tabla de contenidos
1. [Definición de la arritmia](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%201/README.md#definici%C3%B3n-de-la-arritmia)
2. [Contexto nacional y mundial](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%201/README.md#contexto-nacional-y-mundial)
4. [Planteamiento del problema](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%201/README.md#planteamiento-del-problema)
5. [Propuesta de solución](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%201/README.md#propuesta-de-soluci%C3%B3n)
6. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%201/README.md#bibliograf%C3%ADa)
   
## Definición de la arritmia
La definición de este tipo de arritmia describe un ritmo cardíaco irregular y anormal que causa latidos muy rápidos. Los síntomas de esta arritmia incluyen palpitaciones, dolor en el pecho, mareos, fatiga, aturdimiento, menor capacidad para hacer ejercicio, falta de aire y debilidad. Posibles causas pueden ser defectos congénitos, enfermedades cardíacas, presión arterial alta, enfermedades pulmonares, trastornos de la tiroides y factores de estilo de vida, como el consumo excesivo de alcohol y tabaco. [1]
## Contexto nacional y mundial
Es importante recalcar que la fibrilación auricular es la arritmia más prevalente  en el mundo con una prevalencia mundial estimada del 2% a 4% en adultos y se incrementa hasta el 10% en pacientes mayores de 80 años. [2] Datos nacionales indican que esta es la enfermedad vascular más común entre varones con un 21.6 % y un 7% en mujeres y que en más de la mitad de los casos es una fibrilación permanente. Cabe mencionar que en un 85.5% de casos un EKG es utilizado para el diagnóstico de la arritmia. [3]

## Planteamiento del problema
La monitorización ambulatoria con electrocardiografía externa es eficaz como herramienta de diagnóstico basada en evidencia cuando la sospecha de arritmia cardíaca es alta. [4] Actualmente, se utiliza el monitor Holter de 12 derivaciones para establecer el origen de arritmias, ya que es muy preciso y puede diagnosticar instantáneamente fibrilación auricular. [5]

La transformación de la arritmia basada en dispositivos de seguimiento desde el lanzamiento del primer monitor Holter cambió la forma en que se rastrean los ritmos cardíacos fuera del hospital. Después de mejoras y avances continuos, el Holter tiene el tamaño de un teléfono celular pequeño y proporciona 2 tipos de datos primarios para analizar. [5]

Sin embargo, los avances en tecnología, evidencia científica, y las preferencias del paciente/consumidor van cambiando la forma en que se presta la atención sanitaria. [5] Aunque el "estándar de oro" para evaluar las anomalías del ritmo cardíaco sigue siendo un Holter de 12 derivaciones, existe un interés cada vez mayor en los dispositivos de monitorización portátiles que brindan la oportunidad de evaluar el ritmo cardíaco en entornos del mundo real, como el lugar de trabajo o el hogar. [6] 

Además, aunque el ECG es fundamental en la práctica, se ha argumentado que su interpretación puede ser un arte en extinción. Esto puede contribuir a imprecisiones en el diagnóstico, lo cual no se limita sólo a un simple retraso en el diagnóstico, sino también en el tratamiento. Las imprecisiones no son consistentes en todos los estados patológicos, estas varían significativamente en precisión según el ritmo electrocardiográfico subyacente. [7]

Entonces, ¿cómo podríamos diseñar un dispositivo más compacto que mantenga la precisión característica del monitor Holter de 12 derivaciones, considerando aspectos como la miniaturización de componentes electrónicos, algoritmos de procesamiento de señales avanzados e integración de tecnología inalámbrica para evitar irritar la piel subyacente, con el objetivo de mejorar la comodidad y la portabilidad para el monitoreo ambulatorio del ritmo cardíaco en entornos del mundo real?

## Propuesta de solución
Como propuesta de solución, se propone adquirir una señal electrocardiográfica a partir de 1 derivación y evaluar la señal obtenida mediante el análisis en dominio de  frecuencia de la señal de ECG, con el objetivo de determinar la posibilidad de realizar el diagnóstico de fibrilación auricular a partir de diferencias en las frecuencias obtenidas.

El análisis en dominio de frecuencia es la identificación de patrones de frecuencia visibles tras someter la señal de ECG a una transformación del dominio del tiempo al dominio de la frecuencia [8], lo que tradicionalmente se logra mediante la transformada rápida de Fourier (FFT) o la transformada Wavelet. Esta ofrece algunas ventajas en comparación con el método de diagnóstico tradicional, para el cual detección temprana de fibrilación auricular requiere de un análisis de hasta 72 horas de monitoreo continuo.[8] Puede utilizarse para estimar la tasa de activación auricular en fibrilación auricular[9]. Esto permite identificar características de la enfermedad sin la necesidad de recurrir al análisis del ritmo en el tiempo, que es tradicionalmente utilizado por los especialistas al momento de interpretar ECG. 

### Bibliografía

1. Mayo Clinic. “Fibrilación auricular - Síntomas y causas - Mayo Clinic”. Top-ranked Hospital in the Nation - Mayo Clinic. [En línea]. Disponible: https://www.mayoclinic.org/es/diseases-conditions/atrial-fibrillation/symptoms-causes/syc-20350624#:~:text=La%20fibrilación%20auricular%20es%20un,coágulos%20sanguíneos%20en%20el%20corazón
2. J. E. Valdiviezo. “Factores asociados al éxito agudo de cardioversión eléctrica o farmacológica en pacientes con fibrilación auricular de reciente diagnóstico. Hospital Nacional Arzobispo Loayza 2023 – 2024”. Universidad Nacional Mayor de San Marcos. [En línea]. Disponible: https://cybertesis.unmsm.edu.pe/bitstream/handle/20.500.12672/20604/Valdiviezo_cj.pdf?sequence=1&amp;isAllowed=y 
3. J. Gallegos. “Registro Peruano de Fibrilación Auricular (REPERFA). Reporte preliminar.” Hospital Militar Central. [En línea]. Disponible: https://sopecard.org/wp-content/uploads/2021/08/Registro-Peruano-de-Fibrilacion-Auricular.pdf
4. A. Mubarik y A. M. Iqbal, “Holter Monitor”, StatPearls, 2022.
5. A. N. Sharma y A. Baranchuk, “Ambulatory external electrocardiography monitoring: Holter, extended Holter, mobile cardiac telemetry monitoring”, Card. Electrophysiol. Clin., vol. 13, núm. 3, pp. 427–438, 2021.
6. S. S. Lobodzinski, “ECG patch monitors for assessment of cardiac rhythm abnormalities”, Prog. Cardiovasc. Dis., vol. 56, núm. 2, pp. 224–229, 2013.
7. N. Rafie, A. H. Kashou, y P. A. Noseworthy, “ECG interpretation: Clinical relevance, challenges, and advances”, Hearts (Basel), vol. 2, núm. 4, pp. 505–513, 2021.
8. Y. Hu, Y. Zhao, J. Liu, J. Pang, C. Zhang, y P. Li, «An effective frequency-domain feature of atrial fibrillation based on time–frequency analysis», BMC Med Inform Decis Mak, vol. 20, n.o 1, p. 308, dic. 2020, doi: 10.1186/s12911-020-01337-1.
9. V. B. Traykov, R. Pap, y L. Saghy, «Frequency Domain Mapping of Atrial Fibrillation - Methodology Experimental Data and Clinical Implications», CCR, vol. 8, n.o 3, pp. 231-238, sep. 2012, doi: 10.2174/157340312803217229.
