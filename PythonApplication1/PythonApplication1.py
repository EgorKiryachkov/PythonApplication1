print("hello world")

#2 вариант

#1 задача
N = int(input("Кол-во зайцев: "))
print(" (\_/)   " *N)
print(" (o o)   " *N)
print(" / | \*  "*N)

#2 задача
s = 0
for i in range(1, 15):
    s+=i
    print(s)

#3 задача
from random import *
A = randint(0, 101)
for i in range(0, 11):
    B = int(input("Угадай с 10-и раз: "))
    if B==A:
        print("Верно")
        break
    else:
        if B>A:
            print("B>A")
        if B<A:
            print("B<A")
if i==10:
    print("Вы проиграли")
    print("Правильный ответ: ", A)

#4 задача
A = ""
for i in reversed(input("Введите число чтобы перевернуть - ")):
    A+=i
print(A)

#5 задача
A=0
B=1
for i in reversed(input("Введите число - ")):
    A+=int(i)
    B*=int(i)
print(A)
print(B)