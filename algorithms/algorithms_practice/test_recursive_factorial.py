"""Testing module 'recursive_factorial'"""

from recursive_factorial import RecFac
import pytest


@pytest.mark.parametrize('test_arg, expected', ((5, 120),
                                                (3, 6),
                                                (4, 24)))
def test_recfac(test_arg, expected):
    assert RecFac().factor(test_arg) == expected


# testing for raising a TypeError
def test_recfac_type():
    arg = 'er'
    with pytest.raises(TypeError):
        RecFac().factor(arg)


# testing for raising a ValueError
@pytest.mark.parametrize('test_value', (-5, -14))
def test_recfac_value(test_value):
    with pytest.raises(ValueError):
        RecFac().factor(test_value)
