# Exercise 94 pypdf module

'''
#create a pdf
# pip install fpdf

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Hello World!", ln=True, align="C")
pdf.output("test.pdf")
'''
from pypdf import PdfReader


reader = PdfReader("test.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)

# Save the Extracted Text to a File:
with open("extracted_text.pdf", "w") as text_file:
    text_file.write(text)

# Count the Number of Words:
word_count = len(text.split())
print(f"Number of words in the text: {word_count}")

# Example Code for Saving and Searching Text

from pypdf import PdfReader

try:
    reader = PdfReader("test.pdf")
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    
    # Save the extracted text to a file
    with open("extracted_text.txt", "w") as text_file:
        text_file.write(text)
    
    # Search for a specific keyword
    keyword = "World!"
    if keyword in text:
        print(f"'{keyword}' found in the text!")
    else:
        print(f"'{keyword}' not found in the text.")
    
    # Print the number of words
    word_count = len(text.split())
    print(f"Number of words in the text: {word_count}")

except Exception as e:
    print(f"An error occurred: {e}")
