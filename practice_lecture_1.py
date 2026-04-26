#task1 print 1 to 30
for i in range(1,31):
    print(i)

#task2 print 30 to 1 reverse
for i in range(30,0,-1):
    print(i)

#task3 print even numbers from 1 to 50
for i in range(1,51):
    if i % 2 == 0:
        print(i)

#task4 print odd numbers from 1 to 50
for i in range(1,51):
    if i % 2 != 0:
        print(i)

#task5 count numbers divisible by 5 1 -100
count = 0

for i in range(1,101):
    if i % 5 == 0:
        count += 1

print(count)


#task6 sum of numbers from 1 to 50
sum = 0

for i in range(1,51):
    sum = sum + i

print(sum)

#task7 sum of even numbers 1-50
sum = 0

for i in range(1,51):
    if i % 2 == 0:
        sum = sum + i
    
print(sum)

#task8 product of numbers from 1 to 5
product = 1

for i in range(1,6):
    product = product*i

print(product)

#task9 print numbers from 50 to 10 reverse
for i in range(50,9,-1):
    print(i)

#task10 print numbers from 100 to 1 divisible by 7
for i in range(100,0,-1):
    if i % 7 == 0:
        print(i)

#task11 print numbers from 30 to 1 but skip multiple of 4
for i in range(30,0,-1):
    if i % 4 == 0:
        continue
    print(i)

#task12 reverse print 20 1 using while loop
n = 20

while n >= 1:
    print(n)
    n -= 1

#task13 count digits in number
n = 45678
count = 0

while n > 0:
    last_digit = n % 10
    count += 1
    n = n // 10

print(count)

#task14 reverse a number
n = 45678
rev = 0

while n > 0:
    last_digit = n % 10
    rev = rev*10 + last_digit
    n = n // 10

print(rev)

#task15 sum of digits
n = 825
sum = 0

while n > 0:
    last_digit = n % 10
    sum = sum + last_digit
    n = n // 10

print(sum)

#task16 print 1-50 ,stop at 37
for i in range(1,51):
    if i == 37:
        break
    print(i)

#task17 print 1-50, skip multiples of 6
for i in range(1,51):
    if i % 6 == 0:
        continue
    print(i)

#task18 count numbers entered until user enters 0
count = 0

num = int(input("enter number:"))

while num != 0:
    count += 1
    num = int(input("enter number:"))

print(count)


