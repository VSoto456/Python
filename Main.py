# Lista de trabajadores
trabajadores = [
    {"ID": 1, "nombre": "Administrador", "edad": "X", "rut": "123456789-0"},
    {"ID": 2, "nombre": "Usuario", "edad": "Y", "rut": "012345678-9"},
    {"ID": 3, "nombre": "Test", "edad": "Z", "rut": "098765432-1"}
]


def Main():  # Funcion principal
    try:
        print(
            "Gestion de trabajadores\n"
            "1. lista de trabajadores\n"
            "2. Buscar\n"
            "3. Añadir trabajador\n"
            "4. Eliminar trabajador\n"
            "5. editar datos\n"
            "6. Salir\n"
            )
        respuesta = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Opcion no valida (Ingrese un numero)")
        Main()
    if respuesta <= 0 or respuesta > 6:
        print("Opcion no validad")
    else:
        if respuesta == 1:  # Mostrar lista de trabajadores
            for i in trabajadores:
                print(
                    f" ID: {i['ID']},"
                    f" Nombre: {i['nombre']},"
                    f" Edad: {i['edad']},"
                    f" Rut: {i['rut']}"
                    )

        elif respuesta == 2:  # Funcion de busqueda
            Busqueda()

        elif respuesta == 3:  # Añadir trabajadores
            Añadir()

        elif respuesta == 4:  # Eliminar trabajador
            Eliminar()

        elif respuesta == 5:  # Editar datos
            Editar()

        elif respuesta == 6:  # Salir
            print("Saliendo...")
            breakpoint


def Busqueda():  # Funcion de busqueda de trabajadores

    opcion = str(input(
        "Buscar por:\n"
        "1. Nombre\n"
        "2. Edad\n"
        "3. Rut\n"
        "4. ID\n"
        "5. Volver"
        "Opcion: "
        ))

    if opcion == "5":
        print("Volviendo..")
        Main()

    if opcion not in ["1", "2", "3", "4"]:
        print("Opcion no valida")
    else:
        # Buscar por nombre
        if opcion == "1":
            busqueda = input("Ingrese el nombre del trabajador\n")
            encontrado = False
            for i in trabajadores:
                if i['nombre'].lower() == busqueda.lower():
                    print(
                        "Trabajador encontrado\n"
                        f"ID: {i['ID']},"
                        f"nombre: {i['nombre']},"
                        f"edad: {i['edad']},"
                        f"rut: {i['rut']}"
                        )
                    encontrado = True
                    Busqueda()
            if not encontrado:
                print("Trabajador no encontrado")
                Busqueda()

        # Buscar por edad
        if opcion == "2":
            busqueda = input("Ingrese la edad del trabajador\n")
            encontrado = False
            for i in trabajadores:
                if i['edad'].lower() == busqueda.lower():
                    print(
                        "Trabajador encontrado\n"
                        f"ID: {i['ID']},"
                        f"nombre: {i['nombre']},"
                        f"edad: {i['edad']},"
                        f"rut: {i['rut']}"
                        )
                    encontrado = True
                    Busqueda()
            if not encontrado:
                print("Trabajador no encontrado")
                Busqueda()

        # Buscar por rut
        if opcion == "3":
            busqueda = input("Ingrese el rut del trabajador\n")
            encontrado = False
            for i in trabajadores:
                if i['rut'].lower() == busqueda.lower():
                    print(
                        "Trabajador encontrado\n"
                        f"ID: {i['ID']},"
                        f"nombre: {i['nombre']},"
                        f"edad: {i['edad']},"
                        f"rut: {i['rut']}"
                        )
                    encontrado = True
                    Busqueda()
            if not encontrado:
                print("Trabajador encontrado")
                Busqueda()

        # Busqueda por ID
        if opcion == "4":
            busqueda = input("Ingrese el ID del trabajador")
            encontrado = False
            for i in trabajadores:
                if i['ID'] == trabajadores:
                    print(
                        "Trabajador encontrado\n"
                        f"ID: {i['ID']},"
                        f"nombre: {i['nombre']},"
                        f"edad: {i['edad']},"
                        f"rut: {i['rut']}"
                        )
                    Busqueda()
            if not encontrado:
                print("Trabajador no encontrado")
                Busqueda()


def obtener_id():  # Autorrelenado en IDs
    ids_existentes = {i["ID"] for i in trabajadores}
    nuevo_id = 1
    while nuevo_id in ids_existentes:
        nuevo_id += 1
    return nuevo_id


def Añadir():  # Funcion de añadir trabajadores

    nombre = input("Nombre: ")
    edad = input("Edad: ")
    rut = input("Rut: ")
    nuevo_id = obtener_id()
    rutexistente = any(i['rut'] == rut for i in trabajadores)

    if rutexistente:
        print("Valores no validos")
        Main()

    else:
        nuevoTrabajador = {
                            "ID": nuevo_id,
                            "nombre": nombre,
                            "edad": edad,
                            "rut": rut
                            }
        trabajadores.append(nuevoTrabajador)
        trabajadores.sort(key=lambda x: x["ID"])
        print(f"Se añadio el trabajador {nombre} a la lista")
        Main()


def Eliminar():  # Funcion de eliminar trabajadores

    if not trabajadores:
        print("Lista vacia")
        Main()
    try:
        trabajador = int(input("Ingrese el ID de trabajador a eliminar: "))
    except ValueError:
        print("Trabajador no encontrado")
        Main()
    encontrado = False

    for i in trabajadores:
        if i['ID'] == trabajador:
            print(f"trabajador rut {trabajador} eliminado")
            trabajadores.remove(i)
            encontrado = True
            Main()
    if not encontrado:
        print("Trabajador no encontrado")
        Main()


def Editar():  # Funcion de editar datos

    busqueda = int(input("Ingrese el ID del trabajador: "))

    encontrado = False

    for i in trabajadores:
        if i['ID'] == busqueda:
            nombre = input("Nuevo nombre: ")
            edad = input("Edad: ")
            rut = input("Nuevo rut: ")
            i["nombre"] = nombre
            i["edad"] = edad
            i["rut"] = rut
            print("Datos editados exitosamente")
            print(
                f"ID: {i['ID']},"
                f"nombre: {i['nombre']},"
                f"edad: {i['edad']},"
                f"rut: {i['rut']}"
                )
            encontrado = True
            Main()

        if not encontrado:
            print("Trabajador no encontrado")
            Main()


while True:  # Bucle principal
    Main()
