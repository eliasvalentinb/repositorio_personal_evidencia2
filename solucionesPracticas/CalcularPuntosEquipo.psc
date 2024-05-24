Algoritmo CalcularPuntosEquipo
    Definir partidos_ganados, partidos_empatados, partidos_perdidos como Entero
    Definir puntos_totales como Entero
	
    Escribir "Ingrese la cantidad de partidos ganados: "
    Leer partidos_ganados
	
    Escribir "Ingrese la cantidad de partidos empatados: "
    Leer partidos_empatados
	
    Escribir "Ingrese la cantidad de partidos perdidos: "
    Leer partidos_perdidos
	
    puntos_totales = (partidos_ganados * 3) + (partidos_empatados * 1) + (partidos_perdidos * 0)
	
    Escribir "El equipo lleva acumulados ", puntos_totales, " puntos en el campeonato."
FinAlgoritmo