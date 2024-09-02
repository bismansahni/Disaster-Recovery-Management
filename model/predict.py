import joblib
import numpy as np

# Load the trained model
model = joblib.load('hurricane_prediction_gb_model.pkl')

# Function to normalize hypothetical data (if needed)
def normalize(value, mean, std):
    return (value - mean) / std

# Function to take user input and make a prediction
def predict_hurricane():
    print("Choose input method:")
    print("1. Enter custom data")
    print("2. Use hypothetical data")
    
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        # Custom input
        lat = float(input("Latitude: "))
        long = float(input("Longitude: "))
        wind = float(input("Wind Speed (normalized value): "))
        pressure = float(input("Pressure (normalized value): "))
    # elif choice == '2':
    #     # Hypothetical data
    #     print("\nUsing hypothetical data:")
    #     lat = 30.0  # Hypothetical latitude
    #     long = -80.0  # Hypothetical longitude
    #     wind = normalize(75, 50, 15)  # Hypothetical wind speed, assuming mean=50, std=15
    #     pressure = normalize(1000, 1010, 10)  # Hypothetical pressure, assuming mean=1010, std=10
    #     print(f"Latitude: {lat}, Longitude: {long}, Wind Speed (normalized): {wind}, Pressure (normalized): {pressure}")
    elif choice == '2':
        print("\nUsing hypothetical data:")
        lat = 30.0  # Hypothetical latitude
        long = -80.0  # Hypothetical longitude
        wind = normalize(30, 50, 15)  # Hypothetical wind speed, lower value (assume mean=50, std=15)
        pressure = normalize(1020, 1010, 10)  # Hypothetical pressure, higher value (assume mean=1010, std=10)
        print(f"Latitude: {lat}, Longitude: {long}, Wind Speed (normalized): {wind}, Pressure (normalized): {pressure}")
    
    else:
        print("Invalid choice. Exiting.")
        return

    # Create a feature array for prediction
    features = np.array([[lat, long, wind, pressure]])

    # Make the prediction
    prediction = model.predict(features)

    # Output the result
    if prediction == 1:
        print("\nPrediction: A hurricane is likely to occur within the next 24 hours.")
    else:
        print("\nPrediction: No hurricane is likely to occur within the next 24 hours.")

if __name__ == "__main__":
    predict_hurricane()
