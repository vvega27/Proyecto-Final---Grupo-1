#Estudiantes
#Bryan Orozco Rojas 
#Valeria Vega Madrigal
#Jafeth


from turtle import delay
import time
import os

file=open("listaEmpleados.txt","a")
file=open("listaClientes.txt","a")
file=open("listaProvedores.txt","a")
file=open("listaProductos.txt","a")
file=open("listaVentas.txt","a")
file=open("listaAvis","a")
file=open("listaAmerican","a")
file=open("listaTica","a")
file=open("listaAirCanada","a")

ListaEmpleados=['Bryan','Valeria','Jafet','Anderson']
ListaCedula=[304920966,128376533,4653912873,652730165]
Salario=[2000,1500,1000,850]
Puesto=['Presidente','Vicepresidenta','tesorero','Recepcionista']
ListaClientes=[]

print("Bievenido a la agencia de Viajes los Patitos Voladores")
i=0
while i<3:
      usuario=input("Ingrese su nombre de usuario :\n")
      i=i +1
      if str(usuario)=="Bryan" or "Valeria" or "Jafet":
            print("USUARIO CORRECTO\n")
            clave=input("ingrese su clave\n")
            if str(clave)=="a":
                  print("Bienvenid@!\n")
                  break
            else:
                  print("Password incorrecto\n")
                  if    i==3:
                        print("Se agotaron sus intentos")
                        break
      else:
            print("USUARIO INCORRECTO\n")
            if    i==3:
                  print("INTENTOS AGOTADOS")

