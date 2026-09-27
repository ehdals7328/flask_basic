class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t # 최소 차수 t
        self.leaf = leaf # 리프 노드 여부
        self.keys = [] # 노드가 가진 키 목록들
        self.child = [] # 자식 노드 pointer 목록 

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def search(self, k, x=None):
        if x is None:
            x = self.root 

        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and k == x.keys[i]:
            return True # 탐색 성공

        if x.leaf:
            return False # 리프 (끝)에도 존재하지 않음

        return self.search(k, x.child[i])

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(t, y.leaf)

        z.keys = y.keys[t:]
        x.keys.insert(i, y.keys[t - 1])
        y.keys = y.keys[:t - 1]

        if not y.leaf:
            z.child = y.child[t:]
            y.child = y.child[:t]

        x.child.insert(i + 1, z)

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:  # 루트가 가득 찬 경우
            s = BTreeNode(self.t, False)
            self.root = s
            s.child.insert(0, root)
            self.split_child(s, 0)
            self._insert_non_full(s, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.child[i], k)


if __name__ == "__main__":
    btree = BTree(t=2)

    data = [10, 20, 5, 6, 12, 30, 7, 17]
    for key in data:
        btree.insert(key)

    print("6 탐색 결과:", btree.search(6))   # True
    print("15 탐색 결과:", btree.search(15)) # False