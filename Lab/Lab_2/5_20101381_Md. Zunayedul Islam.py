"""
CSE422 Lab Assignment - 2
Task: Genetic Algorithm

Author: Md Zunayedul Islam
Student ID: 20101381
Course Section: 5
"""


import sys
import random as rd
import numpy as np
from queue import Queue


sys.stdin = open("input.txt", 'r')

COUNT, TARGET = map(int, input().split())
GEN = Queue()
INFO = []
LENGTH = 10

for i in range(COUNT):
    name, run = input().split()
    INFO.append((name, int(run)))

print([INFO[i][0] for i in range(len(INFO))])


def populate(length):
    """
    Population Function:
    Generates L number of strings of the randomly chosen combination
    of 0s & 1s and puts them into the queue.
    """
    for x in range(length):
        gene = np.random.choice([0, 1], size=len(INFO))
        GEN.put(str(gene)[1:-1].replace(" ", ""))


def fit(gene):
    """
    Fitness Function:
    Calculates the total runs of the players according to the combination
    string and check if it fits the target.
    """
    fitness = 0
    for x in range(len(gene)):
        if gene[x] == '1':
            fitness += INFO[x][1]
            
    return fitness == TARGET


def cross(gene_1, gene_2):
    """
    Crossover Function:
    Generates two new combinations of strings by crossing two strings
    from the middle.
    """
    x = rd.randint(0, len(gene_1)-1)
    gene_3 = gene_1[:x] + gene_2[x:]
    gene_4 = gene_2[:x] + gene_1[x:]
    
    return gene_3, gene_4


def mutate(gene):
    """
    Mutation Function:
    Swaps an item of a randomly chosen index of the first half of the
    string with that of the last half.
    """
    gene = [int(i) for i in gene]
    m = rd.randint(0, len(gene) // 2 - 1)
    n = rd.randint(len(gene) // 2, len(gene) - 1)
    gene[m], gene[n] = gene[n], gene[m]
    
    return "".join(str(i) for i in gene)


if __name__ == "__main__":
    populate(LENGTH)
    found = False
    for i in range(10**5):
        if not found:
            gene_1, gene_2 = GEN.get(), GEN.get()
            if fit(gene_1):
                print(gene_1)
                found = True
                break
            elif fit(gene_2):
                print(gene_2)
                found = True
                break
            else:
                gene_3, gene_4 = cross(gene_1, gene_2)
                GEN.put(mutate(gene_3))
                GEN.put(mutate(gene_4))

    print(-1) if not found else exit()