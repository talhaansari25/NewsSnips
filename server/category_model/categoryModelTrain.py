import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
import joblib  # For saving the model

# Load the dataset
data = pd.read_csv(r'train_category.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Split the data into training and testing sets
X = df['description']
y = df['category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a machine learning pipeline
pipeline = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())

# Hyperparameter tuning using Grid Search
param_grid = {
    'multinomialnb__alpha': [0.1, 0.5, 1.0, 1.5, 2.0]  # Example alpha values for smoothing
}

# Initialize GridSearchCV
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1, verbose=1)

# Train the model using Grid Search
grid_search.fit(X_train, y_train)

# Best parameters
print("Best parameters found: ", grid_search.best_params_)

# Evaluate the model
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(grid_search.best_estimator_, 'text_classifier_model.joblib')
print("Model saved as 'text_classifier_model.joblib'.")
 