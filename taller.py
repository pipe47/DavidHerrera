# 1. Intercambio sin variable auxiliar
a, b = 5, 10
a, b = b, a

# 2. Suma de cuadrados
a, b = 5, 3
c = a**2 + b**2

# 3. Conversión de tipos
n = 42
n_str = str(n)
n_float = float(n_str)
n_int = int(n_float)
print(n_str, n_float, n_int)

# 4. Redondeo y formato
num = 17.8567
resultado = round(num, 2)
print(f"Resultado: {resultado:.2f}")

# 5. Concatenación de variables
nombre = "Juan"
edad = 25
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# 6. Cálculo de edad actual
anio_actual = 2025
anio_nacimiento = 2000
edad = anio_actual - anio_nacimiento

# 7. Cuenta regresiva con una variable
n = 10
while n >= 0:
    print(n)
    n -= 1

# 8. Valor absoluto sin abs()
x = -7
abs_x = x if x >= 0 else -x

# 9. Incremento/decremento según paridad
n = 4
n = n + 1 if n % 2 == 0 else n - 1
print(n)

# 10. Máximo entre tres números sin max()
a, b, c = 3, 7, 5
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print(mayor)
# 11. Verificación de rango
x = 55
print(10 <= x <= 100)

# 12. Comparación de strings ignorando mayúsculas
a = "Hola"
b = "hola"
print(a.lower() == b.lower())

# 13. Igualdad entre tres variables
a, b, c = 4, 4, 4
print(a == b == c)

# 14. Presencia en lista
lista = [1, 3, 5, 7]
x = 5
print(x in lista)

# 15. Divisibilidad por 3 y 5
n = 15
print(n % 3 == 0 and n % 5 == 0)

# 16. Números en orden estricto
a, b, c = 2, 5, 8
print(a < b < c)

# 17. Comparación doble
x, a, b = 7, 5, 10
print(a < x < b)

# 18. Relación proporcional
a, b = 10, 5
print(a == 2 * b)

# 19. Cambio de signo si negativo
x = -12
if x < 0:
    x = -x
print(x)

# 20. Detección de tipo
x = 3.14
if isinstance(x, int):
    print("int")
elif isinstance(x, float):
    print("float")
elif isinstance(x, str):
    print("str")
# 21. ¿Puede votar?
edad = 20
tiene_doc = True
print(edad >= 18 and tiene_doc)

# 22. Control de acceso lógico
pase_vip = False
pago_entrada = True
esta_ebrio = False
puede_entrar = pase_vip or (pago_entrada and not esta_ebrio)
print(puede_entrar)

# 23. Validación XOR
cond1 = True
cond2 = False
print(cond1 != cond2)

# 24. Validación compuesta múltiple
n = 6
print(n > 0 and (n % 2 == 0 or n % 3 == 0))

# 25. Condición contradictoria
x = 7
print(x > 5 and x < 1)  # Siempre False

# 26. Negación lógica
x = 8
print(not (x <= 10))  # Equivale a x > 10

# 27. Aprobación de estudiante
nota = 3.5
asistencia = 85
print(nota >= 3.0 and asistencia >= 80)

# 28. Simulación de alarma
temperatura = 39
humedad = 85
alarma = (temperatura < 0 or temperatura > 38) and humedad > 80
print(alarma)

# 29. Contraseña segura
password = "Python123"
es_segura = len(password) > 8 and any(char.isdigit() for char in password)
print(es_segura)

# 30. Doble negación lógica
tiene_acceso = False
print(not not tiene_acceso)
