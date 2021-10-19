from CommonFunctions import checkIfTransitionIsValid,checkIfStateIsFinal,makeTransition
from Globals import nrOfCouples,listOfStates,solution,persons

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
    person()
    for i in range(0, len(solution), 3):
        print(persons[solution[i] - 1] + " ")
        if (solution[i + 1] != -1):
            print(persons[solution[i + 1] - 1] + " ")
    print(solution)


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
