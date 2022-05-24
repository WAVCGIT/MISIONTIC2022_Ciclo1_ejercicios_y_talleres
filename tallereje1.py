# datos de entreada
# precio_telefono = 420
# incremento_de_precio = 20

# Procedimiento
def precio_final (precio, incremento):
    """realiza una regla de tres para calcular el incremento
    de acuerdo al porcentaje ingresado"""
    
    
    incremento = (precio * incremento) / 100
    
    return (precio + incremento)

precio_final = (input = ("ingrese el precio del producto:"), input =("ingrese el incremento en %:"))
                
print ("el precio final es: ", precio_final(420, 100), "euros")

       

