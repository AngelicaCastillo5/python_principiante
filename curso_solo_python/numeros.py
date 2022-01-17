suma_int=4+4
suma_float=4.5 + 4.5
print("suma de enteros: ",suma_int)
print("suma de flotantes: ", suma_float)
modulo=7%4
print("El modulo de 7/4es : ", modulo)
potencia=20**2
print("la potencia de 20 es :", potencia)
suma_multiplicacion=(2+10)*(10+4)
print("operaciones matematicas : ", suma_multiplicacion)

## Reglas de buenas prácticas en python
# nombres de variables en minusculas
# evitar usar palabras con significado como list o str

## Python con nomenclatura Dinamica
# se pueden reasignar variables a otros tipos de datos
# es un lenguaje flexible

### Pros de nomenclatura dinamica
# Facil de trabajar
# Rapido de desarrollar

### Cons 
# Resultan errores de datos inesperados 
# cuidado con type()

caracter="cadena de Texto con Muchos caracteres"

print("largo de la cadena caracter ",len(caracter))
# comilla simple para expresiones dentro de algo
# comillas dobles para expresiones por fuera
#las cadenas tienen indices
# las cadenas tienen indice inverso
# indexado y slicing

print("indexado de la cadena de caracteres: ",caracter[3])
print("indexado inverso: ", caracter[-1])
print("slicing: ", caracter[:])
print("slicing por tramos:", caracter[0:5])
print("slicing saltados: ", caracter[0:8:2])
print("Cadena en mayusculas: ", caracter.upper())
print("Cadena en minusculas: ",caracter.lower())
print("separacion split: ", caracter.split())

##format 

print('Esta es una cadena de {}'.format('TEXTO'))
print('Esta {} {} {}'.format('es','una','cadena'))
print('Esta {0} {1} {2}'.format('es','una','cadena'))
print('Esta {e} {u} {c}'.format(e='es',u='una',c='cadena'))


resultado=100/888
print("Los resultados son: {}".format(resultado))
print("Los resultados son: {r:1.3f}".format(r=resultado))
print("Los resultados son: {r:10.3f}".format(r=resultado))
nombre="Angelica"
edad=27
print(f"La persona se llama : {nombre} con edad de {edad}")
