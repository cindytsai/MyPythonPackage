import sys
from termcolor import colored
from imppkg.harmony import main


def test_harmony_happy_path(monkeypatch, capsys):
    # patching fake inputs
    inputs = ["1", "4", "4"]
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)

    # get inputs from sys.argv and test it
    main()

    # check the value
    expected_value = 2.0
    assert float(capsys.readouterr().out.strip()) == colored(expected_value, "yellow", "on_cyan", attrs=["bold"])


def test_harmony_unhappy_path_value_error(monkeypatch, capsys):
    # patching fake inputs
    inputs = ["1", "a"]
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)

    # get inputs from sys.argv and test it
    main()

    # check the result
    assert capsys.readouterr().out.strip() == "ValueError"


def test_harmony_unhappy_path_zero_division_error(monkeypatch, capsys):
    # patching fake inputs
    inputs = ["0", "0"]
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)

    # get inputs from sys.argv and test it
    main()

    # check the result
    assert capsys.readouterr().out.strip() == "ZeroDivisionError"

def test_always_pass():
    assert True
