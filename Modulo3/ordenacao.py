n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segunto número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

lista_numeros = [n1, n2, n3]    
lista_ordenada = sorted(lista_numeros)

if lista_numeros == lista_ordenada:
    print("crescente")

else:
    print("não está em ordem crescente")