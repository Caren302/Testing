# Forma 1
"""def mayor(numero1,numero2): #-> int | None:
    result = None
    
    if numero1 > numero2:
        result = numero1
    elif numero2 > numero1:
        result = numero2
        
    return result"""

# Forma 2

"""def mayor(numero1,numero2): #-> int | None:
    
    if numero1 > numero2:
        return numero1
    elif numero2 > numero1:
        return numero2
    else:
        return None"""

# Prueba de escritorio1
"""def test_mayor1():
    assert mayor(2,1) == 2
    
def test_mayor2():
    assert mayor(1,2) == 2
    
def test_mayor3():
    assert mayor(2,2) == None"""

# Prueba de escritorio2

"""def test_mayor1():
    assert mayor(2,1) == 2
    assert mayor(1,2) == 2
    assert mayor(2,2) == None"""

# prueba de escritorio3

"""print(mayor(2,1)) # 2
print(mayor(1,2)) # 2
print(mayor(2,2)) # None"""