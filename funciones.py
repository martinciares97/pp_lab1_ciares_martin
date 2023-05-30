import json, re, os, copy
from functools import reduce
from main import *


"""
__________________________________
PRIMER PARCIAL:
    • APELLIDO: CIARES
    • NOMBRE: MARTIN MAXIMILIANO
    • DNI: 43.014.500
__________________________________
"""


def print_menu(lista_opciones):
    print("\n------------------ MENU ------------------\n")
    for option in range(len(lista_opciones)):
        print(f"• {option+1}. {lista_opciones[option]}")


def imprimir_menu():
    """
    Imprime un menú de opciones basado en los puntos especificados.

    Returns:
        int: La opción seleccionada por el usuario.
    """
    print("------- Menú de Opciones -------")
    print("1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Mostrar estadísticas completas de un jugador seleccionado")
    print("3. Guardar estadísticas de un jugador en un archivo CSV")
    print("4. Buscar un jugador por su nombre y mostrar sus logros")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("14. Calcular el jugador con la mayor cantidad de bloqueos totales")
    print(
        "15. Mostrar jugadores con un porcentaje de tiros libres superior a un valor dado"
    )
    print(
        "16. Calcular el promedio de puntos por partido del equipo excluyendo al jugador con menos puntos"
    )
    print("17. Calcular el jugador con la mayor cantidad de logros obtenidos")
    print(
        "18. Mostrar jugadores con un porcentaje de tiros triples superior a un valor dado"
    )
    print("19. Calcular el jugador con la mayor cantidad de temporadas jugadas")
    print(
        "20. Mostrar jugadores con un porcentaje de tiros de campo superior a un valor dado"
    )
    print("---------------------------------")

    opcion = int(input("Seleccione una opción (1-20): "))
    return opcion


def menu_app(lista_jugadores):
    lista_indice_jugadores = []
    while True:
        lista_opciones = [
            "Mostrar la lista de todos los jugadores del Dream Team",
            "Mostrar estadísticas completas de un jugador seleccionado",
            "Guardar estadísticas de un jugador en un archivo CSV",
            "Buscar un jugador por su nombre y mostrar sus logros",
            "Calcular el promedio de puntos por partido de todo el equipo del Dream Team",
            "Verificar si un jugador es miembro del Salón de la Fama del Baloncesto",
            "Calcular el jugador con la mayor cantidad de rebotes totales",
            "Calcular el jugador con el mayor porcentaje de tiros de campo",
            "Calcular el jugador con la mayor cantidad de asistencias totales",
            "Mostrar jugadores que promedian más puntos por partido que un valor dado",
            "Mostrar jugadores que promedian más rebotes por partido que un valor dado",
            "Mostrar jugadores que promedian más asistencias por partido que un valor dado",
            "Calcular el jugador con la mayor cantidad de robos totales",
            "Calcular el jugador con la mayor cantidad de bloqueos totales",
            "Mostrar jugadores con un porcentaje de tiros libres superior a un valor dado",
            "Calcular el promedio de puntos por partido del equipo excluyendo al jugador con menos puntos",
            "Calcular el jugador con la mayor cantidad de logros obtenidos",
            "Mostrar jugadores con un porcentaje de tiros triples superior a un valor dado",
            "Calcular el jugador con la mayor cantidad de temporadas jugadas",
            "Mostrar jugadores con un porcentaje de tiros de campo superior a un valor dado",
            "",
            "",
            "BONUS: Calcular posición en cada ranking y exportar a CSV",
        ]
        print_menu(lista_opciones)
        option = ingresar_opcion()
        separador()
        match (option):
            case "1":
                mostrar_lista_jugadores(lista_jugadores)
            case "2":
                mostrar_estadisticas_completas(lista_jugadores, lista_indice_jugadores)
            case "3":
                guardar_estadisticas_en_csv(lista_jugadores, lista_indice_jugadores)
            case "4":
                mostrar_logros_jugador(lista_jugadores, "logros")
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case "10":
                pass
            case "11":
                pass
            case "12":
                pass
            case "13":
                pass
            case "14":
                pass
            case "15":
                pass
            case "16":
                pass
            case "17":
                pass
            case "18":
                pass
            case "19":
                pass
            case "20":
                pass
            case "21":
                pass
            case "22":
                pass
            case "23":
                llamada_punto_23(lista_jugadores)
            case "0":
                break
        limpiar_consola()


