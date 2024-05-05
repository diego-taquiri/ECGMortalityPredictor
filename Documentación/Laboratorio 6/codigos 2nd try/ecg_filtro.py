import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from scipy.signal import firwin, filtfilt, iirnotch, cheby2, filtfilt

# URL of the raw text file containing ECG data
#url = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%204/ecg_raw_data/reposo/opensignals_98D341FD4F0D_2024-04-19_12-34-17.txt"
url = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%204/ecg_raw_data/ejercicio/opensignals_98D341FD4F0D_2024-04-19_12-46-31.txt"
# Download the data from the URL
response = urlopen(url)
data = response.read().decode('utf-8').splitlines()

# Load data from the downloaded text file skipping the first 3 rows
x = np.loadtxt(data, skiprows=3)

# Calculate data in millivolts
data_mV = (x[:, 5] / 1024) * 3.223 - 3.223 / 2

# Generate time array in seconds
time = np.arange(len(data_mV)) / 1000

# Define filter parameters
cutoff_freq = 40  # Cutoff frequency in Hz
notch_freq = 60  # Notch frequency in Hz
filter_order = 56  # Filter order (number of taps)
sampling_freq = 1000  # Sampling frequency in Hz
nyquist_freq = sampling_freq / 2  # Nyquist frequency is half of the sampling rate

# Normalize frequencies relative to the Nyquist frequency
normalized_cutoff = cutoff_freq / nyquist_freq
normalized_notch = notch_freq / nyquist_freq

# Choose an appropriate beta value for the Kaiser window (controls trade-off between ripple and attenuation)
beta = 6.0

# Design Kaiser windowed FIR filter for low-pass
fir_coeff = firwin(filter_order + 1, normalized_cutoff, window=('kaiser', beta))

# Design notch filter
b_notch, a_notch = iirnotch(normalized_notch, Q=30, fs=sampling_freq)

# Apply the FIR filter followed by the notch filter
filtered_data_mV = filtfilt(b_notch, a_notch, filtfilt(fir_coeff, 1.0, data_mV))

# Define filter parameters
cutoff_freq = 40  # Cutoff frequency in Hz
filter_order = 4  # Filter order

# Design Chebyshev Type II lowpass filter
sos = cheby2(filter_order, rs=30, Wn=cutoff_freq, btype='low', analog=False, fs=1000)

# Apply the Chebyshev Type II filter using filtfilt (zero-phase filtering)
IIR_mV = filtfilt(sos[0], sos[1], data_mV)
# Plotting original ECG signal and its filtered version
plt.figure(figsize=(12, 10))

#plt.subplot(3, 1, 1)
plt.plot(time, data_mV, )
plt.title('Unfiltered ECG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(50, 55)
plt.ylim(-1,1)

plt.figure(figsize=(12, 10))
#plt.subplot(3, 1, 2)
plt.plot(time, filtered_data_mV, )
plt.title('Filtered ECG Signal (Kaiser FIR + Notch Filter)')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(50, 55)
plt.ylim(-1,1)

# Plotting original ECG signal and its filtered version
plt.figure(figsize=(12, 6))

plt.plot(time, IIR_mV)
plt.title('Filtered ECG Signal (Chebyshev Type II Lowpass Filter)')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.grid(True)
plt.xlim(50, 55)
plt.ylim(-1,1)
plt.tight_layout()
plt.show()

