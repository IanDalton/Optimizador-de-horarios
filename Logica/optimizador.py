import json
import numpy as np
from math import floor

archivo = json.load(open("materias.json", "r"))

"""
Valores modificables
    vectorIdealTemp:
        -cantidad de parciales en la primera semana
        -cantidad de parciales en la segunda semana
        -cantidad de parciales en la tercera semana
        -cantidad de parciales (2) en la primera semana
        -cantidad de parciales (2) en la segunda semana
        -cantidad de parciales (2) en la tercera semana
        -cantidad de bloques de 3 horas durante la mañana    |
        -cantidad de bloques de 3 horas durante la mediodia  | Por ej. con 24 creditos esto suma 8, con 27 suma 9
        -cantidad de bloques de 3 horas durante la tarde     |
    excluirTemp:
        -Se excluye las materias que listas,
        idealmente poner las que ya aprobaste y las que no te interesan cursar
        -EJ: ["(93.39)","(93.16)","(81.07)"]
    creditos:
        -Son los creditos que se desean cursar, por default viene en 24 pero se puede cambiar a cualquier multiplo de 3
"""

vectorIdealTemp = [2, 2, 2, 2, 2, 2, 8, 0, 0]
excluirTemp = []
creditos = 24


def filtroCorrelativas(todo,excluir):
    """
    La idea es recibir la lista completa de materias y si están en la lista de excluir sacarlas.
    Luego filtrar la lista restante para excluir las que tienen las correlativas incluidas
    """

    for materia in excluir:
        todo.remove(materia)

    excluir = []
    for materia in todo:
        info = archivo[materia][0]["Correlativas"]
        if len(info) != 0:
            for dato in info:
                if (dato in todo) and (materia not in excluir):
                    excluir.append(materia)
    for materia in excluir:
        todo.remove(materia)


def calculadoraDeAngulos(vectorIdeal, lista):
    vectorIdeal = np.array(vectorIdeal)
    vectorTotal = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sumaMatriz = []
    # Genero una matriz con todos los vectores de las materias
    for materia in archivo:
        for info in archivo[materia]:
            if materia in lista:
                sumaMatriz.append(
                    [
                        info["Parcial en semana 1"],
                        info["Parcial en semana 2"],
                        info["Parcial en semana 3"],
                        info["Parcial 2 en semana 1"],
                        info["Parcial 2 en semana 2"],
                        info["Parcial 2 en semana 3"],
                        info["Clases a la manana"],
                        info["Clases al mediodia"],
                        info["Clases a la tarde"],
                    ]
                )
    # Sumo todos los vectores de la matriz armada
    for vector in sumaMatriz:
        for i in range(len(vector)):
            vectorTotal[i] += vector[i]

    # Lo convierto todo a un vector y obtengo el cos del angulo
    vectorTotal = np.array(vectorTotal)

    angulo = vectorIdeal.dot(vectorTotal) / (
        np.linalg.norm(vectorTotal) * np.linalg.norm(vectorIdeal)
    )
    return angulo


def generadorDeListas(preferencias,excluir):
    # calculo que esto se puede optimizar y usar una sola matriz pero lo voy a dejar para despues
    todMaterias = []
    posiblesComb = []
    topCombinaciones = [["", 0], ["", 0], ["", 0]]
    i = 0

    # Armo una lista con todas las materias posibles
    for materia in archivo:
        todMaterias.append(materia)

    filtroCorrelativas(todMaterias,excluir)
    """
    Genero todas las combinaciones posibles con todas las posibles agrupaciones que pueden tener
        Por ejemplo tenemos 24 creditos asi que como maximo podemos anotarnos a 8 materias,
        pero no hay que descartar las combinaciones que se pueden dar desde 7,6,5 o 4.
        Como el usuario puede especificar si quiere cursar solo 3,6 o 9 creditos generamos las combinaciones de 1,2 y 3 pero
        luego se descartan.

    """
    for Creditos in range(1, floor(creditos / 3)):
        for combinaciones in combinations(todMaterias, Creditos):
            posiblesComb.append([])
            for materia in combinaciones:
                posiblesComb[i].append(materia)
            i += 1

    # Elimino las que no cumplen con los creditos especificados

    verificadorComb(posiblesComb)
    """ Calculo el angulo de las combinaciones restantes y si es mayor al registrado en el primer puesto
        simplemente muevo todo un lugar a la derecha y lo registro en el primer lugar.
        Verifico tambien si es mas grande que el segundo o el tercero, si se les ocurre una forma mas eficiente, genial. """
    for grupo in posiblesComb:
        angulo = calculadoraDeAngulos(vectorIdealTemp, grupo)
        if angulo >= topCombinaciones[0][1]:
            topCombinaciones[2] = topCombinaciones[1]
            topCombinaciones[1] = topCombinaciones[0]
            topCombinaciones[0] = [grupo, angulo]
        elif angulo >= topCombinaciones[1][1]:
            topCombinaciones[2] = topCombinaciones[1]
            topCombinaciones[1] = [grupo, angulo]
        elif angulo >= topCombinaciones[2][1]:
            topCombinaciones[2] = [grupo, angulo]

    return topCombinaciones


def verificadorComb(vector):
    # registro la lista para eliminar la posicion que no cumple con los creditos pedidos
    eliminar = []

    # Hago un ciclo en donde sumo el valor de los creditos y si la suma es distinta a lo pedido se anota para eliminar
    for i in range(len(vector)):
        suma = 0
        for materia in vector[i]:
            for datos in archivo[materia]:
                suma += datos["Creditos"]
        if suma != creditos:
            eliminar.append(i)

    # Se eliminan las combinaciones que no cumplen
    eliminados = 0
    for valor in eliminar:
        vector.pop(valor - eliminados)
        eliminados += 1

# Codigo que me robe de el ejemplo, no entiendo que pasa aca


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


combinaciones = generadorDeListas(vectorIdealTemp,excluirTemp)
print(combinaciones)
