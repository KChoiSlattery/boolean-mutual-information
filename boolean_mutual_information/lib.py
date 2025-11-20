import numpy as np
from matplotlib import pyplot as plt

__all__ = ("binary_entropy", "make_A")


def binary_entropy(p):
    """Computes the binary entropy function. Broadcasts to multiple values of p.

    Example:
        >>> binary_entropy(0.5)
        np.float64(1.0)
        >>> plt.plot(p := np.linspace(1e-6,1-1e-6,100), binary_entropy(p))
        >>> plt.show()
    """
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)


def make_A(alpha, n):
    """Constructs

    Args:
        alpha: _description_
        n: _description_

    Returns:
        _description_
    """
    k = 2**n  # Number of possible values of x or y
    i, j = np.meshgrid(range(k), range(k))
    C = np.bitwise_count(
        np.bitwise_xor(i, j)
    )  # Number of mismatches between y_i and x_j
    A = alpha**C * (1 - alpha) ** (n - C)  # p(y|x)
    A *= 1 / (k)  # p(x)
    return A
