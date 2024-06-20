import sys
import math

def distanciaFuerzaBruta(puntos):
    min_dist = float('inf')
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            d = math.sqrt((puntos[i][0] - puntos[j][0]) ** 2 + (puntos[i][1] - puntos[j][1]) ** 2)
            if d < min_dist:
                min_dist = d
    return min_dist

def parMasCercano(p, q, n):
    if n <= 3:
        return distanciaFuerzaBruta(p)
    else:
        medio = n // 2
        medio_x = p[medio][0]

        p_l = p[:medio]
        p_r = p[medio:]
        q_l = [pt for pt in q if pt[0] <= medio_x]
        q_r = [pt for pt in q if pt[0] > medio_x]

        d_l = parMasCercano(p_l, q_l, medio)
        d_r = parMasCercano(p_r, q_r, n - medio)

        d = min(d_l, d_r)

        strip = [pt for pt in q if abs(pt[0] - medio_x) < d]

        dminsq = d * d
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j][1] - strip[i][1]) ** 2 < dminsq:
                    distq = (strip[j][0] - strip[i][0]) ** 2 + (strip[j][1] - strip[i][1]) ** 2
                    dminsq = min(distq, dminsq)
        return math.sqrt(dminsq)

def distanciaCercana(puntos):
    P = sorted(puntos, key=lambda p: p[0])
    Q = sorted(puntos, key=lambda p: p[1])
    return parMasCercano(P, Q, len(puntos))

def leerInput():
    input_data = sys.stdin.read().strip().split('\n')
    indices = 0
    casos = []
    while indices < len(input_data):
        n = int(input_data[indices].strip())
        indices += 1
        puntos = []
        coordenadas = list(map(int, input_data[indices].strip().split()))
        for i in range(0, len(coordenadas), 2):
            puntos.append((coordenadas[i], coordenadas[i + 1]))
        indices += 1
        casos.append(puntos)
    return casos

def truncar_a_dos_decimales(numero):
    return math.floor(numero * 100) / 100

casos = leerInput()
for puntos in casos:
    distancia = distanciaCercana(puntos)
    distancia_truncada = truncar_a_dos_decimales(distancia)
    print(f"{distancia_truncada:.2f}")

