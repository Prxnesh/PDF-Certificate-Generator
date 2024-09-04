PDF Certificate Generator
==========================

This project generates personalized PDF certificates by overlaying text onto a pre-designed PDF template. The names are sourced from a CSV file, and each name is placed at a specific position on the template using a custom font.

Features
--------

- Customizable Font: You can use your own font by placing the `.ttf` file in the `fonts` directory.
- Automated PDF Creation: Generates individual PDFs for each name listed in the CSV file.
- Flexible Text Positioning: Allows for adjustment of the text position on the PDF.

Prerequisites
-------------

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your local machine.
- Install the required Python packages using the command:

  pip install PyPDF2 reportlab

Project Structure
-----------------

project-directory/
│
├── data/
│   └── names.csv                     # CSV file containing the names
│
├── fonts/
│   └── custom_font.ttf               # Custom font file
│
├── output/                           # Output directory for generated PDFs
