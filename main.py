def baneados(archivo):
    baneados = []
    f = open(archivo, 'r')
    for linea in f:
        datos = linea.strip().split(';')
        if datos[-1] == 'Yes' and datos[0] not in baneados:
            baneados.append(datos[0])
    f.close()
    return baneados

def ranking(archivo, juego):
    lista_baneados = baneados(archivo)
    categorias = {}
    
    f = open(archivo, 'r')
    for linea in f:
        datos = linea.strip().split(';')
        jugador = datos[0]
        pais = datos[1]
        juego_act = datos[2]
        cat = datos[3]
        tiempo = datos[4]
        trampa = datos[5]
        
        if juego_act == juego and trampa == 'No' and jugador not in lista_baneados:
            if cat not in categorias:
                categorias[cat] = []
    
            categorias[cat].append((tiempo, jugador, pais))
    f.close()
    
    resultado = {}
    for cat in categorias:
        categorias[cat].sort()
        resultado[cat] = [[jug, pais, tiempo] for (tiempo, jug, pais) in categorias[cat][:3]]
    
    return resultado

def reporte(archivo):
    juegos = []  
    
    f = open(archivo, 'r')
    for linea in f:
        juego = linea.strip().split(';')[2]
        if juego not in juegos:  
            juegos.append(juego)
    f.close()
    
    for juego in juegos:
        nombre_archivo = juego.replace(':', '').replace('?', '') + ".txt"
        rank = ranking(archivo, juego)
        
        f_out = open(nombre_archivo, 'w')
        for cat in rank:
            f_out.write("{}:\n".format(cat))  
            i = 1  
            for (jug, pais, tiempo) in rank[cat]:
                f_out.write("{}. {} ({}): {}\n".format(i, jug, pais, tiempo))
                i += 1
            f_out.write("\n")
        f_out.close()
    
    return len(juegos)

# debug XD
print("Archivos creados:", reporte("speedruns.txt"))