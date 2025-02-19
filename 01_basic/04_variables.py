###
# 04 - variables types()
# Guardar datos en memoria
# python es un lenguaje de tipado dinámico y típado fuerte
# No hace falta indicar si es lef, const, 

#ASIGNAR VARIABLE
# Solo hace falta poner esto

my_name = "midudev"
print(my_name)

age = 32
print(age)

age = 39 
print(age)

# Típado dinámico: el tipo de dato se determina en tiempo de ejecución
# que no tienens que declararlo explícitamente>
name = "midudev"
print(type(name))

name = 33
print(type(name))

# Típado fuertes: python no realiza conversiones de tipo automáticas
# ptint("10" + 2)

# f-dtring (literak de cadeba de firnati)
# desde la versión python 3.6
print(f"Hola {my_name}, tengo {age + 5} años")

# No recomendada forma de asignar variables
##name, age, city = "midudev", 32 "Bogotá"

# Convenciones de nombres de variables
""" mi_nombre_variable = "ok" # snake_Case
MiNombredevariable = "ok"
minombredevariable = "ok"
mi_nombre_de_variable_123 = "ok" """

##MI_CONSTANTE = 3.14 # Python no usa constantes pero se puede simular de esta forma  UPPER_CASE -> constantes

# Nombres no validos de variables
# 123121545_variable= "ko"
# mi-variable = "ko"
# mi variable = "ko"

""" True = False """
""" 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] """

is_user_logged_in: bool = True
print(is_user_logged_in)

name: str = "midudev"