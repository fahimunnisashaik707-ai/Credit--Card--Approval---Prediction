# 5. Project Development — Source Code

This folder contains the existing project code:
app.py               Flask application (routes: / and /predict)
notebook.ipynb       Data exploration, preprocessing, and model training
models/
card_model.joblib  Trained classification model
static/              CSS/JS assets
templates/           HTML form + result display
## Run Locally

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
pip install flask joblib pandas scikit-learn
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## How Prediction Works
1. User submits Gender, Annual Income, Income Type, and Education Level
2. `app.py` loads `models/card_model.joblib` and predicts approval (1) or rejection (0)
3. The result is returned with a plain-language explanation of the decision