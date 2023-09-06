import math

c = float(input("unit cost : "))
r = float(input("unit price : "))
N = int(input("max need : "))
q = float(input("order : "))
p = []
list1 = [0.06,0.15,0.22,0.22,0.17,0.1,0.05,0.02,0.01]
list2 = [0.11,0.01,0.0,0.04,0.82,0.0,0.0,0.02,0.0]
list3 = [0.06,0.11,0.11,0.11,0.11,0.1,0.1,0.1,0.2]
list4 = [0.07,0.43,0.11,0.27,0.06,0.02,0.02,0.0,0.02]
list5 = [0.11,0.11,0.11,0.11,0.12,0.11,0.11,0.11,0.11]

cost = float(-(c * q))
print(cost)
profit = 0
for i in range(N + 1):
    profit += float(min(q, i)) * r * list1[i]

print(profit)
print(math.floor(profit + cost))
