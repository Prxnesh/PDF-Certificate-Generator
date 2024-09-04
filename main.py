import csv
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO

# Constants (generalized paths)
CSV_FILE_PATH = './data/names.csv'
OUTPUT_DIR = './output/'
FONT_PATH = './fonts/custom_font.ttf'
PDF_TEMPLATE_PATH = './templates/certificate_template.pdf'

# Text positioning variables (in inches)
TEXT_POSITION_X_INCHES = 3.4  # Horizontal position adjustment
TEXT_POSITION_Y_INCHES = 0.05  # Vertical position adjustment

def create_pdf_with_text(template_pdf_path, output_pdf_path, name):
    # Read the existing PDF template
    existing_pdf = PdfReader(template_pdf_path)
    output = PdfWriter()
    
    # Add existing pages from the template
    for page_num in range(len(existing_pdf.pages)):
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        
        # Register and set the custom font
        pdfmetrics.registerFont(TTFont('CustomFont', FONT_PATH))
        can.setFont("CustomFont", 24)
        
        # Get text size
        text_width, text_height = can.stringWidth(name, "CustomFont", 31), 31
        
        # Calculate position (convert inches to points: 1 inch = 72 points)
        x_position = (letter[0] - text_width) / 2 + TEXT_POSITION_X_INCHES * 72
        y_position = (letter[1] - text_height) / 2 - TEXT_POSITION_Y_INCHES * 72  # Subtract to move text down

        # Place the text at the specified coordinates
        can.drawString(x_position, y_position, name)
        can.save()
        
        # Move the PDF canvas to the output buffer
        packet.seek(0)
        new_pdf = PdfReader(packet)
        
        # Add the "watermark" (which is the new PDF with the text) to the existing page
        page = existing_pdf.pages[page_num]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)
    
    # Save the final output
    with open(output_pdf_path, "wb") as f:
        output.write(f)

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Check if the font file exists
    if not os.path.isfile(FONT_PATH):
        print(f"Font file not found at {FONT_PATH}")
        return

    # Read names from CSV file
    names = []
    with open(CSV_FILE_PATH, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            names.append(row[0])

    # Generate PDFs for each name
    for name in names:
        output_pdf_path = os.path.join(OUTPUT_DIR, f"{name}.pdf")
        create_pdf_with_text(PDF_TEMPLATE_PATH, output_pdf_path, name)
        print(f"Generated certificate for: {name}")

if __name__ == "__main__":
    main()
