Algoritmo compra_de_leche
    Definir caja_leche Como Real
    Definir descuento_jubilado, descuento_10, descuento_15, descuento Como Real
    Definir compra, valor_original, total Como Real
    Definir es_jubilado, continuar Como Cadena
	
    caja_leche = 1000
    descuento_jubilado = 0.10
    descuento_10 = 0.10
    descuento_15 = 0.15
	
    continuar = "s"
	
    Mientras continuar == "s"
        Escribir "¿Cuántas cajas de leche va a comprar?: "
        Leer compra
        Escribir "¿Es jubilado? s/n: "
        Leer es_jubilado
		
        Si es_jubilado <> "s" Y es_jubilado <> "n" Entonces
            Escribir "Ingrese una opción válida."
        Sino
            valor_original = compra * caja_leche
			
            Si compra > 24 Entonces
                descuento = descuento_15
            Sino
                Si compra >= 12 Entonces
                    descuento = descuento_10
                Sino
                    descuento = 0
                FinSi
            FinSi
			
            Si es_jubilado == "s" Entonces
                descuento = descuento + descuento_jubilado
            FinSi
			
            total = valor_original * (1 - descuento)
            Escribir "El total de la compra es de $", total
        FinSi
		
        Escribir "¿Desea realizar otra compra? s/n: "
        Leer continuar
    FinMientras
FinAlgoritmo