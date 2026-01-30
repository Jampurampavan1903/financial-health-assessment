from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io
from sklearn.linear_model import LinearRegression
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Financial Health Assessment API")


# ---------- RESPONSE MODELS ----------

class Summary(BaseModel):
    average_savings_rate: float
    overall_score: float
    overall_health: str
    trend: str


class MonthlyRecord(BaseModel):
    month: str
    income: float
    expenses: float
    savings: float
    savings_rate: float
    expense_ratio: float
    health_score: float
    health: str


class ApiResponse(BaseModel):
    summary: Summary
    monthly_analysis: List[MonthlyRecord]
    forecast_next_month_income: float


# ---------- ROOT ----------

@app.get("/")
def root():
    return {"status": "Backend is running"}


# ---------- ANALYZE ----------

@app.post("/analyze", response_model=ApiResponse)
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()

    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    # Calculations
    df["savings"] = df["income"] - df["expenses"]
    df["savings_rate"] = df["savings"] / df["income"]
    df["expense_ratio"] = df["expenses"] / df["income"]

    df["health_score"] = (df["savings_rate"] > 0.3).astype(int)
    df["health"] = df["health_score"].map({1: "Excellent", 0: "Needs Improvement"})

    # Trend
    if df["health_score"].iloc[-1] > df["health_score"].iloc[0]:
        trend = "Improving"
    elif df["health_score"].iloc[-1] < df["health_score"].iloc[0]:
        trend = "Declining"
    else:
        trend = "Stable"

    # Summary
    average_savings_rate = round(df["savings_rate"].mean(), 2)
    overall_score = round(df["health_score"].mean(), 2)

    if overall_score >= 0.8:
        overall_health = "Excellent"
    elif overall_score >= 0.5:
        overall_health = "Good"
    else:
        overall_health = "Poor"

    summary = Summary(
        average_savings_rate=average_savings_rate,
        overall_score=overall_score,
        overall_health=overall_health,
        trend=trend
    )

    # ML Forecast
    X = pd.RangeIndex(len(df)).values.reshape(-1, 1)
    y = df["income"].values
    model = LinearRegression()
    model.fit(X, y)
    forecast = round(model.predict([[len(df)]])[0], 2)

    monthly_analysis = df[[
        "month",
        "income",
        "expenses",
        "savings",
        "savings_rate",
        "expense_ratio",
        "health_score",
        "health"
    ]].to_dict(orient="records")

    return ApiResponse(
        summary=summary,
        monthly_analysis=monthly_analysis,
        forecast_next_month_income=forecast
    )