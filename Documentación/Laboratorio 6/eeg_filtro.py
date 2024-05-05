import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from scipy.signal import filtfilt, firwin, iirnotch, cheby2

# URL of the text file containing the data
url = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%205/Raw%20data/Raw%20Data%20UltraCortex/OpenBCI-RAW-mate.txt"
#url = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%205/Raw%20data/Raw%20Data%20UltraCortex/OpenBCI-RAW-base.txt"
#url="https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%205/Raw%20data/Raw%20Data%20UltraCortex/OpenBCI-RAW-abrecierra.txt"


# Specify the number of lines to skip
lines_to_skip = 7  # Adjust this number as needed

# Open the URL and read the contents
response = urlopen(url)
lines = response.read().decode('utf-8').splitlines()

# Skip the first 'lines_to_skip' lines
lines = lines[lines_to_skip:]

# Initialize an empty list to store the sixth elements (index 5) from each line
sixth_elements = []

# Parse each line in the remaining lines
for line in lines:
    # Split the line into individual values using comma as delimiter
    values = line.strip().split(',')
    
    # Convert the sixth value (index 5 since indexing starts from 0) to float
    sixth_value = float(values[10])
    
    # Append the voltage value to the list of sixth elements in millivolts (mV)
    sixth_elements.append(sixth_value)

# Convert the list of sixth elements to a numpy array in millivolts (mV)
data_mV = np.array(sixth_elements, dtype=np.float64)

# Sampling rate in Hz
sampling_rate = 125

# Generate time array in seconds
time = np.arange(len(data_mV)) / sampling_rate

# Apply notch filter at 60 Hz using an IIR notch filter
notch_freq = 60.0  # Frequency to notch out
Q = 30.0  # Quality factor
b_notch, a_notch = iirnotch(notch_freq / (sampling_rate / 2), Q)

# Apply the notch filter to the data
data_notched = filtfilt(b_notch, a_notch, data_mV)

# Design a Kaiser FIR filter with order 6 and cutoff frequency of 50 Hz
cutoff_freq = 50.0  # Cutoff frequency in Hz
nyquist_rate = sampling_rate / 2.0  # Nyquist rate
width = 5.0  # Transition width in Hz
beta = 6.00  # Kaiser window beta parameter

# Calculate filter length for the FIR filter
filter_length = int(6 * nyquist_rate / width)

# Design the FIR filter using the Kaiser window method
b_fir = firwin(filter_length, cutoff_freq / nyquist_rate, window=('kaiser', beta))

# Apply the FIR filter to the notched data
filtered_data_mV_fir = filtfilt(b_fir, 1.0, data_notched)

# Convert the filtered FIR data to microvolts (µV) within the range of -15 µV to 15 µV
filtered_data_uV_fir = ((filtered_data_mV_fir - np.mean(filtered_data_mV_fir)) / (np.max(filtered_data_mV_fir) - np.min(filtered_data_mV_fir))) * 30.0

# Design a Chebyshev Type II bandpass filter with order 4 and cutoff frequencies of 12.51-17.5 Hz
bandpass_low = 12.51
bandpass_high = 17.5
order = 4
rp = 0.5  # Passband ripple (in dB)

# Normalize cutoff frequencies to Nyquist frequency
normalized_low = bandpass_low / nyquist_rate
normalized_high = bandpass_high / nyquist_rate

# Design Chebyshev Type II bandpass filter
b_cheby2, a_cheby2 = cheby2(order, rp, [normalized_low, normalized_high], btype='bandpass', analog=False)

# Apply the Chebyshev Type II bandpass filter to the original data
filtered_data_uV_cheby2 = filtfilt(b_cheby2, a_cheby2, data_mV)

# Apply the notch filter at 60 Hz to the Chebyshev Type II filtered data
filtered_data_uV_cheby2_notch = filtfilt(b_notch, a_notch, filtered_data_uV_cheby2)

# Convert the Chebyshev Type II filtered data to microvolts (µV) within the range of -15 µV to 15 µV
filtered_data_uV_cheby2_notch = ((filtered_data_uV_cheby2_notch - np.mean(filtered_data_uV_cheby2_notch)) / (np.max(filtered_data_uV_cheby2_notch) - np.min(filtered_data_uV_cheby2_notch))) * 30.0

# Convert the original data to microvolts (µV) within the range of -15 µV to 15 µV
original_data_uV = ((data_mV - np.mean(data_mV)) / (np.max(data_mV) - np.min(data_mV))) * 30.0

# Plotting the signals
plt.figure(figsize=(12, 10))
plt.plot(time, original_data_uV)
plt.title('Señal EEG ejercicios matemáticos')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (µV)')
plt.grid(True)
plt.xlim(0, 30)

# Plot the FIR filtered EEG signal with notch at 60 Hz in microvolts
plt.figure(figsize=(12, 10))
plt.plot(time, filtered_data_uV_fir)
plt.title('Señal filtrada FIR con notch a 60 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (µV)')
plt.grid(True)
plt.xlim(0, 30)

# Plot the Chebyshev Type II filtered EEG signal with notch at 60 Hz in microvolts
plt.figure(figsize=(12, 10))
plt.plot(time, filtered_data_uV_cheby2_notch)
plt.title('Señal filtrada IIR con notch a 60 Hz')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (µV)')
plt.grid(True)
plt.xlim(0, 30)

# Show all plots
plt.tight_layout()
plt.show()
