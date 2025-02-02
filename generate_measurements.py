import csv
import random
import time
import os


def generate_voltage():
    """Simulates the generation of voltage values."""
    return random.uniform(30, 31)  # Adjust the range as per your requirements
def generate_vin():
    """Simulates the generation of voltage values."""
    return random.uniform(41.0, 41.5)  # Adjust the range as per your requirements

def generate_temperature():
    """Simulates the generation of voltage values."""
    return random.uniform(119, 120)  # Adjust the range as per your requirements
def generate_ctm(p):
    """Simulates the generation of voltage values."""
    weights = [p, 1 - p]
    return random.choices([1, 0], weights=weights)[0]
    #return random.randint(0, 1)  # Adjust the range as per your requirements


def calculate_power(voltage):
    """Calculates the power based on the voltage value."""
    return (voltage * 10)  # Adjust the formula as per your requirements

def save_to_csv(data, filename):
    """Saves the data to a CSV file, overwriting if it already exists."""
    file_exists = os.path.isfile(filename)
    mode = 'a' if file_exists else 'w'  # Use 'w' mode only if the file doesn't exist
    with open(filename, mode, newline='') as file:
        writer = csv.writer(file)
        if not file_exists and mode == 'w':  # Only write header if the file is newly created
            writer.writerow(header)
        if mode == 'a':
            writer.writerow(data)

# Configuration
num_readings = 100000  # Number of readings to generate
delay = 0.5  # Delay in seconds between each reading
output_file = 'measurements.csv'  # Output file name

# Generate and save the measurements
header = ['Time', 'Vin', 'Vout', 'Power', 'thermistor', 'Is_CTM']
if not os.path.isfile(output_file):
    save_to_csv(header, output_file)

for _ in range(num_readings):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    voltage = generate_voltage()
    v_in = generate_vin()
    power = calculate_power(voltage)
    temperature = generate_temperature()
    is_ctm = generate_ctm(0.05)
    measurement = [timestamp, v_in, voltage, power, temperature, is_ctm]
    save_to_csv(measurement, output_file)
    time.sleep(delay)

print(f"{num_readings} measurements saved to '{output_file}'")
