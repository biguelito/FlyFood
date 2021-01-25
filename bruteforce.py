# noinspection PyTypeChecker,PyNoneFunctionAssignment
class BruteForce:

    def __init__(self, m):
        self.matrix = m
        self.vertices = list(m.keys())
        self.paths = []

        self.shortestpath()
        return

    def possibilites(self, v):
        if len(v) == 0:
            return []

        if len(v) == 1:
            return [v]

        path = []
        for i in range(len(v)):
            a = v[i]
            remV = v[:i] + v[i+1:]

            for poss in self.possibilites(remV):
                path.append([a] + poss)
        return path

    def shortestpath(self):
        v = self.vertices[:]
        v.remove('R')
        sh = []
        shcost = float('inf')

        allpaths = self.possibilites(v)
        print(allpaths)
        for n in allpaths:
            temp = 0

            for i in range(1, len(n)):
                temp += self.matrix[n[i-1]][n[i]]
            temp += self.matrix['R'][n[0]] + self.matrix['R'][n[len(n)-1]]

            if temp < shcost:
                shcost = temp
                sh = n
        sh = ['R'] + sh + ['R']

        for p in sh:
            print(p, end=' ')
        print('')
        print('cost: ', shcost)

        return sh, shcost
