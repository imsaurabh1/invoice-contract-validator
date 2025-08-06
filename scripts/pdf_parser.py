import pdfplumber
import re

# Extracting text from PDF file
def extract_text_from_pdf(file_path):
    text = ""

    # open PDF file
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    # return combined text from all pages        
    return text


# Finding and exacting specific fields from invoice text
def extract_invoice_info(text):
    info = {}
    # Amount search
    info['amount'] = re.search(r'Total Amount:?\s+(?:EUR\s*)?([\d,\.]+)', text)
    # Due Date Search
    info['due_date'] = re.search(r'Due Date:?\s+(\d{1,2}\s+\w+\s+\d{4})', text)
    # Service Search
    info['service'] = re.search(r'Service:?\s+(.+)', text)
    
    # return dictionary with extracted strings
    return {
        'amount': info['amount'].group(1) if info['amount'] else '',
        'due_date': info['due_date'].group(1) if info['due_date'] else '',
        'service': info['service'].group(1) if info['service'] else '',
    }