import time

class Servidor:
    def __init__(self, direccion_ip, puerto):
        """Constructor: Inicializa la conexión al servidor."""
        self.direccion_ip = direccion_ip
        self.puerto = puerto
        self.conectado = True
        print(f"Conexión establecida con el servidor en {self.direccion_ip}:{self.puerto}")

    def enviar_datos(self, datos):
        """Método para simular el envío de datos al servidor."""
        if self.conectado:
            print(f"Enviando datos al servidor: {datos}")
        else:
            print("No se puede enviar datos. No está conectado.")

    def __del__(self):
        """Destructor: Cierra la conexión al servidor."""
        if self.conectado:
            self.conectado = False
            print(f"Conexión cerrada con el servidor en {self.direccion_ip}:{self.puerto}")

class Sensor:
    def __init__(self, id_sensor, tipo):
        """Constructor: Inicializa el sensor con su ID y tipo."""
        self.id_sensor = id_sensor
        self.tipo = tipo
        self.lectura_actual = None
        print(f"Sensor creado: ID={self.id_sensor}, Tipo={self.tipo}")

    def tomar_lectura(self):
        """Método para simular la toma de una lectura del sensor."""
        self.lectura_actual = 25 + (time.time() % 10)  # Simulación de una lectura de temperatura
        print(f"Lectura del sensor {self.id_sensor}: {self.lectura_actual}°C")

    def __del__(self):
        """Destructor: Limpia los recursos del sensor."""
        print(f"Sensor eliminado: ID={self.id_sensor}")

# Ejemplo de uso
print("Creación de una instancia de Servidor:")
servidor = Servidor('192.168.1.1', 8080)
servidor.enviar_datos('Temperatura: 25°C')
del servidor  # Llamada explícita al destructor

print("\nCreación de una instancia de Sensor:")
sensor = Sensor('001', 'Temperatura')
sensor.tomar_lectura()
del sensor  # Llamada explícita al destructor
