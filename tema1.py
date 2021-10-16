# Modelarea problemei :
#  Starea problemei este reprezentata de un vector de 0 si 1 unde state[0] - reprezinta pozitia barcii si perechile consecutive disjuncte
#  doua cate doua reprezinta un cuplu (husband i, wife i) unde :
#  0 - persoana se afla pe malul de start (stang)
#  1 - persoana se afla pe malul final (drept)
nrOfCouples = 10
listOfStates = []
visited= []
solution = []
persons = []
parent = []


def person():
    global persons
    for i in range(1, 2 * nrOfCouples, 2):
        persons.append("h" + str(i // 2 + 1))
        persons.append("w" + str(i // 2 + 1))


def initialize_state():
    state = []
    for i in range(0, nrOfCouples * 2 + 1):
        state.append(0)
    return state


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


def displaySolutionBKT():
    for i in range(0, len(solution), 3):
        print(persons[solution[i] - 1] + " ")
        if (solution[i + 1] != -1):
            print(persons[solution[i + 1] - 1] + " ")
    print(solution)


def revealTransition(state1, state2):
    toDisplay = ''
    for i in range(1, len(state1)):
        if (state1[i] != state2[i]):
            toDisplay += persons[i - 1]
            toDisplay + " "
    return toDisplay


def displaySolutionBFS():
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


def BackTracking(state):
    global listOfStates
    global solution
    copyState = state.copy()
    listOfStates.append(copyState)
    if (checkIfStateIsFinal(state)):
        displaySolutionBKT()
        exit()
    else:
        for i in range(1, 2 * nrOfCouples + 1):
            if checkIfTransitionIsValid(state, i, -1, 1 - state[0]):
                newState1 = makeTransition(state, i, -1, 1 - state[0])
                if not newState1 in listOfStates:
                    solution.append(i)
                    solution.append(-1)
                    solution.append(1 - state[0])
                    BackTracking(newState1)
                    solution.pop()
                    solution.pop()
                    solution.pop()
            for j in range(i + 1, 2 * nrOfCouples + 1):
                if checkIfTransitionIsValid(state, i, j, 1 - state[0]):
                    newState2 = makeTransition(state, i, j, 1 - state[0])
                    if not newState2 in listOfStates:
                        solution.append(i)
                        solution.append(j)
                        solution.append(1 - state[0])
                        BackTracking(newState2)
                        solution.pop()
                        solution.pop()
                        solution.pop()

    listOfStates.remove(copyState)



person()
BackTracking(initialize_state())
# BFS(initialize_state())
