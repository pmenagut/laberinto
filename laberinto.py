def construir_laberinto(filas, columnas, muros):
    # Inicializar el laberinto con espacios en blanco
    laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]

    # Colocar muros en las posiciones especificadas
    for muro in muros:
        fila, columna = muro
        laberinto[fila][columna] = 'X'

    return laberinto

# Coordenadas de las casillas con muro
muros = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Tamaño del laberinto
filas = 5
columnas = 5

# Construir el laberinto
laberinto = construir_laberinto(filas, columnas, muros)

# Imprimir el laberinto
for fila in laberinto:
    print(' '.join(fila))
