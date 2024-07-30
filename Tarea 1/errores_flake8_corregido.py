def example_function(a, b):
    result = (a+b) * 2  # Espacio extra al final de esta línea
    if result > 10:
        # Línea demasiado larga que excede el límite recomendado por PEP 8
        print("Result is greater than 10")
    return result


x = 5
y = 7
z = example_function(x, y)
print("The result is:", z)  # Espacio antes de los dos puntos
