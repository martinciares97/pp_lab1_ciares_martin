import json
import re
import os
import copy
import platform
import time
from functools import reduce

"""
PRIMER PARCIAL

Apellido: Ciares
Nombre: Martin Maximiliano
DNI: 43014500
"""


def limpiar_consola():
    """
    Limpia la consola según el sistema operativo.

    No recibe argumentos.

    No retorna ningún valor.
    """
    input("\nPresione Enter para continuar...")
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


def limpiar_pantalla():
    """
    Limpia la pantalla según el sistema operativo y añade un retraso.

    No recibe argumentos.

    No retorna ningún valor.
    """
    if platform.system() == "Windows":
        os.system("cls & echo.")
        time.sleep(0.1)
    else:
        os.system("clear; printf '\033c'")
        time.sleep(0.1)


def parse_json(nombre_archivo: str):
    """
    Parsea un archivo JSON y devuelve una lista de jugadores.

    Args:
        nombre_archivo (str): El nombre del archivo JSON a parsear.

    Returns:
        list: Una lista de jugadores.
    """
    lista = []
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        diccionario = json.load(file)
        lista = diccionario["jugadores"]
        return lista


# /////////////////////////////////// EJERCICIOS /////////////////////////////////////////
def mostrar_lista_jugadores(lista_jugadores: list) -> None:
    """
    Muestra la lista de todos los jugadores del equipo.

    Args:
        lista_jugadores (list): Una lista de jugadores.

    Returns:
        None
    """
    print("NOMBRE JUGADOR - POSICIÓN\n")
    for player in lista_jugadores:
        print(f"{player['nombre']} - {player['posicion']}")


def mostrar_estadisticas_por_jugador(lista_jugadores: list) -> int:
    """
    Muestra las estadísticas de un jugador específico y devuelve su índice en la lista.

    Args:
        lista_jugadores (list): Una lista de jugadores.

    Returns:
        int: El índice del jugador en la lista.
    """
    while True:
        indice = input(
            "Ingrese el indice del jugador que deseas mostrar sus estadisticas: "
        )
        if re.match(r"^[0-9]+$", indice):
            indice = int(indice)
            if indice < len(lista_jugadores):
                player = lista_jugadores[indice]["estadisticas"]

                print(f'ESTADISTICAS DE {lista_jugadores[indice]["nombre"].upper()}\n')
                for clave, valor in player.items():
                    print(f"{reemplazar_guion_bajo(clave)} {valor}")
                return indice


def definir_nombre_archivo(lista_jugadores: list, indice: int):
    """
    Define el nombre del archivo CSV según el nombre del jugador.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        indice_jugador (int): El índice del jugador en la lista.

    Returns:
        str: El nombre del archivo CSV.
    """
    nombre_archivo = f'{lista_jugadores[indice]["nombre"]}.csv'
    return nombre_archivo


def guardar_estadisticas_jugador(lista_jugadores: list):
    """
    Guarda las estadísticas de un jugador en un archivo CSV.

    Args:
        lista_jugadores (list): Una lista de jugadores.

    Returns:
        None
    """
    indice_player = mostrar_estadisticas_por_jugador(lista_jugadores)
    nombre_archivo = definir_nombre_archivo(lista_jugadores, indice_player)
    exportar_csv(nombre_archivo, lista_jugadores, indice_player)


def exportar_csv(nombre_archivo: str, lista_jugadores: list, indice: int):
    """
    Exporta las estadísticas de un jugador a un archivo CSV.

    Args:
        nombre_archivo (str): El nombre del archivo CSV.
        lista_jugadores (list): Una lista de jugadores.
        indice (int): El índice del jugador en la lista.

    Returns:
        None
    """
    with open(nombre_archivo, "w+", encoding="utf-8") as file:
        formato_encabezado = "nombre,posicion,temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,promedio_rebotes_por_partido,asistencias_totales,promedio_asistencias_por_partido,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples\n"
        formato_mensaje = formato_encabezado + (
            "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}\n".format(
                lista_jugadores[indice]["nombre"],
                lista_jugadores[indice]["posicion"],
                lista_jugadores[indice]["estadisticas"]["temporadas"],
                lista_jugadores[indice]["estadisticas"]["puntos_totales"],
                lista_jugadores[indice]["estadisticas"]["promedio_puntos_por_partido"],
                lista_jugadores[indice]["estadisticas"]["rebotes_totales"],
                lista_jugadores[indice]["estadisticas"]["promedio_rebotes_por_partido"],
                lista_jugadores[indice]["estadisticas"]["asistencias_totales"],
                lista_jugadores[indice]["estadisticas"][
                    "promedio_asistencias_por_partido"
                ],
                lista_jugadores[indice]["estadisticas"]["robos_totales"],
                lista_jugadores[indice]["estadisticas"]["bloqueos_totales"],
                lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
                lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_libres"],
                lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_triples"],
            )
        )
        file.write(formato_mensaje)


