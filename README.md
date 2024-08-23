# LSTM-enhanced Predictive Maintenance

## Introduction

This project creates a predictive maintenance framework using sensor data and Long Short-Term Memory (LSTM) neural networks to estimate the Remaining Useful Life (RUL) of industrial equipment, thereby preventing unexpected failures and optimizing maintenance schedules.

Predictive maintenance uses data analysis and machine learning to predict equipment failures before they occur. By leveraging sensor data and advanced deep learning models, we can provide actionable insights to enhance the reliability and efficiency of industrial operations.

[LSTM networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) are particularly useful in this case due to their ability to learn from sequences of data, making them ideal for time-series data. They can detect temporal patterns that may indicate an impending failure.

The dataset is sourced from the [Predictive Maintenance Template](https://gallery.azure.ai/Collection/Predictive-Maintenance-Template-3) by Azure AI Gallery. It includes multiple time-series data points from various sensors monitoring the health of industrial equipment.

## Project Structure

### Data Ingestion and Preprocessing

- **Loading the Data**: Reading sensor data for training and testing.
- **Cleaning**: Removing columns with no variance.
- **Feature Engineering**: Creating rolling statistics, exponential moving averages, and lag features to capture temporal patterns.
- **Normalization**: Applying MinMaxScaler to ensure all features are on a consistent scale.

### Exploratory Data Analysis (EDA)

Specific EDA techniques were performed to understand the data better and guide feature engineering:

- **Sensor Trends Visualization**: Plotted sensor readings over time to observe trends and anomalies.
- **Correlation Matrix**: Identified relationships between different sensors and settings.

### Model Development

The LSTM model captures the sequential nature of the sensor data. The architecture includes:

- **LSTM Layers**: To capture long-term dependencies in the data.
- **Dropout Layers**: To prevent overfitting.
- **Dense Layer**: For the final RUL prediction.

### Training and Evaluation

The model is trained on the training dataset and evaluated using Mean Squared Error (MSE) and Mean Absolute Error (MAE). Visualization techniques such as loss curves and scatter plots of actual vs. predicted RUL provide insights into model performance.

### Testing

The trained model can be tested through a POST API request using a Flask server. The Flask server hosts an endpoint where you can send data in the form of a JSON array, and the server will return the predicted RUL value. This setup allows for easy integration with other systems or applications that require real-time RUL predictions.

### Results

The model’s performance is visualized through:

- **Training and Validation Loss Curves**: To assess overfitting and convergence.
- **Plot of Actual vs. Predicted RUL**: To evaluate prediction accuracy.

## Conclusion

This project demonstrates the application of LSTM neural networks for predictive maintenance. Accurate RUL predictions can significantly enhance maintenance strategies, reduce downtime, and increase operational efficiency. The inclusion of a Flask server and API endpoint facilitates easy testing and integration, making the model readily deployable in real-world scenarios.
