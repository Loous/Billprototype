import re

def ValidarFacturaN(name):
    
    validarNF = re.compile("^[A-Za-zÁÉÍÓÚáéíóú0-9]{5,100}$")
    
    if validarNF.match(name) == None:
        return True
    
    else:
        return False
    
    
def ValidarFacturaD(date):
    
    validarFF = re.compile("^[0-9]{1,2}(-)[0-9]{1,2}(-)[0-9]{4}$")
    
    if validarFF.match(date) == None:
        return True
    
    else:
        return False
    
    
def ValidarFacturaT(total):
    
    validarFT = re.compile("^[0-9]{1,1000}$")
    
    if validarFT.match(total) == None:
        return True
    
    else:
        return False
        
        
        
        
    
    
    