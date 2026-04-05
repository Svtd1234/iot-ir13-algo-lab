class BinaryTree:
    def __init__(self, v=0):
        self.value = v
        self.left = None
        self.right = None

    def __build(self, w):
        if not w: return None
        val = w.pop(0)
        if val == "Null": return None
        n = BinaryTree(int(val))
        n.left = self.__build(w)
        n.right = self.__build(w)
        return n

    def __get_h(self, n):
        if not n: return 0
        return max(self.__get_h(n.left), self.__get_h(n.right)) + 1

    def __put(self, m, r, c, val):
        s = str(val)
        offset = len(s) // 2
        for i in range(len(s)):
            pos = c + i - offset
            if 0 <= r < len(m) and 0 <= pos < len(m[0]):
                m[r][pos] = s[i]

    def __fill(self, n, m, r, c, side, gr, gc):
        if not n: return
        self.__put(m, r, c, n.value)

        s_len = len(str(n.value))
        left_conn = c - (s_len // 2) - 1
        right_conn = c + (s_len - s_len // 2)
        nr = max(2, gr - 2)

        if side == "root":
            if n.left:
                m[r][left_conn] = "-"
                self.__fill(n.left, m, r, c - gc, "left", gr, gc)
            if n.right:
                m[r][right_conn] = "-"
                self.__fill(n.right, m, r, c + gc, "right", gr, gc)

        elif side == "left":
            if n.left:
                m[r - 1][left_conn] = "\\"
                self.__fill(n.left, m, r - gr, c - gc, "left", nr, gc)
            if n.right:
                m[r + 1][left_conn] = "/"
                self.__fill(n.right, m, r + gr, c - gc, "left", nr, gc)

        elif side == "right":
            if n.left:
                m[r - 1][right_conn] = "/"
                self.__fill(n.left, m, r - gr, c + gc, "right", nr, gc)
            if n.right:
                m[r + 1][right_conn] = "\\"
                self.__fill(n.right, m, r + gr, c + gc, "right", nr, gc)

    def load(self, filename):
        try:
            with open(filename, "r") as f:
                w = f.read().split()
            if w:
                v = w.pop(0)
                if v != "Null":
                    self.value = int(v);
                    self.left = self.__build(w);
                    self.right = self.__build(w)
        except:
            pass

    def print_tree(self):
        h = self.__get_h(self)
        rows, cols = 45, 80
        m = [[" " for _ in range(cols)] for _ in range(rows)]
        self.__fill(self, m, rows // 2, cols // 2, "root", 6, 6)

        print("\n")
        for r in m:
            line = "".join(r).rstrip()
            if line: print(line)

    def print_preorder(self):
        def p(n):
            if not n: print("Null", end=" "); return
            print(n.value, end=" ");
            p(n.left);
            p(n.right)

        print("преордер", end=" ")
        p(self)
        print()

    def is_balanced(self):
        def check(n):
            if not n: return 0
            l, r = check(n.left), check(n.right)
            if l == -1 or r == -1 or abs(l - r) > 1: return -1
            return max(l, r) + 1

        return check(self) != -1

tree = BinaryTree()
tree.load("preordertree.txt")
tree.print_preorder()
tree.print_tree()
print("")
print("збалансоване ", tree.is_balanced())