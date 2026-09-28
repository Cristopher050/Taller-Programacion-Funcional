from collections import OrderedDict


def memoizar_avanzado(fn_costosa, max_items):

    cache = OrderedDict()

    def memoizada(*args):

        if args in cache:
            print("Resultado obtenido desde caché")
            return cache[args]

        print("Calculando resultado...")

        resultado = fn_costosa(*args)

        cache[args] = resultado

        if len(cache) > max_items:
            cache.popitem(last=False)

        return resultado

    return memoizada


# Función costosa
def calcular(numero):
    print("Ejecutando cálculo...")
    return numero * numero


# Crear función memoizada
memo = memoizar_avanzado(calcular, 2)


print(memo(5))
print(memo(5))
print(memo(10))