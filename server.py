from flask import Flask, request, jsonify
import joblib
import numpy as np

model = joblib.load('models/lstm_model.pkl')

app = Flask(__name__)

def predict(data):
    # assuming 'data' is already preprocessed and ready for prediction
    prediction = model.predict(data)
    return prediction

=@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = predict(np.array(list(data.values())))
    return jsonify(prediction.tolist())

if __name__ == "__main__":
    app.run(port=5000, debug=True)
