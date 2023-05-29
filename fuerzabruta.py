import sys
import time

def solve_sudoku_brute_force(board):
# Función que resuelve el Sudoku utilizando fuerza bruta (backtracking)
  def is_valid(board, row, col, num):
  # Verifica si el número num es válido en la posición (row, col)
  # basándose en las reglas del Sudoku
  # Verificar fila
    for i in range(9):
      if board[row][i] == num:
        return False
  # Verificar columna
    for i in range(9):
       if board[i][col] == num:
         return False
  # Verificar región 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
      for j in range(3):
        if board[start_row + i][start_col + j] == num:
          return False
    
    return True

  def solve(board):
    # Función recursiva para resolver el Sudoku
    for row in range(9):
      for col in range(9):
        if board[row][col] == 'X':
          for num in range(1, 10):
            if is_valid(board, row, col, str(num)):
              board[row][col] = str(num)
              if solve(board):
                return True
              board[row][col] = 'X'  # Deshacer la asignación si no lleva a la solución
          return False  # No se encontró ninguna solución válida
    return True  # Se llenaron todas las celdas correctamente
    
  start_time = time.time()
  solved = solve(board)
  elapsed_time = time.time() - start_time

  if solved:
    return board, elapsed_time
  else:
    return None, elapsed_time

def load_board(filename):
  # Carga el tablero desde un archivo
  board = []
  with open(filename, 'r') as file:
    for line in file:
      row = list(line.strip())
      board.append(row)
  return board

def print_board(board):
  # Imprime el tablero
  for row in board:
    print(' '.join(row))

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Uso: python main.py <nombre_archivo>")
    sys.exit(1)

  filename = sys.argv[1]
  board = load_board(filename)

  print("Tablero inicial:\n")
  print_board(board)
  print()

  print("Resolviendo el Sudoku por fuerza bruta...\n")
  brute_force_solution, brute_force_time = solve_sudoku_brute_force(board)
  
  if brute_force_solution:
    print("Tablero resuelto por fuerza bruta:\n")
    print_board(brute_force_solution)
    print("\nTiempo transcurrido: {:.9f} segundos".format(brute_force_time))
  else:
    print("\nNo se pudo resolver el Sudoku por fuerza bruta en el tiempo límite de 5 minutos.")
