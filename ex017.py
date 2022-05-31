from math import hypot

catetoOposto = float(input('digite o cateto oposto'))
catetoAdjacente = float(input('digite o cateto adjacente'))

hipotenuza = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
hipotenuza2 = hypot(catetoOposto, catetoAdjacente)

print('comprimento da hipotenuza = {:.2f}' .format(hipotenuza))
print('comprimento da hipotenuza = {:.2f}' .format(hipotenuza2))