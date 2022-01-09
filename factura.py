import sqlite3
import os

import vfechas
import banners
import vfactura

class Facturas:
    def __init__(self):
        
        self._billName = ""
        self._value = False
        
            
        
    def FacturaNombre(self):
        while True:
            os.system('cls')
            banners.IngresarFactura()
            
            n = input("Ingresa el nombre de la factura: ")
            
            if self.EditarCF(n, "s"):
                return True
                
            
            if vfactura.ValidarFacturaN(n):
                input("\nEl nombre ha ingresar debe tener como mínimo 5 caracteres y máximo 100, presiona enter para continuar...")
                
            elif self.ValidarNombreF(n):
                input("\nEl nombre de factura que desea ingresar ya se encuentra registrado, presiona enter para continuar...")
                
            else:
                self._billName = n
                
                self.FacturaFecha(self._billName)
                break
            
            
            
            
    def ValidarNombreF(self, name):
        x = sqlite3.connect("facturas.db")
        cursoObj = x.cursor()
        
        k = cursoObj.execute(f"SELECT name FROM rfacturas where name = '{name}'")
        
        if len(k.fetchall()) > 0:
            return True
        
        
        x.close()
        
        
        
    def EditarCF(self, option, value):
        if option in ["x", "X"] and value == "x":
            return True
        
        if option in ["s", "S"] and value == "s":
            return True
        
                
                
    def FacturaFecha(self, name):
        while True:
            os.system('cls')
            banners.IngresarFactura()
            
            f = input("Ingresa la fecha de la factura: ")
            if self.EditarCF(f, "x"):
                self.FacturaNombre()
                break
            
            if vfactura.ValidarFacturaD(f):
                input("""
Fecha no válida, el formato de fecha debe ser como este: dd-mm-aaaa, presiona enter para continuar...""")
                
            else:
                if vfechas.ValidarFechas(f):
                    self.FacturaTotal(name, f)
                    break
                
                
            
    def FacturaTotal(self, name, date):
        while True:
            os.system('cls')
            banners.IngresarFactura()
            
            t = input("Ingresa el total de la factura: ")
            if self.EditarCF(t, "x"):
                self.FacturaFecha(self._billName)
                break
            
            if vfactura.ValidarFacturaT(t):
                input("\nSolo puedes ingresar números enteros, presiona enter para continuar...")
                
            else:
                self.InsertarTabla(name, date, t)
                break
                
            
            
    def InsertarTabla(self, name, date, total):
        x = sqlite3.connect("facturas.db")
        cursoObj = x.cursor()
        
        cursoObj.execute(f"INSERT INTO rfacturas VALUES('{name}', '{date}', '{total}')")
        x.commit()
        
        k = input("""
Factura registrada con éxito, presiona enter para ingresar otra factura o presiona (s)
para volver al menú principal: """)
        
        if self.EditarCF(k, "s"):
            self._value = True
            
        
        
        x.close()
        
        
    def MenuPrincipalFactura(self):
        
        try:
        
            while True:
                
                if self.FacturaNombre() or self._value:
                    break
                    
        except KeyboardInterrupt:
            os.system('cls')
           
           
if __name__ == "__main__":
    Facturas().MenuPrincipalFactura()
    
    
    
    

    
    
    
    
    
    
    
           
           
           
           
           
           
           
           
           
           
           
           

    
           
           
            
            

            
            
            
            
            
            
            
            
            
        
            
        















        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
    
        
        
        
        
        
        
        
        
    
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        