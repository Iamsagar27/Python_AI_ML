# 6. Train three Decision Tree models with:
# max_depth = 1
# max_depth = 3
# max_depth = None
# Compare their testing accuracies and write your observations.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

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
    random_state=42
)

model1 = DecisionTreeClassifier(
    criterion="gini",
    max_depth=1,
    random_state=42
)

model3 = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

# Train the model
model.fit(X_train, Y_train)
model1.fit(X_train, Y_train)
model3.fit(X_train, Y_train)


# Test the model
train_Pred = model.predict(X_train)
test_Pred = model.predict(X_test)

train_Pred_1 = model1.predict(X_train)
test_Pred_1 = model1.predict(X_test)

train_Pred_3 = model3.predict(X_train)
test_Pred_3 = model3.predict(X_test)

print("Actual Value : ", Y_test.values)
print("Predicted Value with max_depth none : ", test_Pred)
print("Predicted Value with max_depth 1 : ", test_Pred_1)
print("Predicted Value with max_depth 3: ", test_Pred_3)
print("--------------------------------------------------------------------------")


# Model Performance
training_accuracy = accuracy_score(Y_train, train_Pred)
testing_accuracy = accuracy_score(Y_test, test_Pred)

training_accuracy_1 = accuracy_score(Y_train, train_Pred_1)
testing_accuracy_1 = accuracy_score(Y_test, test_Pred_1)

training_accuracy_3 = accuracy_score(Y_train, train_Pred_3)
testing_accuracy_3 = accuracy_score(Y_test, test_Pred_3)


print("Accuracy of the model in training : ", training_accuracy*100)
print("Accuracy of the model in testing : ", testing_accuracy*100)
print("--------------------------------------------------------------------------")
print("Accuracy of the model in training  max_depth 1: ", training_accuracy_1*100)
print("Accuracy of the model in testing max_depth 1: ", testing_accuracy_1*100)
print("--------------------------------------------------------------------------")
print("Accuracy of the model in training max_depth 3: ", training_accuracy_3*100)
print("Accuracy of the model in testing max_depth 3: ", testing_accuracy_3*100)

