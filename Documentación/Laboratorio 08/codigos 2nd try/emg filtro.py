import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from scipy.signal import butter, filtfilt, firwin

# URL of the raw text file containing EMG data
url = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2004/emg_raw_data/isb-reposo-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-12-05.txt"
#url = "https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2004/emg_raw_data/isb-isometrico-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-17-43.txt"
#url = "https://github.com/diego-taquiri/ISB-equipo11/blob/main/Documentaci%C3%B3n/Laboratorio%2004/emg_raw_data/isb-contrafuerza-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-19-52.txt"
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
def butter_highpass(data, cutoff_freq, fs, order=2):
    nyquist_freq = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist_freq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

def butter_lowpass(data, cutoff_freq, fs, order=8):
    nyquist_freq = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist_freq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

def butter_stopbands(data, stopbands, fs, order=2):
    nyquist_freq = 0.5 * fs
    normalized_stopbands = [(sb / nyquist_freq) for sb in stopbands]
    b, a = butter(order, normalized_stopbands, btype='bandstop', analog=False)
    filtered_data = filtfilt(b, a, data)
    return filtered_data

# Define cutoff frequencies and stopbands for filters
highpass_cutoff = 10  # Highpass cutoff frequency in Hz
lowpass_cutoff = 400  # Lowpass cutoff frequency in Hz
stopbands = [(9, 61), (119, 121), (179, 181), (239, 241), (299, 301), (359, 361)]  # Stopband ranges in Hz

# Apply highpass, lowpass, and multiple stopband filters
filtered_highpass = butter_highpass(data_mV, highpass_cutoff, fs=1000, order=2)
filtered_lowpass = butter_lowpass(filtered_highpass, lowpass_cutoff, fs=1000, order=8)
filtered_final = filtered_lowpass.copy()  # Start with the lowpass-filtered signal for stopband filtering
for band in stopbands:
    filtered_final = butter_stopbands(filtered_final, band, fs=1000, order=2)

# Define filter parameters
cutoff_freq = 40  # Cutoff frequency in Hz
nyquist_freq = 500  # Nyquist frequency in Hz (half of the sampling rate, assuming fs = 1000 Hz)

# Design Hanning windowed FIR filter
filter_order = 8  # Filter order (make it odd for zero-phase filtering)
fir_coeff = firwin(filter_order, cutoff_freq / nyquist_freq, window='hann')

# Apply the FIR filter using filtfilt (zero-phase filtering)
filtered_data_mV = filtfilt(fir_coeff, 1.0, data_mV)

# Plotting the original and filtered signals in subplots
plt.figure(figsize=(12, 10))

# Plot original EMG signal

plt.plot(time, data_mV)
plt.title('Original EMG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(11,25)
plt.ylim(-1.5,1.5)


# Plot final filtered EMG signal (lowpass + stopbands)
plt.figure(figsize=(12, 10))
plt.plot(time, filtered_final)
plt.title('Combined Filtered EMG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(11,25)
plt.ylim(-1.5,1.5)


plt.figure(figsize=(12, 6))

plt.plot(time, filtered_data_mV, )
plt.title('Filtered EMG Signal (Hann FIR Filter, 40 Hz cutoff)')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(11,25)
plt.ylim(-1.5,1.5)
plt.tight_layout()
plt.show()
