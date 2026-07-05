# Credit Card Approval Prediction — Project Overview

## Description
This project predicts whether a credit card application should be approved or rejected, using a machine learning model trained on historical applicant data, exposed through a simple Flask web interface.

## Features
- Predicts credit card approval based on Gender, Annual Income, Income Type, and Education Level
- Returns a plain-language explanation for both approvals and rejections
- Simple, lightweight Flask web interface

## Tech Stack
| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Machine Learning | scikit-learn |
| Model Persistence | joblib |
| Data Processing | pandas |
| Frontend | HTML, CSS |

## Input Features
| Feature | Encoding |
|---|---|
| Gender | 0 = Female, 1 = Male |
| Annual Income | Numeric value |
| Income Type | 0 = Commercial Sector, 1 = State/Government Sector, 2 = Working Sector |
| Education Level | 0 = Bachelor's, 1 = High School, 2 = Master's, 3 = PhD |