def crear_sistema_eventos():

    suscriptores = {}

    def gestor(
        accion,
        evento=None,
        callback=None,
        dato=None
    ):

        if accion == "suscribir":

            suscriptores.setdefault(
                evento, []
            ).append(callback)

            return True

        if accion == "emitir":

            resultados = []

            for funcion in suscriptores.get(
                evento, []
            ):
                resultados.append(
                    funcion(dato)
                )

            return resultados

        return None

    return gestor


# Crear sistema
eventos = crear_sistema_eventos()


# Registrar funciones
eventos(
    "suscribir",
    "saludo",
    lambda nombre: f"Hola {nombre}"
)

eventos(
    "suscribir",
    "saludo",
    lambda nombre: f"Bienvenido {nombre}"
)


# Emitir evento
print(
    eventos(
        "emitir",
        "saludo",
        dato="Crist"
    )
)