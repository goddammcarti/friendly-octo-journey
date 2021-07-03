f = int(input())
t = int(input())
d = int(input())

m = f
if m < t:
    m = t
if m < d:
    m = d

print(m)