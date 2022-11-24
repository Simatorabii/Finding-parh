# 01:59:55 in AI 7-2.m4a

import ghpythonlib.components as gh
import random as r

seed = r.seed(y)

grid = []
# create a grid of pts in 3d(x,y,z)

for i in range(10):
    for j in range(10):
        for k in range(10):
            grid.append(gh.ConstructPoint(i,j,k))

ground = filter(lambda x: x[2]==0,grid)

# 02:05:25
class Agent:
    #constructor
    def __init__(self):
        self.route = [r.choice(ground)]
        self.pts = grid[:]
        self.pts.remove(self.route[0])
        self.update()

    def update(self):
        while self.route[-1][2]<9: # white true untill the route[2] is 9 
            pt = self.nextStep(self.route[-1])
            self.route.append(pt)
        
        self.path = gh.PolyLine(self.route, False)
    
    def nextStep(self, currentPt):
        possible_move = filter(lambda x: abs(x[0]-currentPt[0]) +
        abs(x[1]-currentPt[1]) + x[2]-currentPt[2] == 1 and x[2]-currentPt[2]>=0,self.pts)
        
        nextPt = r.choice(possible_move)
        self.pts.remove(nextPt)
        return nextPt


agents = [Agent() for _ in range(x)]
paths = [i.path for i in agents]
