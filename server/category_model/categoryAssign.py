import pandas as pd
import joblib  # For saving the model

# Load the trained model
model = joblib.load('text_classifier_model.joblib')

# Load your dataset
data = pd.read_csv(r'app/FinalData.csv')

# Ensure the dataset has a 'description' column
if 'description' not in data.columns:
    raise ValueError("The input data must contain a 'description' column.")

# Extract the descriptions
descriptions = data['description'].tolist()

# Predict categories for each description
predicted_categories = model.predict(descriptions)

# Create a new DataFrame with the predictions
result_df = pd.DataFrame({
    'description': descriptions,
    'category': predicted_categories
})

# Specify the path for the new CSV file
output_file_path = 'predicted_categories.csv'  # Change this to your desired output file path

# Save the new DataFrame to a new CSV file
result_df.to_csv(output_file_path, index=False)

print(f"Predictions saved to: {output_file_path}")

