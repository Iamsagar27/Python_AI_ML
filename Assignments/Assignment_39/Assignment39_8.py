# 8. Write a single structured Python program that performs:
# 1. Dataset loading
# 2. Data analysis
# 3. Visualization
# 4. Train-test split
# 5. Model training
# 6. Prediction
# 7. Accuracy calculation
# 8. Confusion matrix generation
# 9. Final conclusion
# Your code should include proper comments explaining each step.

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

Border = "-"*50

#############################################################################
# Step 1 : Load the dataset
#############################################################################
print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully")
print("Initial entries from dataset :")
print(df.head())


#############################################################################
# Step 2 : Data Analysis (EDA - Exploratory Data Analysis)
#############################################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset : ", df.shape)
print("Column Names :", list(df.columns))

print("Missing values (per column)")
print(df.isnull().sum())

print("Class Distribution")
print(df['FinalResult'].value_counts())

print("Statistical Report of Dataset")
print(df.describe())

#############################################################################
# Step 3 : Decide Independent and Dependent Variables
#############################################################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

student_data = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[student_data]
Y = df["FinalResult"]

print("X shape : ", X.shape)
print("Y shape : ", Y.shape)

#############################################################################
# Step 4 : Visualisation of dataset
#############################################################################

print(Border)
print("Step 4 : Visualisation of dataset")
print(Border)

# Scatter Plot
pass_student = df[df["FinalResult"] == 1]
fail_student = df[df["FinalResult"] == 0]

plt.figure()

plt.scatter(pass_student["StudyHours"], pass_student["PreviousScore"], label = "Pass")
plt.scatter(fail_student["StudyHours"], fail_student["PreviousScore"], label = "Fail")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.title("Study Hours vs Previous Score")
plt.legend()
plt.show()

#############################################################################
# Step 5 : Split the dataset for training and testing
#############################################################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)

print("Data Spliting activity done :")
print("X - Independent :", X.shape)                     
print("Y - Dependent :", Y.shape)                       

print("X_train :", X_train.shape)                       
print("X_test :", X_test.shape)                         

print("Y_train :", Y_train.shape)                       
print("Y_test :", Y_test.shape)                         

#############################################################################
# Step 6 : Build the model
#############################################################################

print(Border)
print("Step 6 : Build the model")
print(Border)

print("We are going to use DecisionTreeClassifier")

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

print("Model successfully created : ", model)


#############################################################################
# Step 7 : Train the model
#############################################################################

print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(X_train, Y_train)

print("Model training completed")

#############################################################################
# Step 8 : Evaluate the model
#############################################################################

print(Border)
print("Step 8 : Evaluate the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model evaluation (test) completed")

print(Y_pred.shape)

print("Expected answer :")
print(Y_test)

print("Predicted answer :")
print(Y_pred)

#############################################################################
# Step 9 : Evaluate the model performance
#############################################################################

print(Border)
print("Step 9 : Evaluate the model performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accurancy of model :", accuracy*100)

cm = confusion_matrix(Y_test, Y_pred)

print("Confusion Matrix : ")
print(cm)

print("Classification Report :")
print(classification_report(Y_test, Y_pred))


#############################################################################
# Step 10 : Plot Confusion matrix
#############################################################################

print(Border)
print("Step 10 : Plot Confusion matrix")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)

data.plot()
plt.title("Confusion Matrix of Iris Dataset")
plt.show()