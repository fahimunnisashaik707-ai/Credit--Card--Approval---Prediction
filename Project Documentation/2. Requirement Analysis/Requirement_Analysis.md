# 2. Requirement Analysis

## Functional Requirements
- Accept 4 applicant inputs: Gender, Annual Income, Income Type, Education Level
- Predict credit card approval status (Approved / Rejected) using a trained ML model
- Return a human-readable explanation for the decision (approval or rejection reasoning)
- Expose the prediction via a simple web interface (form submission)

## Non-Functional Requirements
- Response time: prediction should return in well under 1 second
- Usability: simple web form, no technical knowledge required to use
- Portability: runs locally on Windows/Linux/macOS with Python installed

## Hardware Requirements
- Processor: Intel Core i3 or above
- RAM: Minimum 4 GB
- Storage: Minimum 5 GB free space
- Internet connection (for installing dependencies)

## Software Requirements
- OS: Windows / Linux / macOS
- Python 3.x
- VS Code or Jupyter Notebook
- Git & GitHub account

## Required Libraries
- Flask (web framework)
- joblib (model loading/persistence)
- pandas (data handling for inference)
- scikit-learn (model training, used in `notebook.ipynb`)

## Dataset Requirement
A labeled historical credit card application dataset (`creditcard_data.csv`, placed in a `data/` folder) containing applicant demographic/financial fields and the actual approval outcome, used to train the model in `notebook.ipynb`.

## Input Feature Requirements
| Feature | Type | Notes |
|---|---|---|
| Gender | Categorical | Encoded as 0 = Female, 1 = Male |
| Annual Income | Numeric | Applicant's yearly income |
| Income Type | Categorical | 0 = Commercial Sector, 1 = State/Government Sector, 2 = Working Sector |
| Education Level | Categorical | 0 = Bachelor's Degree, 1 = High School, 2 = Master's Degree, 3 = PhD |