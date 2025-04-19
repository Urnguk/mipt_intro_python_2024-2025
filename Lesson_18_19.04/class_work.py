class Node:
    def __init__(self, parent):
        self.children = dict()
        self.fail = None
        self.parent = parent
        self.patterns = []


class Trie:
    def __init__(self, patterns):
        self.root = Node(None)
        for pat in patterns:
            cur_node = self.root
            for symbol in pat:
                if symbol not in cur_node.children:
                    cur_node.children[symbol] = Node(cur_node)
                cur_node = cur_node.children[symbol]
            cur_node.patterns.append(pat)

        self.root.fail = None
        queue = []
        for symbol in self.root.children:
            children_node = self.root.children[symbol]
            children_node.fail = self.root
            for ch_symbol in children_node.children:
                queue.append((ch_symbol, children_node.children[ch_symbol]))
        while queue:
            symbol, cur_node = queue.pop(0)
            cur_fail = cur_node.parent.fail
            while cur_fail is not None:
                if symbol in cur_fail.children:
                    cur_node.fail = cur_fail.children[symbol]
                    break
                cur_fail = cur_fail.fail
            if cur_fail is None:
                if symbol in self.root.children:
                    cur_node.fail = self.root.children[symbol]
                else:
                    cur_node.fail = self.root
            cur_node.patterns += cur_node.fail.patterns
            for next_symbol in cur_node.children:
                queue.append((next_symbol, cur_node.children[next_symbol]))

    def search(self, base):
        res = []
        cur_node = self.root
        for i in range(len(base)):
            while cur_node is not None and base[i] not in cur_node.children:
                cur_node = cur_node.fail
            if cur_node is None:
                cur_node = self.root
                if base[i] not in cur_node.children:
                    continue
            cur_node = cur_node.children[base[i]]
            if cur_node.patterns:
                for pat in cur_node.patterns:
                    res.append((pat, i - len(pat) + 1))
        return res


patterns = ["aba", "daba", "cdaba", "cok"]
T = Trie(patterns)
print(T.search("kabacdabakcok"))








