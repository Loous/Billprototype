import registroylogin
import factura
import efactura
import dfactura
import sfactura
import mfactura
import cfactura
import ffactura


import sqlite3
import os

import banners




class FacturasInterfaz:
    def __init__(self):
        
        self._facturaUsuario = []
        self._loginUsuario = True
        
        
    def CrearTablaRYL(self):
        x = sqlite3.connect("users.db")
        cursorObj = x.cursor()
        cursorObj.execute("CREATE TABLE if not exists usuarios(name, password)")
        x.close()
        
    def CrearTablaFacturas(self):
        x = sqlite3.connect("facturas.db")
        cursorObj = x.cursor()
        cursorObj.execute("CREATE TABLE if not exists rfacturas(name, date, total)")
        x.close()
    
        
        
    def Menu(self):
        self.CrearTablaRYL()
        self.CrearTablaFacturas()
        
        try:
            
            
            while True:
                os.system('cls')
                
                if self._loginUsuario:
                    if registroylogin.RegistroYLogin().MenuPrincipalFacturas():
                        self._loginUsuario = False
                        
                    else:
                        break
                        
                          
        
                else:
                    
                    os.system('cls')
                    banners.menuPrincipal()
                    
                    x = input("Ingresa una opción: ")
                    
                    if x == "1":
                        factura.Facturas().MenuPrincipalFactura()
                        
                    elif x == "2":
                        efactura.EditarFactura().MenuPrincipalFacturaE()
                        
                    elif x == "3":
                        dfactura.EliminarFactura().MenuPrincipalEF()
                        
                    elif x == "4":
                        sfactura.BuscarFactura().MenuPrincipalBuscarF()
                        
                    elif x == "5":
                        mfactura.MostrarFacturas().MostrarUF()
                        
                    elif x == "7":
                        cfactura.TotalFacturas().MostrarFacturasT()
                        
                    elif x == "8":
                        ffactura.FechasFacturas().MenuPrincipalFF()
                        
                    elif x == "6":
                        break
                    
                    else:
                        input("\nLa opción ingresada no se encuentra en la lista de opciones disponibles, presiona enter para continuar...")
                        
                        
                        
        except KeyboardInterrupt:
            os.system('cls')
            
            
if __name__ == "__main__":
    FacturasInterfaz().Menu()
    
                        
            
            
            
            
                

                
                

                
                
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
   
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
    
        
        
        
        
        
        
        
        



        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    