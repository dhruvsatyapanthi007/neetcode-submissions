class TrieNode:
    def __init__(self, character):
        self.character = character
        self.children = {}
        self.leaf = False

    def addChild(self, character):
        if character not in self.children:
            self.children[character] = TrieNode(character)

    def setLeaf(self):
        self.leaf = True

    def getChildren(self):
        return self.children

    def getChild(self, l):
        return self.children[l]

    def isLeaf(self):
        return self.leaf


class PrefixTree:

    def __init__(self):
        self.root = TrieNode(".")

    def insert(self, word: str) -> None:
        curr = self.root
        for l in word:
            curr.addChild(l)
            curr = curr.getChild(l)

        curr.setLeaf()

    def search(self, word: str) -> bool:
        curr = self.root
        for l in word:
            if l not in curr.getChildren():
                return False
            curr = curr.getChild(l)

        return curr.isLeaf()

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for l in prefix:
            if l not in curr.getChildren():
                return False
            curr = curr.getChild(l)

        return True
        