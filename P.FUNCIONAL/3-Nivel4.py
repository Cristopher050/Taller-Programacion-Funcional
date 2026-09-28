def componer_dos(f, g):
    def compuesto(x):
        return f(g(x))

    return compuesto


# Prueba
doble = lambda x: x * 2
sumar_tres = lambda x: x + 3

combinada = componer_dos(
    sumar_tres,
    doble
)

print(combinada(5))