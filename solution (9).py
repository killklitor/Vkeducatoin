import string
s = input()
a = {}
for word in s.lower().split():
    a[word] = a.get(word, 0) + 1
max_count = max(a.values())
for word, count in a.items():
    if count == max_count:
        print(word, count)
        break