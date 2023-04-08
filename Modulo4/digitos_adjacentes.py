number = int(input("Digite um numero inteiro: "))

adjacente = False

while (number > 0 and adjacente == False):
  fstDig = number % 10
  tempNumber = number // 10
  secDig = tempNumber % 10
  number = number // 10

  if (fstDig == secDig):
    adjacente = True

if (adjacente == False):
  print("não")

else:
  print("sim")    
      