# Financial Health Assessment

## Project Overview

The Financial Health Assessment project is a full-stack application designed to analyze monthly financial data and provide insights into a user’s overall financial health. By processing income and expense data, the system calculates key financial metrics and presents them in a clear, visual, and easy-to-understand format.

This project helps users understand:
- How much they save each month
- Whether their spending habits are healthy
- Financial trends over time

The solution is built using a FastAPI backend for data processing and a Streamlit frontend for visualization.

---

## Problem Statement

Many individuals track their income and expenses but find it difficult to interpret what those numbers mean for their financial well-being. Raw financial data alone does not provide insights into savings behavior, expense control, or long-term stability.

This project addresses that gap by automating financial analysis and converting raw data into meaningful metrics and visual insights.

---

## Features

- Upload monthly cashflow data using a CSV file
- Calculate key financial metrics:
  - Savings Rate
  - Expense Ratio
  - Health Score
- Identify overall financial trend:
  - Improving
  - Stable
  - Declining
- Classify financial health:
  - Excellent
  - Good
  - Needs Improvement
- Monthly financial breakdown in tabular format
- Interactive income vs expense charts
- REST API with automatic Swagger documentation

---

## System Architecture

The project follows a client–server architecture:

Frontend (Streamlit):
- Handles user interaction
- Accepts CSV uploads
- Displays metrics, tables, and graphs
- Runs locally for visualization

Backend (FastAPI):
- Processes financial data
- Performs calculations and analysis
- Exposes REST APIs
- Deployed publicly on Render

---

## Tech Stack

- Programming Language: Python
- Backend Framework: FastAPI
- Frontend Framework: Streamlit
- Data Processing: Pandas
- API Communication: Requests
- Backend Deployment: Render
- Frontend Execution: Local (Streamlit)

---

## Project Structure

financial-health-assessment/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── sample_data/
│   └── monthly_cashflow.csv
│
└── README.md

---

## Live Deployment

Backend (Publicly Deployed):
https://financial-health-assessment.onrender.com

This endpoint confirms that the backend is live and running.

API Documentation (Swagger UI):
https://financial-health-assessment.onrender.com/docs

---

## Frontend (Streamlit)

The Streamlit frontend runs locally and communicates with the deployed backend API to visualize financial health metrics and charts.

To run the frontend locally:

cd frontend  
streamlit run app.py

---

## How to Run the Project Locally

1. Start the backend:
cd backend  
uvicorn main:app --reload

2. Start the frontend:
cd frontend  
streamlit run app.py

---

## Input CSV Format

The CSV file must contain the following columns:
- month
- income
- expenses

Example:

month,income,expenses  
2024-01-01,150000,90000  
2024-02-01,160000,95000  
2024-03-01,155000,92000  

---

## Output

After uploading the CSV, the application provides:
- Average savings rate
- Expense ratio
- Overall financial health classification
- Trend analysis
- Monthly financial breakdown table
- Income vs expense visualization

---

## Demo Video

A complete demonstration video showing:
- Backend deployment on Render
- API documentation via Swagger UI
- Local Streamlit frontend with charts and tables

(The demo video link is provided in the submission portal.)

---

## Future Enhancements

- Public deployment of frontend UI
- Support for multiple users
- Monthly financial forecasting using machine learning
- Export financial reports as PDF
- Database integration for persistent storage

---

## Author

Saipavan Jamuram

---

## Conclusion

This project demonstrates how financial data can be transformed into actionable insights using modern Python frameworks. By combining FastAPI and Streamlit, the system provides both a robust backend and an intuitive frontend for financial health analysis.
