from flask import Flask, request, render_template
import pandas as pd
import pickle


app = Flask(__name__)

# Loading model
with open("rf_model.pkl", "rb") as file:
    rf_model = pickle.load(file)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Prediction process : Predict with data taken from user
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # form data
        inputs = {
            'area': float(request.form['area']),
            'bedrooms': int(request.form['bedrooms']),
            'bathrooms': int(request.form['bathrooms']),
            'stories': int(request.form['stories']),  
            'mainroad': int(request.form['mainroad']),
            'guestroom': int(request.form['guestroom']),
            'basement': int(request.form['basement']),
            'hotwaterheating': int(request.form['hotwaterheating']),
            'airconditioning': int(request.form['airconditioning']),
            'parking': int(request.form['parking']),
            'prefarea': int(request.form['prefarea']),
            'furnishingstatus': int(request.form['furnishingstatus'])
        }
        
        features = pd.DataFrame([inputs])
        
        prediction = rf_model.predict(features)[0]

        return render_template('result.html', prediction=round(prediction, 2))
    except Exception as e:
        return f"Hata oluştu: {e}"

if __name__ == "__main__":
    app.run(debug=True)
