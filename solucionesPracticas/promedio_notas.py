""""
En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas 
(las notas van de 0 a 10) de los alumnos de un curso. Se necesita saber si el rendimiento ha sido 
elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo 
(promedio es inferior a 6). Desarrollar un algoritmo que resuelva este problema. Para tener en 
cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.
"""

total_alumnos = int(input("¿Cuantos alumnos rindieron el examen?: "))

#Agregamos una variable sum para almacenar la suma
sum = 0

for i in range(1, total_alumnos+1):
    #Agregamos un bucle por si el usuario ingresa una nota mayor de 10.
    while True: 
        nota_alumno = float(input(f"Ingresá la nota del alumno {i}: "))
        if nota_alumno > 10:
            print("Ingresá una nota válida.")
        sum += nota_alumno
        break

#Se divide la suma total de las notas por el total de alumnos para sacar el promedio
promedio_alumnos = sum / total_alumnos

#Se imprime el resultado teniendo en cuenta las condiciones de rendimiento
if promedio_alumnos > 8 and promedio_alumnos <= 10:
    print(f"El rendimiento ha sido elevado, con un promedio de {round(promedio_alumnos, 2)}")
elif promedio_alumnos >= 6 and promedio_alumnos <= 8:
    print(f"El rendimiento ha sido aceptable, con un promedio de {round(promedio_alumnos, 2)}")
elif promedio_alumnos < 6:
    print(f"El rendimiento ha sido bajo, con un promedio de {round(promedio_alumnos, 2)}")