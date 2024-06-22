import os
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from scipy.signal import filtfilt, firwin, lfilter, find_peaks
import csv

# Define constants
C = 0.01  # Constant

# URL of the raw text file containing ECG data
url = "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2006/ecg_raw_data/ejercicio/opensignals_98D341FD4F0D_2024-04-19_12-46-31.txt"
# Fetch the input text file from the URL
response = urlopen(url)
data = response.read().decode('utf-8').splitlines()

# Load data from the downloaded text file, skipping the first 3 rows
x = np.loadtxt(data, skiprows=3)

# Calculate data in millivolts
data_mV = (x[:, 5] / 1024) * 3.223 - 3.223 / 2

# Generate time array in seconds
time = np.arange(len(data_mV)) / 1000

start_index = np.searchsorted(time, 50)  # Find the index corresponding to 50 seconds
end_index = np.searchsorted(time, 300)  # Find the index corresponding to 300 seconds
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

def find_r_peaks(feature_signal, fs):
    # Find the R peaks (maximum peaks) in the feature signal
    peaks, _ = find_peaks(feature_signal, distance=fs/2.5, height=0.02)  # Assuming a minimum distance of 0.4 seconds between R peaks
    return peaks

# Find R peaks
peaks = find_r_peaks(feature_signal, fs)

# Extract RR intervals
RR_intervals = np.diff(time[peaks]) * 1000

# Calculate RMSSD
if len(RR_intervals) > 1:
    diff_rr_intervals = np.diff(RR_intervals)
    squared_diff_rr_intervals = np.square(diff_rr_intervals)
    mean_squared_diff = np.mean(squared_diff_rr_intervals)
    RMSSD = np.sqrt(mean_squared_diff)
else:
    RMSSD = np.nan  # Not enough RR intervals to calculate RMSSD

print(f"RMSSD: {RMSSD:.2f} ms")

# Function to plot signals and R peaks with lines before and after
def plot_signals_with_r_peaks(time, data_mV, smoothed_signal, feature_signal, peaks, x1, x2):
    plt.figure(figsize=(15, 10))

    plt.subplot(3, 1, 1)
    plt.plot(time, data_mV, label='Original Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude [mV]')
    plt.title('Original ECG Signal')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(time, smoothed_signal, label='Filtered and Smoothed Signal', color='orange')
    for peak in peaks:
        plt.axvline(x=time[peak] - x1/1000, color='blue', linestyle='--')
        plt.axvline(x=time[peak] + x2/1000, color='red', linestyle='--')
        
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

# Function to save segments around R peaks as CSV files
def save_segments_as_csv(time, smoothed_signal, peaks, x1, x2, output_folder):
    # Create folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each R peak
    for i, peak in enumerate(peaks):
        start_idx = max(0, int(peak - x1 * fs / 1000))
        end_idx = min(len(time), int(peak + x2 * fs / 1000))

        segment_time = time[start_idx:end_idx]
        segment_signal = smoothed_signal[start_idx:end_idx]

        # Create CSV filename
        csv_filename = os.path.join(output_folder, f"segment_{i+1}.csv")

        # Write segment to CSV
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Timestamps', 'Signal'])

            # Write timestamps starting from 1 for each segment
            for j, signal_value in enumerate(segment_signal, start=1):
                csv_writer.writerow([j, signal_value])

        print(f"Segment {i+1} saved to {csv_filename}")

# Get user input for x1 and x2
x1 = 100  # Time before peak in milliseconds
x2 = 300  # Time after peak in milliseconds

# Plot the signals with R peaks and lines
plot_signals_with_r_peaks(time, data_mV, smoothed_signal, feature_signal, peaks, x1, x2)

# Save segments around R peaks as CSV files
output_folder = 'dataset_ecg_ejercicio'
save_segments_as_csv(time, smoothed_signal, peaks, x1, x2, output_folder)
