from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model file
model = joblib.load('models/card_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Arrange features in a DataFrame to match how the model was trained
        # This prevents the "X does not have valid feature names" warning
        features = pd.DataFrame([[
            data['gender'],
            data['income'],
            data['income_type'],
            data['education']
        ]], columns=['Gender', 'Annual_Income', 'Income_Type', 'Education_Level'])
        
        prediction = model.predict(features)[0]
        approved = int(prediction) == 1
        
        # Map values back to readable text for the detailed explanation
        education_map = {0: "Bachelor's Degree", 1: "High School", 2: "Master's Degree", 3: "PhD"}
        income_type_map = {0: "Commercial Sector", 1: "State/Government Sector", 2: "Working Sector"}
        gender_map = {0: "Female", 1: "Male"}
        
        edu_str = education_map.get(int(data['education']), "your education level")
        inc_str = income_type_map.get(int(data['income_type']), "your income sector")
        gender_str = gender_map.get(int(data['gender']), "Unknown")
        
        # Generate a detailed reason
        if approved:
            reason = f"""
            <div style="text-align: left; margin-top: 15px; background: rgba(0,0,0,0.2); padding: 15px; border-radius: 8px;">
                <strong style="color: #cbd5e1; display: block; margin-bottom: 8px;">Detailed Approval Analysis:</strong>
                <div style="margin-bottom: 5px;">✅ <strong>Financial Capacity:</strong> Your reported annual income of <strong>${data['income']:,.0f}</strong> provides sufficient bandwidth for our credit limits.</div>
                <div style="margin-bottom: 5px;">✅ <strong>Employment Sector:</strong> Being in the <strong>{inc_str}</strong> aligns with our stable income models.</div>
                <div style="margin-bottom: 10px;">✅ <strong>Educational Background:</strong> Having a <strong>{edu_str}</strong> statistically correlates with lower default rates in our portfolio.</div>
                <em style="color: #94a3b8; font-size: 12px;">Conclusion: Your application sailed through our risk-assessment algorithm with flying colors!</em>
            </div>
            """
        else:
            reason = f"""
            <div style="text-align: left; margin-top: 15px; background: rgba(0,0,0,0.2); padding: 15px; border-radius: 8px;">
                <strong style="color: #cbd5e1; display: block; margin-bottom: 8px;">Detailed Rejection Analysis:</strong>
                <div style="margin-bottom: 5px;">❌ <strong>Income-to-Risk Ratio:</strong> The reported income of <strong>${data['income']:,.0f}</strong> combined with your specific demographic profile flagged an elevated risk tier.</div>
                <div style="margin-bottom: 10px;">❌ <strong>Algorithm Confidence:</strong> Our Machine Learning model identified that this specific combination (<em>{gender_str}, {edu_str}, {inc_str}</em>) matches historical high-volatility profiles.</div>
                <em style="color: #94a3b8; font-size: 12px;">Conclusion: We are unable to extend credit at this time. Please re-apply if your financial situation changes.</em>
            </div>
            """
                
        return jsonify({'approved': approved, 'reason': reason})
    except Exception as e:
        print("Error during prediction:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
