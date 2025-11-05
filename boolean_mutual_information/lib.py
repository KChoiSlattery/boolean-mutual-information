__all__ = ("multiply",)


def multiply(x: int | float, y: int | float) -> int | float:
    """An example of a Python function that takes two scalars and returns a scalar. Computes the product of x and y, $x\\times y$.

    Args:
        x: First number to be multiplied.
        y: Second number to be multiplied.

    Returns:
        The product of `x` and `y`.

    Example:

        >>> multiply(2, 3)
        6

        >>> multiply(0.5, 3)
        1.5
    """

    return x * y
