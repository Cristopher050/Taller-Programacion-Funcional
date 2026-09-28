def ejecutar_y_rastrear(fn_tarea, n):
    historial = []

    for _ in range(n):
        historial.append(fn_tarea())

    def consultar_historial():
        return historial.copy()

    return consultar_historial


# Prueba
contador = [0]

def tarea():
    contador[0] += 1
    return f"Tarea ejecutada {contador[0]}"


rastreador = ejecutar_y_rastrear(tarea, 3)

print(rastreador())