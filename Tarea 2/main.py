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
    if n < 3:
        return distanciaFuerzaBruta(p)
    else:
        medio = n//2
        p_l, p_r = p[:medio], p[medio:]
        medio_x = p[medio][0]
        q_l, q_r =  [p for p in q if p[0] <= medio_x] , [p for p in q if p[0] > medio_x]  

        d_l = parMasCercano(p_l,p_r,medio)
        d_r = parMasCercano(q_l,q_r,medio)

        d = min(d_l,d_r)

        strip = [p for p in q if abs(p[0] - medio_x) < d]

        dminsq = d*d

        for i in range(len(strip)):
            for j in range(i + 1,len(strip)):
                if (strip[j][1] - strip[i][1])**2 < dminsq:             #comparar solo los puntos que están suficientemente cerca en la coordenada
                    distq = (strip[j][0] - strip[i][0])**2 + (strip[j][1] - strip[i][1])**2
                    dminsq = min(distq,dminsq)

        return math.sqrt(dminsq)
                




def distanciaCercana(puntos):
    P = sorted(puntos, key=lambda p: p[0])
    Q = sorted(puntos, key=lambda p: p[1])
    return parMasCercano(P,Q,len(puntos))

if __name__ == "__main__":
    P = [(2, 3), (3, 4), (5, 1), (12, 10), (12, 30), (40, 50)]
    n = distanciaCercana(P)
    print(n)