#1
num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))

for i in range(num1, num2 + 1):
    if i % 7 == 0:
        print(i)

#2
num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))
count = 0

for i in range(num1, num2 + 1):
    print(i, end=" ")

print("\n")
for i in range(num2, num1 - 1, -1):
    print(i, end=" ")

print("\n")
for i in range(num1, num2 + 1):
    if i % 7 == 0:
        print(i, end=" ")

print("\n")
for i in range(num1, num2 + 1):
    if i % 5 == 0:
        count += 1
print(count)

#3
num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))

for i in range(num1, num2 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz.Buzz", end=" ") #поставил точку, чтобы было видно, что это два слова, а то порой не понятно
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
