import vfechas


def Calcular(list2, data):
    
    lista2, lista3, lista4 = [], [], []    
        
    for n3 in list2:
        lista2.append(n3[-1])
        lista3.append(n3[1])
        lista4.append(n3[0])
            
        
                 
    lista2 = list(set(lista2))
    lista3 = list(set(lista3))
    lista4 = list(set(lista4))
            
    lista2.sort(), lista3.sort(), lista4.sort()
        
     
    for n4 in lista2:
        print(f"\n-----------Año {n4}----------------------------\n")
        
            
        for n5 in lista3:
                
            for n6 in lista4:
                    
                for n7, t in data.items():
                    if n4 == vfechas.FechaD(t[0])[-1] and n5 == vfechas.FechaD(t[0])[1] and n6 == vfechas.FechaD(t[0])[0]:
                        x = f'{n7}, {t[0]}, {"{:,}".format(int(t[1])) + "$"}'
                        print(f"{x}\n")
                            
    input("\nPresiona enter para continuar...")