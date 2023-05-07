def crear_tablero(filas,columnas):
    return np.full((filas,columnas),mar)

tablero = crear_tablero(filas,columnas)

def colocar_flota():
    lista_barcos = []
    while len(lista_barcos) < 20:
        x = random.randint(0,9)
        y = random.randint(0,9)
        coordenada = (x,y)
        if coordenada not in lista_barcos:
            lista_barcos.append(coordenada)
    for i in lista_barcos:
        tablero[i] = barco

def ocultar_flota():
    return np.where(tablero == barco, mar, tablero)

grand_line = ocultar_flota()

def explotar_flota():
    return np.full((filas,columnas),hundido)

sbcb = explotar_flota()

def turno():
    print('- Pirata: ¿Dónde quiere que disparemos capitán?')
    tx = input('FILA [1-10]')
    ty = input('COLUMNA [1-10]')
    if tx == 'BOOM' and ty == 'BOOM':
        print('- Buggy el payaso: ¡Traedme la SÚPER BALA DE CAÑÓN BUGGY!')
        print('- Pirata: ¡A la orden Capitán!')
        time.sleep(5)
        print(sbcb)
        print('- Buggy el payaso: Y ahora ¡HUYAMOS!')
        print('YOU WIN!')
        return True
    else:
        tx, ty = int(tx)-1, int(ty)-1
        if tablero[tx, ty] == barco:
            grand_line[tx, ty] = hundido
            print('- Buggy el payaso: ¡Uno menos!')
        else:
            grand_line[tx, ty] = agua
            print('- Galdino: ¿Buggy, estás ciego?')
        print(tablero_oculto(grand_line))
        return False

def imprimir_tablero(tablero):
    for i in range(filas):
        for j in range(columnas):
            print(tablero[i][j], end=' ')
        print()

def tablero_oculto(tablero):
    return np.where(tablero == agua, agua, mar)

def jugar(balas_cañon):
    print('- Pirata: ¡Capitán! Hemos detectado una flota de La Marina en las proximidades')
    start = input('y/n')
    if start == 'y':
        colocar_flota()
        print('- Buggy el payaso: ¿LA MARINA? ¡Preparadme el cañón Buggy!')
        time.sleep(2)
        while balas_cañon > 0:
            if turno():
                break
            balas_cañon -= 1
            if (tablero == hundido).sum() == flota:
                print('YOU WIN!')
                break
        else:
            print('- Buggy el payaso: ¡HUYAMOS SON DEMASIADOS!')
            print('- Pirata: ¡Buggy, eres un cobarde!')