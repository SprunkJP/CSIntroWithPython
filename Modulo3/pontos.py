import math

#   Prompt user for the points coordinates
xPoint1 = int(input("Insira a coordenada X do primeiro ponto: "))
yPoint1 = int(input("Insira a coordenada Y do primeiro ponto: "))

xPoint2 = int(input("Insira a coordenada X do segundo ponto: "))
yPoint2 = int(input("Insira a coordenada Y do segundo ponto: "))

#   Measure the distance between the points
pointsDistance = math.sqrt(((xPoint1 - xPoint2) ** 2) + ((yPoint1 - yPoint2) ** 2))
print(" ")
#   Conditional for output distance
if(pointsDistance >= 10):
    print("longe")
    
else:
    print("perto")