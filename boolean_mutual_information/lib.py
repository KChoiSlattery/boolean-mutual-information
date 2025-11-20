import numpy as np
import numba
from matplotlib import pyplot as plt

__all__ = ("binary_entropy",)


def binary_entropy(p):
    """Computes the binary entropy function. Broadcasts to multiple values of p.

    Example:
        >>> binary_entropy(0.5)
        np.float64(1.0)
        >>> plt.plot(p := np.linspace(1e-6,1-1e-6,100), binary_entropy(p))
        >>> plt.show()
    """
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)
