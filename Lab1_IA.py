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

    #verificar en que habitacion se encuentra la camara
    if depart_ingreso == 'departamentos1':
        #mensaje de ubicacion  de la camara
        print("La camara se encuentra en el departamento 1" )
        #caso en que el departamento registre una termperatura alta
        if temp_ingreso == '1':
            #mensaje de alerta
            print("Se ha registrado una temperatura alta dentro del departamento 1.")
            #activar el sistema de enfriamiento
            objetivo['departamento1'] = '0'
            #incremento del costo por el funcionamiento
            costo += 1
            #mensaje de la solución y aumento del costo
            print("Temperatura del departamento establecida en baja.")
            print("Costo actual: "+str(costo))

            
            

