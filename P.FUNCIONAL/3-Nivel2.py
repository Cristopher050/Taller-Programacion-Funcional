def agrupar_por(lista, fn_clave):
    resultado = {}

    for elemento in lista:
        clave = fn_clave(elemento)

        if clave not in resultado:
            resultado[clave] = []

        resultado[clave].append(elemento)

    return resultado


# Prueba
personas = [
    {"nombre": "Ana", "grupo": "A"},
    {"nombre": "Luis", "grupo": "B"},
    {"nombre": "Pedro", "grupo": "A"}
]

resultado = agrupar_por(
    personas,
    lambda persona: persona["grupo"]
)

print(resultado)