import math

def area_cuadrado(lado):
    area=lado**2
    return print('El Área del Cuadrado es: ',area)

def area_triangulo(base, altura):
    area=base*altura/2
    return print('El Área del Triángulo es: ',area)

def area_circulo(radio):
    area=math.pi*radio**2
    return print('El Área del Circulo es %.3f'% area)

while True:
    print("\nCalcular Áreas de Figuras Geometricas.\n")
    print('1) Cuadrado.')
    print('2) Triangulo.')
    print('3) Circulo.')
    print('0) Salir.')
    x=int(input('\nEscoja la Figura: '))

    if x==1:
        lado=int(input('\nIngrese el Lado del Cuadrado: '))
        area_cuadrado(lado)

    elif x==2:
        base=int(input('\nIngrese la Base del Triángulo: '))
        altura=int(input('Ingrese la Altura del Triángulo: '))
        area_triangulo(base,altura)

    elif x==3:
        radio=int(input('\nIngrese el Radio del Circulo: '))
        area_circulo(radio)

    elif x == 0:
        print("\nPrograma Terminado :D\n")
        break