def menu():
    print("Elige una opción:\n",
          "1-Empleados.\n",
          "2-Clientes.\n",
          "3-Provedores.\n",
          "4-Productos.\n",
          "5-Ventas.\n",
          "6-Salir.\n")

    opcion = input("Escribe un número y pulsa enter: \n")
    

    if opcion == "1":

        print("Modulo de Empleados!\n")
        
        def menu1():
            
            print("Elige una opción:\n\n",
                "1-Ver empleados actuales.\n",
                "2-Modificar datos de empleados.\n",
                "3-Ingresar nuevo empleado.\n",
                "4-Salir al menu principal.\n")
            op1= input("Escribe un número y pulsa enter: ")
            
            
            if op1=="1":
                print("Los colaboradores actuales son los siguientes\n")
                for x in ListaEmpleados:
                    print (x)
                time.sleep(3)
            
                return menu1()


            elif op1=="2":
                NomEmpleado=input(" Digite el nombre del empleado al que desea modificar los datos: ")
                if NomEmpleado in ListaEmpleados:
                    print("Los datos del empleado",NomEmpleado,"Son los siguientes:")
                    

                else:
                    print("El nombre digitado no se encuentra en la base de datos ")
                
                return menu1()

            elif op1=="3":
                AgregarEmpleado=input(print(" Digite el nombre del colaborador que desea Agregar a la lista"))
                
                
                Cedula=input(print("Digite el numero de cedula"))
                
                hora=input(print("Digite el salario por hora que ganara",AgregarEmpleado))
                
                trabajo=input(print("Ingrese el puesto que tendra ",AgregarEmpleado))
                
                ListaEmpleados.append(AgregarEmpleado)
                ListaCedula.append(Cedula)
                Salario.append(hora)
                Puesto.append(trabajo)
                print("El Colaborador",AgregarEmpleado,"con la cedula",Cedula," ganara un salario de ",hora, "por hora, en el puesto de ",Puesto, " ha sido agregado con exito")
                
                for valor_a, valor_b, valor_c, valor_d in zip(ListaEmpleados, ListaCedula, Salario, Puesto): 
	                print("Empleado: ",valor_a, "Cedula de identidad :",valor_b, "con salario de ",valor_c, " colones por hora en el puesto de:",valor_d, "ha sido agregado con exito ")
                  
                return menu1()
            
            elif op1=="4":
                print("Volviendo al menu principal")
                return menu()
        menu1()

    elif opcion == "2":
        
        print("Modulo de Clientes!\n")
        
        def menu2():

            print("Elige una opción:\n\n",
                "1-Ver clientes registrados.\n",
                "2-Ingresar nuevo Cliente.\n",
                "3-Salir al menu principal.\n")
            op2= int(input("Escribe un número y pulsa enter: "))
         
        
            if op2 == 1:

                def mostrarinfo():
                    
                    file=open("listaClientes.txt","r")
                    clientes=file.read()
                    print("Los clientes actuales son los siguientes: \n",clientes)
                    file.close()

                mostrarinfo()
                print("Volviendo a Menu")
                time.sleep(3)
                return menu2()
            
                    
            elif op2== 2:

                def crearTxt():

                    file=open("listaClientes.txt","a")
                    print("Edicion Habilitada")
                    file.close()
                crearTxt()

                def agregarCliente():
                
                    nombreb=str(input("Ingrese su nombre: "))
                    apellido1b=str(input("Ingrese su primer apellido: "))
                    apellido2b=str(input("Ingrese su segundo apellido: "))
                    cedulab=str(input("Ingrese su cedula: "))
                    telefonob=str(input("Ingrese su telefono: "))
                    direccionb=str(input("Ingrese su direccion: "))

                    file=open("listaClientes.txt","a")
                    file.write("El nombre del cliente es: ")
                    file.write(nombreb)
                    file.write("\n")
                    file.write("El primer apellido del cliente es: ")
                    file.write(apellido1b)
                    file.write("\n")
                    file.write("El segundo apellido del cliente es: ")
                    file.write(apellido2b)
                    file.write("\n")
                    file.write("La cedula del cliente es: ")
                    file.write(cedulab)
                    file.write("\n")
                    file.write("El telefono del cliente es: ")
                    file.write(telefonob)
                    file.write("\n")
                    file.write("La direccion del cliente es: ")
                    file.write(direccionb)
                    file.write("\n")
                    print("Informacion almacenada con exito")

                    file.close()
                agregarCliente()
                menu2()
                    
                
            elif op2== 3:
                print("Volviendo al menu principal")
                return menu()

        menu2()
            
                
    elif opcion == "3":
        
        print("Modulo de Proovedores")
        
        def menu3():

            print("Elige una opción:\n\n",
                "1-Ver provedores de la empresa.\n",
                "2-Salir al menu principal.\n")
            op3= int(input("Escribe un número y pulsa enter: "))
         
        
            if op3 == 1:

                def mostrarinfo():
                    
                    file=open("listaProvedores.txt","r")
                    provedores=file.read()
                    print("Los Provedores actuales son los siguientes: \n",provedores)
                    file.close()

                mostrarinfo()
                print("Volviendo a Menu")
                time.sleep(3)
                return menu3()


            if op3 == 2: 

                print("Volviendo al menu principal")
                return menu()
                
        menu3()

    elif opcion == "4":
        
        print("Modulo de Productos")

        def menu4():

            print("Elige una opción:\n\n",
                 "1-Ver .\n",
                 "2-Ver .\n",
                 "3-Ver .\n",
                 "4-Salir al menu principal.\n")
            op4= int(input("Escribe un número y pulsa enter: "))
       
        
            if op4 == 1:

             print("in progress")
             print(ListaClientes)
             

            elif op4== 2:

             print("in progress")
             

            elif op4== 3:

             print("in progress")
             

            elif op4== 4:

             print("Volviendo al menu principal")
             return menu()
        menu4()

    elif opcion == "5":
        
        print("Modulo de Ventas")
        

        def menu5():

            print("Elige una opción:\n\n",
                "1-Ingresar Ventas.\n",
                "2-Consultar Ventas.\n",
                "3-Ver lista de ventas.\n",
                "4-Salir al menu principal.\n")
            op5 = int(input("Escribe un número y pulsa enter: "))
        
        
            if op5 == 1:
             

             print("in progress")
             

            elif op5 == 2:

              print("in progress")
             

            elif op5 == 3:

             print("in progress")
             

            elif op5 == 4:
             print("Volviendo al menu principal")
             return menu()
            
        menu5()
        
    elif opcion == "6":
     print("Finalizando Programa")
     exit

    else:
     print("No has introducido una opción válida.\n")
    return menu()

menu()

