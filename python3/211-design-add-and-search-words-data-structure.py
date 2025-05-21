class TrieNode:
    
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c)-ord('a')
            if not curr.child[index]:
                curr.child[index] = TrieNode()
            
            curr = curr.child[index]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        # index accesses character of word
        def dfs_helper(root: TrieNode, index: int) -> bool:
            # base case
            if not root:
                return False

            if index == len(word):
                return root.isEnd

            c = word[index]

            # must be exact match in trie node
            if c != '.':
                id = ord(c)-ord('a')
                if not root.child[id]:
                    return False
                else:
                    return dfs_helper(root.child[id], index+1)
            
            # wildcard condition
            else:
                for trie_c in root.child:
                    if trie_c and dfs_helper(trie_c, index+1):
                        return True
                return False

        return dfs_helper(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))