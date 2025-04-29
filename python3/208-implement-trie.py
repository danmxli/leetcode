class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:    
        # root node with null values
        curr = self.root

        # build the descendant nodes
        for c in word:
            index = ord(c) - ord('a')
            if not curr.child[index]:
                curr.child[index] = TrieNode()
            curr = curr.child[index]

        curr.is_end = True
        
    def search(self, word: str) -> bool:
        # root node with null values
        curr = self.root

        # build the descendant nodes
        for c in word:
            index = ord(c) - ord('a')
            if not curr.child[index]:
                return False
            curr = curr.child[index]

        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        # root node with null values
        curr = self.root

        # build the descendant nodes
        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.child[index]:
                return False
            curr = curr.child[index]

        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "apple"
obj.insert(word)
obj.insert("app")
print(obj.search("app"))
print(obj.startsWith("appl"))