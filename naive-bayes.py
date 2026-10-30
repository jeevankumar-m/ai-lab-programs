import math

X = [
    [25, 30000],
    [30, 40000],
    [35, 50000],
    [40, 60000],
    [45, 70000],
    [50, 80000]
]

y = [0, 0, 1, 1, 1, 1]

class_0 = [X[i] for i in range(len(X)) if y[i] == 0]
class_1 = [X[i] for i in range(len(X)) if y[i] == 1]

def mean(values):
    return sum(values) / len(values)

def variance(values):
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)

def gaussian(x, m, v):
    return (1 / math.sqrt(2 * math.pi * v)) * math.exp(
        -((x - m) ** 2) / (2 * v)
    )

def probability(data, group):
    p = 1
    for i in range(len(data)):
        values = [row[i] for row in group]
        p *= gaussian(data[i], mean(values), variance(values))
    return p

test_data = [38, 55000]

p0 = probability(test_data, class_0)
p1 = probability(test_data, class_1)

if p1 > p0:
    print("Prediction: Yes")
else:
    print("Prediction: No")
