def CountWaitTime(task1, task2, task3, task4, q, w=0):
    wait1 = wait2 = wait3 = wait4 = 0
    wait1last = wait2last = wait3last = wait4last = 0
    while task1 > 0 or task2 > 0 or task3 > 0 or task4 > 0:
        for i in range(4):
            if i == 0:
                if task1 > q:
                    task1 -= q
                    if wait2last == 0 or wait3last == 0 or wait4last == 0:
                        wait1 += w
                    wait2 += (q + w)
                    wait3 += (q + w)
                    wait4 += (q + w)
                elif task1 != 0:
                    wait2 += (task1 + w)
                    wait3 += (task1 + w)
                    wait4 += (task1 + w)
                    task1 = 0
                    wait1last = wait1
            elif i == 1:
                if task2 > q:
                    task2 -= q
                    if wait1last == 0 or wait3last == 0 or wait4last == 0:
                        wait2 += w
                    wait1 += (q + w)
                    wait3 += (q + w)
                    wait4 += (q + w)
                elif task2 != 0:
                    wait1 += (task2 + w)
                    wait3 += (task2 + w)
                    wait4 += (task2 + w)
                    task2 = 0
                    wait2last = wait2
            elif i == 2:
                if task3 > q:
                    task3 -= q
                    if wait1last == 0 or wait2last == 0 or wait4last == 0:
                        wait3 += w
                    wait1 += (q + w)
                    wait2 += (q + w)
                    wait4 += (q + w)
                elif task3 != 0:
                    wait1 += (task3 + w)
                    wait2 += (task3 + w)
                    wait4 += (task3 + w)
                    task3 = 0
                    wait3last = wait3
            elif i == 3:
                if task4 > q:
                    task4 -= q
                    if wait1last == 0 or wait2last == 0 or wait3last == 0:
                        wait4 += w
                    wait1 += (q + w)
                    wait2 += (q + w)
                    wait3 += (q + w)
                elif task4 != 0:
                    wait1 += (task4 + w)
                    wait2 += (task4 + w)
                    wait3 += (task4 + w)
                    task4 = 0
                    wait4last = wait4
    print(f"[RR($q={q}$)], [{wait1last}], [{wait2last}], [{wait3last}], [{wait4last}], [{(wait1last+ wait2last + wait3last + wait4last) / 4}], ")

CountWaitTime(53, 8, 68, 24, 5 , 0)
CountWaitTime(53, 8, 68, 24, 8, 0)
CountWaitTime(53, 8, 68, 24, 10, 0)
CountWaitTime(53, 8, 68, 24, 20, 0)
CountWaitTime(53, 8, 68, 24, 5 , 2)
CountWaitTime(53, 8, 68, 24, 8, 2)
CountWaitTime(53, 8, 68, 24, 10, 2)
CountWaitTime(53, 8, 68, 24, 20, 2)

import numpy as np

a = np.mat([[-1, 0, 0, 1, 1, -1, 0, 0, 0, 0],
                  [0, 0, 0, -1, 0, 0, 1, -1, -1, 0],
                  [0, -1, 0, 0, 0 , 0, -1, 1, 0, -1],
                  [0, 0, -1, 0, -1, 1, 0, 0, 1, 1]])
print(np.matmul(a, a.T))
print(np.linalg.det(np.matmul(a, a.T)))

b = np.mat([[-1, 0, 0, 1, 1, -1, 0, 0],
            [0, 0, 0, -1, 0, 0, 1, 0],
            [0, -1, 0, 0, 0, 0, -1, -1],
            [0, 0, -1, 0, -1, 1, 0, 1]])
print(np.matmul(b, b.T))
print(np.linalg.det(np.matmul(b, b.T)))
c = np.mat([[-1, 0, 0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, -1, -1, 0],
            [0, -1, 0, 0, 0, 0, -1, 0, 0, -1],
            [0, 0, -1, 0, -1, 0, 0, 0, 0, 0]])
print(np.matmul(c, a.T))
print(np.linalg.det(np.matmul(c, a.T)))

d = np.mat([[-1, 0, 0, 0, 0, -1, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0],
            [0, -1, 0, 0, 0 , 0, -1, -1],
            [0, 0, -1, 0, -1, 0, 0, 0]])
print(np.matmul(d, b.T))
print(np.linalg.det(np.matmul(d, b.T)))

from sympy import Matrix, symbols, ZZ
from sympy.matrices.normalforms import smith_normal_form
# Define the variable
lambda_symbol = symbols('lambda')


a = np.mat([[0,0, 1, 0],
            [0,1,0,0],
            [-1,0, 0, -1],
            [1,-1,0,0]
])
print(np.linalg.inv(a))
b = np.mat([[-1,1,0,0],
            [1,0,1,0],
            [0,-1,0,0],
            [0,0,0,1]
])
print(-np.matmul(b.T, np.linalg.inv(a).T))
c = np.mat([
    [1,0,1,0],
    [0,1,0,0],
    [-1,0,0,0],
    [0,0,0,-1]
])
print(np.linalg.inv(c))
d = np.mat([
    [-1,0,0,0],
    [1,0,1,0],
    [0,-1,0,-1],
    [0,1,-1,0]
])
print(np.matmul(np.linalg.inv(c), d))
