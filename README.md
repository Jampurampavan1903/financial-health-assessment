\# Financial Health Assessment



This project is a full-stack Financial Health Assessment application that analyzes monthly cashflow data and provides insights into savings, expenses, and overall financial health.



The application consists of:

\- A FastAPI backend for data processing and analysis

\- A Streamlit frontend for interactive visualization



---



\## Features



\- Upload monthly cashflow CSV file

\- Calculate savings rate and expense ratio

\- Generate overall financial health classification

\- Display monthly breakdown in tabular format

\- Visualize income vs expenses using charts

\- REST API with Swagger documentation



---



\## Tech Stack



\- Python

\- FastAPI (Backend API)

\- Streamlit (Frontend UI)

\- Pandas

\- Requests



---



\## Project Structure



financial-health-assessment/

│

├── backend/

│   └── main.py

│

├── frontend/

│   └── app.py

│

├── sample\_data/

│   └── monthly\_cashflow.csv

│

└── README.md



---



\## How to Run the Project



\### Step 1: Start the Backend Server



Open a terminal and run:



cd backend  

uvicorn main:app --reload



Backend will start at:

http://127.0.0.1:8000



Swagger UI:

http://127.0.0.1:8000/docs



---



\### Step 2: Start the Frontend Application



Open another terminal and run:



cd frontend  

streamlit run app.py



Frontend will start at:

http://localhost:8501



---



\## Input CSV Format



The CSV file should contain the following columns:



\- month

\- income

\- expenses



Example:



month,income,expenses  

2024-01-01,150000,90000  

2024-02-01,160000,95000  



---



\## Output



The application provides:



\- Average Savings Rate

\- Trend Analysis (Improving / Stable / Declining)

\- Overall Financial Health (Excellent / Good / Needs Attention)

\- Monthly financial breakdown table

\- Income vs Expenses visualization



---



\## Author



SaiPavanKalyan Jamuram

