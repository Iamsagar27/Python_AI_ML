# 4. Generate confusion matrix using sklearn.
# Display it using ConfusionMatrix Display.
# Explain clearly:
# True Positive
# True Negative
# False Positive
# False Negative


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
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
    max_depth=5,
    random_state=42
)


# Train the model
model.fit(X_train, Y_train)


# Test the model
Y_Pred = model.predict(X_test)

print("Actual Value : ", Y_test.values)
print("Predicted Value : ", Y_Pred)


# Model Performance
accuracy = accuracy_score(Y_test, Y_Pred)
print("Accuracy of the model : ", accuracy*100)


# Confusion Matrix
confusionmatrix = confusion_matrix(Y_test, Y_Pred)
print(confusionmatrix)

matrix_display = ConfusionMatrixDisplay(confusion_matrix=confusionmatrix, display_labels=model.classes_)
matrix_display.plot()

plt.show()