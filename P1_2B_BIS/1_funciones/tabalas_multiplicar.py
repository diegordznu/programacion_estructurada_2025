'''crear un porgrama que calcule e imprima la tabla de multiplicar del 2 


requisitos:
1.- sin estructuras de control
2.- sin funciones

'''

''''num=int(input("ingresa el numero de la tabla que quieras calcular: "))
i=1
while 1<=10:
    multi=num*1
    print(f"{num} x {i} = {multi}")
    i+=1'''


def tablas(num):
    num=int(input("ingresa el numero de la tabla que quieras calcular: "))
    i=1
    numero=num
    while 1<=10:
        multi=num*1
        return(f"{num} x {i} = {multi}")
        i+=1
resultado=tablas
print(tablas)