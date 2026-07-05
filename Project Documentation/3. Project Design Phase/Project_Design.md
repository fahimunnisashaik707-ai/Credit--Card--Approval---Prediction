# 3. Project Design

## System Architecture
┌───────────────────────────┐
        │     User's Browser         │
        │  (HTML form, templates/)   │
        └─────────────┬─────────────┘
                      │ POST /predict (JSON: gender, income,
                      │ income_type, education)
                      ▼
        ┌───────────────────────────┐
        │      Flask Backend         │
        │       (app.py)             │
        │  - Receives form data      │
        │  - Builds a DataFrame      │
        │    matching training       │
        │    feature order           │
        │  - Runs model.predict()    │
        │  - Builds a readable       │
        │    approval/rejection      │
        │    explanation             │
        └─────────────┬─────────────┘
                      │ loads at startup
                      ▼
        ┌───────────────────────────┐
        │   models/card_model.joblib │
        │   (trained classifier)     │
        └───────────────────────────┘
        ## Data Flow
1. User submits Gender, Annual Income, Income Type, and Education Level via the web form
2. Flask (`app.py`) receives the JSON payload at `/predict`
3. Input is arranged into a pandas DataFrame with the exact column names/order used during training (`Gender`, `Annual_Income`, `Income_Type`, `Education_Level`)
4. The pre-trained model (`models/card_model.joblib`) predicts approval (1) or rejection (0)
5. The backend maps encoded values back to readable labels (e.g. `2` → "Master's Degree") and builds a formatted HTML explanation
6. The result (`approved: true/false` + `reason` HTML) is returned as JSON and rendered on the page

## Module Design
| Module | Responsibility |
|---|---|
| `notebook.ipynb` | Data exploration, preprocessing, model training & evaluation |
| `models/card_model.joblib` | Persisted trained model |
| `app.py` | Flask routes, feature assembly, prediction, explanation generation |
| `templates/` | Frontend HTML (input form, result display) |
| `static/` | CSS/JS assets |