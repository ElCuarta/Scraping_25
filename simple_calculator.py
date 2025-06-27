"""Calculadora simple en Python.

Este programa permite realizar operaciones basicas de suma, resta,
multiplicacion y division. Tambien mantiene un historial de
operaciones realizadas y ofrece opciones para borrar la ultima
operacion (borrado simple) o borrar todo el historial (borrado final).
"""


def add(a, b):
    """Devuelve la suma de `a` y `b`."""
    return a + b


def subtract(a, b):
    """Devuelve la resta de `b` a `a`."""
    return a - b


def multiply(a, b):
    """Devuelve la multiplicacion de `a` y `b`."""
    return a * b


def divide(a, b):
    """Devuelve la division de `a` entre `b`. Si `b` es cero,
    se lanza una excepcion ValueError.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


class Calculator:
    """Clase que gestiona las operaciones y su historial."""

    def __init__(self):
        self.history = []  # Lista para guardar las operaciones realizadas

    def perform_operation(self, op, a, b):
        """Realiza la operacion indicada y guarda el resultado en el historial."""
        if op == '+':
            result = add(a, b)
            expression = f"{a} + {b} = {result}"
        elif op == '-':
            result = subtract(a, b)
            expression = f"{a} - {b} = {result}"
        elif op == '*':
            result = multiply(a, b)
            expression = f"{a} * {b} = {result}"
        elif op == '/':
            result = divide(a, b)
            expression = f"{a} / {b} = {result}"
        else:
            raise ValueError("Operacion no soportada")

        # Guardamos en el historial
        self.history.append(expression)
        return result

    def clear_last(self):
        """Elimina la ultima operacion del historial, si existe."""
        if self.history:
            self.history.pop()

    def clear_all(self):
        """Limpia por completo el historial de operaciones."""
        self.history.clear()

    def show_history(self):
        """Devuelve el historial completo como una cadena."""
        if not self.history:
            return "Sin operaciones registradas"
        return "\n".join(self.history)


def main():
    """Interfaz interactiva de la calculadora."""
    calc = Calculator()
    menu = (
        "\nSelecciona una opcion:\n"
        "1) Sumar\n"
        "2) Restar\n"
        "3) Multiplicar\n"
        "4) Dividir\n"
        "5) Borrado simple (elimina la ultima operacion)\n"
        "6) Borrado final (limpia todo el historial)\n"
        "7) Ver historial\n"
        "8) Salir\n"
    )

    while True:
        choice = input(menu)

        if choice == '1':
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
            resultado = calc.perform_operation('+', a, b)
            print(f"Resultado: {resultado}")
        elif choice == '2':
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
            resultado = calc.perform_operation('-', a, b)
            print(f"Resultado: {resultado}")
        elif choice == '3':
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
            resultado = calc.perform_operation('*', a, b)
            print(f"Resultado: {resultado}")
        elif choice == '4':
            a = float(input("Ingresa el primer numero: "))
            b = float(input("Ingresa el segundo numero: "))
            try:
                resultado = calc.perform_operation('/', a, b)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            calc.clear_last()
            print("Ultima operacion eliminada")
        elif choice == '6':
            calc.clear_all()
            print("Historial eliminado")
        elif choice == '7':
            print("--- Historial ---")
            print(calc.show_history())
        elif choice == '8':
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida. Intenta de nuevo")


if __name__ == "__main__":
    main()
