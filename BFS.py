from Globals import nrOfCouples,visited,solution,parent,persons
def checkIfStateIsFinal(state):
    for i in range(0, nrOfCouples * 2 + 1):
        if state[i] == 0:
            return False
    return True


def checkIfTransitionIsValid(state, person1, person2, side):
    newState = state.copy()

    if newState[person1] != 1 - side:
        return False

    newState[person1] = side
    if person2 != -1:
        if newState[person2] != 1 - side:
            return False
        newState[person2] = side
    newState[0] = side
    for i in range(1, len(newState), 2):
        if newState[i] != newState[i + 1]:
            for j in range(1, len(newState), 2):
                if newState[i + 1] == newState[j]:
                    return False
    return True


def makeTransition(state, person1, person2, side):
    copyState = state[:]
    copyState[person1] = side
    if person2 != -1:
        copyState[person2] = side
    copyState[0] = side
    return copyState


def revealTransition(state1, state2):
    global persons
    toDisplay = ''
    for i in range(1, len(state1)):
        if (state1[i] != state2[i]):
            toDisplay += persons[i - 1]
            toDisplay + " "
    return toDisplay
def displaySolutionBFS():
    global parent
    global visited
    current_index = len(parent) - 1
    toDisplay = []
    while parent[current_index] != -1:
        toDisplay.append(revealTransition(visited[parent[current_index]], visited[current_index]))
        current_index = parent[current_index]
    toDisplay.reverse()
    for display in toDisplay:
       print(display)

def BFS(state):
    global solution
    coada = [state]
    visited.append(state)
    global parent
    parent.append(-1)
    nod = 0
    while coada:
        current_state = coada.pop(0)
        for i in range(1, 2 * nrOfCouples + 1):
            if checkIfTransitionIsValid(current_state, i, -1, 1 - current_state[0]):
                newState1 = makeTransition(current_state, i, -1, 1 - current_state[0])
                if not newState1 in visited:
                    visited.append(newState1)
                    parent.append(nod)
                    coada.append(newState1)
                    if (checkIfStateIsFinal(newState1)):
                        displaySolutionBFS()
                        exit()
            for j in range(i + 1, 2 * nrOfCouples + 1):
                if checkIfTransitionIsValid(current_state, i, j, 1 - current_state[0]):
                    newState2 = makeTransition(current_state, i, j, 1 - current_state[0])
                    if not newState2 in visited:
                        visited.append(newState2)
                        parent.append(nod)
                        coada.append(newState2)
                        if (checkIfStateIsFinal(newState2)):
                            displaySolutionBFS()
                            exit()

        nod = nod + 1
