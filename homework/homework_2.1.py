# 1. квадрат числа
num = int(input('Введіть ціле число : '))
print ('Квадрат числа', num, " = ", (num ** 2))

# 2. середне значення

print ('Введіть три числа : ')
a = int(input('Перше число: '))
b = int(input('Друге число: '))
c = int(input('Трете число: '))
print("Середне значення :", (a+b+c) / 3)

# 3. Перетворення хвилин у години

qnt = int(input('Введіть кількість хвилин :'))
print (qnt // 60, "години", qnt % 60, "хвилин")

# 3. Перетворення хвилин у години

qnt = int(input('Введіть кількість хвилин :'))
hours, minutes = divmod( qnt , 60)
print ("годин = ", hours)
print ("хвилин = ", minutes)

# 3. Перетворення секунд у години, хвилини, секунди

qnt = int(input('Введіть кількість секунд :'))
a, remainder = divmod( qnt , 3600)
b,c = divmod (remainder, 60)

print ("Кількість годин :", a)
print ("Кількість хвилин :", b)
print ("Кількість секунд :", c)

# 4. Розрахунок знижки

price = float(input("Введіть ціну товару :"))
discount = float(input("Введіть знижку (%) :"))/ 100
discounted_price = price - (price *  discount)
print("Ціна за знижкою :", discounted_price)

# 5. Остання цифра числа

num = int(input('Введіть ціле число : '))

print('Остання цифра числа = ',(num %10))

# 6. Периметр прямокутника

length = float(input("Введіть довжину :"))
width = float(input("Введіть ширину :"))
perimeter = 2 * (length + width)
print("Периметр прямокутника =", perimeter)

# 7. Виведення числа у стопчик

num = int(input("Введіть чотирьохзначне число :"))
print (num // 1000)
print ((num // 100)%10)
print ((num // 10)%10)
print (num % 10)

# 7. Виведення числа у стопчик

num = int(input("Введіть чотирьохзначне число :"))
a, remainder = divmod (num , 1000)
b, remainder = divmod (remainder ,  100)
c,d, = divmod (remainder, 10)
print (a)
print (b)
print (c)
print (d)
