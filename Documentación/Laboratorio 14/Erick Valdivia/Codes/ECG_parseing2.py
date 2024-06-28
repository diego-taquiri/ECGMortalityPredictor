import os
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from scipy.signal import filtfilt, firwin, lfilter
import csv

# Define constants
C = 0.01  # Constant

# URLs of the raw text files containing ECG data
urls = {
    "ejercicio": "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2006/ecg_raw_data/ejercicio/opensignals_98D341FD4F0D_2024-04-19_12-46-31.txt",
    "reposo": "https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2006/ecg_raw_data/reposo/opensignals_98D341FD4F0D_2024-04-19_12-34-17.txt"
}

def process_ecg_data(url, start_time, end_time, output_folder):
    # Fetch the input text file from the URL
    response = urlopen(url)
    data = response.read().decode('utf-8').splitlines()

    # Load data from the downloaded text file, skipping the first 3 rows
    x = np.loadtxt(data, skiprows=3)

    # Calculate data in millivolts
    data_mV = (x[:, 5] / 1024) * 3.223 - 3.223 / 2

    # Generate time array in seconds
    time = np.arange(len(data_mV)) / 1000

    start_index = np.searchsorted(time, start_time)  # Find the index corresponding to start_time seconds
    end_index = np.searchsorted(time, end_time)  # Find the index corresponding to end_time seconds
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

    # Function to save segments every 2 seconds as CSV files
    def save_segments_as_csv(time, smoothed_signal, segment_duration, output_folder):
        segment_samples = int(segment_duration * fs)

        # Create folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Iterate through the signal in steps of segment_samples
        for i in range(0, len(time), segment_samples):
            segment_time = time[i:i+segment_samples]
            segment_signal = smoothed_signal[i:i+segment_samples]

            if len(segment_signal) < segment_samples:
                break  # Ignore the last segment if it is shorter than the segment duration

            # Create CSV filename
            csv_filename = os.path.join(output_folder, f"segment_{i//segment_samples + 1}.csv")

            # Write segment to CSV
            with open(csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Timestamps', 'Signal'])

                # Write timestamps starting from 1 for each segment
                for j, signal_value in enumerate(segment_signal, start=1):
                    csv_writer.writerow([j, signal_value])

            print(f"Segment {i//segment_samples + 1} saved to {csv_filename}")

    # Save segments every 2 seconds (2000 samples)
    segment_duration = 2  # Duration in seconds
    save_segments_as_csv(time, smoothed_signal, segment_duration, output_folder)

# Process both URLs
for condition, url in urls.items():
    print(f"Processing {condition} data...")
    process_ecg_data(url, start_time=50, end_time=300, output_folder=f'dataset_ecg_{condition}')
    print(f"{condition.capitalize()} data processing complete.")
