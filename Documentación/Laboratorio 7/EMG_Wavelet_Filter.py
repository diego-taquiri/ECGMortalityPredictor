import numpy as np
import matplotlib.pyplot as plt
import pywt

def wavelet_denoise(signal, wavelet='db4', level=10):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    sigma = np.median(np.abs(coeffs[-level])) / 0.6745
    uthresh = sigma * np.sqrt(2 * np.log(len(signal)))
    denoised_coeffs = [pywt.threshold(c, uthresh, mode='soft') for c in coeffs]
    denoised_signal = pywt.waverec(denoised_coeffs, wavelet)
    return denoised_signal

def load_emg_data(filepath):
    return np.loadtxt(filepath)

# File paths
files = [
    'Documentación/Laboratorio 3/emg_raw_data/isb-reposo-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-12-05.txt',
    'Documentación/Laboratorio 3/emg_raw_data/isb-isometrico-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-16-36.txt',
    'Documentación/Laboratorio 3/emg_raw_data/isb-contrafuerza-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-19-52.txt'
]

# Plot original and denoised signals
fig, axs = plt.subplots(len(files), 2, figsize=(15, 10))

for i, file in enumerate(files):
    # Load data
    emg_signal = load_emg_data(file)
    
    # Denoise signal
    denoised_emg_signal = wavelet_denoise(emg_signal)
    
    # Plot original signal
    axs[i, 0].plot(emg_signal)
    axs[i, 0].set_title(f'Señal EMG Original - Archivo {i+1}')
    
    # Plot denoised signal
    axs[i, 1].plot(denoised_emg_signal)
    axs[i, 1].set_title(f'Señal EMG Filtrada - Archivo {i+1}')

plt.tight_layout()
plt.show()
