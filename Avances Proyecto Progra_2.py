#Estudiantes
#Bryan Orozco Rojas 
#Valeria Vega Madrigal


from turtle import delay
import time

ListaEmpleados=['Bryan','Valeria','Jafet']
ListaClientes=['Maria Araya','Daniela Blanco','Ronaldo Arias']
CedulasClientes=['Maria Araya > 117910384','Daniela Blanco > 117910384','Ronaldo Arias > 117910384']
NumerosClientes=['Maria Araya > 88888888','Daniela Blanco > 88776655','Ronaldo Arias > 88990099']
NumerosClientes=['Maria Araya > Alajuela','Daniela Blanco > Heredia','Ronaldo Arias > Limon']
ListaProvedores=['Delta','American Airlines']
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

        menu1()

        while op1 != 0:
            
            if op1=="1":
                print("Los colaboradores actuales son los siguientes",ListaEmpleados)
                print()
                time.sleep(3)
                return menu1()


            elif op1=="2":
                print(ListaEmpleados)
                print(" Digite el nombre que desea Agregar")
                AgregarEmpleado=input()
                print("El nombre a agregar es el siguiente",AgregarEmpleado)
                ListaEmpleados.append(AgregarEmpleado)
                print(ListaEmpleados)
                return menu1()

            elif op1=="3":
                print(ListaEmpleados)
                print(" Digite el nombre que desea Agregar")
                AgregarEmpleado=input()
                print("El nombre a agregar es el siguiente",AgregarEmpleado)
                ListaEmpleados.append(AgregarEmpleado)
                print(ListaEmpleados)
                return menu1()
            
            elif op1=="4":
                print("Volviendo al menu principal")
                return menu()


    elif opcion == "2":
        
        print("Modulo de Clientes!\n")

        def menu2():

            print("Elige una opción:\n\n",
            "1-Ver clientes registados.\n",
            "2-Ingresar nuevo Cliente.\n",
            "3-Salir al menu principal.\n")

        menu2()
        
        op2= int(input("Escribe un número y pulsa enter: "))

        while op2 != 0:

            if op2 == 1:

                print("Los clientes actuales son los siguientes")
                print(ListaClientes)
                return menu2()

            elif op2== 2:

                print(ListaClientes)
                print(" Digite el nombre del cliente que desea Agregar: ")
                AgregarCliente=input()
                print("El nombre a agregar es el siguiente",AgregarCliente)
                ListaClientes.append(AgregarCliente)
                print(ListaClientes)
                print(CedulasClientes)
                print(" Digite el nombre de la cedula del cliente que desea Agregar: ")
                AgregarCedulaCliente=input()
                print("La Cedula a agregar es el siguiente",AgregarCedulaCliente)
                CedulasClientes.append(AgregarCliente)
                print(CedulasClientes)
                return menu()
                
            elif op2== 3:
                print("Volviendo al menu principal")
                return menu()

            
                
    elif opcion == "3":
        
        print("Modulo de Proovedores")
        
        def menu3():

            print("Elige una opción:\n\n",
            "1-Ver provedores de la empresa.\n",
            "2-Ver desinos transporte aereo.\n",
            "3-Ver destinos transporte terrestre.\n",
            "4-Salir al menu principal.\n")

        menu3()
        
        op3= int(input("Escribe un número y pulsa enter: "))

        while op3 != 0:

            if op3 == 1:

                print("Los provedores actuales son los siguientes")
                print(ListaProvedores)
                return menu3()
                
            elif op3== 2:

                print("in progress")
                return menu3()
              
                
            elif op3== 3:

                print("in progress")
                return menu3()
                

            elif op3== 4:
                print("Volviendo al menu principal")
                return menu()
        

    elif opcion == "4":
        
        print("Modulo de Productos")

        def menu4():

            print("Elige una opción:\n\n",
            "1-Ver .\n",
            "2-Ver .\n",
            "3-Ver .\n",
            "4-Salir al menu principal.\n")

        menu4()
        
        op4= int(input("Escribe un número y pulsa enter: "))

        while op4 != 0:

            if op4 == 1:

                print("in progress")
                print(ListaClientes)
                return menu()

            elif op4== 2:

                print("in progress")
                return menu()

            elif op4== 3:

                print("in progress")
                return menu()

            elif op4== 4:
                print("Volviendo al menu principal")
                return menu()

    elif opcion == "5":
        
        print("Modulo de Ventas")

        def menu5():

            print("Elige una opción:\n\n",
            "1-Ver .\n",
            "2-Ver .\n",
            "3-Ver .\n",
            "4-Salir al menu principal.\n")

        menu5()
        
        op5= int(input("Escribe un número y pulsa enter: "))

        while op5 != 0:

            if op5 == 1:

                print("in progress")
                return menu()

            elif op5 == 2:

                print("in progress")
                return menu()

            elif op5 == 3:

                print("in progress")
                return menu()

            elif op5 == 4:
                print("Volviendo al menu principal")
                return menu()
    
    elif opcion == "6":
        print("Finalizando Programa")
        exit

    else:
        print("No has introducido una opción válida.\n")
        return menu()

menu()
print("Bryan")