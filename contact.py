from collections import deque

class TrieNode:
    special_character = '$'

    def __init__(self, ch):
        self.children = []
        self.character = ch
        self.counter = 0

    def __cmp__(self, other):
        return self.character == other.character

    def is_word(self):
        for x in self.children:
            if x.character == TrieNode.special_character:
                return True

        return False

    def add(self, word):
        aux_word = word
        node = self

        for ch in aux_word:
            aux_node = None
            for child in node.children:
                if child.character == ch:
                    aux_node = child
                    break

            if aux_node is None:
                aux_node = TrieNode(ch)
                node.children.append(aux_node)

            node = aux_node
            node.counter += 1

        if not node.is_word():
            node.children.append(TrieNode(TrieNode.special_character))

    def find(self, prefix):
        node = self

        for ch in prefix:
            aux_node = None
            for child in node.children:
                if child.character == ch:
                    aux_node = child
                    break

            if aux_node is None:
                return 0

            node = aux_node

        return node.counter


test_cases = int(input())
root = TrieNode('')

for i in range(test_cases):
    method, word = input().strip().split(' ')

    if method == "add":
        root.add(word)
    else:
        print(root.find(word), end="\n")