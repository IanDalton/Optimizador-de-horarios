import json
from operator import pos
from re import M
import numpy as np
import itertools

archivo = json.load(open("Materias.json", "r"))
listaTemp = ["(61.81)", "(61.82)", "(71.20)", "(81.11)", "(82.15)", "(94.61)"]

i = 0
vectorIdealTemp = [2, 2, 2, 2, 2, 2, 12, 0, 0]
creditos = 24


def calculadoraDeAngulos(vectorIdeal, lista):
    vectorIdeal = np.array(vectorIdeal)
    vectorTotal = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    sumaMatriz = []

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

    for vector in sumaMatriz:
        for i in range(len(vector)):
            vectorTotal[i] += vector[i]

    vectorTotal = np.array(vectorTotal)

    angulo = vectorIdeal.dot(vectorTotal) / (
        np.linalg.norm(vectorTotal) * np.linalg.norm(vectorIdeal)
    )
    return angulo


def generadorDeListas(preferencias):
    # calculo que esto se puede optimizar y usar una sola matriz pero lo voy a dejar para despues
    todMaterias = []
    posiblesComb = []
    topCombinaciones = [["", 0], ["", 0], ["", 0]]
    i = 0
    for materia in archivo:
        todMaterias.append(materia)
    for Creditos in range(1, round(creditos / 3)):
        for combinaciones in combinations(todMaterias, Creditos):
            posiblesComb.append([])
            for materia in combinaciones:
                posiblesComb[i].append(materia)
            i += 1

    posiblesComb = verificadorComb(posiblesComb)

    for grupo in posiblesComb:
        angulo = calculadoraDeAngulos(vectorIdealTemp, grupo)
        if angulo >= topCombinaciones[0][1]:
            topCombinaciones[2] = topCombinaciones[1]
            topCombinaciones[1] = topCombinaciones[0]
            topCombinaciones[0] = [grupo, angulo]

    return topCombinaciones


def verificadorComb(vector):
    eliminar = []

    for i in range(len(vector)):
        suma = 0
        for materia in vector[i]:
            for datos in archivo[materia]:
                suma += datos["Creditos"]
        if suma != creditos:
            eliminar.append(i)
    eliminados = 0
    for valor in eliminar:
        vector.pop(valor - eliminados)
        eliminados += 1

    return vector


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


combinaciones = generadorDeListas(vectorIdealTemp)
print(combinaciones)
