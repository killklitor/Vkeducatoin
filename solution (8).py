import string
s = input()
a = {}
for b in s.lower():
    if b not in string.whitespace:
        a[b] = a.get(b, 0) + 1
for b in sorted(a.keys()):
    print(b, end=' ')