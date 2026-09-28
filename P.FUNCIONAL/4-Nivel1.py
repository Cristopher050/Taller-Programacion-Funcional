def crear_validador_múltiple(*lambdas_criterios):

    def validar(objeto):
        return all(
            criterio(objeto)
            for criterio in lambdas_criterios
        )

    return validar


# Prueba
validar_usuario = crear_validador_múltiple(
    lambda usuario: len(usuario["nombre"]) >= 3,
    lambda usuario: usuario["edad"] >= 18,
    lambda usuario: usuario["activo"] is True
)


usuario = {
    "nombre": "Carlos",
    "edad": 20,
    "activo": True
}

print(validar_usuario(usuario))