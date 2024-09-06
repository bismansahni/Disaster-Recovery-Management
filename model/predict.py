import joblib
import numpy as np
import json
import os

# Load the trained model
model = joblib.load('hurricane_prediction_gb_model.pkl')

# Function to normalize hypothetical data (if needed)
def normalize(value, mean, std):
    return (value - mean) / std

# Conversion functions
def convert_pressure_to_hpa(pressure_hg):
    # Convert pressure from in Hg to hPa
    return pressure_hg * 33.86

def normalize_wind_mph(wind_mph):
    # Normalize wind speed from mph (mean=50, std=15)
    return normalize(wind_mph, 50, 15)

def normalize_pressure_hpa(pressure_hpa):
    # Normalize pressure (mean=1010, std=10)
    return normalize(pressure_hpa, 1010, 10)

# Function to read from weather_data.json and make a prediction
def predict_hurricane():
    # Set the correct path to the weather_data.json file
    json_path = os.path.join('..', 'ingestion', 'weather_data.json')
    
    # Read the weather data from the JSON file
    with open(json_path, 'r') as file:
        weather_data = json.load(file)

    # Extract relevant data
    location_name = weather_data['location']['name']
    lat = weather_data['location']['lat']
    long = weather_data['location']['lon']
    wind_mph = weather_data['current']['wind_mph']
    pressure_hg = weather_data['current']['pressure_in']

    # Convert and normalize the values
    wind = normalize_wind_mph(wind_mph)
    pressure_hpa = convert_pressure_to_hpa(pressure_hg)
    pressure = normalize_pressure_hpa(pressure_hpa)
    
    print(f"\nLocation: {location_name}")
    print(f"Converted and Normalized Values:\nLatitude: {lat}, Longitude: {long}, Wind Speed (normalized): {wind}, Pressure (normalized): {pressure}")

    # Create a feature array for prediction
    features = np.array([[lat, long, wind, pressure]])

    # Make the prediction
    prediction = model.predict(features)

    # Output the result with location name
    if prediction == 1:
        print(f"\nPrediction: A hurricane is likely to occur within the next 24 hours in {location_name}.")
    else:
        print(f"\nPrediction: No hurricane is likely to occur in {location_name} within the next 24 hours.")

if __name__ == "__main__":
    predict_hurricane()