def validar_nombre_jugador(nombre_jugador: str) -> bool:
    """
    Valida que el nombre de un jugador solo contenga letras y espacios.

    Args:
        nombre_jugador (str): El nombre del jugador a validar.

    Returns:
        bool: True si el nombre es válido, False en caso contrario.
    """
    flag_retorno = True
    if re.search(r"[^a-zA-Z ]", nombre_jugador):
        flag_retorno = False
    return flag_retorno


def buscar_jugador_por_nombre(lista_jugadores: list) -> list:
    """
    Busca jugadores por nombre y devuelve una lista con los jugadores encontrados.

    Args:
        lista_jugadores (list): Una lista de jugadores.

    Returns:
        list: Una lista de jugadores encontrados.
    """
    nombre = input("Ingrese el nombre que desea buscar: ")
    lista_jugadores_por_nombre = []
    if validar_nombre_jugador(nombre) == True:
        for player in lista_jugadores:
            if re.search(f"({nombre})", player["nombre"], re.IGNORECASE):
                lista_jugadores_por_nombre.append(player)
        if len(lista_jugadores_por_nombre) == 0:
            print("No se encontraron coincidencias.")
    else:
        print("No se ingreso un nombre valido.")
    return lista_jugadores_por_nombre


def print_logros_de_jugador(lista_jugadores: list) -> None:
    """
    Imprime los logros de un jugador.

    Args:
        lista_jugadores (list): Una lista de jugadores.

    Returns:
        None
    """
    for player in lista_jugadores:
        print(f"\n------- LOGROS DE {player['nombre'].upper()} --------")
        logros_del_jugador = player["logros"]
        for logro in logros_del_jugador:
            print(f"{logro}")


def mostrar_logros_del_jugador(lista_jugadores: list):
    """
    4) Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como
    campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la
    Fama del Baloncesto, etc.
    """
    lista_jugadores_por_nombre = buscar_jugador_por_nombre(lista_jugadores)
    print_logros_de_jugador(lista_jugadores_por_nombre)


""" 
def bubble_sort(lista_jugadores: list, key: str, sentido: str):
    flag_swap = True
    rango = len(lista_jugadores)
    while flag_swap:
        rango = rango - 1
        flag_swap = False
        for indice in range(rango):
            if sentido == "mayor":
                if (
                    lista_jugadores[indice]["estadisticas"][key]
                    > lista_jugadores[indice + 1]["estadisticas"][key]
                ):
                    lista_jugadores[indice], lista_jugadores[indice + 1] = (
                        lista_jugadores[indice + 1],
                        lista_jugadores[indice],
                    )
            else:
                if (
                    lista_jugadores[indice]["estadisticas"][key]
                    < lista_jugadores[indice + 1]["estadisticas"][key]
                ):
                    lista_jugadores[indice], lista_jugadores[indice + 1] = (
                        lista_jugadores[indice + 1],
                        lista_jugadores[indice],
                    )
 """


def bubble_sort_lite(lista_jugadores: list, key: str, sentido: str):
    """
    Ordena una lista de jugadores utilizando el algoritmo Bubble Sort de forma simplificada.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        key (str): La clave para acceder al valor que se utilizará para ordenar.
        sentido (str): El sentido de ordenamiento ("mayor" o "desc").

    Returns:
        None
    """
    for indice in range(len(lista_jugadores) - 1):
        if sentido == "mayor":
            if (
                lista_jugadores[indice]["estadisticas"][key]
                > lista_jugadores[indice + 1]["estadisticas"][key]
            ):
                lista_jugadores[indice], lista_jugadores[indice + 1] = (
                    lista_jugadores[indice + 1],
                    lista_jugadores[indice],
                )
        elif sentido == "desc":
            if (
                lista_jugadores[indice]["estadisticas"][key]
                < lista_jugadores[indice + 1]["estadisticas"][key]
            ):
                lista_jugadores[indice], lista_jugadores[indice + 1] = (
                    lista_jugadores[indice + 1],
                    lista_jugadores[indice],
                )


