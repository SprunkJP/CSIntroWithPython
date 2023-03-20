n = int(input("Digite um número inteiro:"))
par = n % 10
if par == 2 or par == 4 or par == 6 or par == 8 or par == 0:
    print("par")
else:
    print("ímpar")