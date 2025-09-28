# Import libraries
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# -------------------- Step 1: Define Symptoms Dataset --------------------
Symptoms = {
    'Chills': ['Y','Y','Y','N','N','N','N','Y'],
    'Running nose': ['N','Y','N','Y','N','Y','Y','Y'],
    'Headache': ['mild','no','strong','mild','no','strong','strong','mild'],
    'Fever': ['Y','N','Y','Y','N','Y','N','Y'],
    'hasFlu': ['N','Y','Y','Y','N','Y','N','Y']
}

df = pd.DataFrame(Symptoms)

# -------------------- Step 2: Encode categorical values --------------------
encoders = {}
df_encoded = pd.DataFrame()

for col in df.columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df[col])
    encoders[col] = le

# -------------------- Step 3: Features and Target --------------------
X = df_encoded.drop('hasFlu', axis=1)
y = df_encoded['hasFlu']

# -------------------- Step 4: Train Naive Bayes on Entire Dataset --------------------
gnb = GaussianNB()
gnb.fit(X, y)

# -------------------- Step 5: Accuracy on same dataset (overfitted) --------------------
print("Naive Bayes Score:", gnb.score(X, y))

# -------------------- Step 6: Predict new patient --------------------
xnew = pd.DataFrame([['Y','N','mild','Y']], columns=X.columns)

# Encode new patient data
for col in xnew.columns:
    xnew[col] = encoders[col].transform(xnew[col])

ynew = gnb.predict(xnew)

# Decode prediction
print("Predicted output:", encoders['hasFlu'].inverse_transform(ynew)[0])
