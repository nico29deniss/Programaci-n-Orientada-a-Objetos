"""
Este programa calcula el área de diferentes figuras geométricas: círculo, rectángulo, cuadrado y triángulo.
El usuario debe ingresar el tipo de figura y las dimensiones necesarias para calcular el área.
"""

import math  # Importamos la librería math para utilizar la constante pi


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    area = math.pi * radio ** 2  # Fórmula para calcular el área de un círculo
    return area


def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo dado su largo y ancho.
    :param largo: Largo del rectángulo (float)
    :param ancho: Ancho del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    area = largo * ancho  # Fórmula para calcular el área de un rectángulo
    return area


def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el lado.
    :param lado: Lado del cuadrado (float)
    :return: Área del cuadrado (float)
    """
    area = lado ** 2  # Fórmula para calcular el área de un cuadrado
    return area


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    :param base: Base del triángulo (float)
    :param altura: Altura del triángulo (float)
    :return: Área del triángulo (float)
    """
    area = 0.5 * base * altura  # Fórmula para calcular el área de un triángulo
    return area


def main():
    """
    Función principal que solicita al usuario ingresar la figura y las dimensiones necesarias para calcular el área.
    """
    print("Calculadora de áreas de figuras geométricas")
    print("Opciones: círculo, rectángulo, cuadrado, triángulo")

    figura = input(
        "Ingrese la figura que desea calcular el área: ").strip().lower()  # Solicita la figura y la convierte a minúsculas

    if figura == "circulo" or figura == "círculo":
        # Solicita el radio y calcula el área del círculo
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area}")
    elif figura == "rectangulo" or figura == "rectángulo":
        # Solicita el largo y el ancho y calcula el área del rectángulo
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        area = calcular_area_rectangulo(largo, ancho)
        print(f"El área del rectángulo es: {area}")
    elif figura == "cuadrado":
        # Solicita el lado y calcula el área del cuadrado
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)
        print(f"El área del cuadrado es: {area}")
    elif figura == "triangulo" or figura == "triángulo":
        # Solicita la base y la altura y calcula el área del triángulo
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area}")
    else:
        # Mensaje de error si la figura no es reconocida
        print("Figura no reconocida. Por favor, ingrese una figura válida.")


if __name__ == "__main__":
    main()  # Llama a la función principal
