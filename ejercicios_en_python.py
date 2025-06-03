# Ejercicio 1: Suma de dos números
num1 = float(input("Ejercicio 1 - Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
print("La suma es:", num1 + num2)

# Ejercicio 2: Conversión de grados Celsius a Fahrenheit
celsius = float(input("\nEjercicio 2 - Ingresa la temperatura en Celsius: "))
fahrenheit = celsius * 1.8 + 32
print("Temperatura en Fahrenheit:", fahrenheit)

# Ejercicio 3: Área de un triángulo
base = float(input("\nEjercicio 3 - Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area = (base * altura) / 2
print("Área del triángulo:", area)

# Ejercicio 4: Par o impar
numero = int(input("\nEjercicio 4 - Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Ejercicio 5: Intercambiar valores entre dos variables
a = input("\nEjercicio 5 - Ingresa el valor de a: ")
b = input("Ingresa el valor de b: ")
a, b = b, a
print("Después del intercambio, a =", a, "y b =", b)

# Ejercicio 6: Calculadora simple
x = float(input("\nEjercicio 6 - Ingresa el primer número: "))
y = float(input("Ingresa el segundo número: "))
print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
if y != 0:
    print("División:", x / y)
else:
    print("No se puede dividir por cero.")

# Ejercicio 7: Edad en años, meses y días
edad = int(input("\nEjercicio 7 - Ingresa tu edad en años: "))
meses = edad * 12
dias = edad * 365
print("Edad en meses:", meses)
print("Edad en días (aproximadamente):", dias)

# Ejercicio 8: Número mayor
n1 = float(input("\nEjercicio 8 - Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))
mayor = max(n1, n2, n3)
print("El número mayor es:", mayor)

# Ejercicio 9: Verificar si un número es múltiplo de otro
numA = int(input("\nEjercicio 9 - Ingresa el primer número: "))
numB = int(input("Ingresa el segundo número: "))
if numA % numB == 0:
    print(f"{numA} es múltiplo de {numB}")
else:
    print(f"{numA} no es múltiplo de {numB}")

# Ejercicio 10: Salario con bonificación
salario_base = float(input("\nEjercicio 10 - Ingresa el salario base: "))
bono = salario_base * 0.10
salario_total = salario_base + bono
print("Salario total con bonificación:", salario_total)
