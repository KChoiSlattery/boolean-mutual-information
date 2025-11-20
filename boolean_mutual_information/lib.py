import numpy as np
import numba
from matplotlib import pyplot as plt

__all__ = ("binary_entropy", "popcount")


@numba.njit()
def binary_entropy(p):
    """Computes the binary entropy function. Broadcasts to multiple values of p.

    Example:
        >>> binary_entropy(0.5)
        1.0
        >>> plt.plot(p := np.linspace(1e-6,1-1e-6,100), binary_entropy(p))
        >>> plt.show()
    """
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)


# The signature is critical for the function to be correct
@numba.njit("int_(uint32)")
def popcount(v):
    """From https://stackoverflow.com/questions/71097470/msb-lsb-popcount-in-numba.
    The number of "1" bits in an integer v. Numba does not support int.bit_count or
    np.count_bits."""
    v = v - ((v >> 1) & 0x55555555)
    v = (v & 0x33333333) + ((v >> 2) & 0x33333333)
    c = np.uint32((v + (v >> 4) & 0xF0F0F0F) * 0x1010101) >> 24
    return c
