from rotations import Matrix, Rotation

case1 = Matrix([[20, 20, 20]])@(Rotation(10, 10, 10).matrix_x+Rotation(10, 10, 10).matrix_y-Rotation(10, 10, 10).matrix_z)
case2 = (Matrix([[20, 20, 20]])@Rotation(10, 10, 10).matrix_x)+(Matrix([[20, 20, 20]])@Rotation(10, 10, 10).matrix_y)-(Matrix([[20, 20, 20]])@Rotation(10, 10, 10).matrix_z)

print(case1, case2)
