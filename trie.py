

class TrieNode:
    def __init__(self, isEnd = False):
        self.children = {}
        self.isEnd = isEnd
    
    def __str__(self):
        return f"{self.children}, {self.isEnd}"

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node if node.isEnd else None
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def delete(self, s):
        def dfs(node, s, i):
            if i == len(s):
                node.isEnd = False
                return len(node.children) == 0
            else:
                next_deletion = dfs(node.children[s[i]], s, i + 1)
                if next_deletion:
                    del node.children[s[i]]
                return next_deletion and not node.isEnd and len(node.children) == 0
        if self.search(s):
            dfs(self.root, s, 0) 

    def get_strings(self):
        def dfs(node, string, strings):
            if node.isEnd:
                strings.append("".join(string))
            for ch in node.children:
                string.append(ch)
                dfs(node.children[ch], string, strings)
                string.pop()
        strings = []
        dfs(self.root, [], strings)
        return strings