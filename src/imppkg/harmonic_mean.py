def harmonic_mean(num_list):
    """Return harmonic mean of a list of floats.

    :param num_list: A list of floats containing values to calculate
    :type num_list: list
    :return: harmonic mean
    :rtype: float
    """
    value = 0.0
    for m in num_list:
        value += 1 / float(m)
    return len(num_list) / value
