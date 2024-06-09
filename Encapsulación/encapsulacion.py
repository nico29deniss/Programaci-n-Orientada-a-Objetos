class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self._nombre = nombre  # Atributo protegido
        self._fuerza = fuerza  # Atributo protegido
        self._inteligencia = inteligencia  # Atributo protegido
        self._defensa = defensa  # Atributo protegido
        self._vida = vida  # Atributo protegido

    def atributos(self):
        print(self._nombre, ":", sep="")
        print("·Fuerza:", self._fuerza)
        print("·Inteligencia:", self._inteligencia)
        print("·Defensa:", self._defensa)
        print("·Vida:", self._vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self._fuerza += fuerza
        self._inteligencia += inteligencia
        self._defensa += defensa

    def esta_vivo(self):
        return self._vida > 0

    def morir(self):
        self._vida = 0
        print(self._nombre, "ha muerto")

    def daño(self, enemigo):
        return self._fuerza - enemigo._defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo._vida -= daño
        print(self._nombre, "ha realizado", daño, "puntos de daño a", enemigo._nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo._nombre, "es", enemigo._vida)
        else:
            enemigo.morir()


class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._espada = espada  # Atributo protegido

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self._espada = 8
        elif opcion == 2:
            self._espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self._espada)

    def daño(self, enemigo):
        return self._fuerza * self._espada - enemigo._defensa


class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self._libro = libro  # Atributo protegido

    def atributos(self):
        super().atributos()
        print("·Libro:", self._libro)

    def daño(self, enemigo):
        return self._inteligencia * self._libro - enemigo._defensa


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1._nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2._nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1._nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2._nombre)
    else:
        print("\nEmpate")


personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
