# PDF Certificate Generator

This Python tool automates the creation of personalized PDF certificates using a pre-designed template. It overlays names sourced from a CSV file onto the template, with customizable text positioning and font support.

## Features

- **Custom Font Support:** Use your own `.ttf` font for professional styling.
- **Automated PDF Creation:** Generate individual certificates for each name in bulk.
- **Precise Text Positioning:** Easily adjust the placement of text on the template.
- **Batch Processing:** Efficiently handles multiple names from a CSV file.

## Prerequisites

Ensure you have Python 3.x installed along with the following Python packages:

```bash
pip install PyPDF2 reportlab

## Project Structure

Copy code
project-directory/
├── data/
│   └── names.csv                     # CSV file containing the names
├── fonts/
│   └── custom_font.ttf               # Custom font file
├── output/                           # Output directory for generated PDFs
├── templates/
│   └── certificate_template.pdf      # PDF template for certificates
├── main.py                           # Main script to run the generator
└── README.md                         # This README file
