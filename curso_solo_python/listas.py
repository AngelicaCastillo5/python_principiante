mi_lista=[0,1,2,3,4,5,6,7,8,9]
print("lista de enteros: ",mi_lista)
lista_con_cadena=['Cadena',2,3]
print("largo lista con cadena: ",len(lista_con_cadena))
segunda_lista=['uno','dos','tres']
print("lista por tramos: ",mi_lista[2:8:2])
lista_nueva=mi_lista+ segunda_lista
print(lista_nueva)
lista_nueva[0]='Angelica'
print(lista_nueva)
lista_nueva.append('cuatro')
print(lista_nueva)
item_popeado=lista_nueva.pop()
print("eliminacion con pop: ",lista_nueva)
print("item popeado: ",item_popeado)
letras_lista=['a','z','x','b','d']
num_lista=[4,1,5,7,3]
letras_lista.sort()
print(letras_lista)
num_lista.sort()
num_lista.reverse()
print(num_lista)