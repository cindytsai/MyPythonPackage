import sys
import imppkg.harmonic_mean
import termcolor


def main():
    result = 0.0

    try:
        nums = [float(num) for num in sys.argv[1:]]
        try:
            result = imppkg.harmonic_mean.harmonic_mean(nums)
            termcolor.cprint(result, "yellow", "on_cyan", attrs=["bold"])
        except ZeroDivisionError:
            termcolor.cprint("ZeroDivisionError", "red", "on_blue", attrs=["blink"])
    except ValueError:
        nums = []
        termcolor.cprint("ValueError", "red", "on_blue", attrs=["underline"])
