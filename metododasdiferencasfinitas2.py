import numpy as np
import matplotlib.pyplot as plt

# Específico para a matriz do exercício
def build_matrix(ny, nx):
    empty_matrix = np.zeros((ny, nx))
    for i in range (nx):
        for j in range (ny):
            if (i == (ny-1) or j == (nx-1) or j == 0):
                empty_matrix[i][j] = 0
            elif(i == 0):
                empty_matrix[i][j] = 100
            else:
                empty_matrix[i][j]= -1
    return empty_matrix

def solve_matrix(act_matrix, nx, ny, alpha):
    nxt_matrix = build_matrix(ny, nx)
    for i in range (nx):
        for j in range (ny):
            if (nxt_matrix[i][j] == -1):
                nxt_matrix[i][j] = alpha * 0.01  * ((act_matrix[i+1][j]+act_matrix[i-1][j]-2*act_matrix[i][j])/0.01 + (act_matrix[i][j+1]+act_matrix[i][j-1]-2*act_matrix[i][j])/0.01) + act_matrix[i][j]
    return nxt_matrix



act_matrix = build_matrix(6, 6) # para 50 cm de 10 em 10 cm
for i in range (6):
    for j in range (6):
        if (act_matrix[i][j] == -1):
            act_matrix[i][j] = 0
   

for qq in range(1000):
    act_matrix = solve_matrix(act_matrix, 6, 6, 0.25)
    
  

plt.imshow(act_matrix)
plt.colorbar()
plt.show()