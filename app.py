from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load('linear_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        session_length = float(request.form['session_length'])
        time_on_app = float(request.form['time_on_app'])
        time_on_website = float(request.form['time_on_website'])
        membership_length = float(request.form['membership_length'])

        # Prepare input
        input_data = np.array([[session_length, time_on_app, time_on_website, membership_length]])

        # Predict
        prediction = model.predict(input_data)[0]
        prediction = round(prediction, 2)

        return render_template('index.html', prediction_text=f'Predicted Yearly Amount Spent: ${prediction}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
