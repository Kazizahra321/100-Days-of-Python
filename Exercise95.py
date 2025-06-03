# Exercise 95 :  example of how to merge multiple PDF files using pypdf:

'''
from pypdf import PdfMerger

merger = PdfMerger()

# Open the PDF files
with open("file1.pdf", "rb") as file1, open("file2.pdf", "rb") as file2, open("file3.pdf", "rb") as file3:
    # Append the first 3 pages of file1
    merger.append(fileobj=file1, pages=(0, 3))
    
    # Insert the first page of file2 at position 2
    merger.merge(position=2, fileobj=file2, pages=(0, 1))
    
    # Append the entire file3
    merger.append(file3)

# Write the merged PDF to a new file
with open("merged.pdf", "wb") as output_pdf:
    merger.write(output_pdf)
merger.close()

'''


from pypdf import PdfWriter, PdfReader

# List of PDF files to merge
pdfs = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Create a PdfWriter object
writer = PdfWriter()

# Append each PDF file to the writer
for pdf in pdfs:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)

# Write the merged PDF to a new file
with open("merged.pdf", "wb") as output_pdf:
    writer.write(output_pdf) 


'''
# or
from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close() 
'''