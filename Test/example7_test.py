from Tested_Method.MethodToTest import working_function_3
from unittest.mock import patch
import pytest
TESTED_MODULE = 'Tested_Method.MethodToTest'
# mocking just the public function
# if you have functions such as: connection to DB ecc that executes in more tests we can create fixture
# pre-processing for test

@patch(f'{TESTED_MODULE}.get_element_1', return_value = -10)
@patch(f'{TESTED_MODULE}.get_element_2',return_value= 5)
@patch(f'{TESTED_MODULE}.sendAPI')
def test_working_function__apply_division_of_number1_by_number2_and_send(mock_sendAPi,mock_get_element_1,mock_get_element_2,login):
    #check if the exception is generated
    with pytest.raises(ValueError):
        working_function_3()
    
   
    