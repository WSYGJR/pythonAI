s1 = {5,2,5,9,0,0,4,30,5,6,12}
print(s1)
print(type(s1))

s2 = set()
print(s2)

s3 = {5,2,5,9,6,12,152,0.6,15485,151,123}
print(s3)
s3.add(4856)
print(s3)
s3.remove(4856)
print(s3)
e = s3.pop()
print(e)
print(s3)
s3.clear()
print(s3)
s3 = {5,2,5,9,6,12,152,0.6,15485,151,123}
print(s3)
s4 = s1.difference(s3)
print(s4)
s4 = s1.union(s3)
print(s4)
s4 = s1.intersection(s3)
print(s4)