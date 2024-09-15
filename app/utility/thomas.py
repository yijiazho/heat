import numpy as np


class ThomasAlgorithm:
    @staticmethod
    def thomas(A, r):
        """
        Preprocess to extract diagonals of the tridiagonal matrix A.
        A: 2D numpy array representing a tridiagonal matrix.
        r: 1D numpy array representing the right-hand side vector.
        """
        n = len(r)
        f = np.zeros(n)
        e = np.zeros(n - 1)
        g = np.zeros(n - 1)
        
        for i in range(n - 1):
            f[i] = A[i][i]
            g[i] = A[i][i + 1]
            e[i] = A[i + 1][i]
            
        f[n - 1] = A[n - 1][n - 1]
            
        return ThomasAlgorithm.thomas_solver(f, g, e, r)

    @staticmethod
    def thomas_solver(f, g, e, r):
        """
        Thomas Algorithm to solve tridiagonal system Ax = r
        where A is represented by its diagonals.
        f: main diagonal of matrix A
        g: upper diagonal of matrix A
        e: lower diagonal of matrix A
        r: right-hand side vector
        """
        n = len(r)
        x = np.zeros(n)
        
        for i in range(1, n):
            e[i - 1] /= f[i - 1]
            f[i] -= e[i - 1] * g[i - 1]
            
        for i in range(1, n):
            r[i] -= e[i - 1] * r[i - 1]
        
        x[n - 1] = r[n - 1] / f[n - 1]  
        for i in range(n - 2, -1, -1):
            x[i] = (r[i] - g[i] * x[i + 1]) / f[i]
            
        return x