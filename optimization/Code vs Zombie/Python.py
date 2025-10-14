import sys
import math

def getNextPos(startCoord, endCoord, vectorLen):
    if startCoord == endCoord:
        return endCoord
    v_x = endCoord[0] - startCoord[0]
    v_y = endCoord[1] - startCoord[1]
    len = math.sqrt(v_x**2 + v_y**2)
    mul = abs(vectorLen) / len
    v_x *= mul
    v_y *= mul
    return [startCoord[0] + v_x, startCoord[1] + v_y]

def getDistance(coord1, coord2):
    a = max(coord1[0], coord2[0]) - min(coord1[0], coord2[0])
    b = max(coord1[1], coord2[1]) - min(coord1[1], coord2[1])
    c = math.sqrt(a**2 + b**2)
    return c

ZOMBIE_SPEED = 400
ASH_SPEED = 1000
ASH_RANGE = 2000

while True:
    ash_coord = [int(i) for i in input().split()]
    human_count = int(input())
    humans = []
    for i in range(human_count):
        humans.append([int(j) for j in input().split()])
    zombie_count = int(input())
    zombies = []
    for i in range(zombie_count):
        zombies.append([int(j) for j in input().split()])
 
    lowestDist = 18358
    nearestZomId = -1
    
    for j in range(human_count):
        human_coord = [humans[j][1], humans[j][2]]
        for i in range(zombie_count):
            zombie_coord = [zombies[i][3], zombies[i][4]]
            
            distZomHum = getDistance(zombie_coord, human_coord)

            ash_next = getNextPos(ash_coord, zombie_coord, ASH_SPEED)
            distZomAsh = getDistance(zombie_coord, ash_next)
            
            remainingRounds = int(distZomHum/ZOMBIE_SPEED)
            requiredRounds = int((distZomAsh - 0.5 * ASH_RANGE)/ASH_SPEED)
            
            reachable = remainingRounds >= requiredRounds
            
            print("Zombie " + str(zombie_coord), file=sys.stderr)
            print("Remaining: " + str(remainingRounds) + " Required: " + str(requiredRounds), file=sys.stderr)

            if reachable and distZomHum < lowestDist:
                nearestZomId = i
                lowestDist = distZomHum
                print("-> New aim", file=sys.stderr)

            print("DistZomHum: " + str(distZomHum), file=sys.stderr)
            print("Rechable: " + str(reachable) + " - Lowest: " + str(lowestDist), file=sys.stderr)
            print("---------------------", file=sys.stderr)

    print(str(zombies[nearestZomId][3]) + " " + str(zombies[nearestZomId][4]))