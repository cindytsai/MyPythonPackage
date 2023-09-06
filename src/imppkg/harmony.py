import sys
import imppkg.harmonic_mean


def main():
    num_list = []
    for i in range(1, len(sys.argv)):
        try:
            num_list.append(float(sys.argv[i]))
        except ValueError:
            print("Cannot convert {} to float ... ignoring it".format(sys.argv[i]))

    try:
        result = imppkg.harmonic_mean.harmonic_mean(num_list)
        print(result)
    except ZeroDivisionError:
        print("ZeroDivisionError")
