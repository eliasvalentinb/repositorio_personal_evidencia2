"""
Desarrollar en Python un módulo que gestione una agenda telefónica en un diccionario de Python utilizando 
los recursos ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para 
cada uno de estos casos:
Mostrar al usuario un menú de opciones
Opción 1: Agregar una persona (apellido, nombre, dni, email y número de teléfono). Esta opción debe a
gregar al diccionario a la persona que el usuario ingrese
Opción 2: Modificar una persona: dado su dni debe buscar la persona y preguntar si desea cambiar 
los demás campos de la persona, cambiando los que quiera.
Opción 3: Eliminar una persona del diccionario. Elimina según el DNI
Opción 4: Mostrar todos la agenda
Opción 5: Salir
"""
# Importamos el módulo 'time' para imprimir las opciones de forma más ordenada
import time
# Variable para controlar el bucle
continuar = True
# Diccionario donde se almacenarán los datos de los contactos
my_dict = {}
while continuar:
    print("¡Bienvenido a tu agenda!")
    print("-" * 25)
    time.sleep(0.2)
    print("1 Para agregar un nuevo contacto.")
    time.sleep(0.2)
    print("2 Para modificar un contacto.")
    time.sleep(0.2)
    print("3 Para eliminar un contacto.")
    time.sleep(0.2)
    print("4 Para mostrar la agenda completa.")
    time.sleep(0.2)
    print("5 Para salir.")
    time.sleep(0.5)

    options = (input("Ingresá una opción: "))
    if options == "1":
        nombre = input("Ingrese el nombre del nuevo contacto: ").capitalize()
        apellido = input("Ingrese el apellido del nuevo contacto: ").capitalize()
        dni = int(input("Ingrese el DNI del nuevo contacto: "))
        # Se ponen condiciones en ciertos puntos para que los datos sean más exactos.
        while True:
            email = input("Ingrese el email del nuevo contacto: ")
            if "@" not in email:
                print("Ingrese una dirección de correo válida.")
                continue
            else: 
                break
        while True:
            numero = int(input("Ingrese el número del nuevo contacto: "))
            if numero < 10:
                print("El número debe tener al menos diez dígitos.")
                continue
            else: 
                break

        my_dict[dni] = {"Nombre": nombre, "Apellido": apellido, "Email": email, "Número de teléfono": numero }
        print("Contacto agregado correctamente.")

#Para modificar utilizamos como clave el dni para identificar el contacto a modificar
    elif options == "2":
        dni = input("Ingrese el DNI (sin puntos) del contacto que desea modificar: ")
        print("Estos son los datos actuales del contacto: ")
        for dni in my_dict:
            print(my_dict[dni])
            time.sleep(0.1)
            print("1 Para modificar nombre.")
            time.sleep(0.1)
            print("2 Para modificar apellido.")
            time.sleep(0.1)
            print("3 Para modificar Email")
            time.sleep(0.1)
            print("4 Para modificar número.")
            time.sleep(0.1)
            print("5 Para salir. ")
            time.sleep(0.1)
            new_modification = input("Ingrese una opción: ")
            if new_modification == "1":
                new_name = input("Ingrese nuevo nombre del contacto: ")
                my_dict[dni]['Nombre'] = new_name
                print("Se ha modificado correctamente el nombre.")
            elif new_modification == "2":
                new_last_name = input("Ingrese nuevo apellido del contacto: ")
                my_dict[dni]['Apellido'] = new_last_name
                print("Se ha modificado correctamente el apellido.")
            elif new_modification == "3":
                while True:
                    new_email = input("Ingrese el nuevo Email: ")
                    my_dict[dni]['Email'] = new_email
                    if "@" not in new_email:
                        print("Ingrese una dirección de correo válida.")
                        continue
                    else:                     
                        print("Se ha modificado correctamente el Email.")
                        break
            elif new_modification == "4":
                new_num = int(input("Ingrese el nuevo número: "))
                my_dict[dni]['Número'] = new_num
                print("Se ha modificado correctamente el número.")
            elif new_modification ==  "5":
                continuar = True
    # Utilizamos 'del' para eliminar un contacto de la agenda, utilizando como clave el dni
    elif options == "3":
        delete_contact = int(input("Ingrese el DNI (sin puntos) del contacto que desea eliminar: "))
        if delete_contact in my_dict:
            are_you_sure = input("¿Está seguro que desea eliminar este contacto? s/n: ")
            if are_you_sure == "s":
                del my_dict[delete_contact]
                print("El contacto ha sido eliminado con éxito.")
            else:
                print ("El contacto no ha podido ser eliminado.")
    
    elif options == "4":
        print("Agenda completa: ")
        print(my_dict)
    
    elif options == "5":
        continuar = False
        print("Saliendo...")
    
    else:
        print("Opción no válida. Intente nuevamente.")