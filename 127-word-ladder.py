from typing import List
from collections import defaultdict, deque

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    # build the adjacency list
    # nodes are words
    # key is the pattern of the word, distinct by "*" character
    # values (adjacent node ids) are the words that match the pattern
    D = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            D[pattern].append(word)

    # bfs with level tracking
    def bfs_visit() -> int:
        seen = set()
        bfs_queue = deque()

        # init
        seen.add(beginWord)
        bfs_queue.append(beginWord)
        level = 0

        while bfs_queue:
            level += 1
            l = len(bfs_queue)
            
            for _ in range(l):
                word = bfs_queue.popleft()
                if word == endWord:
                    return level

                # neighbor exploration
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for adj_word in D[pattern]:
                        if adj_word in seen:
                            continue
                        seen.add(adj_word)
                        bfs_queue.append(adj_word)
        
        # finished exploration means endword not hit
        return 0
    
    # driver
    return bfs_visit()

print(ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))