import sys
import math
import copy

def debut_mot(w : str, matrix : list[list[str]]):
    result = []
    for i in range(4):
        for j in range(len(matrix[0])):
            if matrix[i][j] == w:
                result.append([i,j])
    return result


def voisins(pos, matrix):
    x,y = pos
    result = []
    if x != 0:
        result.append((matrix[x-1][y],[x-1, y]) )
        if y != 0:
            result.append((matrix[x-1][y - 1],[x-1, y - 1]))
        if y != taille_mot:
            result.append((matrix[x-1][y + 1], [x-1, y + 1]))
    if x != taille_mot:
        result.append((matrix[x + 1] [y], [x + 1, y]))
        if y != 0:
            result.append((matrix[x + 1][ y - 1], [x + 1 , y - 1]))
        if y != taille_mot:
            result.append((matrix[x+1][y + 1], [x+1 , y + 1]))
    if y !=0:
        result.append((matrix[x][y - 1], [x, y - 1]))
    if y != taille_mot:
        result.append((matrix[x ][ y + 1], [x , y + 1]))

    return result 

def is_present(w : str, matrix : list[list[str]], pos_debut : list[int], index : int, already_see : list[int]):
    if index == len(w)  :
        return True
    for elem in voisins(pos_debut, matrix):
        if elem[0] == w[index] and elem[1] not in already_see:
            tmp = copy.deepcopy(already_see)
            tmp.append(elem[1])
            if is_present(w, matrix, elem[1], index + 1, tmp):
                return True
    return False



matrix = []
matrix.append(list(input()))
matrix.append(list(input()))

matrix.append(list(input()))
global taille_mot
taille_mot = len(matrix[0]) - 1

matrix.append(list(input()))

n = int(input())
for i in range(n):
    w = input()
    flag = 0
    pos_debut = debut_mot(w[0],matrix)
    for elem in pos_debut:

        if is_present(w,matrix, elem, 1, [elem]):
            print("true")
            flag = 1
            break
    if not flag:
        print("false")
