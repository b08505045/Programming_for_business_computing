import math

c = float(input("unit cost : "))
r = float(input("unit price : "))
N = int(input("max need : "))
listex = [0.06,0.15,0.22,0.22,0.17,0.1,0.05,0.02,0.01]
list1 = [0.78,0.08,0.1,0.01,0.02,0.0,0.0,0.0,0.01]
list2 = [0.11,0.01,0.0,0.04,0.82,0.0,0.0,0.02,0.0]
list3 = [0.06,0.11,0.11,0.11,0.11,0.1,0.1,0.1,0.2]
list4 = [0.07,0.43,0.11,0.27,0.06,0.02,0.02,0.0,0.02]
list5 = [0.0,0.0,0.0,0.0,0.2,0.2,0.2,0.2,0.2]
# for i in range(N + 1) :
#     p.append(float(input(f"p[{i}] : ")))
profit = maxprofit = 0
order = 0
for q in range(N + 1):
    profit = -(q * c)
    for i in range(N + 1):
        profit += float(min(q, i)) * r * list5[i]
    # print(f"profit = {profit} at order {q}")
    if(profit > maxprofit):
        maxprofit = profit
        order = q
    profit = 0
    

print(order)
print(math.floor(maxprofit))
