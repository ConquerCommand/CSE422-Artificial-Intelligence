"""
CSE422 Lab Assignment - 3
Task: Alpha-Beta Pruning

Author: Md. Zunayedul Islam
Student ID: 20101381
Course Section: 5
"""


import math
import random


id = input('Student ID: ')
print()

if len(id) != 8:
    raise ValueError('Student ID must be of 8 digits')

if '0' in id:
    id = id.replace('0', '8')

SHUFFLE = int(id[3])
LEN, MIN = 8, int(id[4])
TARGET = int(id[-1] + id[-2])
MAX = int(TARGET * 1.5)
INF = math.inf
leaves = random.sample(range(MIN, MAX), LEN)


def pruning(ñ, ç, α, β, ƒ, µ):
    """
    It is a recursive function that performs alpha-beta
    pruning on the leaf-nodes and returns the optimal
    value. 
    ñ = node [int]
    ç = depth [int]
    α = alpha [int]
    β = beta [int]
    ƒ = leaves [list]
    µ = maximize [bool]
    """

    if ç == 3:
        return ƒ[ñ]

    if µ:  # Optimus Prime's Turn
        point = -INF
        for i in range(2):
            value = pruning(ñ * 2 + i,
                            ç + 1,
                            α, β,
                            ƒ, False)
            point = max(point, value)
            α = max(α, point)
            
            if α >= β:
                break
        
        return point
        
    else:   # Megatron's Turn
        point = INF
        for i in range(2):
            value = pruning(ñ * 2 + i,
                            ç + 1,
                            α, β,
                            ƒ, True)
            point = min(point, value)
            β = min(β, point)
            
            if α >= β:
                break
            
        return point


if __name__ == '__main__':
    record = 0
    scores = []
    
    for i in range(SHUFFLE):
        final = pruning(0, 0,
                        -INF, INF,
                        leaves, True)
        
        if final >= TARGET:
            winner = 'Optimus Prime'
            record += 1
        else:
            winner = 'Megatron'
        
        print('Generated 8 random points between minimum & maximum limits:')
        print(str(leaves)[1:-1])
        print(f'Total points to win: {TARGET}')
        print(f'Achieved point by applying Alpha-Beta Pruning: {final}')
        print(f'Winner is {winner}')
        print()
        
        scores.append(final)
        random.shuffle(leaves)
    
    print('After the shuffle,')
    print('List of all point values from each shuffle:')
    print(str(scores)[1:-1])
    print(f'The maximum value of all shuffles: {max(scores)}')
    print(f'Won {record} times out of {SHUFFLE} number of shuffles')