def limpiar_consola() -> None:
    """
    Limpia la consola luego de presionar Enter.

    Args:
        None

    Return:
        None
    """
    separador()
    input("\nPresiona Enter para continuar...")
    if os.name == "nt":
        os.system("cls")


def crear_lista_jugadores() -> list:
    """
    Crea una lista de jugadores a partir de un archivo.json

    Args:
        None

    Return:
        list: Una lista de jugadores
    """
    path = r"C:\Users\mciar\OneDrive\Documentos\UTN\01_primer_cuatrimestre\laboratorio_programacion_1\clase_05_23_parcial\dt.json"
    return parse_json(path, "jugadores")


def parse_json(nombre_archivo: str, key: str) -> list:
    """
    Carga un archivo JSON y devuelve el valor asociado a una clave específica.

    Args:
        nombre_archivo (str): Una cadena de texto que representa el nombre del archivo JSON a cargar.
        key (str): Una cadena de texto que representa la clave cuyo valor se desea extraer del archivo JSON.

    Return:
        Una lista que contiene el valor asociado a la clave especificada.

    Exception:
        Si ocurre algún error al cargar el archivo JSON, se muestra el mensaje "Error. No se pudo cargar
        el JSON".
    """

    try:
        lista_jugadores = []
        with open(nombre_archivo, "r") as archivo:
            datos_cargados = json.load(archivo)
            if key in datos_cargados:
                lista_jugadores = datos_cargados[key]
            else:
                print(f"No se encontro la clave {key} en el JSON")
            return lista_jugadores
    except Exception:
        print("Error. No se pudo cargar el JSON")


def ingresar_opcion():
    """
    Permite ingresar una de las opciones de la app

    Args:
        None
    Return:
        opcion (str): Opcion ingresada y validada.
    """
    while True:
        opcion = input("\nIngrese una de las opciones: ")
        if validar_ingreso_por_teclado(r"^[0-9]+$", opcion):
            return opcion
        else:
            print("No se ingreso una opción valida. Intente nuevamente\n")


def validar_ingreso_por_teclado(patron: str, cadena: str):
    """
    Valida el ingreso por teclado de acuerdo a un patrón dado.

    Args:
        patron (str): Patrón de expresión regular.
        cadena (str): Cadena de texto a validar.

    Returns:
        bool: True si la cadena coincide con el patrón, False en caso contrario.
    """
    flag_validate = False
    if re.match(patron, cadena):
        flag_validate = True
    return flag_validate


def separador():
    """
    Imprime una línea de guiones como separador.
    """
    print("__________________________________________________")


def reemplazar_guion_bajo(cadena: str):
    """
    Reemplaza los guiones de una cadena de texto
    """
    return cadena.replace("_", " ").capitalize()


"--------------------------------------- EJERCICIOS ---------------------------------------"


# 1º --------------------------------------------------------------------
def mostrar_lista_jugadores(lista_jugadores: list) -> None:
    """
    Muestra la plantilla de jugadores del Dream Team

    Args:
        lista_jugadores (list): La lista de jugadores a imprimir.

    Return:
        None
    """
    print(f'\n{"nombre"} {"posicion"}'.upper())
    for jugador in lista_jugadores:
        print(jugador["nombre"], jugador["posicion"])


# 2º ---------------------------------------------------------------------
def mostrar_indices_de_jugadores(lista_jugador: list) -> None:
    """
    Muestra los índices y nombres de los jugadores en una lista.

    Argumentos:
        lista_jugador (list): Una lista de jugadores.

    Retorno:
        None
    """
    if len(lista_jugador) != 0:
        print(f"INDICE - NOMBRE\n")
        for indice in range(len(lista_jugador)):
            print("{0} - {1}".format(indice, lista_jugador[indice]["nombre"]))
    else:
        print("La lista se encuentra vacia.")


def seleccionar_jugador_por_indice(lista_jugadores: list) -> dict:
    """
    Permite al usuario seleccionar un jugador de una lista y devuelve un diccionario con sus estadísticas.

    Args:
        lista_jugadores (list): Una lista de jugadores.

    Return:
        dict: Un diccionario con las estadísticas del jugador seleccionado.
    """
    while True:
        mostrar_indices_de_jugadores(lista_jugadores)
        indice_ingresado = input(
            "\nIngrese el indice de un jugador para ver sus estadisticas: "
        )
        if validar_ingreso_por_teclado(r"^[0-9]+$", indice_ingresado):
            indice_ingresado = int(indice_ingresado)
            if indice_ingresado < len(lista_jugadores):
                break
            else:
                print(
                    "El indice ingresado se encuentra fuera de rango. MAX {0}".format(
                        len(lista_jugadores)
                    )
                )
        else:
            print("El indice ingresado no es valido. Intente nuevamente")
            separador()
    return indice_ingresado


