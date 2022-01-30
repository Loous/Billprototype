from time import strftime

def ValidarFechas(fecha):
    
    x = int(strftime("%Y"))
    
    d, m, a = [], [], []
    
    c = 0
    
    for n in fecha:
        if n != "-":
            if c == 0:
                d.append(n)
                
            elif c == 1:
                m.append(n)
                
            elif c == 2:
                a.append(n)
                
        else:
            c += 1
            
    day = int("".join(d))
    month = int("".join(m))
    year = int("".join(a))
    
    if year > x:
        input(f"\nEl año ingresado debe ser menor o igual al año {x}, presiona enter para continuar...")
        
        
    else:
        
        if month == 1 and day >= 1:
            return True
        
        elif month == 2:
            if day == 29:
                if year % 4 == 0:
                    return True
                
            elif day >= 1 and day <= 28:
                return True
            
        elif month == 3 and day >= 1 and day <= 31:
            return True
        
        elif month == 4 and day >= 1 and day <= 30:
            return True
        
        elif month == 5 and day >= 1 and day <= 31:
            return True
        
        elif month == 6 and day >= 1 and day <= 30:
            return True
        
        elif month == 7 and day >= 1 and day <= 31:
            return True
        
        elif month == 8 and day >= 1 and day <= 31:
            return True
        
        elif month == 9 and day >= 1 and day <= 30:
            return True
        
        elif month == 10 and day >= 1 and day <= 31:
            return True
        
        elif month == 11 and day >= 1 and day <= 30:
            return True
        
        elif month == 12 and day >= 1 and day <= 31:
            return True
        
    
def FechaD(fecha):
    
    d, m, a = [], [], []
    
    c = 0
    
    for n in fecha:
        if n != "-":
            if c == 0:
                d.append(n)
                
            elif c == 1:
                m.append(n)
                
            elif c == 2:
                a.append(n)
                
        else:
            c += 1
            
        
    day = int("".join(d))
    month = int("".join(m))
    year = int("".join(a))
    
    return [day, month, year]
    
    
    
     
    
    
    
    