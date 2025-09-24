# Task 1: Load and Explore the Dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset from sklearn
iris = load_iris(as_frame=True)
df = iris.frame   # Convert to DataFrame

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore data structure
print("\nDataset Info:")
print(df.info())

print("\nMissing Values Check:")
print(df.isnull().sum())

# Clean dataset (Iris has no missing values, but if they exist we can handle)
df = df.dropna()

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Grouping by species and calculating mean of numerical columns
grouped = df.groupby("target").mean()
print("\nMean of numerical features by Species:")
print(grouped)

# Interesting findings
print("\nObservations:")
print("1. Setosa generally has smaller sepal and petal sizes compared to Virginica and Versicolor.")
print("2. Virginica tends to have the largest petal length and width.")

# Task 3: Data Visualization

# Line Chart (simulating a trend: index vs sepal length)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# Bar Chart: Average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="target", y="petal length (cm)", data=df, estimator="mean", palette="viridis")
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# Histogram: Distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, color="purple", edgecolor="black")
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="Set2")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
