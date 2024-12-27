#This script uses a CSV file Downloaded from Meraki Dashboard to batch rename devices.

import meraki
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Replace with your API key and organization ID
API_KEY = ''
ORG_ID = ''

# Initialize the Meraki Dashboard API client
dashboard = meraki.DashboardAPI(API_KEY)

# Use tkinter to open a file dialog and select the CSV file
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
CSV_FILE = askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

if not CSV_FILE:
    print("No file selected. Exiting.")
else:
    # Read the CSV file
    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Iterate over each row in the CSV file
        #This script anticipates that the source CSV is coming from Dashboard and the data is in the original columns
        for row in reader:
            serial = row[2]
            new_name = row[0]

            # Update the device name
            try:
                dashboard.devices.updateDevice(
                    serial=serial,
                    name=new_name
                )
                print(f"Device {serial} renamed to {new_name}")
            except meraki.APIError as e:
                print(f"Error updating device {serial}: {e}")