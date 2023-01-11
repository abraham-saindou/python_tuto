import sys
mytyple = tuple(["Max", 28, "Boston", 'p', 'p'])
print(mytyple)
print(mytyple.count('p'))
print(mytyple.index('p'))

print(sys.getsizeof(mytyple), "bytes")