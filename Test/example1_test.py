from Tested_Method.MethodToTest import Add 
def test_Add_2_and_2_return_4():
    #given
    x = 2
    y = 2
    #when
    result = Add(x,y)
    #then
    assert result == 4