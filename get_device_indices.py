import sounddevice as sd
import csv

def find_device_index(device_name):
    devices = sd.query_devices()
    for index, device in enumerate(devices):
        if device['name'] == device_name:
            return index
    return None

def update_config(config_file, input_index, output_index):
    config = []
    with open(config_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'input':
                row[1] = str(input_index)
            elif row[0] == 'output':
                row[1] = str(output_index)
            config.append(row)

    with open(config_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(config)
# Usage
input_device = find_device_index("pulse")
output_device = find_device_index("default")

config_file_path = "MED/config.csv"  # Replace with your CSV file path


if (input_device and  output_device) is not None:
    # Update the CSV file with the new device indices
    update_config(config_file_path, input_device, output_device)
    print("Device indices updated in the configuration file.")
else:
    if input_device is None and output_device is None:
        print("Both Input and Output Devices not found.")
    elif input_device is None:
        print("Input Device not found.")
    elif output_device is None:
        print("Output Device not found.")
