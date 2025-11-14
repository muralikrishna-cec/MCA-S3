import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# ---- Create Dataset ----
data = {
    'Colour':  ['red','red','red','yellow','yellow','yellow','yellow','yellow','red','red'],
    'Type':    ['sports','sports','sports','sports','sports','SUV','SUV','SUV','SUV','sports'],
    'Origin':  ['domestic','domestic','domestic','domestic','imported','imported','imported','domestic','imported','imported'],
    'Stolen':  ['yes','no','yes','no','yes','no','yes','no','no','yes']
}

df = pd.DataFrame(data)

# ---- Encode all columns ----
encoders = {}
df_encoded = pd.DataFrame()

for col in df.columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df[col])
    encoders[col] = le

# ---- Split into features & target ----
X = df_encoded[['Colour', 'Type', 'Origin']]
y = df_encoded['Stolen']

# ---- Train-Test Split ----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.80, random_state=19)

# ---- Train Naive Bayes ----
model = GaussianNB()
model.fit(X_train, y_train)

# ---- Accuracy ----
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# ---- Predict for red, SUV, domestic ----
new_data = pd.DataFrame([['red','SUV','domestic']], columns=['Colour','Type','Origin'])

# Encode new sample
for col in new_data.columns:
    new_data[col] = encoders[col].transform(new_data[col])

# Predict final result
pred = model.predict(new_data)
result = encoders['Stolen'].inverse_transform(pred)[0]

print("Prediction:", result)
