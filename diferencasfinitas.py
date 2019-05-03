import numpy as np

def solve(k0, t_atras, t_frente, t_atual):
    return k0*(t_atras - 2*t_atual + t_frente) + t_atual

# Específico para a matriz do exercício
def build_matrix(ny, nx):
    empty_matrix = np.zeros((nx, ny))
    for i in range (nx):
        for j in range (ny):
            if (j == 0 or j == (ny-1)):
                empty_matrix[i][j] = 0
            elif(i == 0):
                empty_matrix[i][j] = 20
            else:
                empty_matrix[i][j]= -1
    return empty_matrix

def solve_matrix(matrix, ny, nx, k0):
    for i in range (nx):
        for j in range (ny):
            if (matrix[i][j] == -1):
                matrix[i][j] = k0 * (matrix[i-1][j+1] - 2 * matrix[i-1][j] + matrix[i-1][j-1]) + matrix[i-1][j]
    return matrix



full_matrix = build_matrix(10, 100) # para 50 cm e 500 segundos
#print(full_matrix)
right_matrix = solve_matrix(full_matrix, 10, 100, 0.2)
print(right_matrix)
