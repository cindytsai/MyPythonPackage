import sys
import pytest
from imppkg.harmony import main


@pytest.mark.parametrize("input_args, expected", [(["1", "4", "4"], 2.0), (["1", "a"], 0.0), (["0"], 0.0)])
def test_harmony(input_args, monkeypatch, capsys, expected):
    # patching fake inputs
    monkeypatch.setattr(sys, "argv", ["harmony"] + input_args)

    # get inputs from sys.argv and test it
    main()

    # check the value
    assert capsys.readouterr().out.strip() == str(expected)


@pytest.mark.mystuff
def test_mystuff():
    a = 1
    b = 2
    assert a + b == 3


@pytest.mark.xfail
def test_expected_failure():
    a = 1
    b = 2
    assert a + b == 4
