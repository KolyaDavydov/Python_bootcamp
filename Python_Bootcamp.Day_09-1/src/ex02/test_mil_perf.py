from time import time

import matrix
import mult_python
from random import randint


n = 200
x = [[randint(1, 1000) for _ in range(n)] for _ in range(n)]
y = [[randint(1, 1000) for _ in range(n)] for _ in range(n)]


start_cy = time()
res_cy = matrix.mul(x, y)
end_cy = time()
time_cy = end_cy - start_cy

start_py = time()
res_py = mult_python.mul(x, y)
end_py = time()
time_py = end_py - start_py


assert res_cy == res_py
print('требуемое время для умножения матриц 200*200:')
print(f"Cython: {time_cy} c")
print(f"Python: {time_py} c")

print(
    f"Cython быстрее в {time_py/time_cy} раз"
)
