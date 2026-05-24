'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''

print("\033c")

num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar: "))
num=1
multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

multi=num_tabla*num
print(f"{num_tabla} x {num} = {multi}")
num+=1

'''
Con estrufcturas de control
'''
print("\033c")

num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar: "))
for num in range(1,11):
    multi=num_tabla*num
    print(f"{num_tabla} x {num} = {multi}")

print("\033c")
num=1
for num in range(100,0,-10):
    multi=num_tabla*num
    print(f"{num_tabla} x {num} = {multi}")
    num+=1

print("\033c")
num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar: "))
num=100
while num>=0:
    multi=num_tabla*num
    print(f"{num_tabla} x {num} = {multi}")
    num=num-10

print("\033c")
num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar: "))
num=1
while num<=10:
    multi=num_tabla*num
    print(f"{num_tabla} x {num} = {multi}")
    num=num+1

'''
Sin estructuras de control y con funciones
'''
print("\033c")
def tablaMultiplicar(num_tabla,num):
    multi=num_tabla*num
    print(f"{num_tabla} x {num} = {multi}")
    num+=1
    return num

num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar: "))
num=1
num=tablaMultiplicar(num_tabla,num)
num=tablaMultiplicar(num_tabla,num)
num=tablaMultiplicar(num_tabla,num)
num=tablaMultiplicar(num_tabla,num)
num=tablaMultiplicar(num_tabla,num)
num=tablaMultiplicar(num_tabla,num)
num=tablaMultiplicar(num_tabla,num)
num=tablaMultiplicar(num_tabla,num)
num=tablaMultiplicar(num_tabla,num)
num=tablaMultiplicar(num_tabla,num)

'''
Con estructuras de control y con funciones
'''
print("\033c")
def tablaMultiplicar(num_tabla,num):
    multi=num_tabla*num
    print(f"{num_tabla} x {num} = {multi}")
    num+=1
    return num
num_tabla=int(input("Dame un numero para obtener la tabla de multiplicar: "))
num=1
for num in range(1,11):
    num=tablaMultiplicar(num_tabla,num)
