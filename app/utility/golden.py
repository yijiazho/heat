import numpy as np

class GoldenSection:
    @staticmethod
    def golden_section_search(func, a, b, tol=1e-5, max_iter=100):
        """
        Golden Section Search to find the minimum of a unimodal function.

        Parameters:
        func: The function to minimize.
        a: float, Lower bound of the search interval.
        b: float, Upper bound of the search interval.
        tol: float, Tolerance for convergence.
        max_iter: int, Max iteration times.

        Returns: The optimal point and its function value.
        """
        gr = (np.sqrt(5) + 1) / 2  # Golden ratio
        c = b - (b - a) / gr
        d = a + (b - a) / gr

        for _ in range(max_iter):
            if abs(b - a) < tol:
                break

            if func(c) < func(d):
                b = d
            else:
                a = c

            c = b - (b - a) / gr
            d = a + (b - a) / gr

        return (b + a) / 2