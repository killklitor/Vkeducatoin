a=int(input())
b=float(input())
c=int(input())
print(f"{a:010}")
print(f"{b:#>10.2f}")
d=(f"{c:b}")
print('_'.join([d[i:i+4] for i in range(0, len(d), 4)]))