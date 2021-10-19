from Globals import nrOfCouples,listOfStates,visited,solution,persons,parent
def person():
    global persons
    for i in range(1, 2 * nrOfCouples, 2):
        persons.append("h" + str(i // 2 + 1))
        persons.append("w" + str(i // 2 + 1))


def initialize_state(nrOfCouples):
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

