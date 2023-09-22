import sys
import imppkg.harmonic_mean
import termcolor


def _parses_num(inputs: list[str]) -> list[float]:
    try:
        return [float(num) for num in inputs]
    except ValueError:
        return []


def _calculate_results(nums: list[float]) -> float:
    try:
        return imppkg.harmonic_mean.harmonic_mean(nums)
    except ZeroDivisionError:
        return 0.0


def _format_output(result: float) -> str:
    return termcolor.colored(str(result), "red", "on_cyan", attrs=["bold"])


def main() -> None:
    nums = _parses_num(sys.argv[1:])
    result = _calculate_results(nums)
    print(_format_output(result))
