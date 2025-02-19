# QR Code Generator

## Overview

This is a simple app to create QR codes. You can type in the text, generate a QR code, and save it as an image file.

## Features

- Create QR Codes: Enter text and generate a QR code.
- Display QR Codes: See the generated QR code in the app.
- Save QR Codes: Save the QR code as a PNG image file.

## Requirements

- Python 3.x
- `pyqrcode` library
- `tkinter` library (included with Python)
- `Pillow` library for image handling

## Installation

1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   ```
2. **Go to the project folder**:
   ```sh
   cd qr-code-generator
   ```
3. **Install the required libraries**:
   ```sh
   pip install pyqrcode pillow
   ```

## Usage

1. **Run the app**:
   ```sh
   python qr_code_generator.py
   ```
2. **Generate a QR Code**:
   - Enter text in the input field.
   - Click the "Create" button to generate the QR code.
   - The QR code will be displayed in the app.

3. **Save the QR Code**:
   - Click the "Download" button.
   - Choose where to save the QR code image.

## File Information

- `qr_code_generator.py`: The main app file with the code.

## Notes

- The app uses a high-quality filter for resizing images.
- The default file name for the QR code is `qrcode.png`.
