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

# Initialize FastAPI app
app = FastAPI()

# Define tax computation with updated slabs based on ClearTax
class TaxComputation:
    def __init__(self, income: float, deductions: float = 0, regime: str = "new"):
        self.income = income
        self.deductions = deductions + 75000  # Standard deduction of ₹75,000
        self.regime = regime

    def calculate_tax(self):
        taxable_income = max(0, self.income - self.deductions)
        
        if self.regime == "new":
            if taxable_income <= 300000:
                return 0
            elif taxable_income <= 700000:
                return (taxable_income - 300000) * 0.05
            elif taxable_income <= 1000000:
                return (400000 * 0.05) + (taxable_income - 700000) * 0.1
            elif taxable_income <= 1200000:
                return (400000 * 0.05) + (300000 * 0.1) + (taxable_income - 1000000) * 0.15
            elif taxable_income <= 1500000:
                return (400000 * 0.05) + (300000 * 0.1) + (200000 * 0.15) + (taxable_income - 1200000) * 0.2
            else:
                return (400000 * 0.05) + (300000 * 0.1) + (200000 * 0.15) + (300000 * 0.2) + (taxable_income - 1500000) * 0.3
        
        else:  # Old tax regime
            if taxable_income <= 250000:
                return 0
            elif taxable_income <= 500000:
                return (taxable_income - 250000) * 0.05
            elif taxable_income <= 1000000:
                return (250000 * 0.05) + (taxable_income - 500000) * 0.2
            else:
                return (250000 * 0.05) + (500000 * 0.2) + (taxable_income - 1000000) * 0.3

# Define API Models
class TaxInput(BaseModel):
    income: float
    deductions: float = 0.0
    regime: str = "new"  # User can choose "new" or "old" tax regime

@app.post("/calculate_tax")
def get_tax(input_data: TaxInput):
    tax_comp = TaxComputation(input_data.income, input_data.deductions, input_data.regime)
    tax_amount = tax_comp.calculate_tax()
    return {"income": input_data.income, "deductions": input_data.deductions, "tax_regime": input_data.regime, "tax_due": tax_amount}

@app.post("/chatbot")
def chatbot_response(query: str = Form(...)):
    return {"response": "Chatbot functionality not implemented yet."}

@app.post("/process_receipt")
def process_receipt(file: UploadFile = File(...)):
    file.file.seek(0)
    return {"extracted_text": "OCR functionality not implemented yet."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)