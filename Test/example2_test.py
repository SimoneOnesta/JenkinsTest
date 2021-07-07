from Tested_Method.MethodToTest import Add,ComplexFunc
from unittest.mock import patch
TESTED_MODULE = 'Tested_Method.MethodToTest'

@patch(f'{TESTED_MODULE}.Add')
def test_ComplexFunc_is_called_three_times_with_5_2_10(mock_Add):
      #given
    x = 2
    #when
    ComplexFunc(x)
    #than
    mock_Add.assert_any_call(x,2)
    mock_Add.assert_any_call(x,10)
    mock_Add.assert_any_call(x,5)