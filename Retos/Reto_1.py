def CDT (usuario: str, capital: int, tiempo: int):
    """Datos ingresados: nombre: el nombre del cliente
                         capital: el valor a invertir
                         tiempo: el tiempo que va a estar la inversion en el CDT
    Procedimiento: si el tiempo es <= 2 meses se penaliza con un 2%
                   si en > a 2 meses tiene una ganancia del 3%
    Retorna: Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un
             tiempo de {} meses es: {}"""
             
    if  tiempo <= 2:
        valor_a_perder = capital * 0.02
        valor_total_a_perder = capital - valor_a_perder
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total_a_perder}"
    
    else: 
        valor_interes = (capital * 0.03 * tiempo) / 12
        valor_total = valor_interes + capital
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"
    

print (CDT ("william andres velez", 2900000, 1))





