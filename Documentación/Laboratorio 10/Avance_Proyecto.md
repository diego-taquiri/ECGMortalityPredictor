# Avance del proyecto

### Tabla de contenidos
1. [Problemática](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2010/Avance_Proyecto.md#problem%C3%A1tica)
2. [Propuesta de solución](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2010/Avance_Proyecto.md#propuesta-de-soluci%C3%B3n)
3. [Materiales y métodos](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2010/Avance_Proyecto.md#materiales-y-m%C3%A9todos)
4. [Bibliografía](https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2010/Avance_Proyecto.md#bibliograf%C3%ADa)

Como se acordó, la presentación del avance del proyecto será de manera asíncrona y por video. La fecha de presentación será hasta el sábado 18 de mayo a las 23:55 pm subido en su GitHub.

La estructura del video y ppt y/o md debe contener como mínimo:

### Problemática (máx 3 pts).
<p align="justify">Las enfermedades cardiovasculares representan la principal causa de defunción en el mundo, cobrándose aproximadamente 17,9 millones de vidas anualmente [1]. Este grupo de trastornos, que incluye cardiopatías coronarias, enfermedades cerebrovasculares y cardiopatías reumáticas, afecta principalmente a países de bajos y medianos ingresos, donde más del 75% de las muertes ocurren [1]. En las Américas, la prevención y tratamiento de estas enfermedades es vital, ya que se estima que causan 2 millones de muertes al año [2]. En Perú, EsSalud advierte que las enfermedades cardiovasculares son la segunda causa de muerte [3]. Un estudio del INEI reveló que más del 40% de las personas mayores de 15 años tienen un riesgo cardiovascular muy alto, siendo el 60% de estos casos en mujeres de 60 años o más [3, 4]. El Dr. José Ercilla, vicepresidente de la Sociedad Peruana de Cardiología (Sopechard), destaca que estas enfermedades representan un desafío futuro, especialmente ante la proyección de un aumento significativo de la población mayor de 50 años para el año 2050 [4].<br>
  
<p align="justify">La miocardiopatía chagásica, principal causa de miocardiopatía no isquémica (MNIC) en América Latina, afecta aproximadamente al 30% de los pacientes infectados y surge durante el desarrollo de la enfermedad de Chagas como su manifestación más grave, siendo esta endémica en toda la región. [5] La enfermedad de Chagas es una afección parasitaria, sistémica, crónica, transmitida por vectores y causada por el protozoario Trypanosoma cruzi, con una firme vinculación con aspectos socioeconómico-culturales deficitarios, considerándola una enfermedad desatendida. [6]  Las características más destacadas de la miocardiopatía chagásica incluyen una miocarditis difusa con fibrosis focal, localizada principalmente en el ápice y segmentos basales de la pared posterior e inferior, lo que da lugar a una enfermedad altamente arritmogénica. [5]<br>
  
<p align="justify">El principal mecanismo de transmisión es vectorial: se da al picar al ser humano, produciendo una lesión y defecando en dicha lesión, donde al rascarse hace que los parásitos ingresen al torrente sanguíneo [8]. Otras modalidades de transmisión son transfusional, congénita, trasplantes de órganos u oral. Aunque la mortalidad ha disminuido significativamente, la enfermedad puede causar consecuencias irreversibles y crónicas en el corazón, el sistema digestivo y el sistema nervioso. [7] 
La Organización Panamericana de la Salud estima que alrededor de 8 millones de personas están infectadas en estas regiones, lo que provoca aproximadamente 12 000 muertes cada año, siendo su propagación a nivel mundial acelerada debido a la migración humana: se considera que hay unos 75 millones de personas en riesgo de infección. [5, 6]. <br>
  
<p align="justify">Aunque esta enfermedad, conocida como chirimacha, se encuentra poco estudiada en Perú, el área chagásica más importantes se encontró en la vertiente suroccidental del pacifico comprendida entre los 13 y los 19 grados de latitud sur entre las altitudes de 10 a 3,000 msnm y hasta el 2019 se observaba como en la figura 1. [9, 10] La pobreza en las zonas rurales contribuye a la presencia de vectores en viviendas precarias, aumentando el riesgo de infección. Además, la migración de las poblaciones rurales hacia los centros urbanos, incluyendo la capital, ha incrementado la relevancia de esta enfermedad en áreas donde la presencia del vector no ha sido detectada, evidenciando posibles mecanismos de transmisión no vectorial, como en Lima. [9] <br>
Figura 1. [11]<br>
  
<p align="justify">Para prevenir defunciones prematuras por enfermedades cardiovasculares, es esencial identificar a las personas en alto riesgo y garantizar que reciban el tratamiento adecuado, lo cual requiere un acceso universal a medicamentos y tecnologías esenciales en todos los centros de atención primaria [1]. Expertos en cardiología, resaltados en la revista El Peruano, enfatizan la importancia de reducir la discapacidad y la muerte prematura mediante tratamientos oportunos, así como la necesidad de reducir las listas de espera y adoptar procedimientos menos invasivos para una recuperación más rápida [4]. Además, se subraya la importancia de un trabajo coordinado entre las entidades involucradas para lograr un control efectivo de la enfermedad de chagas, tomando como referencia el éxito de estrategias implementadas en otros países latinoamericanos. [9]

### Propuesta de solución (máx 5 pts)
<p align="justify">Nuestro objetivo es desarrollar un sistema de alerta temprana basado en electrocardiografía (ECG) para la detección de pacientes de alto riesgo de mortalidad por la enfermedad de Chagas en Perú con miras a extenderse a otras patologías cardiovasculares. Este sistema busca impulsar la atención clínica oportuna y reducir la mortalidad asociada a esta enfermedad.<br>
  
<p align="justify">Para lograrlo, utilizaremos técnicas avanzadas de procesamiento de señales y aprendizaje automático. A diferencia de trabajos existentes, como el uso de IA descrito por Chin-Sheng Lin et. al [12], emplearemos la extracción de características mediante la Transformada Wavelet y aplicaremos Tiny Machine Learning (TinyML). Esta combinación nos permitirá identificar patrones específicos en las señales cardíacas de los pacientes con Chagas de manera eficiente y a bajo costo, facilitando su implementación en zonas de bajos recursos.

### Materiales y métodos  (máx 12 pts)
- Debe explicar el protocolo de adquisición de la señal a estudiar, preferente basado en una guía clínica o investigación anterior [consultar con el Prof. Alonso si necesitan ayuda] (máx 3 pts)
- Debe explicar qué métodos se utilizará para analizar/procesar la señal, CON REFERENCIAS. (máx 3 pts)
- Debe explicar el plan de análisis de los datos resultantes del procesamiento de las señales (pruebas estadísticas como mínimo). (máx 3 pts)
- Todos los materiales y/o recursos deben estar identificados, incluido bases de datos (máx 3 pts)
Buenas noches estimados estudiantes,

### Bibliografía
