"""
CSE422 Lab Assignment - 1

Name: Md. Zunayedul Islam
Student ID: 20101381
Section: 05

Task 1: Outbreak
"""

import sys
import numpy as np

sys.stdin = open("input1.txt", 'r')

M = []
while True:
    try:
        M.append(list(input().split()))
    except:
        break

visited = np.zeros((len(M), len(M[0])), dtype=bool)
affected = []


def spread(x, y):
    """
    Spreads the virus from the given position to
    its neighboring positions recursively.
    N N N
    N Y N
    N N N
    Input: x, y - position of the affected
    """
    if not visited[x][y]:
        visited[x][y] = True
        if M[x][y] == 'Y':
            global count
            count += 1
            spread(x, y - 1) if y - 1 >= 0 else None
            spread(x, y + 1) if y + 1 < len(M[x]) else None
            spread(x + 1, y) if x + 1 < len(M) else None
            spread(x + 1, y - 1) if x + 1 < len(M) and y - 1 >= 0 else None
            spread(x + 1, y + 1) if x + 1 < len(M) and y + 1 < len(M[x]) else None
            spread(x - 1, y) if x - 1 >= 0 else None
            spread(x - 1, y - 1) if x - 1 >= 0 and y - 1 >= 0 else None
            spread(x - 1, y + 1) if x - 1 >= 0 and y + 1 < len(M[x]) else None
        else:
            return
    else:
        return


for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] == 'Y' and not visited[i][j]:
            count = 0
            spread(i, j)
            affected.append(count)

print(max(affected))


"""
CSE422 Lab Assignment - 1

Name: Md. Zunayedul Islam
Student ID: 20101381
Section: 05

Task 2: Apocalypse
"""


import sys
from queue import Queue

sys.stdin = open("input2.txt", 'r')

rows, cols = int(input()), int(input())
global A, Q
N = []
Q = Queue()

while True:
    try:
        N.append(list(input().split()))
    except:
        break

for a in range(rows):
    for b in range(cols):
        if N[a][b] == 'A':
            Q.put((a, b))


def humans():
    """
    Counts the current number of humans.
    Input: None
    Return: Number of humans
    """
    count = 0
    for a in range(rows):
        for b in range(cols):
            if N[a][b] == 'H':
                count += 1
    return count


def convert(x, y):
    """
    Converts position to 'A' if the position is 'H'
    and puts the position into the queue.
    Input: x, y - position
    """
    N[x][y] = 'A'
    Q.put((x, y))


def attack(x, y):
    """
    Attacks the top, bottom, left and right of the
    given position to 'A' if the position is 'H' and 
    converts them.
    T H T
    H A H
    T H T
    Input: x, y - position
    """
    convert(x - 1, y) if x - 1 >= 0 and N[x - 1][y] == 'H' else None
    convert(x + 1, y) if x + 1 < rows and N[x + 1][y] == 'H' else None
    convert(x, y - 1) if y - 1 >= 0 and N[x][y - 1] == 'H' else None
    convert(x, y + 1) if y + 1 < cols and N[x][y + 1] == 'H' else None


time = 0
wave = Q.qsize()

while Q.qsize() > 0:
    x, y = Q.get()
    attack(x, y)
    wave -= 1

    if wave == 0:
        if Q.qsize() > 0:
            time += 1
            wave = Q.qsize()

print(f"Time: {time} minutes")
print("No one survived") if humans() == 0 else print(f"{humans()} survived")
