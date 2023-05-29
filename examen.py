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
email: m.ciares97@gmail.com

"""


def limpiar_consola():
    input("\nPresione Enter para continuar...")
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo y añade un retraso."""
    if platform.system() == "Windows":
        os.system("cls & echo.")
        time.sleep(0.1)
    else:
        os.system("clear; printf '\033c'")
        time.sleep(0.1)


def parse_json(nombre_archivo: str):
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
        lista_jugadores (list): Una lista de jugadores

    Return:
        None
    """

    print("NOMBRE JUGADOR - POSICIÓN\n")
    for player in lista_jugadores:
        print(f"{player['nombre']} - {player['posicion']}")


def mostrar_estadisticas_por_jugador(lista_jugadores: list) -> int:
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
    nombre_archivo = f'{lista_jugadores[indice]["nombre"]}.csv'
    return nombre_archivo


def guardar_estadisticas_jugador(lista_jugadores: list):
    indice_player = mostrar_estadisticas_por_jugador(lista_jugadores)
    nombre_archivo = definir_nombre_archivo(lista_jugadores, indice_player)
    exportar_csv(nombre_archivo, lista_jugadores, indice_player)


def exportar_csv(nombre_archivo: str, lista_jugadores: list, indice: int):
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
    flag_retorno = True
    if re.search(r"[^a-zA-Z ]", nombre_jugador):
        flag_retorno = False
    return flag_retorno


def buscar_jugador_por_nombre(lista_jugadores: list) -> list:
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


def normalizar_datos(lista_jugadores):
    pass


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
    mostrar el promedio de puntos por partido de todo el equipo del Dream
    Team, ordenado por nombre de manera ascendente.
    """
    promedio = calcular_promedio_de_puntos_por_partido(lista_jugadores)
    sort_list = quick_sort(lista_jugadores, "nombre", "asc")

    print(f"\nPromedio de puntos por partido de todo el Dream Team: {promedio}")
    for player in sort_list:
        print(player["nombre"], player["estadisticas"]["promedio_puntos_por_partido"])


def mostrar_si_es_miembro(lista_jugadores: list) -> None:
    """
    6) Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es
    miembro del Salón de la Fama del Baloncesto.
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
    print(
        f"""\nJUGADOR CON MAS {key.upper()}
          {lista_jugadores[-1]['nombre']} {lista_jugadores[-1]['estadisticas'][key]} {key}"""
    )


def separador():
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
    for player in lista_filtrada:
        print(player["estadisticas"][key])


def mostrar_jugadores_con_promedio_mayor_v2(lista_filtrada: list, key: str):
    print(reemplazar_guion_bajo(key).upper())
    for player in lista_filtrada:
        print("{0} {1}".format(player["nombre"], player[key]))


def ingresar_valor_numerico(lista_jugadores: list):
    num_value = input(
        "Ingrese un valor numerico para filtrar jugadores con promedio menor: "
    )
    if validar_valor_numerico(num_value):
        return num_value
    print("numero no valido.")


def mostrar_jugadores_filtrados_segun_valor_ingresado(lista_jugadores: list, key: str):
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
    flag_validar = False
    if re.match(r"^[0-9]+\.?[0-9]*$", num):
        flag_validar = True
    return flag_validar


def filtrar_jugadores_con_promedio_mayor(
    lista_jugadores: list, num_value: str, key: str
):
    return list(
        filter(lambda player: player["estadisticas"][key] > num_value, lista_jugadores)
    )


def filtrar_jugadores_con_promedio_mayor_v2(
    lista_jugadores: list, num_value: str, key: str
):
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
    print(
        "{0} {1} {2}".format(
            lista_jugadores[-1]["nombre"],
            lista_jugadores[-1]["estadisticas"][key],
            reemplazar_guion_bajo(key),
        )
    )


def reemplazar_guion_bajo(string: str):
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


def recorrer_logros():
    pass


def calcular_jugador_con_mas_logros(lista_jugadores: list, key: str):
    """
    17) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
    """
    bubble_sort_lite_v2(lista_jugadores, key, "mayor")
    print(
        "{0} {1} {2}".format(
            lista_jugadores[-1]["nombre"], len(lista_jugadores[-1][key]), key
        )
    )


def mostrar_jugadores_ordenados_por_posicion(lista_jugadores, key):
    """
    20) Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por
    posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a
    ese valor."""
    num_str = ingresar_valor_numerico(lista_jugadores)
    lista_ordenada = quick_sort(lista_jugadores, key, "asc")
    lista_filtrada = filtrar_jugadores_con_promedio_mayor_v2(
        lista_ordenada, num_str, "posicion"
    )
    mostrar_jugadores_con_promedio_mayor_v2(lista_filtrada, key)


# 23 BONUS ---------------------------------------------------------------------------
"""
Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking
    • Puntos 
    • Rebotes 
    • Asistencias 
    • Robos
Exportar a csv.

Ejemplo
Jugador         Puntos      Rebotes     Asistencias     Robos
Michael Jordan      1           1           1           2
Magic               2           3           4           4  
"""


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
        "Mostrar la plantilla de jugadores del Dream Team",
        "Mostrar estadísticas de un jugador",
        "Guardar estadísticas de un jugador en un archivo.csv",
        "Buscar jugador por nombre y mostrar logros",
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
