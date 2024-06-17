class Semana:
    def __init__(self, datos_semana):
        self.datos = datos_semana

    def calcular_promedio(self):
        suma_temperaturas = sum(dia["Temperatura"] for dia in self.datos)
        return suma_temperaturas / len(self.datos)


class Ciudad:
    def __init__(self, nombre, datos_semanas):
        self.nombre = nombre
        self.semanas = [Semana(semana) for semana in datos_semanas]

    def temperatura_promedio_ciudad(self):
        promedios_semanales = [semana.calcular_promedio() for semana in self.semanas]
        promedio_general = sum(promedios_semanales) / len(promedios_semanales)
        return promedio_general


def calcular_temperatura_promedio(datos_ciudades):
    for ciudad_datos in datos_ciudades:
        for ciudad_nombre, datos_ciudad in ciudad_datos.items():
            ciudad = Ciudad(ciudad_nombre, datos_ciudad)
            promedio_ciudad = ciudad.temperatura_promedio_ciudad()
            print("\n======================================================>")
            print(f"El promedio de temperatura en {ciudad.nombre} es: {promedio_ciudad:.2f}°Celsius")


# Datos de las ciudades
datos_ciudades = [
    {"Archidona": [
        [  # SEMANA 1
            {"Dia": "Lunes", "Temperatura": 40},
            {"Dia": "Martes", "Temperatura": 53},
            {"Dia": "Miercoles", "Temperatura": 36},
            {"Dia": "Jueves", "Temperatura": 32},
            {"Dia": "Viernes", "Temperatura": 28},
            {"Dia": "Sabado", "Temperatura": 19},
            {"Dia": "Domingo", "Temperatura": 44}
        ],
        [  # SEMANA 2
            {"Dia": "Lunes", "Temperatura": 39},
            {"Dia": "Martes", "Temperatura": 46},
            {"Dia": "Miercoles", "Temperatura": 26},
            {"Dia": "Jueves", "Temperatura": 25},
            {"Dia": "Viernes", "Temperatura": 42},
            {"Dia": "Sabado", "Temperatura": 28},
            {"Dia": "Domingo", "Temperatura": 35}
        ],
        [  # SEMANA 3
            {"Dia": "Lunes", "Temperatura": 27},
            {"Dia": "Martes", "Temperatura": 36},
            {"Dia": "Miercoles", "Temperatura": 56},
            {"Dia": "Jueves", "Temperatura": 28},
            {"Dia": "Viernes", "Temperatura": 32},
            {"Dia": "Sabado", "Temperatura": 28},
            {"Dia": "Domingo", "Temperatura": 34}
        ],
        [  # SEMANA 4
            {"Dia": "Lunes", "Temperatura": 45},
            {"Dia": "Martes", "Temperatura": 26},
            {"Dia": "Miercoles", "Temperatura": 32},
            {"Dia": "Jueves", "Temperatura": 31},
            {"Dia": "Viernes", "Temperatura": 28},
            {"Dia": "Sabado", "Temperatura": 20},
            {"Dia": "Domingo", "Temperatura": 27}
        ]
    ]},
    # Se pueden agregar más ciudades aquí con el mismo formato
]

calcular_temperatura_promedio(datos_ciudades)
