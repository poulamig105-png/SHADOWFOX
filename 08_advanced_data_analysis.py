# Advanced Task: Jupyter-style Data Analysis Project
# Dataset: Iris flower dataset from seaborn.
#
# Research questions:
# 1. How do sepal and petal measurements differ across species?
# 2. Which numerical features have the strongest relationships?
# 3. Can visualizations clearly separate the three species?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = sns.load_dataset("iris")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:", df.shape)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

# Basic data cleaning
df = df.drop_duplicates().dropna()

# Research Question 1:
# Compare feature distributions by species.
features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

for feature in features:
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x="species", y=feature)
    plt.title(f"{feature.replace('_', ' ').title()} by Species")
    plt.tight_layout()
    plt.show()

# Research Question 2:
# Correlation among numerical features.
plt.figure(figsize=(8, 6))
sns.heatmap(df[features].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Research Question 3:
# Relationship between petal length and petal width.
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="petal_length",
    y="petal_width",
    hue="species"
)
plt.title("Petal Length vs Petal Width")
plt.tight_layout()
plt.show()

# Pair plot for overall relationships.
sns.pairplot(df, hue="species")
plt.show()

print("\nKey findings:")
print("1. Petal measurements show clear differences among species.")
print("2. Petal length and petal width have a strong positive relationship.")
print("3. The visualizations help distinguish the species using their measurements.")

print("\nConclusion:")
print("The Iris dataset demonstrates how exploratory data analysis and "
      "visualization can reveal patterns, relationships, and differences "
      "between groups in a dataset.")
