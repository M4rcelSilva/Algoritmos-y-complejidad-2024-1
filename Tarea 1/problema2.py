
import sys

def calcular_gaps(diseño, L):
    suma_gaps = 0
    for fila in diseño:
        longitud_total = sum(fila)
        gap = L - longitud_total
        suma_gaps += gap ** 2
    return suma_gaps

def dp_gaps(L, n, longitudes):
    memo = {}

    def dp(indice, fila_actual, longitud_actual):
        if indice == n:
            if fila_actual:
                diseño_actual = tuple(fila_actual)
                if diseño_actual not in memo:
                    memo[diseño_actual] = calcular_gaps([diseño_actual], L)
                return memo[diseño_actual]
            return 0

        estado = (indice, tuple(fila_actual), longitud_actual)
        if estado in memo:
            return memo[estado]

        min_gaps = float('inf')

        # Caso 1: Añadir la longitud actual a la fila actual si cabe
        if longitud_actual + longitudes[indice] <= L:
            nueva_fila = list(fila_actual)
            nueva_fila.append(longitudes[indice])
            min_gaps = min(min_gaps, dp(indice + 1, nueva_fila, longitud_actual + longitudes[indice]))

        # Caso 2: Empezar una nueva fila con la longitud actual
        if fila_actual:
            diseño_actual = tuple(fila_actual)
            if diseño_actual not in memo:
                memo[diseño_actual] = calcular_gaps([diseño_actual], L)
            min_gaps = min(min_gaps, memo[diseño_actual] + dp(indice + 1, [longitudes[indice]], longitudes[indice]))
        else:
            min_gaps = min(min_gaps, dp(indice + 1, [longitudes[indice]], longitudes[indice]))

        memo[estado] = min_gaps
        return min_gaps

    return dp(0, [], 0)

def main():
    datos_entrada = sys.stdin.read().strip().split()
    indice = 0

    while indice < len(datos_entrada):
        L = int(datos_entrada[indice])
        n = int(datos_entrada[indice + 1])
        longitudes = list(map(int, datos_entrada[indice + 2: indice + 2 + n]))
        indice += 2 + n
        resultado = dp_gaps(L, n, longitudes)
        print(resultado)

if __name__ == "__main__":
    main()