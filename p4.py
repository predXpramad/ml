import csv

# Load dataset
data = []
with open('enjoysport.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

print("Training data:")
for row in data:
    print(row)

print("\nTotal number of training instances:", len(data))

# Initialize hypothesis
num_attributes = len(data[0]) - 1
hypothesis = ['0'] * num_attributes

print("\nInitial hypothesis:", hypothesis)

# Apply Find-S algorithm
for i in range(len(data)):
    if data[i][-1].lower() == 'yes':
        for j in range(num_attributes):
            if hypothesis[j] == '0' or hypothesis[j] == data[i][j]:
                hypothesis[j] = data[i][j]
            else:
                hypothesis[j] = '?'
        print(f"\nHypothesis after instance {i+1}:", hypothesis)

# Final result
print("\nMaximally specific hypothesis:", hypothesis)