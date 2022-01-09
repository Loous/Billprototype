import sqlite3
import re
import random
import os

import banners

class RegistroYLogin:
    def __init__(self):
        
        self._userNameValidate = re.compile("^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9]{5,20}$")
        self._userPasswdValidate = re.compile("^[A-Za-zÁÉÍÓÚáéíóúñÑ0-9]{4,30}$")
        self._login = False
        
    
        
    def Registrarse(self):
        
        continuar = True
        
        while continuar:
            os.system('cls')
            banners.registrarse()
            
            n = input("Crea un nombre de usuario: ")
            if self.volverAlMenu(n):
                break
            
            elif self._userNameValidate.match(n) == None:
                input("\nEl nombre de usuario debe tener como mínimo 5 caracteres y máximo 20, presiona enter para continuar...")
                
                
            else:
                continuar = False
                
                while True:
                    os.system('cls')
                    banners.registrarse()
                    
                    p = input("Crea una contraseña: ")
                    if self.volverAlMenu(p):
                        break
                    
                    elif self._userPasswdValidate.match(p) == None:
                        input("\nLa contraseña debe tener mínimo 4 caracteres y máximo 30, presiona enter para continuar...")
        
                        
                    else:
                        self.InsertarTabla(n, p)
                        break
                    
                    
                    
                    
    def volverAlMenu(self, option):
        if option in ["x", "X"]:
            return True
            
            
                    
    def InsertarTabla(self, name, password):
        x = sqlite3.connect("users.db")
        cursorObj = x.cursor()
        
        k = cursorObj.execute(f"SELECT name FROM usuarios where name = '{name}'")
        
        if len(k.fetchall()) > 0:
            
            input(f"""
                  
                                El nombre que desea ingresar ya se encuentra en uso,
                                ingrese un nombre de usuario diferente, por ejemplo: {name}{random.randint(0, 10000)},
                                presiona enter para continuar...""")
            
        else:
            cursorObj.execute(f"INSERT INTO usuarios VALUES('{name}', '{password}')")
            x.commit()
            input("\nTe has registrado correctamente, presiona enter para continuar...")
            
            
            
        x.close()
        
        
                
    def IniciarSession(self):
        while True:
            os.system('cls')
            banners.iniciarSession()
            
            n = input("Ingresa tu nombre de usuario: ")
            if self.volverAlMenu(n):
                break
            
            p = input("\nIngresa tu contraseña: ")
            if self.volverAlMenu(p):
                break
            
            if self.SessionUsuario(n, p):
                break
        
        
            
            
    def SessionUsuario(self, name, password):
        x = sqlite3.connect("users.db")
        cursoObj = x.cursor()
        k = cursoObj.execute(f"SELECT password from usuarios where name = '{name}'")
        k2 = k.fetchall()
        
        if len(k2) > 0:
            if password == k2[0][0]:
                input("\nHas iniciado sessión correctamente, presiona enter para continuar...")
                self._login = True
                return True
            
            else:
                input("\nEl usuario o contraseña es incorrecto, presiona enter para continuar...")
                
            
            
            
                
        else:
            input("\nEl usuario o contraseña es incorrecto, presiona enter para continuar...")
            
        x.close()
        
            
            
            
            
    def MenuPrincipalFacturas(self):
        
        try:
        
            while True:
                if self._login:
                    return True
                
                else:
                    os.system('cls')
                    banners.facturas()   
                    
                    x = input("Ingresa una opción: ")
                    
                    if x == "1":
                        self.IniciarSession()
                        
                    elif x == "2":
                        self.Registrarse()
                        
                    elif x == "3":
                        return False
                    
                    else:
                        input("\nLa opción ingresada no se encuentra en la lista de opciones disponibles, presiona enter para continuar...")
                    
                    
                    
        except KeyboardInterrupt:
            os.system('cls')
            return False
                    


if __name__ == "__main__":
    RegistroYLogin().MenuPrincipalFacturas()
    
                
     
        
        
        




















        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        


