def mostrar_estadisticas_completas(
    lista_jugadores: list, list_indice_jugadores: list
) -> dict:
    """
    Muestra las estadísticas completas de un jugador seleccionado.

    Argumentos:
        lista_jugadores (list): Una lista de jugadores.
        list_indice_jugadores (list): Una lista que almacena los índices de los jugadores seleccionados.

    Retorno:
        dict: Un diccionario con las estadísticas del jugador seleccionado.
    """
    indice_jugador = seleccionar_jugador_por_indice(lista_jugadores)
    if indice_jugador not in list_indice_jugadores:
        list_indice_jugadores.append(indice_jugador)
    dict_estadisticas = lista_jugadores[indice_jugador]["estadisticas"]
    print(
        "\nESTADISTICAS DE {0}\n".format(
            lista_jugadores[indice_jugador]["nombre"]
        ).upper()
    )

    for estadistica, valor in dict_estadisticas.items():
        print(reemplazar_guion_bajo(estadistica), valor)


# 3 -----------------------------------------------------------------------------
def exportar_archivo_csv(nombre_archivo: str, jugador: list):
    """
    Exporta las estadísticas de un jugador a un archivo CSV.

    Argumentos:
        nombre_archivo (str): El nombre del archivo CSV a exportar.
        jugador (list): Una lista que contiene la información del jugador y sus estadísticas.

    Retorno:
        None
    """
    with open(nombre_archivo, "w+") as archivo:
        formato_encabezado = "nombre,posicion,temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,promedio_rebotes_por_partido,asistencias_totales,promedio_asistencias_por_partido,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples\n"
        formato_csv = formato_encabezado + (
            "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}\n".format(
                jugador["nombre"],
                jugador["posicion"],
                jugador["estadisticas"]["temporadas"],
                jugador["estadisticas"]["puntos_totales"],
                jugador["estadisticas"]["promedio_puntos_por_partido"],
                jugador["estadisticas"]["rebotes_totales"],
                jugador["estadisticas"]["promedio_rebotes_por_partido"],
                jugador["estadisticas"]["asistencias_totales"],
                jugador["estadisticas"]["promedio_asistencias_por_partido"],
                jugador["estadisticas"]["robos_totales"],
                jugador["estadisticas"]["bloqueos_totales"],
                jugador["estadisticas"]["porcentaje_tiros_de_campo"],
                jugador["estadisticas"]["porcentaje_tiros_libres"],
                jugador["estadisticas"]["porcentaje_tiros_triples"],
            )
        )
        archivo.write(formato_csv)


def crear_nombre_csv(nombre_jugador: str):
    return f"{nombre_jugador}.csv"


def guardar_estadisticas_en_csv(lista_jugadores: list, lista_indice_jugadores: list):
    for indice in range(len(lista_indice_jugadores)):
        print(
            "{0} - {1}".format(
                lista_indice_jugadores[indice],
                lista_jugadores[lista_indice_jugadores[indice]]["nombre"],
            )
        )
    if len(lista_indice_jugadores) != 0:
        indice_ingresado = input("\nIngrese el indice que desea guardar: ")
        if validar_ingreso_por_teclado(r"^[0-9]+$", indice_ingresado):
            indice_ingresado = int(indice_ingresado)
            exportar_archivo_csv(
                crear_nombre_csv(lista_jugadores[indice_ingresado]["nombre"]),
                lista_jugadores[indice_ingresado],
            )


# 4 -------------------------------------------------------------------------------
def buscar_jugador_por_nombre(lista_jugadores: list):
    """
    Busca jugadores por su nombre en una lista y devuelve una lista con los jugadores encontrados.

    Argumentos:
        lista_jugadores (list): Una lista de jugadores.

    Retorno:
        list: Una lista con los jugadores encontrados por nombre.
    """
    lista_jugadores_por_nombre = []
    nombre_in_lista = False
    while True:
        nombre_ingresado = input(
            "Ingrese el nombre de el jugador para ver sus logros: "
        )
        if validar_ingreso_por_teclado(r"^[a-zA-Z ]+$", nombre_ingresado):
            for indice in range(len(lista_jugadores)):
                if re.search(
                    f"({nombre_ingresado})",
                    lista_jugadores[indice]["nombre"],
                    re.IGNORECASE,
                ):
                    lista_jugadores_por_nombre.append(lista_jugadores[indice])
                    nombre_in_lista = True
            if nombre_in_lista:
                return lista_jugadores_por_nombre
            print(f"No se encontro {nombre_ingresado} en la lista de jugadores")
        else:
            print("Nombre no valido. Intente nuevamente")


