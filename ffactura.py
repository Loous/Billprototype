import sqlite3, os
import vfactura, vfechas, banners
import fffacturaf

class FechasFacturas:
    def __init__(self):
        
        self._option = ["x", "X"]
        
        
    def FacturaF(self):
        while True:
            os.system('cls')
            banners.FechasFactura(option="x")
            
            f = input("\nIngresa la fecha de la factura: ")
            
            if f in self._option:
                break
            
            
            if vfactura.ValidarFacturaD(f):
                input("\nLa fecha es incorrecta, presiona enter para continuar...")
                
            else:
                self.FacturaB(f)
                break
                
            
            
    def FacturaB(self, date):
        
        x = sqlite3.connect("facturas.db")
        cursorObj = x.cursor()
        
        k = cursorObj.execute(f"SELECT name, date, total FROM rfacturas where date = '{date}'")
        k = k.fetchall()
        
        if len(k) == 0:
            input("\nLa fecha ingresada no se encuentra en la lista de facturas, presiona enter para continuar...")
            
        else:
        
            if len(k) > 1:
                
                c = 1
                
                for n in k:
                    print(f"\nFactura{c}: {n[0]} {n[1]} {'{:,}'.format(int(n[2]))}$")
                    c += 1
                    
                
                
            else:
            
                k2 = f"{k[0][0]} {k[0][1]} {'{:,}'.format(int(k[0][2]))}"
                
                os.system('cls')
                
                banners.FechasFactura(option="v", values=k2)
                
            input("\n\nPresiona enter para continuar...")
                
            
            
            
        
    def FacturasOPF(self):
        
        os.system('cls')
        banners.FechasFactura(option="f")
        
        x = sqlite3.connect("facturas.db")
        cursorObj = x.cursor()
        
        k = cursorObj.execute(f"SELECT name, date, total FROM rfacturas")
        
        datos = {}
        
        for n in k.fetchall():
            datos[n[0]] = [n[1], n[2]]
            
            
        lista = []
            
        for n2, t in datos.items():
            lista.append(vfechas.FechaD(t[0]))
            
        fffacturaf.Calcular(lista, datos)
            
            
            
       
                            
    def MenuPrincipalFF(self):
        
        try:
        
            while True:
                os.system('cls')
                banners.FechasFactura()
                
                x = input("Ingresa una opción: ")
                
                if x == "1":
                    self.FacturaF()
                    
                elif x == "2":
                    self.FacturasOPF()
                    
                elif x == "3":
                    break
                
                else:
                    input("\nLa opción ingresada no se encuentra en la lista de opciones disponibles, presiona enter para continuar...")
                
        except KeyboardInterrupt:
            os.system('cls')
            
            
if __name__ == "__main__":
    FechasFacturas().MenuPrincipalFF()
            
            

    
    
    
    
    