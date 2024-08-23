import numpy as np
from flask import Flask, request, jsonify
import joblib

# Initialize the Flask app
app = Flask(__name__)

# Load the trained LSTM model
model = joblib.load('models/LSTM model.pkl')

@app.route('/predict_api', methods=['POST'])
def predict_api():

    try:
        # Get the input data from the request body (JSON)
        data = request.get_json(force=True)
        
        # Prepare input data for the model
        input_data = np.array([list(data.values())])

        # Make prediction using the model
        prediction = model.predict(input_data)

        # Return the prediction as a JSON response
        return jsonify({'predicted_rul': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)