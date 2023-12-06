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
    
    def __matmul__(self, matrix: Self):
        if self.columns != matrix.rows:
            return
        
        result = [[0 for _ in range(matrix.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(matrix.columns):
                cell = 0
                
                for k in range(self.columns):
                    cell += self.matrix[i][k] * matrix.matrix[k][j]
                
                result[i][j] = cell
                
        return result
