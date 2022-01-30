import sqlite3
import os

import banners
import vfechas
import vfactura

class EditarFactura:
    def __init__(self):
        
        self._BillN = ""
        self._options = ["x", "X"]
        self._billU = ""
        
            
        
    def NombreFactura(self):
        while True:
            os.system('cls')
            banners.EditarFactura()
            
            n = input("Ingresa el nombre de la factura a editar: ")
            
            if n in self._options:
                break
            
            
            if self.NombreFacturaB(n):
                input("\nEl nombre ingresado no se encuentra registrado, presiona enter para continuar...")
                
            else:
                self._BillN = n
                self.OpcionFactura()
                break
            
            
            
    def NombreFacturaB(self, name):
        x = sqlite3.connect("facturas.db")
        cursoObj = x.cursor()
        
        k = cursoObj.execute(f"SELECT name FROM rfacturas where name = '{name}'")
        
        if len(k.fetchall()) == 0:
            return True
        
        x.close()
        
        
        
    def NombreFacturaV(self, name):
        x = sqlite3.connect("facturas.db")
        cursorObj = x.cursor()
        
        k = cursorObj.execute(f"SELECT name from rfacturas where name = '{name}'")
        
        if len(k.fetchall()) > 0:
            return True
        
        x.close()
        
                
        
    def FacturaN(self):
        x = sqlite3.connect("facturas.db")
        cursoObj = x.cursor()
        
        k = cursoObj.execute(f"SELECT name, date, total FROM rfacturas where name = '{self._BillN}'")
        
        self._billU = k.fetchall()[0]
        
        
        
    def OpcionFactura(self):
        
        
        while True:
            self.FacturaN()
            os.system('cls')
            
            
            banners.EditarFactura(self._billU)
            
            x = input("Elige un campo a editar: ")
            
            if x in ["1", "2", "3"]:
                os.system('cls')
                banners.EditarFactura(self._billU, "x")
                
            
            if x == "1":
                self.FacturaCN(self._BillN)
                
            elif x == "2":
                self.FacturaCD(self._BillN)
                
            elif x == "3":
                self.FacturaCT(self._BillN)
                
            elif x == "4":
                break
            
            else:
                input("\nLa opción ingresada no se encuentra en la lista de opciones disponibles, presiona enter para continuar...")
                
                
            
    def FacturaCN(self, name):
        while True:
            os.system('cls')
            banners.EditarFactura(self._billU, "x")
            
            
            n = input("\nIngresa el nuevo nombre de la factura: ")
            
            if n in self._options:
                break
                
            
            if vfactura.ValidarFacturaN(n):
                input("\nEl nuevo nombre de factura es incorrecto, presiona enter para continuar...")
                
            else:
                if self.NombreFacturaV(n):
                    input("\nEl nombre que desea ingresar ya se encuentra registrado, presiona enter para continuar...")
                    
                else:
                    self._BillN = n
                    self.ActualizarCampo("name", n, name)
                    break
            
            
            
    def FacturaCD(self, name):
        while True:
            os.system('cls')
            banners.EditarFactura(self._billU, "x")
            
            
            f = input("\nIngrese la nueva fecha: ")
            
            if f in self._options:
                break
            
            
            if vfactura.ValidarFacturaD(f):
                input("\nLa fecha ingresada es incorrecta, presiona enter para continuar...")
                
            else:
                if vfechas.ValidarFechas(f):
                    self.ActualizarCampo("date", f, name)
                    break
                
                
                
            
            
    def FacturaCT(self, name):
        while True:
            os.system('cls')
            banners.EditarFactura(self._billU, "x")
            
            t = input("\nIngresa el nuevo total: ")
            
            if t in self._options:
                break
                
            
            if vfactura.ValidarFacturaT(t):
                input("\nEl valor ingresado es incorrecto, presiona enter para continuar...")
                
            else:
                self.ActualizarCampo("total", t, name)
                break
            
            
    def ActualizarCampo(self, field, newfield, name):
        x = sqlite3.connect("facturas.db")
        cursorObj = x.cursor()
        
        cursorObj.execute(f"UPDATE rfacturas SET {field} = '{newfield}' where name = '{name}'")
        x.commit()
        x.close()
        
        
        
    def MenuPrincipalFacturaE(self):
        
        try:
        
            self.NombreFactura()
            
        except KeyboardInterrupt:
            os.system('cls')
            
            
if __name__ == "__main__":
    EditarFactura().MenuPrincipalFacturaE()
            
            
             
    
    
    
    