def mostrar_logros_jugador(lista_jugadores, key):
    """
    Muestra los logros de los jugadores encontrados por nombre.

    Argumentos:
        lista_jugadores (list): Una lista de jugadores.
        key (str): La clave para acceder a los logros del jugador.

    Retorno:
        None
    """
    jugadores_encontrados_por_nombre = buscar_jugador_por_nombre(lista_jugadores)
    print_logros_de_jugador(jugadores_encontrados_por_nombre, key)


def print_logros_de_jugador(lista_jugadores_encontrados: list, key: str) -> None:
    """
    Muestra los logros de los jugadores encontrados.

    Argumentos:
        lista_jugadores_encontrados (list): Una lista de jugadores encontrados.
        key (str): La clave para acceder a los logros del jugador.

    Retorno:
        None
    """
    for jugador in lista_jugadores_encontrados:
        print(f"\n------- {key} DE {jugador['nombre'].upper()} --------")
        logros_del_jugador = jugador[key]
        for logro in logros_del_jugador:
            print(f"{logro}")


# 5 ------------------------------------------------------------------------------


def bubble_sort_lite(main_list: list, key: str, sentido: str):
    for indice in range(len(main_list) - 1):
        if sentido == "mayor":
            if (
                main_list[indice]["estadisticas"][key]
                > main_list[indice + 1]["estadisticas"][key]
            ):
                main_list[indice], main_list[indice + 1] = (
                    main_list[indice + 1],
                    main_list[indice],
                )
        elif sentido == "desc":
            if (
                main_list[indice]["estadisticas"][key]
                < main_list[indice + 1]["estadisticas"][key]
            ):
                main_list[indice], main_list[indice + 1] = (
                    main_list[indice + 1],
                    main_list[indice],
                )


def bubble_sort_lite_v2(main_list: list, key: str, sentido: str):
    for indice in range(len(main_list) - 1):
        if len(main_list[indice][key]) > len(main_list[indice + 1][key]):
            main_list[indice], main_list[indice + 1] = (
                main_list[indice + 1],
                main_list[indice],
            )


def quick_sort_v2(main_list: list, key: str, sentido: str) -> list:
    """
    Se encarga de ordenar listas segun la llave

    Args:
        main_list (list)
        key: (str)
        sentido: (str)

    Return:
        left_list: (list)
    """
    # normalizar_datos() no es necesario en este caso
    if len(main_list) <= 1:
        return main_list
    left_list = []
    right_list = []
    pivot = main_list[0]

    for player in main_list[1:]:
        if sentido == "asc":
            if player["estadisticas"][key] > pivot["estadisticas"][key]:
                right_list.append(player)
            else:
                left_list.append(player)
        elif sentido == "desc":
            if player["estadisticas"][key] < pivot["estadisticas"][key]:
                right_list.append(player)
            else:
                left_list.append(player)
    left_list = quick_sort_v2(left_list, key, sentido)
    left_list.append(pivot)
    right_list = quick_sort_v2(right_list, key, sentido)
    left_list.extend(right_list)

    return left_list


def quick_sort(main_list: list, key: str, sentido: str) -> list:
    """
    Se encarga de ordenar listas segun la llave

    Args:
        main_list (list)
        key: (str)
        sentido: (str)

    Return:
        left_list: (list)
    """
    # normalizar_datos() no es necesario en este caso
    if len(main_list) <= 1:
        return main_list
    left_list = []
    right_list = []
    pivot = main_list[0]

    for player in main_list[1:]:
        if sentido == "asc":
            if player["estadisticas"][key] > pivot["estadisticas"][key]:
                right_list.append(player)
            else:
                left_list.append(player)
        elif sentido == "desc":
            if player["estadisticas"][key] < pivot["estadisticas"][key]:
                right_list.append(player)
            else:
                left_list.append(player)
    left_list = quick_sort(left_list, key, sentido)
    left_list.append(pivot)
    right_list = quick_sort(right_list, key, sentido)
    left_list.extend(right_list)

    return left_list


