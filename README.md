# Meraki Bulk Device Rename

A Python script for bulk renaming Meraki devices using a CSV file exported from the Meraki Dashboard.

## Features

- Bulk rename Meraki devices using CSV data
- GUI file selector for choosing the CSV file
- Error handling for API operations
- Progress feedback for each device update

## Prerequisites

- Python 3.6+
- Meraki Python SDK
- Meraki API key with write access
- CSV file exported from Meraki Dashboard

## Installation

1. Install required packages:
   ```bash
   pip install meraki tkinter
   ```

2. Update the script with your API credentials:
   - Set `API_KEY` to your Meraki Dashboard API key

## Usage

1. Export a device list from Meraki Dashboard to CSV
2. Run the script:
   ```bash
   python bulk_rename.py
   ```
3. Select your CSV file in the file dialog
4. The script will process each device and show progress

## CSV Format

The script expects a CSV file exported from Meraki Dashboard with these columns:
- Column 0: New device name
- Column 2: Device serial number

## Error Handling

The script includes error handling for common scenarios:
- Missing or invalid CSV file
- API authentication failures
- Device update errors

Errors are displayed in the console with the affected device serial number.