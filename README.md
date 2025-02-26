# AI-Tax-Assistant

## Repository for Google Hackathon Submission

### **Overview**
AI-Tax-Assistant is designed to simplify tax filing by automating key processes using AI. This tool helps individuals and businesses calculate taxes, get tax-related advice via an AI-powered chatbot, and extract financial data from receipts using OCR technology.

### **Key Features**
- **Tax Calculation**: Computes tax based on income and deductions using a predefined rule-based system.
- **AI Chatbot for Tax Queries**: Provides tax-related guidance using NLP.
- **OCR Document Processing**: Extracts financial details from scanned invoices and receipts.
- **FastAPI Backend**: A lightweight and efficient REST API for easy integration.
- **Security & Scalability**: Ensures data privacy and supports multiple users.

### **Technology Stack**
- **Backend**: Python, FastAPI
- **AI/ML**: Hugging Face Transformers, PyTorch (optional for chatbot)
- **OCR**: Pytesseract, Pillow
- **Data Processing**: Pandas, NumPy
- **Deployment**: Uvicorn (FastAPI Server), GitHub

---

### **Getting Started**
#### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/mistyyx/AI-Tax-Assistant.git
cd AI-Tax-Assistant
```

#### **2️⃣ Set Up Virtual Environment**
```sh
python3 -m venv .venv
source .venv/bin/activate  # On Mac/Linux
.venv\Scripts\activate     # On Windows
```

#### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

#### **4️⃣ Run the Application**
```sh
uvicorn code1:app --reload
```
The API will be accessible at: **http://127.0.0.1:8000/**

---

### **How to Use**
#### **API Endpoints**
- **Calculate Tax** (`POST /calculate_tax`)
  - Request Body:
    ```json
    { "income": 50000, "deductions": 10000 }
    ```
  - Response:
    ```json
    { "income": 50000, "deductions": 10000, "tax_due": 8000 }
    ```

- **Chatbot Query** (`POST /chatbot`)
  - Example Request:
    ```json
    { "query": "How can I reduce my tax?" }
    ```
  - Example Response:
    ```json
    { "response": "You can reduce tax by investing in retirement funds." }
    ```

- **Receipt Processing** (`POST /process_receipt`)
  - Upload an image of a receipt.
  - Response: Extracted text from the receipt.

---

### **Project Structure**
```
📂 AI-Tax-Assistant
 ┣ 📂 .venv            # Virtual environment (optional)
 ┣ 📂 src              # Source code
 ┃ ┣ 📜 code1.py       # Main application file
 ┣ 📂 docs             # Documentation files
 ┣ 📂 data             # Sample data and test files
 ┣ 📂 tests            # Unit tests
 ┣ 📜 requirements.txt # Dependencies
 ┣ 📜 README.md        # Project documentation
```

---

### **Dependencies**
This project requires:
```plaintext
fastapi
uvicorn
pydantic
pandas
numpy
pytesseract
pillow
transformers
torch  # Required if chatbot AI is enabled
```
To install all dependencies, run:
```sh
pip install -r requirements.txt
```

---

### **Limitations**
- The chatbot requires PyTorch or TensorFlow to work fully.
- OCR accuracy depends on the quality of scanned documents.
- The tax computation is simplified and does not cover all tax regulations.

---

### **References**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Transformers by Hugging Face](https://huggingface.co/docs/transformers/index)
- [Pytesseract OCR](https://pypi.org/project/pytesseract/)

---

### **Contributing**
Want to contribute? Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Submit a pull request.

---


### **Contact**
For questions or suggestions, feel free to reach out at [anusuyasadhukhan4@gmail.com].