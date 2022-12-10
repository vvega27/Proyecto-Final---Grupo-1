#Estudiantes
#Bryan Orozco Rojas 
#Valeria Vega Madrigal
#Jafet


from turtle import delay
import time
import os
import sys

file=open("listaEmpleados.txt","a")
file=open("listaClientes.txt","a")
file=open("listaProvedores.txt","a")
file=open("listaProductos.txt","a")
file=open("listaVentas.txt","a")
file=open("listaAvis.txt","a")
file=open("listaAmerican.txt","a")
file=open("listaTica.txt","a")
file=open("listaAirCanada.txt","a")
file=open("listaDestinos.txt","a")
file=open("listaViajesbus.txt","a")
file=open("listaAhorro.txt","a")
file=open("listaEstancia.txt","a")
file=open("listaBuses.txt","a")
file=open("listaProductosNuevos.txt","a")
file=open("listaVentas.txt","a")

ListaEmpleados=['Bryan','Valeria','Jafet']

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
          "\n",
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
                  
                def mostrarinfo():
                    
                    file=open("listaEmpleados.txt","r")
                    empleados=file.read()
                    print("Los Empleados actuales son los siguientes: \n",empleados)
                    file.close()

                mostrarinfo()
                print("Volviendo a Menu")
                time.sleep(3)
                return menu1()

            elif op1=="2":
                NomEmpleado=input(" Digite el nombre del empleado al que desea modificar los datos: ")
                if NomEmpleado in ListaEmpleados:
                    print("Los datos del empleado",NomEmpleado,"Son los siguientes:")
                    def crearTxt():
                        file=open("listaEmpleados.txt","w")
                        print("Edicion Habilitada")
                        file.close()
                    crearTxt()

                    def editarEmpleado():
                        nombrex=str(input("Ingrese nombre del empleado: "))
                        cedulax=str(input("Ingrese la cedula del empleado: "))
                        salariox=str(input("Ingrese el salario del empleado: "))
                        puestox=str(input("Ingrese el puesto del empleado: "))

                        file=open("listaEmpleados.txt","a")
                        file.write("El nombre del empleado es: ")
                        file.write(nombrex)
                        file.write("\n")
                        file.write("La cedula del empleado es: ")
                        file.write(cedulax)
                        file.write("\n")
                        file.write("El salario del empleado es: ")
                        file.write(salariox)
                        file.write("\n")
                        file.write("El puesto del empleado es: ")
                        file.write(puestox)
                        file.write("\n")
                        print("Informacion almacenada con exito")
                        file.close()
                    editarEmpleado()

                else:
                    print("El nombre digitado no se encuentra en la base de datos ")
                
                return menu1()

            elif op1=="3":

                def agregarEmpleado():
                
                    nombree=str(input("Ingrese nombre del empleado: "))
                    cedulae=str(input("Ingrese cedula del empleado: "))
                    salarioe=str(input("Ingrese salario del empleado: "))
                    puestoe=str(input("Ingrese el nombre del puesto: "))

                    file=open("listaEmpleados.txt","a")
                    file.write("El nombre del empleado es: ")
                    file.write(nombree)
                    file.write("\n")
                    file.write("La cedula del empleado es: ")
                    file.write(cedulae)
                    file.write("\n")
                    file.write("El salario del empleado es: ")
                    file.write(salarioe)
                    file.write("\n")
                    file.write("El puesto del empleado es: ")
                    file.write(puestoe)
                    file.write("\n")
                    print("Informacion almacenada con exito")

                    file.close()
                agregarEmpleado()
                menu1()

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
                 "1-Ver Destinos.\n",
                 "2-Ver Planes de Ahorro.\n",
                 "3-Ver Lugares de Estancia.\n",
                 "4-Ver Viajes en Bus.\n",
                 "5-Ingresar un producto.\n",
                 "6-Ver Productos Ingresados.\n",
                 "7-Salir al menu principal.\n")

            op4= int(input("Escribe un número y pulsa enter: "))
       
        
            if op4 == 1:

                def mostrarinfo():
                    
                    file=open("listaDestinos.txt","r")
                    destinos=file.read()
                    print("Los destinos son los siguientes: \n",destinos)
                    file.close()

                mostrarinfo()
                print("Volviendo a Menu")
                time.sleep(3)
                return menu4()
             

            elif op4== 2:

                def mostrarinfo():
                    
                    file=open("listaAhorro.txt","r")
                    ahorro=file.read()
                    print("Los Planes de ahorro son los siguientes: \n",ahorro)
                    file.close()

                mostrarinfo()
                print("Volviendo a Menu")
                time.sleep(3)
                return menu4()
             

            elif op4== 3:

                def mostrarinfo():
                    
                    file=open("listaEstancia.txt","r")
                    estancia=file.read()
                    print("Los Planes de ahorro son los siguientes: \n",estancia)
                    file.close()

                mostrarinfo()
                print("Volviendo a Menu")
                time.sleep(3)
                return menu4()

            elif op4== 4:

                def mostrarinfo():
                    
                    file=open("listaBuses.txt","r")
                    buses=file.read()
                    print("Los Planes de ahorro son los siguientes: \n",buses)
                    file.close()

                mostrarinfo()
                print("Volviendo a Menu")
                time.sleep(3)
                return menu4()

            elif op4 == 5: 

                def crearTxt():

                    file=open("listaProductosNuevos.txt","a")
                    print("Edicion Habilitada")
                    file.close()
                crearTxt()

                def agregarProducto():
                
                    nombrex=str(input("Ingrese nombre del producto: "))
                    codigox=str(input("Ingrese codigo del producto: "))
                    descripcionx=str(input("Ingrese descripcion del producto: "))
                    fechasx=str(input("Ingrese cuando caduca el producto: "))
                    preciox=str(input("Ingrese el precio del producto: "))

                    file=open("listaProductosNuevos.txt","a")
                    file.write("El nombre del producto es: ")
                    file.write(nombrex)
                    file.write("\n")
                    file.write("El codigo del producto es: ")
                    file.write(codigox)
                    file.write("\n")
                    file.write("La descripcion del producto es: ")
                    file.write(descripcionx)
                    file.write("\n")
                    file.write("El producto es valido hasta el: ")
                    file.write(fechasx)
                    file.write("\n")
                    file.write("El precio del producto es: ")
                    file.write(preciox)
                    file.write("\n")
                    print("Informacion almacenada con exito")

                    file.close()
                agregarProducto()
                menu4()
                
            elif op4== 6:

                def mostrarinfo():
                    
                    file=open("listaProductosNuevos.txt","r")
                    productosN=file.read()
                    print("Los Productos Nuevos son los siguientes: \n",productosN)
                    file.close()

                mostrarinfo()
                print("Volviendo a Menu")
                time.sleep(3)
                return menu4()

            elif op4== 7:

             print("Volviendo al menu principal")
             return menu()
            
        menu4()

    elif opcion == "5":
        
        print("Modulo de Ventas")
        

        def menu5():

            print("Elige una opción:\n\n",
                "1-Ingresar Venta.\n",                  
                "2-Ver Ventas Ingresadas.\n",
                "3-Salir al menu principal.\n")
            
            op5 = int(input("Escribe un número y pulsa enter: "))
        
        
            if op5 == 1:

                def crearTxt():

                    file=open("listaVentas.txt","a")
                    print("Ingrese sus datos de Factura")
                    file.close()
                crearTxt()

                def agregarVenta():
                      
                    serie=str(input("Ingrese numero de la venta: "))                
                    nombrec=str(input("Ingrese nombre del comprador: "))
                    nombrev=str(input("Ingrese nombre del vendedor: "))
                    fechav=str(input("Ingrese fecha de la venta: "))
                    metodopago=str(input("Ingrese el metodo de pago: "))
                    productosadq=str(input("Ingrese los productos adquiridos: "))
                    montox=str(input("Ingrese monto facturado: "))

                    file=open("listaVentas.txt","a")
                    file.write("Numero de Venta: ")
                    file.write(serie)
                    file.write("\n")
                    file.write("Nombre del Comprador: ")
                    file.write(nombrec)
                    file.write("\n")
                    file.write("Nombre del Vendedor: ")
                    file.write(nombrev)
                    file.write("\n")
                    file.write("Fecha: ")
                    file.write(fechav)
                    file.write("\n")
                    file.write("Metodo de pago: ")
                    file.write(metodopago)
                    file.write("\n")
                    file.write("Producto Adquirido: ")
                    file.write(productosadq)
                    file.write("\n")
                    file.write("Monto total: ")
                    file.write(montox)
                    file.write("\n")
                    print("Informacion de Factura Almacena con exito. \n")

                    file.close()
                agregarVenta()
                menu5()
             
             

            elif op5 == 2:

                def mostrarinfo():
                    
                    file=open("listaVentas.txt","r")
                    ventasgeneral=file.read()
                    print("Lista de Ventas realizadas: \n",ventasgeneral)
                    file.close()

                mostrarinfo()
                print("Volviendo a Menu")
                time.sleep(3)
                return menu5()

            elif op5 == 3:
             print("Volviendo al menu principal")
             return menu()
            
        menu5()
        
    elif opcion == "6":
     print("Finalizando Programa")
     sys.exit

    else:
     print("No has introducido una opción válida.\n")
     return menu()

menu()

