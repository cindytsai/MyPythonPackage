
def harmonic_mean_c(num_list):
    print("Cython implementation")
    value = 0.0
    for m in num_list:
        value += 1 / float(m)
    return len(num_list) / value
