# Lista de trabajadores
trabajadores = [
    {"nombre": "Pedro", "edad": "27", "rut": "123456789-0"},
    {"nombre": "Juan", "edad": "51", "rut": "123456789-k"},
    {"nombre": "Benja", "edad": "18", "rut": "098765432-1"}
]

def Main():
    try:
        respuesta = int(input("Gestion de trabajadores\n1. lista de trabajadores\n2. Buscar nombre, edad o rut\n3. Salir\n"))
    except ValueError:
        print("Opcion no valida (Ingrese un numero)")
        Main()
    if respuesta <= 0 or respuesta > 3:
        print("Opcion no validad")
    else:
        if respuesta == 1: # Mostrar lista de trabajadores
            for i in trabajadores:
                print(f"nombre: {i['nombre']}, edad: {i['edad']}, Rut: {i['rut']}")
        elif respuesta == 2: # Funcion de busqueda
            Busqueda()
        elif respuesta == 3: # Salir
            print("Saliendo...")
            breakpoint

def Busqueda():
    opcion = str(input("Buscar por:\n1. Nombre\n2. Edad\n3. Rut\n4. Volver\n"))

    if opcion == "4":
        print("Volviendo..")
        Main()

    if opcion not in ["1", "2", "3"]:
        print("Opcion no valida")
    else:
        # Buscar por nombre
        if opcion == "1":
            busqueda = input("Ingrese el nombre del trabajador\n")
            encontrado = False
            for i in trabajadores:
                if i['nombre'].lower() == busqueda.lower():
                    print(f"Trabajador encontrado\nnombre: {i['nombre']}, edad: {i['edad']}, Rut: {i['rut']}")
                    encontrado = True
                    Busqueda()
            if not encontrado:
                print("Trabajador no encontrado")

        # Buscar por edad
        if opcion == "2":
            busqueda = input("Ingrese la edad del trabajador\n")
            encontrado = False
            for i in trabajadores:
                if i['edad'].lower() == busqueda.lower():
                    print(f"Trabajador encontrado\nnombre: {i['nombre']}, edad: {i['edad']}, rut: {i['rut']}")
                    encontrado = True
                    Busqueda()
            if not encontrado:
                print("Trabajador no encontrado")

        if opcion == "3":
            busqueda = input("Ingrese el rut del trabajador\n")
            encontrado = False
            for i in trabajadores:
                if i['rut'].lower() == busqueda.lower():
                    print(f"Trabajador encontrado\nnombre: {i['nombre']}, edad: {i['edad']}, rut: {i['rut']}")
                    encontrado = True
                    Busqueda()
            if not encontrado:
                print("Trabajador encontrado")

while True: 
    Main()