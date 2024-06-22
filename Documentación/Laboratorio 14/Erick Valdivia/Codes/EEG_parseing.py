import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
import pywt
from scipy.signal import iirnotch, filtfilt
import csv
import os

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
    denoised_coeffs = [coeffs[0]]
    for i, coeff in enumerate(coeffs[1:]):
        if i < max_level:
            threshold = thresholds[i]
            denoised_coeff = pywt.threshold(coeff, threshold, mode='hard')
        else:
            denoised_coeff = coeff
        denoised_coeffs.append(denoised_coeff)
    return denoised_coeffs

def apply_notch_filter(signal, freq, fs, quality_factor):
    b, a = iirnotch(freq, quality_factor, fs)
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal

def save_windows_as_csv(time, denoised_signal, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    window_size = 500  # milliseconds
    fs = 1000  # sampling frequency
    num_samples_per_window = int(window_size * fs / 1000)
    num_windows = len(denoised_signal) // num_samples_per_window

    for i in range(num_windows):
        start_idx = i * num_samples_per_window
        end_idx = start_idx + num_samples_per_window
        window_signal = denoised_signal[start_idx:end_idx]
        window_time = np.arange(1, len(window_signal) + 1)  # Enumerate from 1 to size of the segment

        csv_filename = os.path.join(output_folder, f"window_{i+1}.csv")
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Timestamps', 'Signal'])
            for t, signal_value in zip(window_time, window_signal):
                csv_writer.writerow([t, signal_value])

        print(f"Window {i+1} saved to {csv_filename}")

def process_eeg_data(url, num_samples, wavelet, levels, max_threshold_level, notch_freq, notch_q, output_folder):
    response = urlopen(url)
    data = response.read().decode('utf-8').splitlines()
    x = np.loadtxt(data, skiprows=3)
    data_mV = (x[:num_samples, 5] / 1024) * 3.223 - 3.223 / 2
    sampling_frequency = 1000
    data_mV_notched = apply_notch_filter(data_mV, notch_freq, sampling_frequency, notch_q)
    coeffs = pywt.swt(data_mV_notched, wavelet, level=levels, start_level=0)
    thresholds = calculate_thresholds(coeffs)
    denoised_coeffs = apply_threshold(coeffs, thresholds, max_threshold_level)
    denoised_signal = pywt.iswt(denoised_coeffs, wavelet)
    snr = calculate_snr(data_mV, denoised_signal)
    print(f"SNR for {url}: {snr:.2f} dB")
    save_windows_as_csv(np.arange(len(data_mV)) / sampling_frequency, denoised_signal, output_folder)

urls = [
    ("https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2007/Raw%20data/Bitalino/base/opensignals_98D341FD4F50_2024-04-26_12-20-56.txt", "filtered_rest"),
    ("https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2007/Raw%20data/Bitalino/abrecierra/opensignals_98D341FD4F50_2024-04-26_12-22-23.txt", "filtered_eyes"),
    ("https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2007/Raw%20data/Bitalino/mate/opensignals_98D341FD4F50_2024-04-26_12-26-32.txt", "filtered_math")
]

num_samples = 70144
wavelet = 'coif3'
levels = 5
max_threshold_level = 3
notch_freq = 60
notch_q = 30

for url, output_folder in urls:
    process_eeg_data(url, num_samples, wavelet, levels, max_threshold_level, notch_freq, notch_q, output_folder)
