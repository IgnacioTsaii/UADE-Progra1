def LeerArch():
    try:
        arch=open("apellidos.txt","rt", encoding="UTF8")  #realizamos la lectura del arc "apellidos"
        arch1=open("ARMENIA.txt","wt", encoding="UTF8") #generamos los archivos correspondientes
        arch2=open("ITALIA.txt","wt", encoding="UTF8")
        arch3=open("ESPAÑA.txt","wt", encoding="UTF8")
        linea=arch.readline() #leemos c/linea del archivo original
        while linea: 
            #linea=linea.replace("\n","") 
            if linea.upper().find("IAN,")!=-1:
                arch1.write(linea.title()+"\n") # escribe en el arch1 -> ARMENIA
            elif linea.upper().find("INI,")!=-1: 
                arch2.write(linea.title()+"\n") # escribe en el archivo ->ITALIA
            elif linea.upper().find("EZ,")!=-1:
                arch3.write(linea.title()+"\n") # escribe en el archivo -> ESPAÑA
            else:
                print("Descatar-->",linea)      #decartamos Smith john y Mili  Jose
            
            linea=arch.readline()
    except OSError:
        print("No se puede crear el archivo")
    finally: 
        try:  #Realizamos el cierre de todos los archivos, dentro de un bloque protegido           
            arch.close()
            arch1.close()
            arch2.close()
            arch3.close()
        except:
            pass
LeerArch() 