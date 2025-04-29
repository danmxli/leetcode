from typing import List
from collections import deque

# intuition:
# 1. use bfs to find the shortest path to the target
# 2. use a set to store the bank
# 3. use a queue to store the current state
# 4. use a set to store the visited states
# 5. use a variable to store the number of moves

def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    bank_set = set(bank)

    queue = deque([startGene])
    visited = set([startGene])
    moves = -1

    # no such mutation
    if endGene not in bank_set:
        return moves
    
    while queue:
        moves += 1
        for _ in range(len(queue)):
            curr = queue.popleft()

            if curr == endGene:
                return moves
            
            # adjacent mutations
            for i in range(len(curr)):
                for gene in "ACGT":
                    if gene == curr[i]:
                        continue

                    adj = curr[:i] + gene + curr[i+1:]
                    if adj in bank_set and adj not in visited:
                        visited.add(adj)
                        queue.append(adj)

    # exhausted all possibilities
    return -1


print(minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))