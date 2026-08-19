import random

numero1 = random.randint(0, 9)
numero2 = random.randint(0, 9)
numero3 = random.randint(0, 9)

koodi1 = str(numero1) + str(numero2)+ str(numero3)

num1 = random.randint(1,4)
num2 = random.randint(1,4)
num3 = random.randint(1,4)
num4 = random.randint(1,4)

koodi2 = str(num1) + str(num2) + str(num3) + str(num4)

print("Kolmenumeroinen koodi:", koodi1)
print("Nelinumeroinen koodi:", koodi2)