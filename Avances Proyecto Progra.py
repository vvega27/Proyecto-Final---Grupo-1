#Estudiantes
#Bryan Orozco Rojas 
#Valeria Vega Madrigal


i=0
while i<3:
      usuario=input("ingrese su nombre de usuario :\n")
      i=i +1
      if str(usuario)=="Bryan" or "Vale" or "Jafet" or "Anderson":
            print("USUARIO CORRECTO\n")
            clave=input("ingrese su clave\n")
            if str(clave)=="1234":
                  print("Bienvenido Bryan\n")
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

    opcion = input("Escribe un número y pulsa enter: ")

    if opcion == "1":
        
        def menu1():
            
            print("Elige una opción:\n\n",
                "1-Ver empleados actuales.\n",
                "2-Modificar datos de empleados.\n",
                "3-Ingresar nuevo empleado.\n",
                "4-Salir.\n")

            op1= input("Escribe un número y pulsa enter: ")
            ListaEmpleados=['Bryan','Valeria','Jafet','Anderson']
            
            if op1=="1":
                print("Los colaboradores actuales son los siguientes",ListaEmpleados)


            elif op1=="2":
                print(ListaEmpleados)
                print(" Digite el nombre que desea agregar: ")
                AgregarEmpleado=input()
                print("El nombre a agregar es el siguiente: ",AgregarEmpleado)
                ListaEmpleados.append(AgregarEmpleado)
                print(ListaEmpleados)

            elif op1=="3":
                print(ListaEmpleados)
                print(" Digite el nombre que desea agregar: ")
                AgregarEmpleado=input()
                print("El nombre a agregar es el siguiente: ",AgregarEmpleado)
                ListaEmpleados.append(AgregarEmpleado)
                print(ListaEmpleados)
            
            elif op1=="4":
                print("Salistes del programa satisfactoriamente.")


if opcion =="2":

        def menu2():

            print("Elige una opcion:\n")
                  
                

        menu1()


    elif opcion == "2":
        print()

    elif opcion == "3":
        print()

    elif opcion == "4":
        print()

    elif opcion == "5":
        print()
    
    elif opcion == "6":
        print("Finalizando programa")
        exit

    else:
        print("No has introducido una opción válida.\n Cerrando programa")
menu()

