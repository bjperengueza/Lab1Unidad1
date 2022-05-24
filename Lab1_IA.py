#Instrucciones
#ingresar el departamento (ejem: departamento1)
#ingresar el estado del departamento (temperatura alta = 1 o temperatura baja = 0)
def cam_termica():
    #definir las metas que se buscan alcanzar y costo inicial
    objetivo = {'departamento1':'0', 'departamento2':'0', 'departamento3':'0', }
    costo = 0

    #ingreso de datos por el usuario
    #Ingreso del departamento donde se va a utilizar la camara 
    depart_ingreso = input("Ingrese el departamento que desee utilizar la camara termica: ")
    #ingrese el registro de la temperatura
    temp_ingreso = input("La temperatura del departamento es: ")
    nueva_temp_ingreso= input("La temperatura de otro departamentos es:")
    #objetivo a cumplir
    print("Se busca llegar a la temperatura: "+ str(objetivo))

    
