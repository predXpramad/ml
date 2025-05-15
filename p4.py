import csv

# Load data
with open('enjoysport.csv', 'r') as f:
    data = list(csv.reader(f))

print("=== Training Data ===")
[print(r) for r in data]
print("\nTotal training instances:", len(data))

# Initialize hypothesis
n, hypo = len(data[0]) - 1, ['0'] * (len(data[0]) - 1)
print("\nInitial Hypothesis:", hypo)

# Find-S Algorithm
print("\n=== Hypothesis Updates ===")
for i, row in enumerate(data):
    if row[-1].lower() == 'yes':
        for j in range(n):
            hypo[j] = row[j] if hypo[j] in ['0', row[j]] else '?'
        print(f"After instance {i+1}: {hypo}")

print("\n=== Final Hypothesis ===")
print("Maximally Specific Hypothesis:", hypo)
