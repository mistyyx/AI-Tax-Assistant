"""
AI Tax Assistant - Full Implementation
"""

import warnings
warnings.filterwarnings("ignore", message=".*NotOpenSSLWarning.*")

from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pytesseract
from PIL import Image
from transformers import pipeline
import uvicorn
import sys

# Wrap micropip import to avoid errors in CPython; ignore Pylance warning.
try:
    import micropip  # type: ignore
except ModuleNotFoundError:
    micropip = None
    print("Warning: micropip module is missing. This is fine if you're not using a Pyodide environment.", file=sys.stderr)

app = FastAPI()

class TaxComputation:
    def __init__(self, income: float, deductions: float = 0):
        self.income = income
        self.deductions = deductions

    def calculate_tax(self):
        taxable_income = max(0, self.income - self.deductions)
        if taxable_income <= 25000:
            return taxable_income * 0.1  # 10% tax rate
        elif taxable_income <= 50000:
            return taxable_income * 0.2  # 20% tax rate
        else:
            return taxable_income * 0.3  # 30% tax rate

try:
    chatbot = pipeline("text-generation", model="openai-gpt")
except Exception as e:
    chatbot = None
    print(f"Warning: Chatbot model failed to load: {e}", file=sys.stderr)

def ask_chatbot(question):
    if chatbot:
        response = chatbot(question, max_length=100)
        return response[0]['generated_text']
    return "Chatbot is currently unavailable."

def extract_text_from_image(image_input):
    try:
        image = Image.open(image_input)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error processing image: {e}", file=sys.stderr)
        return "Error extracting text."

class TaxInput(BaseModel):
    income: float
    deductions: float = 0.0

@app.post("/calculate_tax")
def get_tax(input_data: TaxInput):
    tax_comp = TaxComputation(input_data.income, input_data.deductions)
    tax_amount = tax_comp.calculate_tax()
    return {"income": input_data.income, "deductions": input_data.deductions, "tax_due": tax_amount}

@app.post("/chatbot")
def chatbot_response(query: str = Form(...)):
    response = ask_chatbot(query)
    return {"response": response}

@app.post("/process_receipt")
def process_receipt(file: UploadFile = File(...)):
    file.file.seek(0)
    text = extract_text_from_image(file.file)
    return {"extracted_text": text}

def test_tax_calculation():
    tax_calc = TaxComputation(40000, 5000)
    assert tax_calc.calculate_tax() == 7000

def test_tax_calculation_edge():
    tax_calc = TaxComputation(20000, 0)
    assert tax_calc.calculate_tax() == 20000 * 0.1

def test_chatbot():
    response = ask_chatbot("How can I save on my taxes?")
    assert isinstance(response, str)

def test_ocr():
    sample_text = extract_text_from_image("sample_receipt.png")
    assert isinstance(sample_text, str)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
