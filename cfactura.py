import sqlite3
import os
import banners


class TotalFacturas:    
        
    def MostrarFacturasT(self):
        
        
        
        x = sqlite3.connect("facturas.db")
        cursorObj = x.cursor()
        
        k = cursorObj.execute("SELECT total FROM rfacturas")
        
        c = 0
        c2 = 0
        
        for n in k.fetchall():
            for n2 in n:
                c += int(n2)
                c2 += 1
                
        os.system('cls')
        banners.DineroFacturas(c2, c)
        
        input("Presiona enter para continuar...")
                
              
if __name__ == "__main__":
    TotalFacturas().MostrarFacturasT()
    
      
    
    
    