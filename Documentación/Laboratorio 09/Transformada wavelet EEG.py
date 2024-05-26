import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
import pywt
from scipy.signal import spectrogram, periodogram, welch, iirnotch, filtfilt

def calculate_snr(original_signal, denoised_signal):
    signal_power = np.mean(original_signal**2)
    noise = original_signal - denoised_signal
    noise_power = np.mean(noise**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

def calculate_thresholds(coeffs):
    thresholds = [np.mean(np.abs(coeff)) + 2 * np.std(np.abs(coeff)) for coeff in coeffs[1:]]  
    return thresholds

def apply_threshold(coeffs, thresholds, max_level):
    denoised_coeffs = [coeffs[0]]  # Keep approximation coefficients unaltered
    for i, coeff in enumerate(coeffs[1:]):
        if i < max_level:  # Apply thresholding only up to the specified level
            threshold = thresholds[i]
            denoised_coeff = pywt.threshold(coeff, threshold, mode='hard')
        else:
            denoised_coeff = coeff  # Keep higher frequency coefficients unaltered
        denoised_coeffs.append(denoised_coeff)
    return denoised_coeffs

def apply_notch_filter(signal, freq, fs, quality_factor):
    # Design notch filter
    b, a = iirnotch(freq, quality_factor, fs)
    # Apply notch filter
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

def process_eeg_data(url, num_samples, wavelet, levels, max_threshold_level, notch_freq, notch_q):
    # Download the data from the URL
    response = urlopen(url)
    data = response.read().decode('utf-8').splitlines()

    # Load data from the downloaded text file skipping the first 3 rows
    x = np.loadtxt(data, skiprows=3)

    # Extract the required number of samples
    data_mV = (x[:num_samples, 5] / 1024) * 3.223 - 3.223 / 2

    # Apply notch filter
    sampling_frequency = 1000  # Hz
    data_mV_notched = apply_notch_filter(data_mV, notch_freq, sampling_frequency, notch_q)

    # Decompose the signal using SWT
    coeffs = pywt.swt(data_mV_notched, wavelet, level=levels, start_level=0)

    # Calculate thresholds
    thresholds = calculate_thresholds(coeffs)

    # Apply thresholding to coefficients using the calculated thresholds
    denoised_coeffs = apply_threshold(coeffs, thresholds, max_threshold_level)

    # Reconstruct the denoised signal using thresholded coefficients
    denoised_signal = pywt.iswt(denoised_coeffs, wavelet)

    # Calculate SNR
    snr = calculate_snr(data_mV, denoised_signal)
    print(f"SNR for {url}: {snr:.2f} dB")

    # Calculate time array in seconds based on sampling frequency (1000 Hz)
    time = np.arange(num_samples) / sampling_frequency

    # Plot Original EEG Signal and Denoised EEG Signal in separate subplots
    plt.figure(figsize=(12, 10))
    plt.plot(time, data_mV, label='Original EEG Signal', alpha=0.7)
    plt.title('Señal EEG original')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Voltaje (mV)')
    plt.xlim(0, 2)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.figure(figsize=(12, 10))
    plt.plot(time, denoised_signal, label='Denoised EEG Signal', alpha=0.7)
    plt.title('Señal EEG filtrada')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Voltaje (mV)')
    plt.xlim(0, 2)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Spectrograms of original and denoised signals
    plt.figure(figsize=(12, 10))
    frequencies, times, spectrogram_orig = spectrogram(data_mV, fs=sampling_frequency)
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_orig), shading='gouraud', cmap='jet', vmin=-200, vmax=0)
    plt.title('Espectrograma de señal EEG original')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Frecuencia (Hz)')
    plt.colorbar(label='Densidad Espectral de Poder (dB)')
    plt.tight_layout()

    plt.figure(figsize=(12, 10))
    frequencies, times, spectrogram_denoised = spectrogram(denoised_signal, fs=sampling_frequency)
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_denoised), shading='gouraud', cmap='jet', vmin=-200, vmax=0)
    plt.title('Espectrograma de señal EEG filtrada')
    plt.xlabel('Tiempo (segundos)')
    plt.ylabel('Frecuencia (Hz)')
    plt.colorbar(label='Densidad Espectral de Poder (dB)')
    plt.tight_layout()

    # Amplitude Spectrum using Periodogram
    plt.figure(figsize=(12, 6))
    freqs_orig, amp_orig = periodogram(data_mV, fs=sampling_frequency)
    plt.plot(freqs_orig, 20 * np.log10(amp_orig), label='Original EEG Signal', alpha=0.7)
    freqs_denoised, amp_denoised = periodogram(denoised_signal, fs=sampling_frequency)
    plt.plot(freqs_denoised, 20 * np.log10(amp_denoised), label='Denoised EEG Signal', color='red')
    plt.title('Amplitude Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (dB)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Define URLs for eyes and math EEG data
url_rest = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2007/Raw%20data/Bitalino/base/opensignals_98D341FD4F50_2024-04-26_12-20-56.txt"
url_eyes = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2007/Raw%20data/Bitalino/abrecierra/opensignals_98D341FD4F50_2024-04-26_12-22-23.txt"
url_math = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2007/Raw%20data/Bitalino/mate/opensignals_98D341FD4F50_2024-04-26_12-26-32.txt"

# Process EEG data for eyes and math tasks
num_samples = 70144  # Update with the closest lower number divisible by 2^level
wavelet = 'coif3'
levels = 5
max_threshold_level = 3  # Apply thresholding up to 16 Hz
notch_freq = 60  # Notch filter frequency at 60 Hz
notch_q = 30  # Quality factor for notch filter

process_eeg_data(url_rest, num_samples, wavelet, levels, max_threshold_level, notch_freq, notch_q)
process_eeg_data(url_eyes, num_samples, wavelet, levels, max_threshold_level, notch_freq, notch_q)
process_eeg_data(url_math, num_samples, wavelet, levels, max_threshold_level, notch_freq, notch_q)
