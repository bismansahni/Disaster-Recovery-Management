# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# import joblib

# # Load the preprocessed and split data
# file_path = '../dataset/storms-preprocessed.csv'
# storms_data = pd.read_csv(file_path)

# # Define the features (X) and target (y)
# X_train = storms_data[['lat', 'long', 'wind', 'pressure']].iloc[:int(len(storms_data)*0.8)]
# X_test = storms_data[['lat', 'long', 'wind', 'pressure']].iloc[int(len(storms_data)*0.8):]
# y_train = storms_data['status_next_24h'].iloc[:int(len(storms_data)*0.8)]
# y_test = storms_data['status_next_24h'].iloc[int(len(storms_data)*0.8):]

# # Initialize the Logistic Regression model
# model = LogisticRegression(random_state=42)

# # Train the model on the training data
# model.fit(X_train, y_train)

# # Predict on the test data
# y_pred = model.predict(X_test)

# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# report = classification_report(y_test, y_pred)
# conf_matrix = confusion_matrix(y_test, y_pred)

# # Print the results
# print("Model Accuracy:", accuracy)
# print("\nClassification Report:\n", report)
# print("\nConfusion Matrix:\n", conf_matrix)

# # Save the trained model to a file
# joblib.dump(model, 'hurricane_prediction_model.pkl')




import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import joblib

# Load the preprocessed and split data
file_path = '../dataset/storms-preprocessed.csv'
storms_data = pd.read_csv(file_path)

# Define the features (X) and target (y)
X_train = storms_data[['lat', 'long', 'wind', 'pressure']].iloc[:int(len(storms_data)*0.8)]
X_test = storms_data[['lat', 'long', 'wind', 'pressure']].iloc[int(len(storms_data)*0.8):]
y_train = storms_data['status_next_24h'].iloc[:int(len(storms_data)*0.8)]
y_test = storms_data['status_next_24h'].iloc[int(len(storms_data)*0.8):]

# Initialize the Gradient Boosting model with early stopping
model = GradientBoostingClassifier(n_estimators=1000, learning_rate=0.1, random_state=42,
                                   validation_fraction=0.1, n_iter_no_change=10, tol=0.0001)

# Train the model on the training data
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Print the results
print("Model Accuracy:", accuracy)
print("\nClassification Report:\n", report)
print("\nConfusion Matrix:\n", conf_matrix)

# Save the trained model to a file
joblib.dump(model, 'hurricane_prediction_gb_model.pkl')
