import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Generate data and assign labels
data = np.random.rand(100)
labels = ["Class1" if x <= 0.5 else "Class2" for x in data[:50]]

# Define Euclidean distance and k-NN classifier
def knn(x_train, y_train, x_test, k):
    dists = sorted([(abs(x - x_test), y) for x, y in zip(x_train, y_train)], key=lambda x: x[0])
    return Counter([y for _, y in dists[:k]]).most_common(1)[0][0]

# Split data
x_train, y_train, x_test = data[:50], labels, data[50:]
k_vals = [1, 2, 3, 4, 5, 20, 30]
results = {}

print("--- k-Nearest Neighbors Classification ---")
print("Training dataset: First 50 points labeled (x <= 0.5 -> Class1, x > 0.5 -> Class2)")
print("Testing dataset: Remaining 50 points\n")

# Classification
for k in k_vals:
    print(f"Results for k = {k}:")
    preds = [knn(x_train, y_train, x, k) for x in x_test]
    results[k] = preds
    for i, label in enumerate(preds, start=51):
        print(f"Point x{i} (value: {x_test[i - 51]:.4f}) is classified as {label}")
    print()

print("Classification complete.\n")

# Plot results
rows = (len(k_vals) + 2) // 3
plt.figure(figsize=(15, 5 * rows))

for i, k in enumerate(k_vals):
    preds = results[k]
    c1 = [x_test[j] for j in range(len(preds)) if preds[j] == "Class1"]
    c2 = [x_test[j] for j in range(len(preds)) if preds[j] == "Class2"]

    plt.subplot(rows, 3, i + 1)
    plt.scatter(x_train, [0]*len(x_train), c=['blue' if y == 'Class1' else 'red' for y in y_train], label='Train', marker='o')
    plt.scatter(c1, [1]*len(c1), c='blue', label='Class1 (Test)', marker='x')
    plt.scatter(c2, [1]*len(c2), c='red', label='Class2 (Test)', marker='x')
    plt.title(f'k-NN Results for k = {k}')
    plt.xlabel('Data Points')
    plt.ylabel('Classification Level')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.savefig('knn_classification.png')
plt.show()