def bubble_sort_lite_v2(lista_jugadores: list, key: str, sentido: str):
    """
    Ordena una lista de jugadores utilizando el algoritmo Bubble Sort de forma simplificada.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        key (str): La clave para acceder al valor que se utilizará para ordenar.
        sentido (str): El sentido de ordenamiento ("mayor" o "desc").

    Returns:
        None
    """
    for indice in range(len(lista_jugadores) - 1):
        if len(lista_jugadores[indice][key]) > len(lista_jugadores[indice + 1][key]):
            lista_jugadores[indice], lista_jugadores[indice + 1] = (
                lista_jugadores[indice + 1],
                lista_jugadores[indice],
            )


def quick_sort(lista_jugadores: list, key: str, sentido: str) -> list:
    """
    Se encarga de ordenar listas segun la llave

    Args:
        lista_jugadores (list)
        key: (str)
        sentido: (str)

    Return:
        left_list: (list)
    """
    # normalizar_datos() no es necesario en este caso
    if len(lista_jugadores) <= 1:
        return lista_jugadores
    left_list = []
    right_list = []
    pivot = lista_jugadores[0]

    for player in lista_jugadores[1:]:
        if sentido == "asc":
            if player[key] > pivot[key]:
                right_list.append(player)
            else:
                left_list.append(player)
        elif sentido == "desc":
            if player[key] < pivot[key]:
                right_list.append(player)
            else:
                left_list.append(player)
    left_list = quick_sort(left_list, key, sentido)
    left_list.append(pivot)
    right_list = quick_sort(right_list, key, sentido)
    left_list.extend(right_list)

    return left_list


def quick_sort_v2(lista_jugadores: list, key: str, sentido: str) -> list:
    """
    Se encarga de ordenar listas segun la llave

    Args:
        lista_jugadores (list)
        key: (str)
        sentido: (str)

    Return:
        left_list: (list)
    """
    # normalizar_datos() no es necesario en este caso
    if len(lista_jugadores) <= 1:
        return lista_jugadores
    left_list = []
    right_list = []
    pivot = lista_jugadores[0]

    for player in lista_jugadores[1:]:
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


def calcular_promedio_de_puntos_por_partido(lista_jugadores: list) -> float:
    """
    Calcula el promedio de puntos por partido para una lista de jugadores.

    Args:
        lista_jugadores (list): Una lista de jugadores.

    Returns:
        float: El promedio de puntos por partido.
    """
    return (
        reduce(
            lambda acumulador, player: acumulador
            + player["estadisticas"]["promedio_puntos_por_partido"],
            lista_jugadores,
            0,
        )
    ) / len(lista_jugadores)


def mostrar_promedio_de_puntos_por_partido(lista_jugadores):
    """
    Muestra el promedio de puntos por partido para todos los jugadores del Dream Team,
    ordenados alfabéticamente por nombre.

    Args:
        lista_jugadores (list): Una lista de jugadores.
    """
    promedio = calcular_promedio_de_puntos_por_partido(lista_jugadores)
    sort_list = quick_sort(lista_jugadores, "nombre", "asc")

    print(f"\nPromedio de puntos por partido de todo el Dream Team: {promedio}")
    for player in sort_list:
        print(player["nombre"], player["estadisticas"]["promedio_puntos_por_partido"])


def mostrar_si_es_miembro(lista_jugadores: list) -> None:
    """
    Muestra si un jugador es miembro del Salón de la Fama del Baloncesto.

    Args:
        lista_jugadores (list): Una lista de jugadores.
    """
    flag_in_lista = False
    nombre_jugador = input(
        "Ingrese el nombre del jugador para saber si es miembro del Salón de la Fama del Baloncesto: "
    )
    if validar_nombre_jugador(nombre_jugador):
        for player in lista_jugadores:
            if player["nombre"] == nombre_jugador:
                if "Miembro del Salon de la Fama del Baloncesto" in player["logros"]:
                    flag_in_lista = True
                    break
        if flag_in_lista == True:
            message = f"{nombre_jugador} es miembro del Salón de la Fama del Baloncesto"
        else:
            message = print(f"{nombre_jugador} no es miembro.")
        print(message)


