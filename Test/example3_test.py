from Tested_Method.MethodToTest import working_function
from unittest.mock import patch
TESTED_MODULE = 'Tested_Method.MethodToTest'
# mocking just the public function

@patch(f'{TESTED_MODULE}.get_element_1', return_value = 10)
@patch(f'{TESTED_MODULE}.get_element_2',return_value= 5)
def test_working_function__apply_division_of_number1_by_number2(mock_get_element_1,mock_get_element_2):
    #given
    expected_result = 2
    #when
    result =  working_function()
    #then
    assert result == expected_result