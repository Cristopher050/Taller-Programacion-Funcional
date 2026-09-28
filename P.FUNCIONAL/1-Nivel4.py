def crear_generador_sufijos(patron_lambda):
    contador = 0

    def generar(nombre):
        nonlocal contador
        contador += 1

        return patron_lambda(nombre, contador)

    return generar


# Prueba
generador = crear_generador_sufijos(
    lambda nombre, numero: f"{nombre}_{numero:03d}.txt"
)

print(generador("reporte"))
print(generador("reporte"))
print(generador("reporte"))