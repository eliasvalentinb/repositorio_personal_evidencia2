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

continuar = True
my_dict = {}
while continuar:
    options = int(input("Presione '1' para agregar un nuevo contacto, 2 para modificar un contacto, 3 para eliminar un contacto, 4 para mostrar la agenda completa o 5 para salir: "))
    if options == 1:
        nombre = input("Ingrese el nombre del nuevo contacto: ").capitalize()
        apellido = input("Ingrese el apellido del nuevo contacto: ").capitalize()
        dni = int(input("Ingrese el DNI del nuevo contacto: "))
        email = input("Ingrese el email del nuevo contacto: ")
        numero = int(input("Ingrese el número del nuevo contacto: "))

        my_dict[dni] = {"Nombre": nombre, "Apellido": apellido, "Email": email, "Número de teléfono": numero }
        print("Contacto agregado correctamente.")

    elif options == 2:
        modif_dni = input("Ingrese el DNI (sin puntos) del contacto que desea modificar: ")
        for modif_dni in my_dict:
            new_modification = input("¿Qué desea modificar? 'n' para nombre, 'a' para apellido, 'e' para Email, 'num' para Número, 'i' para salir: ").lower()
            if new_modification == "n":
                new_name = input("Ingrese nuevo nombre del contacto: ")
                my_dict[modif_dni]['Nombre'] = new_name
                print("Se ha modificado correctamente el nombre.")
            elif new_modification == "a":
                new_last_name = input("Ingrese nuevo apellido del contacto: ")
                my_dict[modif_dni]['Apellido'] = new_last_name
                print("Se ha modificado correctamente el apellido.")
            elif new_modification == "e":
                new_email = input("Ingrese el nuevo Email: ")
                my_dict[modif_dni]['Email'] = new_email
                print("Se ha modificado correctamente el Email.")
            elif new_modification == "num":
                new_num = int(input("Ingrese el nuevo número: "))
                my_dict[modif_dni]['Número'] = new_num
                print("Se ha modificado correctamente el número.")
            elif new_modification ==  "i":
                continuar = True
    
    elif options == 3:
        delete_contact = int(input("Ingrese el DNI (sin puntos) del contacto que desea eliminar: "))
        if delete_contact in my_dict:
            are_you_sure = input("¿Está seguro que desea eliminar este contacto? s/n: ")
            if are_you_sure == "s":
                del my_dict[delete_contact]
                print("El contacto ha sido eliminado con éxito.")
            else:
                print ("El contacto no ha podido ser eliminado.")
    
    elif options == 4:
        print("Agenda completa: ")
        print(my_dict)
    
    elif options == 5:
        continuar = False
        print("Saliendo...")
    
    else:
        print("Opción no válida. Intente nuevamente.")