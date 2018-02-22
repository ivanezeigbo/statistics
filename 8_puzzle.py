from copy import deepcopy

class PuzzleNode:
    def __init__ (self, starting, parent):
        self.board = starting
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0

    def manhattan(self): #manhattan algorithm is admissible 
        h = 0
        for i in range(3):
            for j in range(3):
                x, y = divmod(self.board[i][j], 3)
                h += abs(x-i) + abs(y-j)
        return h

    def getMTcost(self):
        """
        A* Heuristic where the next node to be expanded is chosen based upon how 
        many misplaced tiles (MT) are in the state of the next node 
        """
        totalMTcost = 0
        board = self.board[:]
        value = 0
        for row in self.board:
            for element in row:
                if int(element) != value:
                    totalMTcost += 1
                value += 1
        return totalMTcost


    def goal(self):
        inc = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != inc:
                    return False
                inc += 1
        return True

    def __eq__(self, other):
        return self.board == other.board

    def __str__(self): #shows structure of grid
        for row in self.board:
            for element in row:
                print(element, ' |', end ='\t')
            print ("\n")
            print ("--------------------")
        print("\n")

def solvePuzzle(n, state, heuristic, prnt):
    def move_function(curr, n):
        curr = curr.board
        for i in range(n):
            for j in range(n):
                if curr[i][j] == 0:
                    x, y = i, j
                    break
        q = []
        if x-1 >= 0:
            b = deepcopy(curr)
            b[x][y]=b[x-1][y]
            b[x-1][y]=0
            succ = PuzzleNode(b, curr)
            q.append(succ)
        if x+1 < 3:
            b = deepcopy(curr)
            b[x][y]=b[x+1][y]
            b[x+1][y]=0
            succ = PuzzleNode(b, curr)
            q.append(succ)
        if y-1 >= 0:
            b = deepcopy(curr)
            b[x][y]=b[x][y-1]
            b[x][y-1]=0
            succ = PuzzleNode(b, curr)
            q.append(succ)
        if y+1 < 3:
            b = deepcopy(curr)
            b[x][y]=b[x][y+1]
            b[x][y+1]=0
            succ = PuzzleNode(b, curr)
            q.append(succ)

        return q

    def best_fvalue(openList):
        f = openList[0].f
        index = 0
        for i, item in enumerate(openList):
            if i == 0: 
                continue
            if(item.f < f):
                f = item.f
                index  = i

        return openList[index], index

    def AStar(state, heuristic): #A* implementation
        openList = []
        closedList = []
        openList.append(state)
        
        while openList:
            current, index = best_fvalue(openList)
            if current.goal():
                return current
            openList.pop(index)
            #current.__str__()     #prints grid of current state of board
            closedList.append(current)
            

            X = move_function(current, n)
            for move in X:
                ok = False   #checking in closedList
                for i, item in enumerate(closedList):
                    if item == move:
                        ok = True
                        break
                if not ok:              #not in closed list
                    newG = current.g + 1 
                    present = False

                    #openList includes move
                    for j, item in enumerate(openList):
                        if item == move:
                            present = True
                            if newG < openList[j].g:
                                openList[j].g = newG
                                openList[j].f = openList[j].g + openList[j].h
                                openList[j].parent = current
                    if not present:
                        move.g = newG
                        if heuristic == 'manhattan':
                            move.h = move.manhattan()
                        if heuristic == 'Misplaced Tiles':
                            move.h = move.getMTcost()
                        move.f = move.g + move.h
                        move.parent = current
                        openList.append(move)

        return None

 
    noofMoves = 0
    num = 0 #number of tiles in board state
    for row in Start_state:
        for element in row:
            num += 1
    
    if(int(num) != int(n*n) or type(n) != int):
        return 0, 0, -2
    else:
        frontier = AStar(state, heuristic)
        if(not frontier):
            return 0, 0, -1
        else:
            t=frontier.parent
            stages = []
            while t:
                noofMoves += 1
                stages.append(t.board)
                t=t.parent
    stages = stages[::-1]
    stages.append(frontier.board)
    err = 0
    if prnt:
        print ("There are", noofMoves, "number of steps. And these optimal steps are:", '\n')
        for k in stages:
            print (k)
        print("")
    return noofMoves, stages, err

def main():
    global Start_state
    #Start_state = [[5,7,6],[2,4,3],[8,1,0]] #define initial state : 28 steps manhattan
    #Start_state = [[7,0,8],[4,6,1],[5,3,2]] #define initial state : 25 steps manhattan
    Start_state = [[2,3,7],[1,8,0],[6,5,4]] #define initial state : 17 steps manhattan and MT
    Game_Heuristic = ["manhattan", "Misplaced Tiles"]
    Heuristic = Game_Heuristic[0]
    n = 3 #dimension of board
    prnt = True #set to True
    
    start = PuzzleNode(Start_state, None)
    steps, frontierSize, err = solvePuzzle(n, start, Heuristic, prnt)
    if err == 0:
        print ("Problem solved in", steps, "steps!")
    elif err == -1:
        raise RuntimeError("There is no solution!")
    else:
        raise IndexError("Check input again!")



main()
