import time
from rotations import Matrix, Rotation

a0 = time.perf_counter_ns()
case1 = Matrix([[20, 20, 20]])@(Rotation(10, 10, 10).matrix_x+Rotation(10, 10, 10).matrix_y-Rotation(10, 10, 10).matrix_z)
a1 = time.perf_counter_ns()
print("Case 1: ", a1 - a0)

b0 = time.perf_counter_ns()
case2 = (Matrix([[20, 20, 20]])@Rotation(10, 10, 10).matrix_x) \
    +   (Matrix([[20, 20, 20]])@Rotation(10, 10, 10).matrix_y) \
    -   (Matrix([[20, 20, 20]])@Rotation(10, 10, 10).matrix_z) 
b1 = time.perf_counter_ns()
print("Case 2: ", b1 - b0)

print(case1, case2)
