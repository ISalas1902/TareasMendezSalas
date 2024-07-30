
# Fecha 29/07/2024 Realizado por Isaac Salas Y Daniel Mendez
# Tarea 1 de Microprocesadores y microcontroladores

# Funcion que realizar una operacion deseada entre 2 numeros
def operation_selector(intNum1, intNum2, strOP):
    # Validacion de que los valores sean numero enteros
    aux1 = type(intNum1)
    aux2 = type(intNum2)
    aux3 = type(strOP)
    if ((aux1 == int) & (aux2 == int)):
        # Validación que comprueba si el operador es un string
        if (aux3 == str):
            # Averigua cual operacion se desea realizar y devuelve el resultado
            if (strOP == "+"):
                # Operacion suma con su resultado
                return 0, int(intNum1 + intNum2)
            elif (strOP == "-"):
                # Operacion resta con su resultado
                return 0, int(intNum1 - intNum2)
            elif (strOP == "*"):
                # Operacion multiplicacion con su resultado
                return 0, int(intNum1 * intNum2)
            elif (strOP == "&"):
                # Operacion and logica con su resultado
                return 0, int(intNum1 & intNum2)
            else:
                return -70, None  # Codigo de error por operador invalido
        else:
            return -60, None  # Codigo de error por operador no string
    else:
        return -50, None  # Codigo de error por numeros no enteros


# Funcion que calcula el promedio de una lista de valores
def calculo_promedio(lista_Valores):
    # Valida el tamaño de la lista ingresada
    if (len(lista_Valores) <= 10):
        # Inicializacion de variables
        val = 0
        promedio = 0
        error = False
        # Recorrido de de los valores de la lista
        while ((val < len(lista_Valores)) & (~error)):
            # Comprobacion del tipo de los valores de la lista
            aux = type(lista_Valores[val])
            if ((aux == float) | (aux == int)):
                # Suma de los valores de lista
                promedio = promedio+lista_Valores[val]
                val = val + 1  # Contador para recorrer lista
            else:
                # Caso de tipo invalido en la lista
                error = True
                # Codigo de error por valor invalido en la lista
                return -80, None
        # Calculo del promedio
        return 0, promedio / len(lista_Valores)
    else:
        # Codigo de error por tamaño de lista
        return -90, None
