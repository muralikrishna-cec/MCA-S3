"""
Q1. Load Chipotle dataset from GitHub.
"""

import pandas as pd

url = "https://raw.githubusercontent.com/muralikrishna-cec/MCA-S3/master/chipotle.tsv"
df = pd.read_csv(url, sep="\t")
print("Chipotle DataFrame:\n", df.head(), "\n")


"""
Q2. Load the same dataset using read_table (short URL).
"""
orders = pd.read_table("http://bit.ly/chiporders")
print("Orders DataFrame:\n", orders.head(), "\n")


"""
Q3. Sort items by highest price.
"""
df_sorted = df.sort_values(by="item_price", ascending=False).head()

df.sort_values(by="item_price", key=lambda x: x.str.strip('$').astype(float), ascending=False).head()
print("Top expensive items:\n", df_sorted, "\n")


"""
Q4. Select rows where item_name contains 'chicken' (case insensitive).
"""
chicken_items = df[df['item_name'].str.contains('chicken', case=False, na=False)]
print("Items containing 'chicken':\n", chicken_items, "\n")


"""
Q5. Clean 'choice_description' by removing brackets [].
"""
clean_choice = df['choice_description'].str.replace(r"[\[\]]", "", regex=True)
print("Cleaned choice_description:\n", clean_choice.head(10), "\n")


"""
Q6. Convert 'item_price' column from string to float.
"""
print("Before conversion:\n", df.dtypes, "\n")
df['item_price'] = df['item_price'].str.replace('$', '', regex=False).astype(float)
print("After conversion:\n", df.dtypes, "\n")


"""
. Convert 'item_price' back to string.
"""
df['item_price'] = df['item_price'].astype(str)
print("After converting item_price back to string:\n", df.dtypes, "\n")
