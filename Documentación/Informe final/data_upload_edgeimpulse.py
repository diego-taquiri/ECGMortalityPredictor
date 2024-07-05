import os
import random
import requests
import json

api_key = 'ei_7b0377797eb46d45995e791ec845152154e684137cb3ded067b228d3dfc2485b'
output_folder = r'C:\Users\Erick\Desktop\1113\filtered_data_featuresIII'  # Change to your actual folder path

# Function to upload a single file
def upload_file(file_path, api_key):
    try:
        with open(file_path, 'rb') as f:
            file_name = os.path.basename(file_path)
            res = requests.post(
                url='https://ingestion.edgeimpulse.com/api/training/files',
                headers={
                    'x-api-key': api_key,
                },
                files={'data': (file_name, f, 'application/csv')}
            )

            if res.status_code == 200:
                print(f'Uploaded {file_name} to Edge Impulse\n', res.status_code, res.content)
            else:
                print(f'Failed to upload {file_name} to Edge Impulse\n', res.status_code, res.content)
    except Exception as e:
        print(f'Error uploading {file_path}: {e}')

# Function to create and upload the JSON configuration file
def create_and_upload_config(csv_file_name, api_key):
    try:
        config_data = {
            "version": 1,
            "fileName": csv_file_name,
            "created": 1720147164533,  # Replace with timestamp of creation (optional)
            "delimiter": ",",
            "skipFirstLines": 0,
            "spec": {
                "type": "timeseries-row",
                "labelsColumn": "Timey Data",
                "valueColumns": [
                    "Filtered Signal",
                    "Skewness",
                    "Kurtosis",
                    "Entropy",
                    "RMSSD"
                ],
                "timestamp": {
                    "type": "column",
                    "timestampColumn": "Timestamps",
                    "format": "elapsed-seconds",
                    "frequency": 400  # Adjust based on your data's sampling frequency
                },
                "dealWithMultipleLabels": "use-last-label"
            }
        }

        # Save JSON configuration to file
        config_file_name = "csv_config.json"
        with open(config_file_name, 'w') as json_file:
            json.dump(config_data, json_file, indent=4)

        # Upload the JSON configuration file
        upload_file(config_file_name, api_key)
    
    except Exception as e:
        print(f'Error creating/uploading config for {csv_file_name}: {e}')

# Function to split data into train/test sets
def split_train_test(files, split_ratio=0.8):
    random.shuffle(files)
    split_index = int(len(files) * split_ratio)
    train_files = files[:split_index]
    test_files = files[split_index:]
    return train_files, test_files

# List all files in the output folder
all_files = [os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.endswith('.csv')]

# Split into train and test sets
train_files, test_files = split_train_test(all_files)

# Upload files for training set
for train_file in train_files:
    create_and_upload_config(os.path.basename(train_file), api_key)
    upload_file(train_file, api_key)

# Optionally, upload files for testing set
for test_file in test_files:
    create_and_upload_config(os.path.basename(test_file), api_key)
    print(f'Upload {os.path.basename(test_file)} to CSV Wizard for testing')
