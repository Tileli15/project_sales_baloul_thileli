import numpy as np

def generate_random_sales(min_val, max_val, size):
    """
    Returns a NumPy array of random integers between min_val and max_val (inclusive) of length size.
    """
    return np.random.randint(min_val, max_val + 1, size)
