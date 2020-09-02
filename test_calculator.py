import pytest

@pytest.mark.parametrize("HDLvalue, expected",
    [(70, "Normal"),
    (45, "Borderline Low"),
    (10, "Low"),
    ]) 

def test_analyze_HDL_fun(HDLvalue, expected):
    from calculator import analyze_HDL_fun
    result = analyze_HDL_fun(HDLvalue)
    assert result == expected
