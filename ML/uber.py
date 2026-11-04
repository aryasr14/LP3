# 1. Import libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# 2. Load dataset
data = pd.read_csv("uber.csv")


# 3. Preprocess dataset
data = data.drop(["Unnamed: 0", "key"], axis=1)
data = data.dropna()

data["pickup_datetime"] = pd.to_datetime(data["pickup_datetime"], utc=True)

data["hour"] = data["pickup_datetime"].dt.hour
data["day"] = data["pickup_datetime"].dt.day
data["month"] = data["pickup_datetime"].dt.month

data = data.drop("pickup_datetime", axis=1)

data = data[
    (data["fare_amount"] > 0) &
    (data["fare_amount"] < 100) &
    (data["pickup_longitude"].between(-75, -72)) &
    (data["dropoff_longitude"].between(-75, -72)) &
    (data["pickup_latitude"].between(40, 42)) &
    (data["dropoff_latitude"].between(40, 42)) &
    (data["passenger_count"].between(1, 6))
]


# 4. Split data into input and output
X = data.drop("fare_amount", axis=1)
y = data["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 5. Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_lr = lr.predict(X_test)

print("Linear Regression")
print("R2 Score:", r2_score(y_test, y_pred_lr))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_lr)))
print("MAE:", mean_absolute_error(y_test, y_pred_lr))


# 6. Random Forest Regression
rf = RandomForestRegressor(n_estimators=50, random_state=42)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)

print("\nRandom Forest Regression")
print("R2 Score:", r2_score(y_test, y_pred_rf))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_rf)))
print("MAE:", mean_absolute_error(y_test, y_pred_rf))


# 7. Compare models
print("\nModel Comparison")
print("Linear Regression R2:", r2_score(y_test, y_pred_lr))
print("Random Forest R2:", r2_score(y_test, y_pred_rf))
