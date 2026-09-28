from time import perf_counter


def auditar_ejecucion(fn_objetivo, fn_logger):
    def ejecutar(*args, **kwargs):

        inicio = perf_counter()

        resultado = fn_objetivo(*args, **kwargs)

        fin = perf_counter()

        tiempo = fin - inicio

        fn_logger(resultado, tiempo)

        return resultado

    return ejecutar


# Función que queremos medir
def calcular_cuadrado(numero):
    return numero * numero


# Logger
logger = lambda resultado, tiempo: print(
    f"Resultado: {resultado} | "
    f"Tiempo: {tiempo:.8f} segundos"
)


# Crear función auditada
auditada = auditar_ejecucion(
    calcular_cuadrado,
    logger
)

print(auditada(12))