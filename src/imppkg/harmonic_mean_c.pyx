from typing import List

def harmonic_mean_c(num_list: List[float]) -> float:
    """Return harmonic mean of a list of floats (Cython version).

    :param num_list: A list of floats containing values to calculate
    :type num_list: list
    :return: harmonic mean
    :rtype: float
    """
    print("Cython implementation")
    value = 0.0
    for m in num_list:
        value += 1 / float(m)
    return len(num_list) / value
