import requests
import numpy as np

url = 'http://127.0.0.1:5000/predict_api'

data = {
    'data': [0.5, 1.2, 0.8, 1.0, 1.5, 2.1, 3.5, 0.9, 2.3, 1.7, 0.6, 1.8, 2.6, 3.0, 1.2, 0.4, 0.7, 2.8, 3.2]
}

response = requests.post(url, json=data)

print("Predicted RUL:", response.json())
