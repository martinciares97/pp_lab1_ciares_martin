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
def mostrar_lista_jugadores(main_list: list) -> None:
    """
    Muestra la lista de todos los jugadores del equipo.

    Args:
        main_list (list): Una lista de jugadores

    Return:
        None
    """

    print("NOMBRE JUGADOR - POSICIÓN\n")
    for player in main_list:
        print(f"{player['nombre']} - {player['posicion']}")


def mostrar_estadisticas_por_jugador(main_list: list) -> int:
    """2) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas
    completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por
    partido, rebotes totales, promedio de rebotes por partido, asistencias totales,
    promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de
    tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples."""

    indice = input(
        "Ingrese el indice del jugador que deseas mostrar sus estadisticas: "
    )
    if re.match(r"^[0-9]+$", indice):
        indice = int(indice)
        player = main_list[indice]["estadisticas"]

        print(f'ESTADISTICAS DE {main_list[indice]["nombre"].upper()}\n')
        for clave, valor in player.items():
            print(f"{clave} {valor}")

    return indice


def definir_nombre_archivo(main_list: list, indice: int):
    nombre_archivo = f'{main_list[indice]["nombre"]}.csv'
    return nombre_archivo


def guardar_estadisticas_jugador(main_list: list):
    """
        3) Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
    permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El
    archivo CSV debe contener los siguientes campos: nombre, posición, temporadas,
    puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes
    por partido, asistencias totales, promedio de asistencias por partido, robos totales,
    bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y
    porcentaje de tiros triples.
    """
    indice_player = mostrar_estadisticas_por_jugador(main_list)
    nombre_archivo = definir_nombre_archivo(main_list, indice_player)
    exportar_csv(nombre_archivo, main_list, indice_player)


