class Distance:

    def __init__(self, f):
        self.matrix = []
        self.dictDistance = {}
        self.file = f
        self.m, self.n = 0, 0
        return

    def getDistances(self):

        self.m, self.n = map(int, self.file.readline().split())
        for i in range(self.m):
            x = list(self.file.readline().split())

            for j in range(self.n):
                if x[j] != '0':
                    self.matrix.append((x[j], i, j))

        for touple in self.matrix:
            p, px, py = touple
            self.dictDistance[p] = {}

            for near in self.matrix:
                if touple == near:
                    continue

                p2, px2, py2 = near
                # |px - px2| + |py - py2|
                self.dictDistance[p][p2] = (abs(px - px2) + abs(py - py2))

        return self.dictDistance
