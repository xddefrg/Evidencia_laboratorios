import unidades


def main():
    kilometros = float(input("Kilómetros: "))
    metros = unidades.kilometros_a_metros(kilometros)
    print(f"{kilometros} km equivalen a {metros} m")

    celsius = float(input("Grados Celsius: "))
    fahrenheit = unidades.celsius_a_fahrenheit(celsius)
    print(f"{celsius} °C equivalen a {fahrenheit} °F")


if __name__ == "__main__":
    main()
