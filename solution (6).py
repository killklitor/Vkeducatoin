d=input()
e=d.split()
a=0
b=0
for x in e:
    a += len(x)
    b += 1
c=a / b
print(round(c, 2))