def mostrar_jugador_con_la_mejor_estadistica(lista_jugadores: list, key: str):
    """
    Muestra el jugador con la mejor estadística en la categoría especificada.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        key (str): La categoría de estadística (por ejemplo, "puntos_totales", "rebotes_totales", etc.).
    """
    print(
        f"""\nJUGADOR CON MAS {key.upper()}
          {lista_jugadores[-1]['nombre']} {lista_jugadores[-1]['estadisticas'][key]} {key}"""
    )


def separador():
    """
    Imprime un separador visual en la consola.
    """
    print("_____________________________________________________")


def calcular_jugador_con_la_mejor_estadistica(lista_jugadores: list, key: str):
    """
    7|8|9) Calcular y mostrar el jugador con la mayor estadistica.

    Args:
        lista_jugadores: (list)
        key: (str)

    Return:
        None
    """
    bubble_sort_lite(lista_jugadores, key, "mayor")
    separador()
    mostrar_jugador_con_la_mejor_estadistica(lista_jugadores, key)


def mostrar_jugadores_con_promedio_mayor(lista_filtrada: list, key: str):
    """
    Muestra el valor de la estadística especificada para cada jugador en la lista filtrada.

    Args:
        lista_filtrada (list): Una lista de jugadores filtrada.
        key (str): La categoría de estadística (por ejemplo, "puntos_totales", "rebotes_totales", etc.).
    """
    for player in lista_filtrada:
        print(player["estadisticas"][key])


def mostrar_jugadores_con_promedio_mayor_v2(lista_filtrada: list, key: str):
    """
    Muestra el valor de la estadística especificada para cada jugador en la lista filtrada,
    utilizando el formato de la clave modificada (reemplazo de guiones bajos por espacios y letras mayúsculas).

    Args:
        lista_filtrada (list): Una lista de jugadores filtrada.
        key (str): La categoría de estadística (por ejemplo, "puntos_totales", "rebotes_totales", etc.).
    """
    print(reemplazar_guion_bajo(key).upper())
    for player in lista_filtrada:
        print("{0} {1}".format(player["nombre"], player[key]))


def ingresar_valor_numerico(lista_jugadores: list):
    """
    Solicita al usuario ingresar un valor numérico para filtrar los jugadores.

    Args:
        lista_jugadores (list): Una lista de jugadores.

    Returns:
        str: El valor numérico ingresado por el usuario.
    """
    num_value = input(
        "Ingrese un valor numerico para filtrar jugadores con promedio menor: "
    )
    if validar_valor_numerico(num_value):
        return num_value
    print("numero no valido.")


def mostrar_jugadores_filtrados_segun_valor_ingresado(lista_jugadores: list, key: str):
    """
    Filtra y muestra los jugadores cuya estadística especificada sea mayor al valor numérico ingresado por el usuario.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        key (str): La categoría de estadística (por ejemplo, "puntos_totales", "rebotes_totales", etc.).
    """
    num_value = ingresar_valor_numerico(lista_jugadores)
    if validar_valor_numerico(num_value):
        num_value = int(num_value)
        lista_filtrada = filtrar_jugadores_con_promedio_mayor(
            lista_jugadores, num_value, key
        )
        print(f"\n{reemplazar_guion_bajo(key)} mayores a {num_value}".upper())
        for player in lista_filtrada:
            print(
                "{0}, {1}".format(
                    player["nombre"],
                    player["estadisticas"][key],
                )
            )


def validar_valor_numerico(num: str):
    """
    Valida si el valor ingresado es un número válido.

    Args:
        num (str): El valor ingresado.

    Returns:
        bool: True si es un número válido, False en caso contrario.
    """
    flag_validar = False
    if re.match(r"^[0-9]+\.?[0-9]*$", num):
        flag_validar = True
    return flag_validar


def filtrar_jugadores_con_promedio_mayor(
    lista_jugadores: list, num_value: str, key: str
):
    """
    Filtra los jugadores cuya estadística especificada sea mayor al valor numérico dado.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        num_value (str): El valor numérico a comparar.
        key (str): La categoría de estadística (por ejemplo, "puntos_totales", "rebotes_totales", etc.).

    Returns:
        list: Una lista filtrada de jugadores.
    """
    return list(
        filter(lambda player: player["estadisticas"][key] > num_value, lista_jugadores)
    )


