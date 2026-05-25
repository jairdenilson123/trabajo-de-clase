# Juego de Batalla Naval - Semana 7
# Tablero de 3x3 para la Batalla Naval (0 = Agua, 1 = Barco)
tablero = [
    ["~", "~", "~"],
    ["~", "B", "~"],
    ["~", "~", "~"]
]

print("--- Lógica de Ataque ---")
fila = 1
columna = 1

# Validar el ataque en la matriz
if tablero[fila][columna] == "B":
    print("¡Tocado y hundido!")
    tablero[fila][columna] = "X"  # Actualizacion dinamica
else:
    print("Agua...")
          