def exportar_csv(nombre_archivo: str, main_list: list, indice: int):
    with open(nombre_archivo, "w+", encoding="utf-8") as file:
        formato_encabezado = "nombre,posicion,temporadas,puntos_totales,promedio_puntos_por_partido,rebotes_totales,promedio_rebotes_por_partido,asistencias_totales,promedio_asistencias_por_partido,robos_totales,bloqueos_totales,porcentaje_tiros_de_campo,porcentaje_tiros_libres,porcentaje_tiros_triples\n"
        formato_mensaje = formato_encabezado + (
            "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}\n".format(
                main_list[indice]["nombre"],
                main_list[indice]["posicion"],
                main_list[indice]["estadisticas"]["temporadas"],
                main_list[indice]["estadisticas"]["puntos_totales"],
                main_list[indice]["estadisticas"]["promedio_puntos_por_partido"],
                main_list[indice]["estadisticas"]["rebotes_totales"],
                main_list[indice]["estadisticas"]["promedio_rebotes_por_partido"],
                main_list[indice]["estadisticas"]["asistencias_totales"],
                main_list[indice]["estadisticas"]["promedio_asistencias_por_partido"],
                main_list[indice]["estadisticas"]["robos_totales"],
                main_list[indice]["estadisticas"]["bloqueos_totales"],
                main_list[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
                main_list[indice]["estadisticas"]["porcentaje_tiros_libres"],
                main_list[indice]["estadisticas"]["porcentaje_tiros_triples"],
            )
        )
        file.write(formato_mensaje)


def validar_nombre_jugador(nombre_jugador: str) -> bool:
    flag_retorno = True
    if re.search(r"[^a-zA-Z ]", nombre_jugador):
        flag_retorno = False
    return flag_retorno


def buscar_jugador_por_nombre(main_list: list) -> list:
    nombre = input("Ingrese el nombre que desea buscar: ")
    lista_jugadores_por_nombre = []
    if validar_nombre_jugador(nombre) == True:
        for player in main_list:
            if re.search(f"({nombre})", player["nombre"], re.IGNORECASE):
                lista_jugadores_por_nombre.append(player)
        if len(lista_jugadores_por_nombre) == 0:
            print("No se encontraron coincidencias.")
    else:
        print("No se ingreso un nombre valido.")
    return lista_jugadores_por_nombre


def print_logros_de_jugador(main_list: list) -> None:
    for player in main_list:
        print(f"\n------- LOGROS DE {player['nombre'].upper()} --------")
        logros_del_jugador = player["logros"]
        for logro in logros_del_jugador:
            print(f"{logro}")


def mostrar_logros_del_jugador(main_list: list):
    """
    4) Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como
    campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la
    Fama del Baloncesto, etc.
    """
    lista_jugadores_por_nombre = buscar_jugador_por_nombre(main_list)
    print_logros_de_jugador(lista_jugadores_por_nombre)


def normalizar_datos(main_list):
    pass


""" 
def bubble_sort(main_list: list, key: str, sentido: str):
    flag_swap = True
    rango = len(main_list)
    while flag_swap:
        rango = rango - 1
        flag_swap = False
        for indice in range(rango):
            if sentido == "mayor":
                if (
                    main_list[indice]["estadisticas"][key]
                    > main_list[indice + 1]["estadisticas"][key]
                ):
                    main_list[indice], main_list[indice + 1] = (
                        main_list[indice + 1],
                        main_list[indice],
                    )
            else:
                if (
                    main_list[indice]["estadisticas"][key]
                    < main_list[indice + 1]["estadisticas"][key]
                ):
                    main_list[indice], main_list[indice + 1] = (
                        main_list[indice + 1],
                        main_list[indice],
                    )
 """


def bubble_sort_lite(main_list: list, key_1: str, key_2: str, sentido: str):
    """ """
    for indice in range(len(main_list) - 1):
        if sentido == "mayor":
            if main_list[indice][key_2][key_1] > main_list[indice + 1][key_2][key_1]:
                main_list[indice], main_list[indice + 1] = (
                    main_list[indice + 1],
                    main_list[indice],
                )
        elif sentido == "desc":
            if main_list[indice][key_2][key_1] < main_list[indice + 1][key_2][key_1]:
                main_list[indice], main_list[indice + 1] = (
                    main_list[indice + 1],
                    main_list[indice],
                )


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
            if player[key] > pivot[key]:
                right_list.append(player)
            else:
                left_list.append(player)
        elif sentido == "desc":
            if player[key] > pivot[key]:
                right_list.append(player)
            else:
                left_list.append(player)
    left_list = quick_sort(left_list, key, sentido)
    left_list.append(pivot)
    right_list = quick_sort(right_list, key, sentido)
    left_list.extend(right_list)

    return left_list


def calcular_promedio_de_puntos_por_partido(main_list: list) -> float:
    return (
        reduce(
            lambda acumulador, player: acumulador
            + player["estadisticas"]["promedio_puntos_por_partido"],
            main_list,
            0,
        )
    ) / len(main_list)


def mostrar_promedio_de_puntos_por_partido(main_list):
    """
    5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
    Team, ordenado por nombre de manera ascendente.
    """
    promedio = calcular_promedio_de_puntos_por_partido(main_list)
    sort_list = quick_sort(main_list, "nombre", "asc")

    print(f"\nPromedio de puntos por partido de todo el Dream Team: {promedio}")
    for player in sort_list:
        print(player["nombre"], player["estadisticas"]["promedio_puntos_por_partido"])


def mostrar_si_es_miembro(main_list: list) -> None:
    """
    6) Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es
    miembro del Salón de la Fama del Baloncesto.
    """
    flag_in_lista = False
    nombre_jugador = input(
        "Ingrese el nombre del jugador para saber si es miembro del Salón de la Fama del Baloncesto: "
    )
    if validar_nombre_jugador(nombre_jugador):
        for player in main_list:
            if player["nombre"] == nombre_jugador:
                if "Miembro del Salon de la Fama del Baloncesto" in player["logros"]:
                    flag_in_lista = True
                    break
        if flag_in_lista == True:
            message = f"{nombre_jugador} es miembro del Salón de la Fama del Baloncesto"
        else:
            message = print(f"{nombre_jugador} no es miembro.")
        print(message)


def mostrar_jugador_con_la_mejor_estadistica(main_list: list, key: str):
    print(
        f"""\nJUGADOR CON MAS {key.upper()}
          {main_list[-1]['nombre']} {main_list[-1]['estadisticas'][key]} {key}"""
    )


def separador():
    print("_____________________________________________________")


def calcular_jugador_con_la_mejor_estadistica(main_list: list, key_1: str, key_2: str):
    """
    7|8|9) Calcular y mostrar el jugador con la mayor estadistica.

    Args:
        main_list: (list)
        key_1: (str)

    Return:
        None
    """
    bubble_sort_lite(main_list, key_1, key_2, "mayor")
    separador()
    mostrar_jugador_con_la_mejor_estadistica(main_list, key_1)


def mostrar_jugadores_con_promedio_mayor(lista_filtrada: list, key_1: str):
    for player in lista_filtrada:
        print(player["estadisticas"][key_1])


def ingresar_valor_numerico(main_list: list):
    num_value = input(
        "Ingrese un valor numerico para filtrar jugadores con promedio menor: "
    )
    if validar_valor_numerico(num_value):
        return num_value
    print("numero no valido.")


def mostrar_jugadores_filtrados_segun_valor_ingresado(main_list: list, key: str):
    num_value = ingresar_valor_numerico(main_list)
    if validar_valor_numerico(num_value):
        num_value = int(num_value)
        lista_filtrada = filtrar_jugadores_con_promedio_mayor(main_list, num_value, key)
        print(reemplazar_guion_bajo(key).upper())
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


def filtrar_jugadores_con_promedio_mayor(main_list: list, num_value: str, key: str):
    return list(
        filter(lambda player: player["estadisticas"][key] > num_value, main_list)
    )


def calcular_jugador_con_mayor_cantidad(
    main_list: list, key: str, sentido: str
) -> None:
    """
    Calcula y muestra al jugador con la mayor cantidad en alguna estadistica especificada.

    Args:
        main_list: (list)
        key: (str)
        sentido: (str)

    Return:
        None
    """

    bubble_sort_lite(main_list, key, sentido)
    mostrar_jugador_con_mayor_cantidad(main_list, key)


def mostrar_jugador_con_mayor_cantidad(main_list: list, key: str):
    print(
        "{0} {1} {2}".format(
            main_list[-1]["nombre"],
            main_list[-1]["estadisticas"][key],
            reemplazar_guion_bajo(key),
        )
    )


def reemplazar_guion_bajo(string: str):
    return string.replace("_", " ")


def calcular_ppp_excluyente(main_list: list, key: str, sentido: str):
    """
    Calcula y muestra el promedio de puntos por partido del equipo excluyendo al
    jugador con la menor cantidad de puntos por partido.

    Args:
        main_list: (list)
        key: (str)
        sentido: (str)
    """
    bubble_sort_lite(main_list, key, sentido)
    jugador_excluido = main_list.pop()
    promedio = calcular_promedio_de_puntos_por_partido(main_list)
    print(
        f"""Promedio de puntos por partido del DreamTeam(excluyendo al jugador con menor cantidad de puntos por partido): 
        -> {promedio} - jugador excluido {jugador_excluido["nombre"]} {jugador_excluido["estadisticas"][key]}
        """
    )


def recorrer_logros():
    pass


def calcular_jugador_con_mas_logros(main_list: list, key: str):
    """
    17) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
    """
    calcular_jugador_con_la_mejor_estadistica


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


def menu_app(main_list):
    while True:
        limpiar_consola()
        limpiar_pantalla()
        print_menu()
        option = input("\nSeleccione una de las siguientes opciones: ")
        match option:
            case "1":
                mostrar_lista_jugadores(main_list)
            case "2":
                mostrar_estadisticas_por_jugador(main_list)
            case "3":
                guardar_estadisticas_jugador(main_list)
            case "4":
                mostrar_logros_del_jugador(main_list)
            case "5":
                mostrar_promedio_de_puntos_por_partido(main_list)
            case "6":
                mostrar_si_es_miembro(main_list)
            case "7":
                calcular_jugador_con_la_mejor_estadistica(main_list, "rebotes_totales")
            case "8":
                calcular_jugador_con_la_mejor_estadistica(
                    main_list, "porcentaje_tiros_de_campo"
                )
            case "9":
                calcular_jugador_con_la_mejor_estadistica(
                    main_list, "asistencias_totales"
                )
            case "10":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    main_list, "promedio_puntos_por_partido"
                )
            case "11":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    main_list, "promedio_rebotes_por_partido"
                )
            case "12":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    main_list, "promedio_asistencias_por_partido"
                )
            case "13":
                calcular_jugador_con_mayor_cantidad(main_list, "robos_totales", "mayor")
            case "14":
                calcular_jugador_con_mayor_cantidad(
                    main_list, "bloqueos_totales", "mayor"
                )
            case "15":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    main_list, "porcentaje_tiros_libres"
                )
            case "16":
                calcular_ppp_excluyente(
                    main_list, "promedio_puntos_por_partido", "desc"
                )
            case "17":
                pass
            case "18":
                mostrar_jugadores_filtrados_segun_valor_ingresado(
                    main_list, "porcentaje_tiros_triples"
                )
            case "19":
                pass
            case "20":
                pass
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


"""
19) Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
20) Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por
posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a
ese valor.

"""
