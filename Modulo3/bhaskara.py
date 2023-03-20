import math

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

delta = (b**2) - (4 * a * c)

if delta < 0:
    print("esta equação não possui raízes reais")

else:
    if delta == 0:
        x = -(b) / (2 * a)
        print("a raiz desta equação é", x)
        
    else:
        raizDelta = math.sqrt(delta)
        x1 = (-(b) + raizDelta) / (2 * a)
        x2 = (-(b) - raizDelta) / (2 * a)
        raizes = [x1, x2]
        raizesOrdenadas = sorted(raizes)
        print("as raízes da equação são", raizesOrdenadas[0], "e", raizesOrdenadas[1])
        
        