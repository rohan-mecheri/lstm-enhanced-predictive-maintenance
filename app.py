import numpy as np
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# load the trained LSTM model
model = joblib.load('models/LSTM model.pkl')

@app.route('/predict_api', methods=['POST'])
def predict_api():

    try:
        data = request.get_json(force=True)
        input_data = np.array([list(data.values())])
        prediction = model.predict(input_data)
        return jsonify({'predicted_rul': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