def filtrar_jugadores_con_promedio_mayor_v2(
    lista_jugadores: list, num_value: str, key: str
):
    """
    Filtra los jugadores cuya estadística especificada sea mayor al valor numérico dado.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        num_value (str): El valor numérico a comparar.
        key (str): La categoría de estadística (por ejemplo, "puntos_totales", "rebotes_totales", etc.).

    Returns:
        list: Una lista filtrada de jugadores.
    """
    return list(filter(lambda player: player[key] > num_value, lista_jugadores))


def calcular_jugador_con_mayor_cantidad(
    lista_jugadores: list, key: str, sentido: str
) -> None:
    """
    Calcula y muestra al jugador con la mayor cantidad en alguna estadistica especificada.

    Args:
        lista_jugadores: (list)
        key: (str)
        sentido: (str)

    Return:
        None
    """

    bubble_sort_lite(lista_jugadores, key, sentido)
    mostrar_jugador_con_mayor_cantidad(lista_jugadores, key)


def mostrar_jugador_con_mayor_cantidad(lista_jugadores: list, key: str):
    """
    Muestra el jugador con la mayor cantidad de una estadística específica.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        key (str): La categoría de estadística (por ejemplo, "puntos_totales", "rebotes_totales", etc.).
    """
    print(
        "{0} {1} {2}".format(
            lista_jugadores[-1]["nombre"],
            lista_jugadores[-1]["estadisticas"][key],
            reemplazar_guion_bajo(key),
        )
    )


def reemplazar_guion_bajo(string: str):
    """
    Reemplaza los guiones bajos en una cadena de texto por espacios.

    Args:
        string (str): La cadena de texto a modificar.

    Returns:
        str: La cadena de texto con los guiones bajos reemplazados por espacios.
    """
    return string.replace("_", " ")


def calcular_ppp_excluyente(lista_jugadores: list, key: str, sentido: str):
    """
    Calcula y muestra el promedio de puntos por partido del equipo excluyendo al
    jugador con la menor cantidad de puntos por partido.

    Args:
        lista_jugadores: (list)
        key: (str)
        sentido: (str)
    """
    bubble_sort_lite(lista_jugadores, key, sentido)
    jugador_excluido = lista_jugadores.pop()
    promedio = calcular_promedio_de_puntos_por_partido(lista_jugadores)
    print(
        f"""Promedio de puntos por partido del DreamTeam(excluyendo al jugador con menor cantidad de puntos por partido): 
        -> {promedio} - jugador excluido {jugador_excluido["nombre"]} {jugador_excluido["estadisticas"][key]}
        """
    )


def calcular_jugador_con_mas_logros(lista_jugadores: list, key: str):
    """
    Calcula el jugador con la mayor cantidad de logros en una categoría específica.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        key (str): La categoría de logros (por ejemplo, "logros_nba", "logros_all_star", etc.).
    """
    bubble_sort_lite_v2(lista_jugadores, key, "mayor")
    print(
        "{0} {1} {2}".format(
            lista_jugadores[-1]["nombre"], len(lista_jugadores[-1][key]), key
        )
    )


def mostrar_jugadores_ordenados_por_posicion(lista_jugadores, key):
    """
    Muestra los jugadores ordenados por posición y filtrados según un valor numérico ingresado.

    Args:
        lista_jugadores (list): Una lista de jugadores.
        key (str): La categoría de estadística (por ejemplo, "puntos_totales", "rebotes_totales", etc.).
    """
    num_str = ingresar_valor_numerico(lista_jugadores)
    lista_ordenada = quick_sort(lista_jugadores, key, "asc")
    lista_filtrada = filtrar_jugadores_con_promedio_mayor_v2(
        lista_ordenada, num_str, "posicion"
    )
    mostrar_jugadores_con_promedio_mayor_v2(lista_filtrada, key)


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
    Calcula y exporta las posiciones de los jugadores en diferentes categorías.

    Esta función recibe una lista de jugadores y calcula las posiciones de cada jugador
    en las categorías de puntos, rebotes, asistencias y robos. Luego, exporta los
    resultados a un archivo CSV llamado "ranking_de_posiciones.csv".

    Args:
        lista_jugadores (list): Una lista de jugadores con sus estadísticas.

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


