# Definición de la clase base Personaje, que representa un personaje en el juego
class Personaje:
    # Inicialización de un personaje con atributos básicos
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Método para imprimir los atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    # Método para incrementar los atributos de fuerza, inteligencia y defensa
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    # Método que verifica si el personaje está vivo (vida > 0)
    def esta_vivo(self):
        return self.vida > 0

    # Método que establece la vida del personaje a 0 y notifica la muerte
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Método para calcular el daño infligido a otro personaje (enemigo)
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    # Método para atacar a otro personaje, reduciendo su vida según el daño calculado
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

# Definición de la clase Guerrero, una subclase de Personaje
class Guerrero(Personaje):
    # Inicialización del Guerrero con un atributo adicional: espada
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    # Método para cambiar el tipo de espada del Guerrero
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    # Método para imprimir los atributos del Guerrero, incluyendo la espada
    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    # Método para calcular el daño infligido a otro personaje, considerando el poder de la espada
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

# Definición de la clase Mago, una subclase de Personaje
class Mago(Personaje):
    # Inicialización del Mago con un atributo adicional: libro
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    # Método para imprimir los atributos del Mago, incluyendo el libro
    def atributos(self):
        super().atributos()
        print("·Libro:", self.libro)

    # Método para calcular el daño infligido a otro personaje, considerando el poder del libro
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

# Función de combate entre dos personajes, alternando turnos hasta que uno muera
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_vivo():  # Verifica si el segundo jugador sigue vivo antes de atacar
            print(">>> Acción de ", jugador_2.nombre, ":", sep="")
            jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

# Creación de instancias de Guerrero y Mago con atributos iniciales
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

# Muestra los atributos iniciales de ambos personajes
personaje_1.atributos()
personaje_2.atributos()

# Inicia el combate entre los dos personajes
combate(personaje_1, personaje_2)
