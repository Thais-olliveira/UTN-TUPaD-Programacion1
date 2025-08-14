"""Práctico1_Thaís.ipynb

## Práctico 1- Estructuras secuenciales
Alumno: Thaís Cristina de Oliveira Alvim
"""

# ==========================================
# ==========     EJERCICIO 1     ===========
# ==========================================

# Muestra pantalla "Hola Mundo";
print ("Hola Mundo!")

# ==========================================
# ==========     EJERCICIO 2     ===========
# ==========================================

# Solicita al usuario que ingrese el nombre;
nombre = input ("Ingrese su nombre: ")
# Crea un saludo personalizado utilizando el nombre ingresado;
saludo = (f"Hola {nombre}")
# Muestra el saludo por pantalla
print (saludo)

# ==========================================
# ==========     EJERCICIO 3     ===========
# ==========================================

# Solicita al usuario que ingrese el nombre;
nombre = input ("Ingrese tu nombre: ")
# Solicita al usuario que ingrese el apellido;
apellido = input ("Ingrese tu apellido: ")
# Solicita al usuario que ingrese la edad;
edad = input ("Ingresa la edad: ")
# Solicita al usuario que ingrese el lugar de residencia;
lugar_residencia = input ("Ingrese el lugar de residencia: ")
# Muestra la oración con los datos ingresados;
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")


# ==========================================
# ==========     EJERCICIO 4     ===========
# ==========================================

# Solicita al usuario que ingrese el valor del radio y convierte el valor al tipo float (número decimal);
radio = float (input ("Ingrese el valor del radio: "))
# Define el valor de pi;
pi = 3.14159
# Calcula el área del círculo utilizando la fórmula: área = π * radio²;
area = pi * (radio ** 2)
# Calcula el perímetro utilizando la fórmula: perímetro = 2 * π * radio;
perimetro = 2 * pi * radio
# Muestra el resultado del área;
print (f"El área del circulo es: {area}")
# Muestra el resultado del perímetro;
print (f"El perímetro del circulo es: {perimetro}")

# ==========================================
# ==========     EJERCICIO 5     ===========
# ==========================================

## Solicita al usuario que ingrese la cantidad de segundos y convierte el valor ingresado (cadena de texto) a un número entero;
segundos = int (input ("Ingrese la cantidad de segundos: "))
# Calcula la cantidad de horas dividindo los segundos por 3600;
horas = segundos / 3600
# Muestra el resultado con 2 cifras decimales;
print (f"{segundos} segundos equivale a {horas:.2f} horas.")

# ==========================================
# ==========     EJERCICIO 6     ===========
# ==========================================

# Solicita al usuario que ingrese un número entero y convierte el valor ingresado a un número entero;
num =  int (input ("Ingrese un número entero:"))
# Imprime la tabla de multiplicar del número ingresado, desde 1 hasta 10;
print (f"{num} x 1 =  {num * 1}")
print (f"{num} x 2 =  {num * 2}")
print (f"{num} x 3 =  {num * 3}")
print (f"{num} x 4 =  {num * 4}")
print (f"{num} x 5 =  {num * 5}")
print (f"{num} x 6 =  {num * 6}")
print (f"{num} x 7 =  {num * 7}")
print (f"{num} x 8 =  {num * 8}")
print (f"{num} x 9 =  {num * 9}")
print (f"{num} x 10 =  {num * 10}")

# ==========================================
# ==========     EJERCICIO 7     ===========
# ==========================================

# Solicita al usuario que ingrese dos números enteros y los convierte a un número entero;
num1 = int (input ("Ingrese el primero número entero (distinto del 0):"))
num2 = int (input ("Ingrese el segundo número entero (distinto del 0):"))
# Muestra el resultado de la suma;
print (f"El resultado de la suma es {num1 + num2}")
# Muestra el resultado de la división con 2 cifras decimales;
print (f"El resultado de la división es {num1 / num2:.2f}")
# Muestra el resultado de la mustiplicación;
print (f"El resultado de la multiplicación es {num1 * num2}")
# Muestra el resultado de la resta;
print (f"El resultado de la resta es {num1 - num2}")

# ==========================================
# ==========     EJERCICIO 8     ===========
# ==========================================

# Solicita al usuario que ingrese el peso y lo convierte a un float;
peso = float (input ("Ingrese su peso (Ejemplo: 71.2): "))
# Solicita al usuario que ingrese su altura y lo convierte a un float;
altura = float (input ("Ingrese su altura (Ejemplo: 1.65):"))
# Calcula el IMC usando la fórmula: peso / altura²;
imc = peso / (altura ** 2)
# Muestra el resultado del IMC con 2 cifras decimales;
print (f"Seu IMC es de: {imc:.2f}")

# ==========================================
# ==========     EJERCICIO 9     ===========
# ==========================================

# Solicita al usuario que ingrese la temperatura en grados Celsius y convierte el valor ingresado a un float;
temperatura = float (input ("Ingrese una temperatura en grados Celsius: "))
# Convierte Celsius a Fahrenheit;
fahrenheit = (temperatura * 9/5) + 32
# Muestra el resultado de la temperatura con 2 cifras decimales;
print (f"La temperatura de {temperatura}°C equivale {fahrenheit:.2f}°F en Fahrenheit.")

# ==========================================
# ==========     EJERCICIO 10     ===========
# ==========================================

# Solicita al usuario que ingrese 3 números y convierte los valores ingresados a intero;
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
# Calcula el promedio
promedio = (num1 + num2 + num3) /3
# Muestra el resultado con 2 cifras decimales;
print (f"El promedio de los numeros ingresados es de {promedio:.2f}")