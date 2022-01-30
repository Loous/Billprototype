import sqlite3
import os

import banners
import vfactura


class EliminarFactura:
    def __init__(self):
        
        self._facturaUsuario = []
        
        
    def NombreFactura(self):
        while True:
            os.system('cls')
            banners.EliminarFactura()
            
            n = input("Ingrese el nombre de la factura a eliminar: ")
            
            if n in ["x", "X"]:
                break
            
            if vfactura.ValidarFacturaN(n):
                input("\nEl nombre de la factura es incorrecto, presiona enter para continuar...")
                
            else:
                self.FacturaUsuarioE(n)
                break
                
            
            
    def FacturaUsuarioE(self, name):
        x = sqlite3.connect("facturas.db")
        cursorObj = x.cursor()
        
        k = cursorObj.execute(f"SELECT name FROM rfacturas where name = '{name}'")
        
        
        if len(k.fetchall()) > 0:
            os.system('cls')
            self.NombreFacturaB(name)
            
            t = input("\nPresione enter para confirmar o presione (c) para cancelar: ").lower()
            
            if t == "c":
                self.NombreFactura()
                
            else:
                cursorObj.execute(f"DELETE FROM rfacturas where name = '{name}'")
                x.commit()
                
                p = input("\nFactura eliminada con éxito, presiona enter para salir o (c) para eliminar otra factura: ").lower()
                
                if p == "c":
                    self.NombreFactura()
                
                
            
        else:
            input("\nLa factura ingresada no se encuentra registrada, presiona enter para continuar...")
            self.NombreFactura()
            
        x.close()
            
            
    def NombreFacturaB(self, name):
        x = sqlite3.connect("facturas.db")
        cursoObj = x.cursor()
        
        k = cursoObj.execute(f"SELECT name, date, total FROM rfacturas where name = '{name}'")
        
        k2 = k.fetchall()[0]
        
        banners.EliminarFactura(k2)
        
        
    def MenuPrincipalEF(self):
        
        try:
        
            self.NombreFactura()
            
        except KeyboardInterrupt:
            os.system('cls')
            
            
if __name__ == "__main__":
    EliminarFactura().MenuPrincipalEF()
            
        
        
    
    
    
    
    
    