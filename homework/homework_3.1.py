# 3.1 Калькулятор

num1 = float(input("Введіть число 1 : "))
action = input("Введіть дію над числами : ")
num2 = float(input("Введіть число 2 : "))
if action == "+":
  print(num1 + num2)
elif action == "-":
  print(num1 - num2)
elif action == "*":
  print(num1 * num2)


elif action == "/":
  if num2 == 0:
    print("Ділення на нуль!")
  else:
    print(num1 / num2)
else:
    print("Невірна дія")
