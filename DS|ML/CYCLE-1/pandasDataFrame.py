import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1) Create DataFrame
# -------------------------------
student = {
    'Id': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Sam', 'Tom', 'Raj', 'Babs', 'Kiran', 'Jobin', 'Test'],
    'Department': ['MCA', 'EEE', 'EEE', 'Math', 'MCA', 'CS', 'CS'],
    'Score': [47, 53, 61, 78, 80, 50, None]   # Notice: last student has missing Score
}
db = pd.DataFrame(student)

print("=== Original Data ===")
print(db, "\n")



# -------------------------------
# 2) Add Grade Column Based on Score
# -------------------------------
def grade(score):
    if score >= 85: 
        return "A"
    elif score >= 75: 
        return "B"
    elif score >= 50: 
        return "C"
    else: 
        return "F"

db['Grade'] = db['Score'].apply(grade)
print("=== After Adding Grade Column ===")
print(db, "\n")


# -------------------------------
# 3) Summary Statistics (describe)
# -------------------------------
print("=== db.describe() (numeric columns only) ===")
print(db.describe(), "\n")


# -------------------------------
# 4) Display First 5 Records
# -------------------------------
print("=== db.head() (first 5 rows) ===")
print(db.head(), "\n")


# -------------------------------
# 5) Count of Students per Department (Method 1: value_counts)
# -------------------------------
cnt = db['Department'].value_counts()
print("=== Count per Department (value_counts) ===")
print(cnt, "\n")


# -------------------------------
# 6) Count of Students per Department (Method 2: groupby().size())
# -------------------------------
cnt = db.groupby('Department').size()
print("=== Count per Department (groupby.size) ===")
print(cnt, "\n")


# -------------------------------
# 7) Students with Score > 75
# -------------------------------
score = db[db['Score'] > 75]
print("=== Students with Score > 75 ===")
print(score, "\n")


# -------------------------------
# 8) Department-wise Average Score
# -------------------------------
avg = db.groupby("Department")["Score"].mean()
print("=== Department-wise Average Score ===")
print(avg, "\n")


# -------------------------------
# 9) Fill Missing Values with Average Score
# -------------------------------
db['Score'].fillna(db['Score'].mean(), inplace=True)
print("=== After Filling Missing Values with Average Score ===")
print(db, "\n")



# -------------------------------
# 10) Export Students with Score >= 80 to CSV
# -------------------------------
top = db[db['Score'] >= 80]
top.to_csv("student.csv", index=False)
print("CSV file 'student.csv' created successfully!\n")




# -------------------------------
# 11) Final DataFrame
# -------------------------------
print("=== FULL DATAFRAME ===")
print(db, "\n")




# -------------------------------
# 12) Plot Bar Chart: No. of Students per Department
# -------------------------------
dept_count = db['Department'].value_counts()
dept_count.plot(kind="bar", color="blue", edgecolor="black")

plt.title("Students per Department")
plt.xlabel("Department")
plt.ylabel("No. of Students")
plt.show()