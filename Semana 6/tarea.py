# Definición de la clase base `CuentaBancaria`
class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo):
        # Atributos protegidos (encapsulación)
        self._numero_cuenta = numero_cuenta
        self._titular = titular
        self._saldo = saldo

    # Método para depositar dinero en la cuenta
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f'Depósito de {cantidad} realizado. Nuevo saldo: {self._saldo}')
        else:
            print('La cantidad a depositar debe ser positiva.')

    # Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            print(f'Retiro de {cantidad} realizado. Nuevo saldo: {self._saldo}')
        else:
            print('Fondos insuficientes o cantidad no válida.')

    # Método para mostrar la información de la cuenta
    def mostrar_info(self):
        return f'Número de cuenta: {self._numero_cuenta}, Titular: {self._titular}, Saldo: {self._saldo}'

# Definición de la clase derivada `CuentaAhorros` que hereda de `CuentaBancaria`
class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo, tasa_interes):
        # Llamada al constructor de la clase base
        super().__init__(numero_cuenta, titular, saldo)
        # Atributo privado
        self.__tasa_interes = tasa_interes

    # Método para aplicar intereses al saldo de la cuenta
    def aplicar_interes(self):
        interes = self._saldo * self.__tasa_interes / 100
        self._saldo += interes
        print(f'Interés de {interes} aplicado. Nuevo saldo: {self._saldo}')

    # Método sobrescrito para mostrar la información de la cuenta de ahorros (polimorfismo)
    def mostrar_info(self):
        return f'Número de cuenta: {self._numero_cuenta}, Titular: {self._titular}, Saldo: {self._saldo}, Tasa de interés: {self.__tasa_interes}%'

# Función principal para demostrar la funcionalidad del programa
def main():
    # Crear una instancia de `CuentaBancaria` para Nicole Soto
    cuenta_nicole = CuentaBancaria('123456', 'Nicole Soto', 1500)
    print(cuenta_nicole.mostrar_info())  # Salida: Número de cuenta: 123456, Titular: Nicole Soto, Saldo: 1500
    cuenta_nicole.depositar(500)
    cuenta_nicole.retirar(200)

    # Crear una instancia de `CuentaAhorros` para Elkin Bosquez
    cuenta_elkin = CuentaAhorros('789012', 'Elkin Bosquez', 2500, 3)
    print(cuenta_elkin.mostrar_info())  # Salida: Número de cuenta: 789012, Titular: Elkin Bosquez, Saldo: 2500, Tasa de interés: 3%
    cuenta_elkin.depositar(1000)
    cuenta_elkin.retirar(500)
    cuenta_elkin.aplicar_interes()

    # Crear una instancia de `CuentaBancaria` para Daniela Cedillo
    cuenta_daniela = CuentaBancaria('345678', 'Daniela Cedillo', 1800)
    print(cuenta_daniela.mostrar_info())  # Salida: Número de cuenta: 345678, Titular: Daniela Cedillo, Saldo: 1800
    cuenta_daniela.depositar(700)
    cuenta_daniela.retirar(400)

    # Crear una instancia de `CuentaAhorros` para Camilla Gonzalez
    cuenta_camilla = CuentaAhorros('901234', 'Camilla Gonzalez', 3200, 4)
    print(cuenta_camilla.mostrar_info())  # Salida: Número de cuenta: 901234, Titular: Camilla Gonzalez, Saldo: 3200, Tasa de interés: 4%
    cuenta_camilla.depositar(1500)
    cuenta_camilla.retirar(1000)
    cuenta_camilla.aplicar_interes()

    # Crear una instancia de `CuentaAhorros` para Anahí Castillo
    cuenta_anahi = CuentaAhorros('567890', 'Anahí Castillo', 2200, 2)
    print(cuenta_anahi.mostrar_info())  # Salida: Número de cuenta: 567890, Titular: Anahí Castillo, Saldo: 2200, Tasa de interés: 2%
    cuenta_anahi.depositar(800)
    cuenta_anahi.retirar(600)
    cuenta_anahi.aplicar_interes()

if __name__ == '__main__':
    main()
