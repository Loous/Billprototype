import sqlite3
import os

import banners


class MostrarFacturas:
        
    def MostrarUF(self):
        
        os.system('cls')
        banners.MostrarTF()
        
        x = sqlite3.connect("facturas.db")
        cursorObj = x.cursor()
        
        k = cursorObj.execute("SELECT name, date, total FROM rfacturas")
        
        k2 = k.fetchall()
        
        if len(k2) > 0:

            for n in k2:
                print(f"{n[0]} {n[1]} {'{:,}'.format(int(n[2]))}$\n")
                
            input("Presiona enter para continuar...")
            
        else:
            input("Aún no hay facturas registradas, presiona enter para continuar...")
            
            
                    
                    
if __name__ == "__main__":
    MostrarFacturas().MostrarUF()
    
    
    
    
    
    
    
    