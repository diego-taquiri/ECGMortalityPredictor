# Early ECG Warning System for Chagas Disease Patients Using TinyML

<p align="justify">
This project focuses on the development of an early warning system for predicting high-risk mortality in Chagas disease patients using electrocardiography (ECG) signals and Tiny Machine Learning (TinyML) techniques. Chagas disease, a parasitic illness prevalent in Latin America, leads to severe cardiac complications, often resulting in fatal outcomes if left undetected. In response to this challenge, we have implemented a machine learning solution that processes ECG data using wavelet transforms for denoising and feature extraction. A compact XGBoost model was trained to predict mortality risk, enabling timely medical interventions in low-resource areas where access to healthcare is limited. This system is designed to run efficiently on low-cost, portable devices, such as the Arduino Nano BLE 33, making it a viable solution for remote and underserved communities.

<p align="center">
    <img src="./Documentación/Informe final/figures/abstract.png" alt="Descripción de la imagen" width="800"><br>
    <b>Figure 1.</b> Abstract
</p>

- [Enlace de paperswithcode](https://paperswithcode.com/paper/early-ecg-warning-for-chagas-patients) (UPCH 2024 PDF)
  
# Table of Contents
- [Project Overview](#project-overview)
- [Course Content](#course-content)
- [Course Instructors](#course-instructors)
- [Participants](#participants)

### Project Overview
#### Early ECG Warning for Chagas Patients: Implementation of TinyML for Low-Resource Areas in Peru

##### Summary
This project aims to develop an early warning system based on electrocardiography (ECG) for the detection of high-risk mortality patients affected by Chagas disease in Peru. It leverages advanced signal processing techniques and machine learning, specifically Tiny Machine Learning (TinyML), to efficiently and cost-effectively identify specific cardiac patterns in Chagas patients, facilitating implementation in low-resource regions.

##### Motivation
Cardiovascular diseases are the leading cause of death worldwide, and in Peru, they represent the second leading cause of mortality. Chagas disease, locally known as "Chirimacha," is a neglected parasitic disease that affects millions of people across Latin America, including Peru. This disease can lead to Chagas cardiomyopathy, one of the major causes of non-ischemic cardiomyopathy in the region.

Dr. José Ercilla, vice president of the Peruvian Society of Cardiology (Sopechard), highlights the future challenges posed by these diseases, especially given the significant increase in the population over 50 years projected by 2050. The migration of rural populations to urban centers has increased the relevance of this disease in areas where the vector has not previously been detected.

This project seeks to implement an accessible and efficient technological solution that allows for the early detection of cardiac problems in Chagas patients, thereby improving their quality of life and reducing mortality associated with the disease. The use of TinyML in portable, low-cost devices can revolutionize health monitoring in low-resource communities, enabling more timely and accurate medical care.

##### Key Findings
- The XGBoost model showed reasonable predictive capability with an R-squared value of 0.61.
- The mean squared error (MSE) was 0.38, indicating acceptable accuracy.
- The mean absolute error (MAE) was 0.51, reflecting the precision of the predictions.
- The model was implemented on an Arduino Nano BLE 33, demonstrating feasibility for low-resource environments.
- The number of ECG leads was reduced from 12 to 1, making the system more accessible and cost-effective.
- A feature extraction stage (skewness, entropy) was integrated to enhance the model’s ability to extract and use signal information.
- The model's predictions on ECG signals from healthy subjects showed results comparable to those of surviving patients in the dataset.
- Evaluation metrics suggest the model has good potential, though there is room for further improvements in accuracy and generalization.

##### Informe

- [Ver PDF del Sílabo en Google Docs Viewer](https://docs.google.com/viewer?url=https://github.com/diego-taquiri/ISB-equipo11/raw/main/Documentaci%C3%B3n/Laboratorio%2001/S%C3%ADlabo.pdf&embedded=true)

### Docentes del curso
#### PROFESORES DEL CURSO E INVITADOS

| Grado o Título | Nombre    | Apellidos             | Condición   | Correo electrónico         |
| -------------- | --------- | --------------------- | ----------- | -------------------------- |
| Magister       | U. Lewis  | De la Cruz Rodríguez  | Contratado  | [umbert.de.la.cruz@upch.pe](mailto:umbert.de.la.cruz@upch.pe) |
| Magister       | Moisés    | Meza Rodríguez        | Contratado  | [moises.meza@upch.pe](mailto:moises.meza@upch.pe) |

#### JEFES DE PRÁCTICA

| Grado o Título | Nombre    | Apellidos             | Condición   | Correo electrónico         |
| -------------- | --------- | --------------------- | ----------- | -------------------------- |
| Ingeniería     | Julissa E.| Venancio Huerta       | Contratado  | [julissa.venancio@upch.pe](mailto:julissa.venancio@upch.pe) |
| Licenciado     | José A.   | Cáceres del Águila    | Contratado  | [jose.caceres.d@upch.pe](mailto:jose.caceres.d@upch.pe) |

### Participantes
| Imagen                                                                                           | Grado                            | Nombre y Apellido        | Condición   | Correo electrónico                            |
|-------------------------------------------------------------------------------------------------|----------------------------------|--------------------------|-------------|-----------------------------------------------|
| <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2001/diego.jpeg" alt="Diego" width="100"/> | Estudiante de Biología           | Diego Taquiri            | Colaborador | [diego.taquiri@upch.pe](mailto:diego.taquiri@upch.pe)  |
| <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2001/Armando.jpeg" alt="Armando" width="100"/> | Estudiante de Ingeniería Biomédica | Armando Flórez           | Colaborador | [armando.florez@upch.pe](mailto:armando.florez@upch.pe)  |
| <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2001/ana.jpg" alt="Ana Belen" width="100"/>   | Estudiante de Ingeniería Biomédica | Ana Belen Mantilla       | Colaborador | [ana.mantilla@upch.pe](mailto:ana.mantilla@upch.pe)    |
| <img src="https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2001/Erick.jpg" alt="Erick" width="100"/>  | Estudiante de Ingeniería Biomédica | Erick Valdivia           | Colaborador | [erick.valdivia@upch.pe](mailto:erick.valdivia@upch.pe) |

<p align="justify"> ¡Gracias por visitar nuestro repositorio y por ser parte de nuestro viaje hacia el conocimiento y la innovación en señales biomédicas!
