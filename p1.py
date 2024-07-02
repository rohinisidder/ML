import csv
hypo = []
data = []
with open('sports.csv') as csv_file:
    fd = csv.reader(csv_file)
    print("the given training examples are:")
    for line in fd:
        print(line)
        if line[-1]=="Yes":
            data.append(line)
print("the positive examples are:")
for x in data:
    print(x)
row = len(data)
col = len(data[0])
for j in range(col):
    hypo.append(data[0][j])
for i in range(row):
    for j in range(col):
        if hypo[j]!=data[i][j]:
            hypo[j] = "?"
print("the maximally specific hypothesis is:")
print(hypo)