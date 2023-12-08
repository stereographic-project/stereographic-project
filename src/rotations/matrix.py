from typing      import Self
from dataclasses import dataclass

@dataclass
class Matrix:
    matrix: list[list]
    
    @property
    def rows(self) -> int:
        return len(self.matrix)
    
    @property
    def columns(self) -> int:
        return len(self.matrix[0])
    
    # MAGIC METHODS
    def __add__(self, matrix: Self) -> Self:
        if self.columns != matrix.columns:
            return
        
        if self.rows != matrix.rows:
            return
        
        result = [[self.matrix[i][j] + matrix.matrix[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)
    
    def __sub__(self, matrix: Self) -> Self:
        if self.columns != matrix.columns:
            return
        
        if self.rows != matrix.rows:
            return
        
        result = self + (matrix * -1)
        return result
    
    def __mul__(self, scalar: float) -> Self:
        result = [[self.matrix[i][j] * scalar for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(result)
    
    def __matmul__(self, matrix: Self) -> Self:
        if self.columns != matrix.rows:
            return
        
        result = [[0 for _ in range(matrix.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(matrix.columns):
                cell = 0
                
                for k in range(self.columns):
                    cell += self.matrix[i][k] * matrix.matrix[k][j]
                
                result[i][j] = cell
                
        return Matrix(result)
