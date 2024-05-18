import numpy as np
import pywt
import matplotlib.pyplot as plt

# Función para filtrar la señal usando wavelet con un umbral más estricto
def wavelet_denoise(signal, wavelet='db4', level=10, threshold_scaling_factor=3.0):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    sigma = np.median(np.abs(coeffs[-level])) / 0.6745
    uthresh = sigma * np.sqrt(2 * np.log(len(signal))) * threshold_scaling_factor
    denoised_coeffs = [pywt.threshold(c, uthresh, mode='soft') for c in coeffs]
    denoised_signal = pywt.waverec(denoised_coeffs, wavelet)
    return denoised_signal

# Función para cargar y procesar las señales
def load_and_process_emg(filepath, title, savepath):
    data = np.loadtxt(filepath, skiprows=3)
    data_mV = data[:, 5] / 1024 * 3.223 - 3.223 / 2
    time = np.arange(len(data_mV)) / 1000

    # Plot de la señal original
    plt.figure(figsize=(20, 12))
    plt.plot(time, data_mV)
    plt.ylim(-2, 2)
    plt.xlim(13, 31)
    plt.tick_params(axis='both', which='major', labelsize=34, width=2, length=10)
    plt.xlabel('Tiempo (s)', fontsize=45)
    plt.ylabel('mV', fontsize=45)
    plt.title(f'EMG {title} persona 1', fontsize=45)
    plt.tight_layout()

    
    # Aplicar filtro wavelet
    denoised_data_mV = wavelet_denoise(data_mV)

    # Plot de la señal filtrada
    plt.figure(figsize=(20, 12))
    plt.plot(time, denoised_data_mV)
    plt.ylim(-2, 2)
    plt.xlim(13, 31)
    plt.tick_params(axis='both', which='major', labelsize=34, width=2, length=10)
    plt.xlabel('Tiempo (s)', fontsize=45)
    plt.ylabel('mV', fontsize=45)
    plt.title(f'EMG {title} Filtrada persona 1', fontsize=45)
    plt.tight_layout()
 

# Rutas de los archivos
filepaths = [
    ("opensignals_98D3B1FD3DA9_2024-04-12_12-12-05.txt", "reposo", "isb-reposo-armando"),
    ("opensignals_98D3B1FD3DA9_2024-04-12_12-16-36.txt", "isométrico", "isb-isometrico-armando"),
    ("opensignals_98D3B1FD3DA9_2024-04-12_12-19-52.txt", "contrafuerza", "isb-contrafuerza-armando")
]

# Procesar y plotear cada señal
for filepath, title, savepath in filepaths:
    load_and_process_emg(filepath, title, savepath)

