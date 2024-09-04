# PDF Certificate Generator

This Python tool generates personalized PDF certificates by overlaying text onto a pre-designed PDF template. Names are sourced from a CSV file, and text is positioned using a custom font with adjustable coordinates.

## Features

- **Custom Font Support:** Use your own `.ttf` font file.
- **Automated PDF Creation:** Generates individual PDF certificates for each name.
- **Flexible Text Positioning:** Adjust the text position on the template for precise placement.

## Prerequisites

- Python 3.x
- Required Python packages:

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
