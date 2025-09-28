# Import libraries
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# -------------------- Step 1: Define Symptoms Dataset --------------------
Symptoms = {
    'Chills': ['Y','Y','Y','N','N','N','N','Y'],
    'Running nose': ['N','Y','N','Y','N','Y','Y','Y'],
    'Headache': ['mild','no','strong','mild','no','strong','strong','mild'],
    'Fever': ['Y','N','Y','Y','N','Y','N','Y'],
    'hasFlu': ['N','Y','Y','Y','N','Y','N','Y']   # Target column
}

df = pd.DataFrame(Symptoms)

# -------------------- Step 2: Encode categorical values --------------------
encoders = {}          # Store label encoders for decoding later
df_encoded = pd.DataFrame()

for col in df.columns:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df[col])  # Convert text → numbers
    encoders[col] = le                           # Save encoder for reuse

# -------------------- Step 3: Separate features (X) and target (y) --------------------
X = df_encoded.drop('hasFlu', axis=1)   # Symptoms only
y = df_encoded['hasFlu']                # Flu or not (Y/N)

# -------------------- Step 4: Split dataset into Train & Test --------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=1
)

# -------------------- Step 5: Train Naive Bayes Classifier --------------------
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# -------------------- Step 6: Evaluate accuracy on test set --------------------
print("Naive Bayes Score:", gnb.score(X_test, y_test))

# -------------------- Step 7: Predict flu for a new patient --------------------
# New patient data: chills=Y, running nose=N, headache=mild, fever=Y
xnew = pd.DataFrame([['Y','N','mild','Y']], columns=X.columns)

# Encode the new input using same encoders
for col in xnew.columns:
    xnew[col] = encoders[col].transform(xnew[col])

# Predict using trained model
ynew = gnb.predict(xnew)

# Decode prediction back to original label (Y/N)
print("Predicted output:", encoders['hasFlu'].inverse_transform(ynew)[0])
