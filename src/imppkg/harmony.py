import sys
import imppkg.harmonic_mean
import termcolor


def main():
    num_list = []
    for i in range(1, len(sys.argv)):
        try:
            num_list.append(float(sys.argv[i]))
        except ValueError:
            termcolor.cprint("Cannot convert {} to float ... ignoring it".format(sys.argv[i]),
                             "red", "on_blue", attrs=["underline"])

    try:
        result = imppkg.harmonic_mean.harmonic_mean(num_list)
        termcolor.cprint(result, "green", "on_cyan", attrs=["bold"])
    except ZeroDivisionError:
        termcolor.cprint("ZeroDivisionError", "red", "on_blue", attrs=["blink"])
