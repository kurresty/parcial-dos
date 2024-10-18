salario_base = float(input("Salario Base: "))
cargo = input("Cargo empleado: ")
nivel_desempeno = input("Nivel de desempeño: ")


def calcular_bonificacion(salario_base, cargo, nivel_desempeno):
    cargo = cargo.lower()
    nivel_desempeno = nivel_desempeno.lower()

    bonificacion = 0

    if cargo == 'directivo':
        if nivel_desempeno == 'alto':
            bonificacion = salario_base * 0.20
        elif nivel_desempeno == 'medio':
            bonificacion = salario_base * 0.10

    elif cargo == 'operativo':
        if nivel_desempeno == 'alto':
            bonificacion = salario_base * 0.15
        elif nivel_desempeno == 'medio':
            bonificacion = salario_base * 0.5

    #para desempeño bajo no se otorga ninguna bonificación

    total_a_recibir = salario_base + bonificacion
    return total_a_recibir, bonificacion


def mostrar_resumen(salario_base, cargo, nivel_de_desempeño):
    total_a_recibir, bonificacion = calcular_bonificacion(salario_base, cargo, nivel_de_desempeño)
    print(f"-----Resumen del pago-----")
    print(f"Cargo: {cargo.capitalize()}")
    print(f"Nivel de Desempeño: {nivel_de_desempeño.capitalize()}")
    print(f"Salario Base: ${salario_base:.0f}")
    print(f"Bonificacion: ${bonificacion:.0f}")
    print(f"Total a Recibir: ${total_a_recibir:.0f}")
    print("---------------------------\n")

    return total_a_recibir


mostrar_resumen(salario_base, cargo, nivel_desempeno)
