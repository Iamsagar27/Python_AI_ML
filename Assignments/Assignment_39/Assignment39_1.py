# 1. Import Decision Tree Classifier from sklearn.
# Create a model object and train it using fit().

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = 'student_performance_ml.csv' 
dataFrame = pd.read_csv(file_path)


# Decide Independent & Dependent variables
student_data = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = dataFrame[student_data]
Y = dataFrame["FinalResult"]


# Split the dataset for training and testing
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.3,
    random_state = 42
)


# Build the model
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)


# Train the model
model.fit(X_train, Y_train)