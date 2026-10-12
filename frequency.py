import random  as r
list=[]
for i in range(1000):
    x = r.randint(1, 1000)
    list.append(x)

print(list)

for i in list:
    print(i ,":",list.count(i))