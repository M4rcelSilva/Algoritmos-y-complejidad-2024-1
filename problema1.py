import sys

def calcular_gaps(diseño, L):
    suma_gaps = 0
    for fila in diseño:
        longitud_total = sum(fila)
        gap = L - longitud_total
        suma_gaps += gap ** 2
    return suma_gaps

def fuerza_bruta(L, n, longitudes):
    def backtrack(indice, diseño_actual, fila_actual, longitud_actual):
        if indice == n:
            if fila_actual:
                diseño_actual.append(fila_actual)
            return calcular_gaps(diseño_actual, L)

        min_gaps = float('inf')

        if longitud_actual + longitudes[indice] <= L:
            nuevo_diseño = list(diseño_actual)
            nueva_fila = list(fila_actual)
            nueva_fila.append(longitudes[indice])
            min_gaps = min(min_gaps, backtrack(indice + 1, nuevo_diseño, nueva_fila, longitud_actual + longitudes[indice]))

        if fila_actual:
            nuevo_diseño = list(diseño_actual)
            nuevo_diseño.append(fila_actual)
            min_gaps = min(min_gaps, backtrack(indice + 1, nuevo_diseño, [longitudes[indice]], longitudes[indice]))

        return min_gaps

    return backtrack(0, [], [], 0)


def main():
    datos_entrada = sys.stdin.read().strip().split()
    indice = 0

    while indice < len(datos_entrada):
        L = int(datos_entrada[indice])
        n = int(datos_entrada[indice + 1])
        longitudes = list(map(int, datos_entrada[indice + 2: indice + 2 + n]))
        indice += 2 + n
        resultado = fuerza_bruta(L, n, longitudes)
        print(resultado)

if __name__ == "__main__":
    main()


