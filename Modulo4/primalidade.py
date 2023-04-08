import math

number = int(input("Digite um numero inteiro: "))

if (number < 2):
  print("não primo")

else:
  is_prime = True
  for i in range(2, int(math.sqrt(number)) + 1):
    if number % i == 0:
      is_prime = False
   

if (is_prime == True):
  print("primo")

else:
  print("não primo")
