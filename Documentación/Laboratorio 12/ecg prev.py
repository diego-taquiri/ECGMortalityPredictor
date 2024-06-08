import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from scipy.signal import filtfilt, firwin, lfilter, find_peaks

# URL of the raw text file containing ECG data
url= "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2006/ecg_raw_data/reposo/opensignals_98D341FD4F0D_2024-04-19_12-34-17.txt"
#url = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2006/ecg_raw_data/ejercicio/opensignals_98D341FD4F0D_2024-04-19_12-46-31.txt"
#url= "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2006/ecg_raw_data/paro_cardiaco/opensignals_98D341FD4F0D_2024-04-19_12-56-28.txt"

# Download the data from the URL
response = urlopen(url)
data = response.read().decode('utf-8').splitlines()

# Load data from the downloaded text file skipping the first 3 rows
x = np.loadtxt(data, skiprows=3)

# Calculate data in millivolts
data_mV = (x[:, 5] / 1024) * 3.223 - 3.223 / 2

# Generate time array in seconds
time = np.arange(len(data_mV)) / 1000

start_index = np.searchsorted(time, 50)  # Find the index corresponding to 50 seconds
end_index = np.searchsorted(time, 55)  # Find the index corresponding to 120 seconds
time = time[start_index:end_index]
data_mV = data_mV[start_index:end_index]

# Bandpass filter design (0.5 Hz to 43 Hz)
fs = 1000  # Sampling frequency
nyquist = 0.5 * fs
low_cutoff = 0.5 / nyquist
high_cutoff = 43 / nyquist

# Design FIR filter
numtaps = 101  # Number of taps in the filter
b = firwin(numtaps, [low_cutoff, high_cutoff], pass_zero=False)

# Apply zero-phase digital bandpass filter
filtered_signal = filtfilt(b, 1, data_mV)

# Moving average filter design
window_size = 5  # Window size for the moving average filter
moving_avg_filter = np.ones(window_size) / window_size

# Apply moving average filter
smoothed_signal = lfilter(moving_avg_filter, 1, filtered_signal)

# Calculate the first derivative
first_derivative = np.diff(smoothed_signal, n=1)
# Append a zero to maintain the original signal length
first_derivative = np.append(first_derivative, 0)

# Calculate the second derivative
second_derivative = np.diff(smoothed_signal, n=2)
# Append two zeros to maintain the original signal length
second_derivative = np.append(second_derivative, [0, 0])

# Combine the derivatives to form the feature signal
feature_signal = 1.3 * first_derivative + 1.1 * second_derivative

# Find the R peaks (maximum peaks) in the feature signal
peaks, _ = find_peaks(feature_signal, distance=fs/2.5, height=0.02)  # Assuming a minimum distance of 0.4 seconds between R peaks

# Extract RR intervals
RR_intervals = np.diff(time[peaks])*1000

# Calculate RMSSD
if len(RR_intervals) > 1:
    diff_rr_intervals = np.diff(RR_intervals)
    squared_diff_rr_intervals = np.square(diff_rr_intervals)
    mean_squared_diff = np.mean(squared_diff_rr_intervals)
    RMSSD = np.sqrt(mean_squared_diff)
else:
    RMSSD = np.nan  # Not enough RR intervals to calculate RMSSD

print(f"RMSSD: {RMSSD:.2f} ms")

# Plot the original, filtered, and feature signals with detected peaks
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(time, data_mV, label='Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [mV]')
plt.title('Original ECG Signal')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(time, smoothed_signal, label='Filtered and Smoothed Signal', color='orange')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [mV]')
plt.title('Filtered and Smoothed ECG Signal')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(time, feature_signal, label='Feature Signal (Combination of Derivatives)', color='green')
plt.plot(time[peaks], feature_signal[peaks], 'rx', label='Detected R Peaks')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Feature Signal with Detected R Peaks')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
