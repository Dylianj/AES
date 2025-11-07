#PARTE 1: Funciones básicas

# Función para obtener la dimensión de una matriz
def dimension(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    return filas, columnas

# Función para imprimir matrices
def imprimir(A):
    f, c = dimension(A)
    for i in range(f):
        print("| ", end="")
        for j in range(c):
            print("{:>5} |".format(hex(A[i][j])), end="")
        print("")
    print()

# Función para convertir un texto en una matriz 4x4 
def Mensaje(mensaje):
    ascii = [ord(c) for c in mensaje]
    while len(ascii) < 16:  # si el texto es corto, rellenamos con ceros
        ascii.append(0)
    matriz = []
    for i in range(0, 16, 4):
        matriz.append(ascii[i:i+4])
    return matriz

# XOR de matrices (suma)
def xor_matrices(m1, m2):
    filas, columnas = dimension(m1)
    nueva = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(m1[i][j] ^ m2[i][j])
        nueva.append(fila)
    return nueva