def calcular_promedio_de_puntos_por_partido(lista_jugadores: list):
    """
    Calcular el promedio de puntos por partido de todo el equipo del Dream Team
    """
    return list(
        reduce(
            lambda acumulador, jugador: acumulador
            + jugador["promedio_puntos_por_partido"],
            lista_jugadores,
            0,
        )
    ) / len(lista_jugadores)


def mostrar_promedio_de_puntos_por_partido(main_list):
    """
    Muestra el promedio de puntos por partido de todo el equipo del Dream Team,
    ordenado por nombre de manera ascendente.
    """
    promedio = calcular_promedio_de_puntos_por_partido(main_list)
    sort_list = quick_sort(main_list, "nombre", "asc")

    print(f"\nPromedio de puntos por partido de todo el Dream Team: {promedio}")
    for player in sort_list:
        print(player["nombre"], player["estadisticas"]["promedio_puntos_por_partido"])


# 23 BONUS ---------------------------------------------------------------------------
def exportar_tabla_posiciones_csv(lista_jugadores: list, nombre_archivo: str) -> None:
    """
    Calcula la posición de cada jugador en los rankings de puntos, rebotes, asistencias y robos,
    y exporta los resultados a un archivo CSV.

    Args:
        lista_jugadores (list): Una lista de jugadores representados como diccionarios.
                                Cada jugador contiene un nombre y estadísticas de puntos, rebotes, asistencias y robos.

    Returns:
        None
    """
    with open(nombre_archivo, "a") as archivo:
        formato_csv = "{0},{1},{2},{3},{4}\n".format(
            lista_jugadores[0],
            lista_jugadores[1],
            lista_jugadores[2],
            lista_jugadores[3],
            lista_jugadores[4],
        )
        archivo.write(formato_csv)


def calcular_posicion(lista_jugadores: list, key: str, indice_jugador: int) -> int:
    """
    Calcula la posición de un jugador en un ranking específico basado en una clave de estadística.

    Args:
        lista_jugadores (list): Una lista de jugadores representados como elementos de la lista.
        key (str): La clave de estadística para la cual se calculará la posición del jugador en el ranking.
        indice_jugador (int): El índice del jugador para el cual se calculará la posición.

    Returns:
        int: La posición del jugador en el ranking especificado.
    """
    posicion_jugador = 0
    left_list = quick_sort_v2(lista_jugadores, key, "desc")

    for indice in range(len(left_list)):
        if (
            left_list[indice]["estadisticas"][key]
            == lista_jugadores[indice_jugador]["estadisticas"][key]
        ):
            posicion_jugador = indice + 1

    return posicion_jugador


def llamada_punto_23(lista_jugadores: list) -> None:
    """
    Calcula la posición de cada jugador en los rankings de puntos, rebotes, asistencias y robos,
    y exporta los resultados a un archivo CSV.

    Args:
        lista_jugadores (list): Una lista de jugadores representados como diccionarios.
                                Cada jugador contiene un nombre y estadísticas de puntos, rebotes, asistencias y robos.

    Returns:
        None
    """
    lista_encabezado = ["Nombre", "Puntos", "Rebotes", "Asistencias", "Robos"]
    exportar_tabla_posiciones_csv(lista_encabezado, "ranking_de_posiciones.csv")

    for indice in range(len(lista_jugadores)):
        lista_jugador_posiciones = []
        lista_jugador_posiciones.append(lista_jugadores[indice]["nombre"])
        lista_jugador_posiciones.append(
            calcular_posicion(lista_jugadores, "puntos_totales", indice)
        )
        lista_jugador_posiciones.append(
            calcular_posicion(lista_jugadores, "rebotes_totales", indice)
        )
        lista_jugador_posiciones.append(
            calcular_posicion(lista_jugadores, "asistencias_totales", indice)
        )
        lista_jugador_posiciones.append(
            calcular_posicion(lista_jugadores, "robos_totales", indice)
        )
        separador()
        print(indice)
        print(lista_jugador_posiciones)
        exportar_tabla_posiciones_csv(
            lista_jugador_posiciones, "ranking_de_posiciones.csv"
        )


"--------------------------------------- MAIN ---------------------------------------"


def main():
    main_list = crear_lista_jugadores()
    deep_copy = copy.deepcopy(main_list)
    menu_app(deep_copy)


if __name__ == "__main__":
    main()
