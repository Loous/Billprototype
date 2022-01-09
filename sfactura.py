import sqlite3
import os


import banners
import vfactura

class BuscarFactura:
    def __init__(self):
        
        self._option = ["x", "X"]
        
        
    def FacturaB(self):
        while True:
            os.system('cls')
            banners.BuscarFactura()
            
            n = input("Ingresa el nombre de la factura a buscar: ")
            
            if n in self._option:
                break
                
            
            if vfactura.ValidarFacturaN(n):
                input("\nEl nombre de factura ingresado es incorrecto, presiona enter para continuar...")
                
            else:
                self.NombreFactura(n)
                break
                
            
    def NombreFactura(self, name):
        x = sqlite3.connect("facturas.db")
        cursoObj = x.cursor()
        
        k = cursoObj.execute(f"SELECT name, date, total FROM rfacturas where name = '{name}'")
        
        k2 = k.fetchall()
        
        if len(k2) == 0:
            input("\nLa factura no se encuentra registrada, presiona enter para continuar...")
            self.FacturaB()
            
        else:
            os.system('cls')
            
            k3 = k2[0]
            banners.BuscarFactura(k3)
            
            p = input("Presiona enter para buscar otra factura, o presiona (s) para salir: ").lower()
            
            if p != "s":
                self.FacturaB()
                
                
            
    def MenuPrincipalBuscarF(self):
        
        try:
        
            self.FacturaB()
            
        except KeyboardInterrupt:
            os.system('cls')
            
            
if __name__ == "__main__":
    BuscarFactura().MenuPrincipalBuscarF()
            
            
            
            
            
            

            
        
     
            
            
            







            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
            
            
            
            
            
            
            
        
            
            
            
        
        
        
        
        
        
        
            
            
            
            
            
            
                
                
                
                
                
            
            
            
        
        
        
        
        
    
        
        
    
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    