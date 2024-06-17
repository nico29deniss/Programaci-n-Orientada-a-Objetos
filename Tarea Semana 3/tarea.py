class Ciudad:
    def __init__(self, nombre, datos):
        self._nombre = nombre  # Encapsulamiento de los atributos
        self._datos = datos

    def obtener_nombre(self):
        return self._nombre

    def obtener_datos(self):
        return self._datos

    def calcular_temperatura_promedio(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")


class CiudadConTemperatura(Ciudad):
    def calcular_temperatura_promedio(self):
        promedios_semanales = []

        for semana in self._datos:
            suma_temperaturas = sum(dia["Temperatura"] for dia in semana)
            promedio_semanal = suma_temperaturas / len(week)
            promedios_semanales.append(promedio_semanal)

        promedio_general = sum(promedios_semanales) / len(promedios_semanales)
        return promedio_general


def calcular_temperatura_promedio_ciudades(datos_ciudades):
    for ciudad_datos in datos_ciudades:
        for ciudad_nombre, datos_ciudad in ciudad_datos.items():
            ciudad = CiudadConTemperatura(ciudad_nombre, datos_ciudad)
            promedio_ciudad = ciudad.calcular_temperatura_promedio()
            print(" \n ======================================================>")
            print(f"El promedio de temperatura en {ciudad.obtener_nombre()} es: {promedio_ciudad:.2f}°Celsius")


datos_ciudades = [
    {"Archidona": [
        # Datos de Archidona...
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
            {"Dia": "Miercoles", "Temperatura": 36},
            {"Dia": "Jueves", "Temperatura": 29},
            {"Dia": "Viernes", "Temperatura": 27},
            {"Dia": "Sabado", "Temperatura": 27},
            {"Dia": "Domingo", "Temperatura": 44}
        ],
    ]},

    {"Sucumbíos": [
        # Datos de Sucumbíos
        [  # SEMANA 1
            {"Dia": "Lunes", "Temperatura": 37},
            {"Dia": "Martes", "Temperatura": 36},
            {"Dia": "Miercoles", "Temperatura": 28},
            {"Dia": "Jueves", "Temperatura": 27},
            {"Dia": "Viernes", "Temperatura": 38},
            {"Dia": "Sabado", "Temperatura": 42},
            {"Dia": "Domingo", "Temperatura": 39}
        ],
        [  # SEMANA 2
            {"Dia": "Lunes", "Temperatura": 35},
            {"Dia": "Martes", "Temperatura": 27},
            {"Dia": "Miercoles", "Temperatura": 18},
            {"Dia": "Jueves", "Temperatura": 27},
            {"Dia": "Viernes", "Temperatura": 23},
            {"Dia": "Sabado", "Temperatura": 28},
            {"Dia": "Domingo", "Temperatura": 29}
        ],
        [  # SEMANA 3
            {"Dia": "Lunes", "Temperatura": 27},
            {"Dia": "Martes", "Temperatura": 29},
            {"Dia": "Miercoles", "Temperatura": 34},
            {"Dia": "Jueves", "Temperatura": 26},
            {"Dia": "Viernes", "Temperatura": 38},
            {"Dia": "Sabado", "Temperatura": 24},
            {"Dia": "Domingo", "Temperatura": 35}
        ],
        [  # SEMANA 4
            {"Dia": "Lunes", "Temperatura": 18},
            {"Dia": "Martes", "Temperatura": 46},
            {"Dia": "Miercoles", "Temperatura": 26},
            {"Dia": "Jueves", "Temperatura": 27},
            {"Dia": "Viernes", "Temperatura": 37},
            {"Dia": "Sabado", "Temperatura": 27},
            {"Dia": "Domingo", "Temperatura": 17}
        ],

    ]},

    {"Sucúa": [
        [  # SEMANA 1
            {"Dia": "Lunes", "Temperatura": 25},
            {"Dia": "Martes", "Temperatura": 16},
            {"Dia": "Miercoles", "Temperatura": 46},
            {"Dia": "Jueves", "Temperatura": 24},
            {"Dia": "Viernes", "Temperatura": 31},
            {"Dia": "Sabado", "Temperatura": 10},
            {"Dia": "Domingo", "Temperatura": 54}
        ],
        [  # SEMANA 2
            {"Dia": "Lunes", "Temperatura": 32},
            {"Dia": "Martes", "Temperatura": 52},
            {"Dia": "Miercoles", "Temperatura": 46},
            {"Dia": "Jueves", "Temperatura": 28},
            {"Dia": "Viernes", "Temperatura": 36},
            {"Dia": "Sabado", "Temperatura": 11},
            {"Dia": "Domingo", "Temperatura": 51}
        ],
        [  # SEMANA 3
            {"Dia": "Lunes", "Temperatura": 15},
            {"Dia": "Martes", "Temperatura": 27},
            {"Dia": "Miercoles", "Temperatura": 36},
            {"Dia": "Jueves", "Temperatura": 24},
            {"Dia": "Viernes", "Temperatura": 28},
            {"Dia": "Sabado", "Temperatura": 39},
            {"Dia": "Domingo", "Temperatura": 27}
        ],
        [  # SEMANA 4
            {"Dia": "Lunes", "Temperatura": 34},
            {"Dia": "Martes", "Temperatura": 36},
            {"Dia": "Miercoles", "Temperatura": 56},
            {"Dia": "Jueves", "Temperatura": 16},
            {"Dia": "Viernes", "Temperatura": 22},
            {"Dia": "Sabado", "Temperatura": 37},
            {"Dia": "Domingo", "Temperatura": 26}
        ]
    ]}
]

calcular_temperatura_promedio_ciudades(datos_ciudades)
