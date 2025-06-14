def baneados(archivo):
    baneados = []
    with open(archivo, 'r') as f:
        for linea in f:
            # elimina los espacios
            datos = linea.strip().split(';')
            # verif si uso malulos
            if datos[-1] == 'Yes' and datos[0] not in baneados:
                baneados.append(datos[0])
    return baneados

def ranking(archivo, juego):
    lista_baneados = baneados(archivo)
    categorias = {}
    
    with open(archivo, 'r') as f:
        for linea in f:
            datos = linea.strip().split(';')
            jugador, pais, juego_act, cat, tiempo, trampa = datos
            
            # filtro 
            if juego_act == juego and trampa == 'No' and jugador not in lista_baneados:
                if cat not in categorias:
                    categorias[cat] = []
                
                # conv a seg (me daba error si no lo usaba xd)
                h, m, s = map(int, tiempo.split(':'))
                segundos = h*3600 + m*60 + s
                categorias[cat].append((segundos, jugador, pais, tiempo))
    
    resultado = {}
    for cat in categorias:
        categorias[cat].sort()  # ordena x tiempo
        # top 3
        resultado[cat] = [[jug, pais, tiempo] for (seg, jug, pais, tiempo) in categorias[cat][:3]]
    
    return resultado

def reporte(archivo):
    juegos = set()
    
    with open(archivo, 'r') as f:
        for linea in f:
            juego = linea.strip().split(';')[2]
            juegos.add(juego)
    
    for juego in juegos:
        # eliminar caracteres
        nombre_archivo = f"{juego.replace(':', '').replace('?', '')}.txt"
        rank = ranking(archivo, juego)
        
        with open(nombre_archivo, 'w') as f:
            for cat in rank:
                f.write(f"{cat}:\n")  
                # top 3
                for i, (jug, pais, tiempo) in enumerate(rank[cat], 1):
                    f.write(f"{i}. {jug} ({pais}): {tiempo}\n")
                f.write("\n")  # separador para que quede bonito
    
    return len(juegos)  # cantidad de archivos creados

# debug XD
print("Archivos creados:", reporte("speedruns.txt"))