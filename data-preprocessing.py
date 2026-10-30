import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Cathy", "David", "Bala"],
    "Age": [20, 21, None, 22, 21],
    "Marks": [85, None, 90, 78, None]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df = df.drop_duplicates()
print("\nPreprocessed Data:")
print(df)