#typecasting
print(int(3.94))
print(int(True))
print(int("4"))


a = 5
b = 10

print("Before swap:", a, b)

temp = a
a = b
b = temp

print("After swap:", a, b)

p = float(input())
r = float(input())
t = float(input())

si = (p * r * t) / 100

print(si)




n = int(input())

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)
