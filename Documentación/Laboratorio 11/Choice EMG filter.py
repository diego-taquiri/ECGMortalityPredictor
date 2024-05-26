import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from scipy.signal import butter, filtfilt, firwin, iirnotch
import pywt
from scipy.stats import kurtosis, entropy
from sklearn.metrics import mean_squared_error

# URL of the raw text file containing EMG data
url = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2004/emg_raw_data/isb-contrafuerza-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-19-52.txt"

# Download the data from the URL
response = urlopen(url)
data = response.read().decode('utf-8').splitlines()

# Load data from the downloaded text file skipping the first 3 rows
x = np.loadtxt(data, skiprows=3)

# Calculate data in millivolts
data_mV = (x[:, 5] / 1024) * 3.223 - 3.223 / 2

# Generate time array in seconds
time = np.arange(len(data_mV)) / 1000

# Define functions for filter design and filtering
def butter_bandpass(data, lowcut, highcut, fs, order=4):
    nyquist_freq = 0.5 * fs
    low = lowcut / nyquist_freq
    high = highcut / nyquist_freq
    b, a = butter(order, [low, high], btype='band', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

def iir_notch(data, cutoff, fs, order=4):
    b, a = iirnotch(cutoff, Q=10, fs=fs)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

def bartlett_fir(data, cutoff, fs, order=20):
    coeff = firwin(order + 1, cutoff / (fs / 2), window='bartlett')
    filtered_data = filtfilt(coeff, 1.0, data)
    return filtered_data

def wavelet_denoise(signal, wavelet='db4', level=10, threshold_scaling_factor=3.0):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    sigma = np.median(np.abs(coeffs[-level])) / 0.6745
    uthresh = sigma * np.sqrt(2 * np.log(len(signal))) * threshold_scaling_factor
    denoised_coeffs = [pywt.threshold(c, uthresh, mode='soft') for c in coeffs]
    denoised_signal = pywt.waverec(denoised_coeffs, wavelet)
    return denoised_signal

def calculate_kurtosis(signal):
    return kurtosis(signal)

def calculate_entropy(signal):
    return entropy(np.histogram(signal, bins='fd')[0])

def calculate_snr(original_signal, filtered_signal):
    noise = original_signal - filtered_signal
    signal_power = np.mean(original_signal ** 2)
    noise_power = np.mean(noise ** 2)
    return 10 * np.log10(signal_power / noise_power)

# Apply IIR filter (bandpass + notch)
filtered_iir_bandpass = butter_bandpass(data_mV, lowcut=20, highcut=250, fs=1000, order=4)
filtered_iir_notch = iir_notch(filtered_iir_bandpass, cutoff=60, fs=1000, order=4)

# Apply FIR filter (Bartlett)
filtered_fir_bartlett = bartlett_fir(data_mV, cutoff=400, fs=1000, order=20)

# Apply wavelet denoising
denoised_data_mV = wavelet_denoise(data_mV)

# Calculate metrics for each filtered signal
kurtosis_diff = []
entropy_diff = []
snr = []

# Original signal
kurtosis_diff.append(0)  # Kurtosis difference with itself is 0
entropy_diff.append(0)   # Entropy difference with itself is 0
snr.append(0)            # SNR with itself is infinite

# Calculate metrics for each filtered signal
for filtered_signal in [filtered_iir_notch, filtered_fir_bartlett, denoised_data_mV]:
    # Kurtosis difference
    kurtosis_diff.append(abs(calculate_kurtosis(data_mV) - calculate_kurtosis(filtered_signal)))
    
    # Entropy difference
    entropy_diff.append(abs(calculate_entropy(data_mV) - calculate_entropy(filtered_signal)))
    
    # SNR
    snr.append(calculate_snr(data_mV, filtered_signal))

# Plotting the original and filtered signals in subplots
plt.figure(figsize=(12, 15))

# Plot original EMG signal
plt.subplot(4, 1, 1)
plt.plot(time, data_mV)
plt.title('Original EMG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(11, 25)
plt.ylim(-1.5, 1.5)

# Plot IIR filtered EMG signal (bandpass + notch)
plt.subplot(4, 1, 2)
plt.plot(time, filtered_iir_notch)
plt.title('IIR Filtered EMG Signal (Bandpass + Notch)')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(11, 25)
plt.ylim(-1.5, 1.5)

# Plot FIR filtered EMG signal (Bartlett)
plt.subplot(4, 1, 3)
plt.plot(time, filtered_fir_bartlett)
plt.title('FIR Filtered EMG Signal (Bartlett)')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(11, 25)
plt.ylim(-1.5, 1.5)

# Plot wavelet denoised EMG signal
plt.subplot(4, 1, 4)
plt.plot(time, denoised_data_mV)
plt.title('Wavelet Denoised EMG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(11, 25)
plt.ylim(-1.5, 1.5)

plt.tight_layout()
plt.show()

# Print results
print("Kurtosis Difference:")
print("IIR Notch:", kurtosis_diff[1])
print("FIR Bartlett:", kurtosis_diff[2])
print("Wavelet Denoised:", kurtosis_diff[3])

print("\nEntropy Difference:")
print("IIR Notch:", entropy_diff[1])
print("FIR Bartlett:", entropy_diff[2])
print("Wavelet Denoised:", entropy_diff[3])

print("\nSignal-to-Noise Ratio (SNR):")
print("IIR Notch:", snr[1])
print("FIR Bartlett:", snr[2])
print("Wavelet Denoised:", snr[3])
