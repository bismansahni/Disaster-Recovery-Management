# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler

# # Load the dataset
# file_path = '../dataset/storms.csv'
# storms_data = pd.read_csv(file_path)

# # Drop unnecessary columns
# storms_data_cleaned = storms_data.drop(columns=['Unnamed: 0', 'tropicalstorm_force_diameter', 'hurricane_force_diameter'])

# # Drop rows with missing 'wind' and 'pressure' values
# storms_data_cleaned = storms_data_cleaned.dropna(subset=['wind', 'pressure'])

# # Fill missing 'category' values with the most frequent value (mode)
# # storms_data_cleaned['category'].fillna(storms_data_cleaned['category'].mode()[0], inplace=True)


# # Instead of using inplace=True with chained assignment, do this:
# storms_data_cleaned['category'] = storms_data_cleaned['category'].fillna(storms_data_cleaned['category'].mode()[0])

# # Encode 'status' as a binary variable: 1 for hurricane, 0 for others
# storms_data_cleaned['status'] = storms_data_cleaned['status'].apply(lambda x: 1 if 'hurricane' in x.lower() else 0)

# # Select features for normalization
# features_to_normalize = ['wind', 'pressure']

# # Initialize the scaler
# scaler = StandardScaler()

# # Normalize the selected features
# storms_data_cleaned[features_to_normalize] = scaler.fit_transform(storms_data_cleaned[features_to_normalize])

# # Split the dataset into features (X) and target (y)
# X = storms_data_cleaned.drop(columns=['status', 'name'])  # Dropping 'status' and 'name' as they are not features
# y = storms_data_cleaned['status']

# # Split into training and testing sets (80% training, 20% testing)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Display the shapes of the resulting datasets
# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)
# print("y_train shape:", y_train.shape)
# print("y_test shape:", y_test.shape)




import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = '../dataset/storms.csv'
storms_data = pd.read_csv(file_path)

# Drop unnecessary columns
storms_data_cleaned = storms_data.drop(columns=['Unnamed: 0', 'tropicalstorm_force_diameter', 'hurricane_force_diameter'])

# Drop rows with missing 'wind' and 'pressure' values
storms_data_cleaned = storms_data_cleaned.dropna(subset=['wind', 'pressure'])

# Instead of using inplace=True with chained assignment, do this:
storms_data_cleaned['category'] = storms_data_cleaned['category'].fillna(storms_data_cleaned['category'].mode()[0])

# Encode 'status' as a binary variable: 1 for hurricane, 0 for others
storms_data_cleaned['status'] = storms_data_cleaned['status'].apply(lambda x: 1 if 'hurricane' in x.lower() else 0)

# Select features for normalization
features_to_normalize = ['wind', 'pressure']

# Initialize the scaler
scaler = StandardScaler()

# Normalize the selected features
storms_data_cleaned[features_to_normalize] = scaler.fit_transform(storms_data_cleaned[features_to_normalize])

# Split the dataset into features (X) and target (y)
X = storms_data_cleaned.drop(columns=['status', 'name'])  # Dropping 'status' and 'name' as they are not features
y = storms_data_cleaned['status']

# Split into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting datasets
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# Save the cleaned and preprocessed dataset to a new CSV file
storms_data_cleaned.to_csv('../dataset/storms-preprocessed.csv', index=False)
