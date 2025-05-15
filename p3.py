import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Load data
iris = load_iris()
X, y, names = iris.data, iris.target, iris.target_names
df = pd.DataFrame(X, columns=iris.feature_names)
print('Iris data features:\n', df.head())

# PCA to 2D
pca = PCA(n_components=2)
pc = pca.fit_transform(X)
df_pca = pd.DataFrame(pc, columns=['PC1', 'PC2'])
df_pca['Target'] = y

# Plot
plt.figure(figsize=(6, 4))
for i, lbl in enumerate(np.unique(y)):
    plt.scatter(df_pca[df_pca['Target'] == lbl]['PC1'],
                df_pca[df_pca['Target'] == lbl]['PC2'],
                label=names[lbl])
plt.title('PCA of Iris Dataset')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.grid()
plt.savefig('pcaofirisdataset.png')
plt.show()
