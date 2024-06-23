# Clase que representa un vuelo
class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, hora_salida, hora_llegada, capacidad):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.capacidad = capacidad
        self.pasajeros = []

    def agregar_pasajero(self, pasajero):
        if len(self.pasajeros) < self.capacidad:
            self.pasajeros.append(pasajero)
            print(f"Pasajero {pasajero.nombre} agregado al vuelo {self.numero_vuelo}.")
        else:
            print(f"El vuelo {self.numero_vuelo} está lleno. No se puede agregar al pasajero {pasajero.nombre}.")

    def eliminar_pasajero(self, pasajero):
        if pasajero in self.pasajeros:
            self.pasajeros.remove(pasajero)
            print(f"Pasajero {pasajero.nombre} eliminado del vuelo {self.numero_vuelo}.")
        else:
            print(f"El pasajero {pasajero.nombre} no está en el vuelo {self.numero_vuelo}.")

    def __str__(self):
        return f"Vuelo {self.numero_vuelo}: {self.origen} a {self.destino}, Salida: {self.hora_salida}, Llegada: {self.hora_llegada}, Capacidad: {self.capacidad}, Pasajeros: {len(self.pasajeros)}"


# Clase que representa un pasajero
class Pasajero:
    def __init__(self, nombre, numero_pasaporte):
        self.nombre = nombre
        self.numero_pasaporte = numero_pasaporte

    def __str__(self):
        return f"Pasajero: {self.nombre}, Número de Pasaporte: {self.numero_pasaporte}"


# Clase que representa una reserva de vuelo
class Reserva:
    def __init__(self, pasajero, vuelo):
        self.pasajero = pasajero
        self.vuelo = vuelo

    def hacer_reserva(self):
        self.vuelo.agregar_pasajero(self.pasajero)
        print(f"Reserva realizada para {self.pasajero.nombre} en el vuelo {self.vuelo.numero_vuelo}.")

    def cancelar_reserva(self):
        self.vuelo.eliminar_pasajero(self.pasajero)
        print(f"Reserva para {self.pasajero.nombre} en el vuelo {self.vuelo.numero_vuelo} ha sido cancelada.")


# Clase que representa una aerolínea y maneja los vuelos y reservas
class Aerolinea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vuelos = []
        self.reservas = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)
        print(f"Vuelo {vuelo.numero_vuelo} agregado a la aerolínea {self.nombre}.")

    def encontrar_vuelo(self, numero_vuelo):
        for vuelo in self.vuelos:
            if vuelo.numero_vuelo == numero_vuelo:
                return vuelo
        return None

    def hacer_reserva(self, nombre_pasajero, numero_pasaporte, numero_vuelo):
        pasajero = Pasajero(nombre_pasajero, numero_pasaporte)
        vuelo = self.encontrar_vuelo(numero_vuelo)
        if vuelo:
            reserva = Reserva(pasajero, vuelo)
            reserva.hacer_reserva()
            self.reservas.append(reserva)
        else:
            print(f"No se encontró el vuelo con número {numero_vuelo}.")

    def cancelar_reserva(self, nombre_pasajero, numero_vuelo):
        for reserva in self.reservas:
            if reserva.pasajero.nombre == nombre_pasajero and reserva.vuelo.numero_vuelo == numero_vuelo:
                reserva.cancelar_reserva()
                self.reservas.remove(reserva)
                return
        print(f"No se encontró la reserva para el pasajero {nombre_pasajero} en el vuelo {numero_vuelo}.")

    def mostrar_vuelos(self):
        for vuelo in self.vuelos:
            print(vuelo)

    def mostrar_reservas(self):
        for reserva in self.reservas:
            print(f"Reserva: {reserva.pasajero.nombre}, Vuelo: {reserva.vuelo.numero_vuelo}")

# Ejemplo de uso del sistema de reservas de vuelos

# Crear una aerolínea
aerolinea = Aerolinea("Aerolíneas Altas")

# Añadir vuelos a la aerolínea
aerolinea.agregar_vuelo(Vuelo("AA123", "Nueva York", "Los Ángeles", "2024-07-01 08:00", "2024-07-01 11:00", 100))
aerolinea.agregar_vuelo(Vuelo("AA456", "San Francisco", "Chicago", "2024-07-02 09:00", "2024-07-02 12:00", 150))

# Mostrar los vuelos disponibles
print("\nVuelos Disponibles:")
aerolinea.mostrar_vuelos()

# Hacer una reserva
aerolinea.hacer_reserva("Juan Pérez", "A12345678", "AA123")

# Mostrar las reservas actuales
print("\nReservas Actuales:")
aerolinea.mostrar_reservas()

# Mostrar los vuelos después de hacer la reserva
print("\nVuelos Disponibles Después de la Reserva:")
aerolinea.mostrar_vuelos()

# Cancelar una reserva
aerolinea.cancelar_reserva("Juan Pérez", "AA123")

# Mostrar los vuelos después de cancelar la reserva
print("\nVuelos Disponibles Después de Cancelar la Reserva:")
aerolinea.mostrar_vuelos()

