Below is a **clean, professional `README.md`** you can directly use for your GitHub repository, based strictly on the three sections shown in the images (Prescription Document, Patient Details Document, FastAPI Server).

---

# 🏥 Medical Data Extraction Project

This repository contains a **Medical Data Extraction system** that processes medical documents (PDFs/images) to extract structured information such as **prescription details** and **patient details**, and exposes the functionality via a **FastAPI server**.

The project follows a modular, testable, and production-ready architecture.

---

## 📌 Project Overview

The project is divided into three main parts:

1. **Prescription Document Processing**
2. **Patient Details Document Processing**
3. **FastAPI Server for API Access & Deployment**

The system uses:

* PDF text extraction
* Image preprocessing with OpenCV
* Regular Expressions for field extraction
* Object-oriented design
* Unit testing with `pytest`
* FastAPI for backend services

---

## 🧾 Part 1: Prescription Document Extraction

### Features

* Extract text from PDF prescription documents
* Apply OpenCV thresholding for better OCR accuracy
* Use Regular Expressions to identify:

  * Medicines
  * Dosage
  * Frequency
  * Instructions
* Object-oriented prescription model
* Code refactoring for maintainability
* Unit testing using `pytest`

### Key Concepts Covered

* PDF text extraction
* Image preprocessing (thresholding)
* Regex-based data extraction
* Python classes
* Test-driven development

---

## 👤 Part 2: Patient Details Document Extraction

### Features

* Extract patient name and demographic details
* Incremental extraction (name first, then remaining fields)
* PatientDetails class design
* Integration with a unified document extractor

### Extracted Fields (Example)

* Patient Name
* Age
* Gender
* Address
* Phone Number
* Document ID (if present)

---

## 🚀 Part 3: FastAPI Server

### Features

* FastAPI basics and setup
* REST API endpoints for document upload
* Integration with extraction modules
* JSON-based structured responses
* Ready for frontend integration and deployment

### Example Endpoints

```http
POST /extract/prescription
POST /extract/patient-details
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/medical-data-extraction.git
cd medical-data-extraction
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the FastAPI Server

```bash
uvicorn src.api.main:app --reload
```

Open API documentation:

* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🧠 Key Technologies Used

* Python
* FastAPI
* OpenCV
* Regular Expressions (Regex)
* Pytest
* OCR / PDF Text Extraction

---

## 📈 Future Enhancements

* Support for handwritten prescriptions
* Database integration
* Authentication & authorization
* Frontend UI
* Cloud deployment (Docker + AWS/GCP)

---

## 🤝 Contribution

Contributions are welcome!
Please fork the repository, create a feature branch, and submit a pull request.

---
