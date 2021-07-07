from Tested_Method.MethodToTest import working_function_2
from unittest.mock import patch,call
TESTED_MODULE = 'Tested_Method.MethodToTest'
# mocking just the public function

@patch(f'{TESTED_MODULE}.get_element_1', return_value = 10)
@patch(f'{TESTED_MODULE}.get_element_2',return_value= 5)
@patch(f'{TESTED_MODULE}.sendAPI')
def test_working_function__apply_division_of_number1_by_number2_and_send(mock_sendAPi,mock_get_element_1,mock_get_element_2):
    #given
    expected_calls = [
        call("Dest",2),
        call("Dest1",2),
        call("Dest2",2),
        call("Dest3",2),
    ]
    #when
    result =  working_function_2()
    #then
    mock_sendAPi.assert_has_calls(expected_calls)