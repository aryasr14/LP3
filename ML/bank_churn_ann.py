# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# 1. Read dataset
data = pd.read_csv("Churn_Modelling.csv")

# 2. Preprocess dataset
data = data.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

# Convert categorical columns into numerical values
data = pd.get_dummies(data, columns=["Geography", "Gender"], drop_first=True, dtype=int)

# Separate features and target
X = data.drop("Exited", axis=1)
y = data["Exited"]

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. Normalize data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 4. Build basic neural network
model = Sequential([
    Dense(16, activation="relu", input_shape=(X_train.shape[1],)),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train basic model
model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=0)

# Predict using basic model
y_pred = (model.predict(X_test) > 0.5).astype(int)

print("Basic Neural Network")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))


# 5. Improved neural network using Dropout and Early Stopping
model = Sequential([
    Dense(16, activation="relu", input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(8, activation="relu"),
    Dropout(0.2),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

early_stop = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)

model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=0
)

# 6. Evaluate improved model
y_pred = (model.predict(X_test) > 0.5).astype(int)

print("\nImproved Neural Network")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
