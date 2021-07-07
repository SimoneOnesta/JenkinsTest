def Add(x: int,y : int):
   
    return x + y

def ComplexFunc(x: int):
    plus_10 = Add(x,10)
    plus_2 = Add(x,2)
    plus_5 = Add(x,5)

    return (plus_10,plus_2,plus_5)

def working_function():

    x = get_element_1()
    
    y = get_element_2()
    

    return _privatefunc(x,y)

def working_function_1():
    x = get_element_1()
    
    y = get_element_2()
    
    result = _privatefunc(x,y)

    sendAPI("Dest",result)
    
    return result
def working_function_2():
    x = get_element_1()
    
    y = get_element_2()
    
    result = _privatefunc(x,y)

    sendAPI("Dest",result)
    sendAPI("Dest1",result)
    sendAPI("Dest2",result)
    sendAPI("Dest3",result)

    
    return result

def working_function_3():
    x = get_element_1()
    
    y = get_element_2()
    
    result = _privatefunc(x,y)

    sendAPI("Dest",result)
    sendAPI("Dest1",result)
    sendAPI("Dest2",result)
    sendAPI("Dest3",result)

    if result < 0:
        raise ValueError

    return result  

def working_function_with_DB(credential):
    #here we set the connection
    x = get_element_1()
    
    y = get_element_2()
    
    result = _privatefunc(x,y)

    sendAPI("Dest",result)
    sendAPI("Dest1",result)
    sendAPI("Dest2",result)
    sendAPI("Dest3",result)

    if result < 0:
        raise ValueError

    return result  

def get_element_1():
    return 100

def get_element_2():
    return 50

def _privatefunc(x,y):
    return x/y

def sendAPI(dest,value):
    pass