"--------------------------------------- END ---------------------------------------"


# ///////////////////////////////////////////////////////////////////////////////////
def print_menu():
    menu = [
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
    print(
        """------ Menú ------)
•  1. Mostrar la plantilla de jugadores del Dream Team.
• 02. Seleccionar jugador y mostrar estadísticas
•  2. Mostrar estadísticas de un jugador.
•  3. Guardar estadísticas de un jugador en un archivo.CSV
•  4. Buscar jugador por nombre y mostrar logros
•  5. Calcular y mostrar el promedio de puntos por partido del equipo
•  6. Verificar si un jugador es miembro del Salón de la Fama
•  7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales
•  8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo
•  9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales
• 10. Filtrar jugadores por promedio de puntos por partido
• 11. Filtrar jugadores por promedio de rebotes por partido
• 12. Filtrar jugadores por promedio de asistencias por partido
• 13. Calcular y mostrar el jugador con la mayor cantidad de robos totales
• 14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales
• 15. Filtrar jugadores por porcentaje de tiros libres
• 16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido
• 17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
• 18. Filtrar jugadores por porcentaje de tiros triples
• 19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
• 20. Filtrar jugadores por porcentaje de tiros de campo
• 23. Bonus.
•  0. Salir"""
    )


def menu_app(lista_jugadores):
    """
    Muestra el menú de opciones del programa.

    No recibe argumentos.

    No retorna ningún valor.
    """
    while True:
        limpiar_consola()
        limpiar_pantalla()
        print_menu()
        option = input("\nSeleccione una de las siguientes opciones: ")
        match option:
            case "1":
                mostrar_lista_jugadores(lista_jugadores)
            case "2":
                mostrar_estadisticas_por_jugador(lista_jugadores)
            case "3":
                guardar_estadisticas_jugador(lista_jugadores)
            case "4":
                mostrar_logros_del_jugador(lista_jugadores)
            case "5":
                mostrar_promedio_de_puntos_por_partido(lista_jugadores)
            case "6":
                mostrar_si_es_miembro(lista_jugadores)
            case "7":
                calcular_jugador_con_la_mejor_estadistica(
                    lista_jugadores, "rebotes_totales"
                )
            case "8":
                calcular_jugador_con_la_mejor_estadistica(
                    lista_jugadores, "porcentaje_tiros_de_campo"
                )
            case "9":
                calcular_jugador_con_la_mejor_estadistica(
                    lista_jugadores, "asistencias_totales"
                )
            case "10":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    lista_jugadores, "promedio_puntos_por_partido"
                )
            case "11":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    lista_jugadores, "promedio_rebotes_por_partido"
                )
            case "12":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    lista_jugadores, "promedio_asistencias_por_partido"
                )
            case "13":
                calcular_jugador_con_mayor_cantidad(
                    lista_jugadores, "robos_totales", "mayor"
                )
            case "14":
                calcular_jugador_con_mayor_cantidad(
                    lista_jugadores, "bloqueos_totales", "mayor"
                )
            case "15":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    lista_jugadores, "porcentaje_tiros_libres"
                )
            case "16":
                calcular_ppp_excluyente(
                    lista_jugadores, "promedio_puntos_por_partido", "desc"
                )
            case "17":
                calcular_jugador_con_mas_logros(lista_jugadores, "logros")
            case "18":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    lista_jugadores, "porcentaje_tiros_triples"
                )
            case "19":
                calcular_jugador_con_la_mejor_estadistica(lista_jugadores, "temporadas")
            case "20":
                mostrar_jugadores_ordenados_por_posicion(lista_jugadores, "posicion")
            case "23":
                llamada_punto_23(lista_jugadores)
            case "0":
                break

        limpiar_consola()
        limpiar_pantalla()


def crear_lista_principal():
    ruta = r"C:\Users\mciar\OneDrive\Documentos\UTN\01_primer_cuatrimestre\laboratorio_programacion_1\clase_05_23_parcial\dt.json"
    return parse_json(ruta)


def main():
    lista_principal = crear_lista_principal()
    deep_copy_list = copy.deepcopy(lista_principal)
    menu_app(deep_copy_list)


if __name__ == "__main__":
    main()
