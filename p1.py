import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_california_housing

# Load data
housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)

# Numerical features
num_feats = df.select_dtypes(include=[np.number]).columns
print(num_feats)

# Histograms
df.hist(bins=30, figsize=(12,7), color='blue')
plt.suptitle('Histograms of Numerical Features')
plt.tight_layout()
plt.show()

# Box plots
plt.figure(figsize=(15,10))
for i, col in enumerate(df.columns, 1):
    plt.subplot(3,3,i)
    sns.boxplot(y=df[col])
    plt.title(f'Box Plot of {col}')
plt.tight_layout()
plt.show()

# Outliers summary
print("Outliers Detection:\n")
out_summ = {}
for f in num_feats:
    q1 = df[f].quantile(0.25)
    q3 = df[f].quantile(0.75)
    iqr = q3 - q1
    lb, ub = q1 - 1.5*iqr, q3 + 1.5*iqr
    out = df[(df[f] < lb) | (df[f] > ub)]
    out_summ[f] = len(out)
    print(f"\t{f}: {len(out)} outliers\t")