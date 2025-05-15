import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing as fch

# Load data
df = pd.DataFrame(fch().data, columns=fch().feature_names)

# Correlation matrix + heatmap
corr = df.corr()
print(corr)
sns.heatmap(corr, annot=True, cmap='crest', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Display column names
print(df.columns)

# Pair plot
sns.pairplot(df, kind='scatter', diag_kind='kde', plot_kws={'alpha': 0.5})
plt.show()
