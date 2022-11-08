from echo import Colors, echo
def cargarPagos(cant):
    vec1 = []
    for i in range(cant):
        vec2 = []
        for j in range(cant):
            echo(
                f'ingrese el pago de la celda [{i+1},{j+1}]:', color=Colors.GREEN, end='')
            pago = int(input())
            vec2.append(pago)
        vec1.append(vec2)
    return vec1
