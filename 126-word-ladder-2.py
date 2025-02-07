from typing import List
from collections import defaultdict, deque

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

    # adjacency list for neighbor exploration
    D = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            D[pattern].append(word)

    ans = []

    # store distance of a word from beginWord
    distance_from_begin = {beginWord: 0}
    # store predecessors of each word for backtracking
    predecessors = defaultdict(set)

    # bfs with level tracking
    seen = set()
    bfs_queue = deque()
    # init bfs
    seen.add(beginWord)
    bfs_queue.append(beginWord)
    level = 0
    found = False

    while bfs_queue and not found:
        level += 1
        level_seen = set()

        for _ in range(len(bfs_queue)):
            word = bfs_queue.popleft()

            # neighbor exploration
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                for adj_word in D[pattern]:
                    if adj_word in seen:
                        continue
                    # update predecessors and distance
                    predecessors[adj_word].add(word)
                    distance_from_begin[adj_word] = level

                    # update seen and bfs queue
                    level_seen.add(adj_word)
                    bfs_queue.append(adj_word)

                    # early termination
                    if adj_word == endWord:
                        found = True
        
        seen.update(level_seen)
    
    # backtracking GG
    def dfs(path: List[str], word: str):
        if word == beginWord:
            ans.append(path[::-1])
            return
        
        for pred_word in predecessors[word]:
            path.append(pred_word)
            dfs(path, pred_word)
            path.pop()

    if found:
        dfs([endWord], endWord)

    return ans

print(findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))