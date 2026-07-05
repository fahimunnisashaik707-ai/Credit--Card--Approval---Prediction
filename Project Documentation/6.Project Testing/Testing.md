# 6. Project Testing

## Testing Approach
Manual and functional testing of the Flask application's `/predict` endpoint, covering both approval and rejection outcomes across different applicant profiles.

## Suggested Functional Test Cases

| # | Test Case | Sample Input | Expected Behavior |
|---|---|---|---|
| 1 | High income, stable sector, high education → likely approval | Gender=Male, Income=90000, Income Type=State/Government Sector, Education=Master's Degree | Returns `approved: true` with a positive explanation |
| 2 | Low income, less stable profile → likely rejection | Gender=Female, Income=15000, Income Type=Working Sector, Education=High School | Returns `approved: false` with a rejection explanation |
| 3 | Missing/invalid field | Income left blank or non-numeric | Should return a clear error |
| 4 | Model file missing | Rename/remove `card_model.joblib` temporarily | App should fail gracefully |
| 5 | Boundary income values | Income = 0, Income = very large number | Confirm the model handles edge values sensibly |

## Recommended Additions
- Add automated tests using Flask's test client
- Add model evaluation metrics (accuracy, precision, recall) from `notebook.ipynb`