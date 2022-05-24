def cliente (informacion):
    """se recibe informacion de los clientes, para dar el valor de las boletas,
    hay unos descuestos para cliente nuevos. las atracciones tienen los sigtes parametros
    
    Atraccion           Valor de boleta edad         primer ingreso  descuento
    x-treme             20000           >18          True            5% descuento
    Carros chocones     5000            >=15 y <=18  True            7% descuento
    Sillas voladoras    10000           >=7 y <15    True            5% descuento
    
    retorna: {'nombre': , 'edad': , 'atraccion': ,'apto':, 'primer_ingreso':, 'total_boleta': }"""
    if informacion ["primer_ingreso"] == True:
        if informacion ["edad"] < 7 :
            mensaje = {"nombre":informacion ["nombre"], "edad":informacion ["edad"],"atraccion":"N/A", "apto":False, "primer_ingreso":"True", "total_boleta":"N/A"}
            return mensaje
        elif informacion ["edad"] >= 7 and informacion ["edad"] <15 :
            atraccion = "Sillas voladoras"
            total_boleta = 10000 - (10000 * 0.05)
            mensaje = {"nombre":informacion ["nombre"], "edad":informacion ["edad"],"atraccion": atraccion,"apto":True, "primer_ingreso":True, "total_boleta":total_boleta}
            return mensaje
        elif informacion ["edad"] >=15 and informacion ["edad"] <=18:
            atraccion = "Carros chocones"
            total_boleta = 5000 - (5000 * 0.07)
            mensaje = {"nombre":informacion ["nombre"], "edad":informacion ["edad"],"atraccion": atraccion,"apto":True,  "primer_ingreso":True, "total_boleta":total_boleta}
            return mensaje 
        elif informacion ["edad"] > 18 :
            atraccion = "X-Treme"
            total_boleta = 20000 - (20000 * 0.05)
            mensaje = {"nombre":informacion ["nombre"], "edad":informacion ["edad"],"atraccion": atraccion,"apto":True,  "primer_ingreso":True, "total_boleta":total_boleta}
            return mensaje
    else:
        if informacion ["edad"] < 7 :
            mensaje = {"nombre":informacion ["nombre"], "edad":informacion ["edad"],"atraccion":"N/A", "apto":False, "primer_ingreso":"False", "total_boleta":"N/A"}
            return mensaje 
        elif informacion ["edad"] >= 7 and informacion ["edad"] <15 :
            atraccion = "Sillas voladoras"
            total_boleta = 10000
            mensaje = {"nombre":informacion ["nombre"], "edad":informacion ["edad"],"atraccion": atraccion,"apto":True, "primer_ingreso":False, "total_boleta":total_boleta}
            return mensaje
        elif informacion ["edad"] >=15 and informacion ["edad"] <=18:
            atraccion = "Carros chocones"
            total_boleta = 5000
            mensaje = {"nombre":informacion ["nombre"], "edad":informacion ["edad"],"atraccion": atraccion,"apto":True,  "primer_ingreso":False, "total_boleta":total_boleta}
            return mensaje
        elif informacion ["edad"] > 18 :
            atraccion = "X-Treme"
            total_boleta = 20000
            mensaje = {"nombre":informacion ["nombre"], "edad":informacion ["edad"],"atraccion": atraccion,"apto":True,  "primer_ingreso":False, "total_boleta":total_boleta}
            return mensaje
        
informacion = {"id_cliente": 1, "nombre": "gabriel", "edad":109 , "primer_ingreso": True}
print (cliente (informacion))   
    