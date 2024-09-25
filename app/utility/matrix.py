import copy
import numpy as np


class MatrixUtils:
    @staticmethod
    def matrix_multiply(A, B):
        """
        multiply two matrices A and B.
        :param A: First matrix (numpy array)
        :param B: Second matrix (numpy array)
        :return: Resultant matrix after multiplication
        """
        m = len(A)
        n = len(A[0])
        p = len(B[0])
        
        # Check if multiplication is possible
        if n != len(B):
            raise ValueError("Matrix size does not match")
        
        # Create result matrix initialized with zeros
        result = np.zeros((m, p))
        
        # Perform multiplication
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    result[i][j] += A[i][k] * B[k][j]
        
        return result   
    
    @staticmethod
    def matrix_inverse(A: np.ndarray) -> np.ndarray:
        """
        Inverse of a matrix using Gauss-Jordan elimination.
        :param A: Input matrix (numpy array)
        :return: Inverse of matrix A
        """
        n = A.shape[0]
        
        identity = np.eye(n)
        matrix = copy.deepcopy(A)
        
        # Perform Gauss-Jordan elimination
        for i in range(n):
            # Make the diagonal element 1
            diag_element = matrix[i][i]
            if diag_element == 0:
                raise ValueError("Matrix is singular and cannot be inverted.")
            for j in range(n):
                matrix[i][j] /= diag_element
                identity[i][j] /= diag_element
            
            # Make the other elements in the column 0
            for k in range(n):
                if k != i:
                    factor = matrix[k][i]
                    for j in range(n):
                        matrix[k][j] -= factor * matrix[i][j]
                        identity[k][j] -= factor * identity[i][j]
        
        return identity
    
    @staticmethod
    def matrix_transpose(A: np.ndarray) -> np.ndarray:
        """
        Manually compute the transpose of a matrix.
        :param A: Input matrix (numpy array)
        :return: Transposed matrix
        """
        A = copy.deepcopy(A)
        if A.ndim == 1:
            A = A.reshape((1, A.shape[0]))
        
        rows_A, cols_A = A.shape
        
        # Initialize transpose matrix
        transpose = np.zeros((cols_A, rows_A))
        
        # Perform transpose
        for i in range(rows_A):
            for j in range(cols_A):
                transpose[j][i] = A[i][j]
        
        return transpose