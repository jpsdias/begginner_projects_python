import pytest
import source.calculator as calc

@pytest.mark.parametrize('num1, num2, result', [(1,2,3), (4,3,7), (6,10,16)])
def test_add(num1,num2,result):
    assert result == calc.add(num1, num2)

@pytest.mark.parametrize('num1, num2, result', [(1,2,0.5), (4,4,1), (6,0.1,60)])
def test_divide(num1,num2,result):
    assert result == calc.div(num1, num2)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.div(10, 0)

def test_div_by_zero():
    """
    Test that div raises a ZeroDivisionError when the divisor is zero.
    """
    with pytest.raises(ZeroDivisionError) as exc_info:
        calc.div(10, 0)
    # Optionally, you can check for the error message as well.
    assert "Division by zero" in str(exc_info.value)