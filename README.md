# AI-Tax-Assistant

## Repository for Google Hackathon Submission

### **Description**
AI-Tax-Assistant is an AI-powered tax assistant that helps automate tax filing by leveraging FastAPI, AI-driven chatbots, and OCR-based document processing. This solution aims to reduce human errors, improve efficiency, and simplify tax calculations for users by integrating multiple AI techniques and structured data processing.

### **Features**
- **Tax Calculation Engine**: Implements a rule-based system to compute tax based on user-provided income and deductions.
- **AI Chatbot for Tax Queries**: Uses Natural Language Processing (NLP) to answer tax-related questions.
- **OCR Document Processing**: Extracts financial data from scanned invoices and receipts.
- **FastAPI Backend**: Provides a RESTful API for integration and user interaction.
- **Secure and Scalable**: Implements security measures to ensure data privacy.

### **Technology Stack**
- **Backend**: Python, FastAPI
- **AI/ML**: Transformers (Hugging Face), PyTorch (for chatbot, optional)
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

#### **2️⃣ Set Up Virtual Environment (Recommended)**
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
The API will be available at: **http://127.0.0.1:8000/**

---

### **Usage**
#### **1️⃣ API Endpoints**
- **Calculate Tax** (`POST /calculate_tax`)
  - Request Body: `{ "income": 50000, "deductions": 10000 }`
  - Response: `{ "income": 50000, "deductions": 10000, "tax_due": 8000 }`

- **Chatbot Query** (`POST /chatbot`)
  - Request: `{ "query": "How can I reduce my tax?" }`
  - Response: `{ "response": "You can reduce tax by investing in retirement funds." }`

- **Receipt Processing** (`POST /process_receipt`)
  - Upload an image file of a receipt.
  - Response: Extracted text from the image.

---

### **File Structure**
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
The project requires the following Python packages:
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
Install all dependencies using:
```sh
pip install -r requirements.txt
```

---

### **Limitations**
- The chatbot requires **PyTorch** or **TensorFlow** to function fully.
- OCR quality depends on the clarity of scanned documents.
- Current tax rules are simplified and may not cover all real-world cases.

---

### **References**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Transformers by Hugging Face](https://huggingface.co/docs/transformers/index)
- [Pytesseract OCR](https://pypi.org/project/pytesseract/)

---

### **Contributing**
If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Submit a pull request.

---

### **License**
This project is licensed under the MIT License.

---

### **Contact**
For any queries, contact the project maintainer at [your-email@example.com].

