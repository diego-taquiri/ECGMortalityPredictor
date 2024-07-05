import os
import h5py
import pandas as pd
from scipy.signal import butter, filtfilt, find_peaks
from scipy.stats import skew, kurtosis
import numpy as np
import itertools

# Define the lead names in the correct order
lead_names = ['DI', 'DII', 'DIII', 'AVR', 'AVL', 'AVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']

# Specify the HDF5 file name and CSV file name
hdf5_filename = r'C:\Users\PC-ERICK\Desktop\1112\exams.hdf5'
csv_filename = r'C:\Users\PC-ERICK\Desktop\1112\exams.csv'
output_filename = r'C:\Users\PC-ERICK\Desktop\1112\exam_features.csv'  # Change this path as needed

# Sampling parameters
sampling_frequency = 400  # Hz
lowcut = 1.0  # Lower cutoff frequency for bandpass filter, in Hz
highcut = 50.0  # Upper cutoff frequency for bandpass filter, in Hz
order = 4  # Filter order for bandpass filter

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band', analog=False)
    y = filtfilt(b, a, data)
    return y

def get_exam_data(exam_number):
    with h5py.File(hdf5_filename, 'r') as file:
        dataset_name = 'tracings'
        data = file[dataset_name]
        
        # Adjust exam_number to match the 0-based index in HDF5 dataset
        index = exam_number - 1
        
        if index < 0 or index >= data.shape[0]:
            print("Invalid exam number. Please enter a number between 1 and", data.shape[0])
            return None
        
        exam_data = data[index]
        return exam_data

def load_exam_metadata():
    metadata = pd.read_csv(csv_filename)
    return metadata

def is_zero_padded(signal, threshold_seconds=1.5):
    num_samples = len(signal)
    max_zero_samples = int(threshold_seconds * sampling_frequency)
    zero_run_lengths = [sum(1 for _ in g) for k, g in itertools.groupby(signal) if k == 0]
    return any(length > max_zero_samples for length in zero_run_lengths)

def find_r_peaks(signal, fs):
    # Find the R peaks (maximum absolute peaks) in the signal
    peaks, _ = find_peaks(np.abs(signal), distance=fs/2.5, height=0.02)  # Adjust parameters as needed
    
    # Calculate average of peak values
    peak_values = np.abs(signal[peaks])
    peak_average = np.mean(peak_values)
    
    # Create an array with R peaks amplitude at appropriate locations
    r_peak_array = np.zeros_like(signal)
    r_peak_array[peaks] = signal[peaks]
    
    return peaks, r_peak_array

def calculate_entropy(signal):
    # Normalize the signal
    signal_normalized = (signal - np.mean(signal)) / np.std(signal)
    hist, bin_edges = np.histogram(signal_normalized, bins='auto', density=True)
    hist = hist[hist > 0]
    entropy = -np.sum(hist * np.log(hist))
    return entropy

def calculate_rmssd(nn_intervals):
    squared_differences = np.diff(nn_intervals) ** 2
    rmssd = np.sqrt(np.mean(squared_differences))
    return rmssd

def calculate_features(filtered_data, r_peak_array):
    # Calculate features
    skewness = skew(filtered_data)
    kurtosis_value = kurtosis(filtered_data)
    entropy_value = calculate_entropy(filtered_data)
    
    # Compute RMSSD from R-R intervals
    rr_intervals = np.diff(np.where(r_peak_array != 0)[0]) / sampling_frequency * 1000  # in milliseconds
    rmssd = calculate_rmssd(rr_intervals)
    
    return skewness, kurtosis_value, entropy_value, rmssd

def filter_valid_exams():
    metadata = load_exam_metadata()
    valid_exams = []
    
    with h5py.File(hdf5_filename, 'r') as file:
        dataset_name = 'tracings'
        data = file[dataset_name]
        
        for i in range(data.shape[0]):
            if not metadata.iloc[i]['death']:
                continue
            
            exam_data = data[i]
            lead_idx = lead_names.index('DII')
            lead_data = exam_data[:, lead_idx]
            
            if not is_zero_padded(lead_data):
                valid_exams.append((i + 1, lead_data, metadata.iloc[i]['timey']))  # Store 1-based index
    
    return valid_exams

def main():
    # Create a DataFrame to store the features of all exams
    features_list = []
    
    valid_exams = filter_valid_exams()
    
    if not valid_exams:
        print("No valid exams found with death=True.")
        return
    
    for exam_number, lead_data, timey_data in valid_exams:
        # Filter DII lead data
        filtered_data = bandpass_filter(lead_data, lowcut, highcut, sampling_frequency)
        
        # Find R peaks and create R peak array
        peaks, r_peak_array = find_r_peaks(filtered_data, sampling_frequency)
        
        # Calculate features
        skewness, kurtosis_value, entropy_value, rmssd = calculate_features(filtered_data, r_peak_array)
        
        # Append features to list
        features_list.append({
            'Exam Number': exam_number,
            'Skewness': skewness,
            'Kurtosis': kurtosis_value,
            'Entropy': entropy_value,
            'RMSSD': rmssd,
            'Timey': timey_data
        })
    
    # Create a DataFrame from the list of features
    features_df = pd.DataFrame(features_list)
    
    # Save the features to a CSV file
    features_df.to_csv(output_filename, index=False)
    print("All features exported successfully.")

if __name__ == "__main__":
    main()
