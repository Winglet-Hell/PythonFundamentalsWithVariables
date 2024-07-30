# 1st program
number = 9
result1 = (number ** 0.5) * 5
print(result1)

# 2nd program
a = 9.99
b = 9.98
c = 1000
d = 1000.1
result2 = a > b and c != d
print(result2)

# 3rd program
num1 = 1234
num2 = 5678
result3 = (num1 // 10 % 100) + (num2 // 10 % 100)
print(result3)

# 4th program
num3 = 13.42
num4 = 42.13
result4 = int(num3) == int((num4 - int(num4)) * 100) or int(num4) == int((num3 - int(num3)) * 100)
print(result4)
