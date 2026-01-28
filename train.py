import joblib
from sklearn.linear_model import LinearRegression

# train your model
model = LinearRegression()
model.fit(X_train, y_train)

# SAVE correctly
joblib.dump(model, "reg_model.pkl")
