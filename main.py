def baneados(archivo):
    baneados = []
    f = open(archivo, 'r')
    for linea in f:
        datos = linea.strip().split(';')
        # verif si tiene malulo o no
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
        
        # filtro juego especifico y k no haga trampas
        if juego_act == juego and trampa == 'No' and jugador not in lista_baneados:
            if cat not in categorias:
                categorias[cat] = []
    
            categorias[cat].append((tiempo, jugador, pais))
    f.close()
    
    # ordenar alfabetikamente x tiempo
    resultado = {}
    for cat in categorias:
        categorias[cat].sort()
        resultado[cat] = [[jug, pais, tiempo] for (tiempo, jug, pais) in categorias[cat][:3]]
    
    return resultado

def reporte(archivo):
    juegos = set()
    
    f = open(archivo, 'r')
    for linea in f:
        juego = linea.strip().split(';')[2]
        juegos.add(juego)
    f.close()
    
    for juego in juegos:
        nombre_archivo = juego.replace(':', '').replace('?', '') + ".txt" # nombre archivo sin caracteres xd
        rank = ranking(archivo, juego)
        
        f_out = open(nombre_archivo, 'w')
        for cat in rank:
            f_out.write(f"{cat}:\n")
            for i, (jug, pais, tiempo) in enumerate(rank[cat], 1): #top3
                f_out.write(f"{i}. {jug} ({pais}): {tiempo}\n")
            f_out.write("\n")
        f_out.close()
    
    return len(juegos)

# debug XD
print("Archivos creados:", reporte("speedruns.txt"))