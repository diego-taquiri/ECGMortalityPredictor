import numpy as np
import pywt
import matplotlib.pyplot as plt
from urllib.request import urlopen
import csv
import os

# Function to denoise signal using wavelet with a stricter threshold
def wavelet_denoise(signal, wavelet='db4', level=10, threshold_scaling_factor=3.0):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    sigma = np.median(np.abs(coeffs[-level])) / 0.6745
    uthresh = sigma * np.sqrt(2 * np.log(len(signal))) * threshold_scaling_factor
    denoised_coeffs = [pywt.threshold(c, uthresh, mode='soft') for c in coeffs]
    denoised_signal = pywt.waverec(denoised_coeffs, wavelet)
    return denoised_signal

# Function to load and process the EMG signals
def load_and_process_emg(url, title, output_csv):
    # Download the data from the URL
    response = urlopen(url)
    data = response.read().decode('utf-8').splitlines()

    # Load data from the downloaded text file skipping the first 3 rows
    x = np.loadtxt(data, skiprows=3)
    data_mV = x[:, 5] / 1024 * 3.223 - 3.223 / 2
    time = np.arange(len(data_mV)) / 1000

    # Apply wavelet filter
    denoised_data_mV = wavelet_denoise(data_mV)

    # Save the filtered signal to CSV files with partitions of 500 samples
    partition_size = 500
    num_partitions = len(denoised_data_mV) // partition_size

    # Create output folder if it doesn't exist
    output_folder = output_csv.split('.')[0]
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each segment
    for i in range(num_partitions):
        start_idx = i * partition_size
        end_idx = (i + 1) * partition_size

        # Adjust end index for the last partition to include all remaining samples
        if i == num_partitions - 1:
            end_idx = len(denoised_data_mV)

        partition_data = denoised_data_mV[start_idx:end_idx]

        # Create CSV filename for each partition
        partition_csv = f"{output_folder}/segment_{i + 1}.csv"

        # Save the partitioned data to CSV
        with open(partition_csv, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Timestamps', 'Signal'])

            # Write timestamps starting from 1 for each segment
            for j, value in enumerate(partition_data, start=1):
                csv_writer.writerow([j, value])

        print(f"Segment {i + 1} saved to {partition_csv}")

# URLs of the EMG data
urls = [
    ("https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2004/emg_raw_data/isb-reposo-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-12-05.txt", "reposo", "filtered_isb_reposo_armando.csv"),
    ("https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2004/emg_raw_data/isb-isometrico-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-16-36.txt", "isométrico", "filtered_isb_isometrico_armando.csv"),
    ("https://raw.githubusercontent.com/diego-taquiri/ISB-equipo11/main/Documentaci%C3%B3n/Laboratorio%2004/emg_raw_data/isb-contrafuerza-armando/opensignals_98D3B1FD3DA9_2024-04-12_12-19-52.txt", "contrafuerza", "filtered_isb_contrafuerza_armando.csv")
]

# Process each URL
for url, title, output_csv in urls:
    print(f"Processing {title} data from {url}")
    load_and_process_emg(url, title, output_csv)

print("All datasets processed and saved.")
