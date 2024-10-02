from thething.module import f1,f2,f3,f4
import pytest

def test_f1_output():
    output = f1()
    assert output == 0

def test_f2_output():
    output = f2()
    assert output == 1

def test_f3_output():
    output = f3()
    assert output == "somestring"

@pytest.mark.parametrize('a,b,expected_output',
                        [
                            (1,1,2),
                            (2,1,3),
                            (2,1,3),
                        ]
                        )
def test_f4_output(a,b,expected_output):
    output = f4(a,b)
    assert output == expected_output


def test_f4_exception():
    with pytest.raises(TypeError) as exception_info:
        f4("a",2)
    assert str(exception_info.value) == "parameter 'a' has to be an integer" 