import random
from Globals import solution,nrOfCouples
from CommonFunctions import checkIfTransitionIsValid,makeTransition,checkIfStateIsFinal

def Heuristic(current_state,nrOfCouples):
    nrOfWives = 0
    for wife in range(2,nrOfCouples*2 + 1,2):
        if(current_state[wife] == 1):
            nrOfWives = nrOfWives + 1
    return nrOfWives

def get_better_or_equal_neighbours(current_state,Heuristic):
    better_neighbours = []
    for i in range(1, 2 * nrOfCouples + 1):
            if checkIfTransitionIsValid(current_state, i, -1, 1 - current_state[0]):
                newState1 = makeTransition(current_state, i, -1, 1 - current_state[0])
                if(Heuristic(newState1,nrOfCouples) >= Heuristic(current_state,nrOfCouples)):
                    better_neighbours.append(newState1)
            for j in range(i + 1, 2 * nrOfCouples + 1):
                if checkIfTransitionIsValid(current_state, i, j, 1 - current_state[0]):
                    newState2 = makeTransition(current_state, i, j, 1 - current_state[0])
                    if(Heuristic(newState2,nrOfCouples) >= Heuristic(current_state,nrOfCouples)):
                        better_neighbours.append(newState2)
    return better_neighbours
                   


def HillClimbing(state,nrOfCouples):
    solution.append(state)
    better_neighbour = state
    while True:
        neighbours = get_better_or_equal_neighbours(better_neighbour,Heuristic)
        if len(neighbours) == 0:
            print("Partial solution found : ")
            print(solution)
            break
        better_neighbour = random.choice(neighbours)
        while better_neighbour in solution and len(neighbours) > 1:
            neighbours.remove(better_neighbour)
            better_neighbour = random.choice(neighbours)
        if better_neighbour in solution :
            neighbours.remove(better_neighbour)
        if len(neighbours)>0 : 
            solution.append(better_neighbour)
        if checkIfStateIsFinal(better_neighbour):
            print("Complete solution found : ")
            print(solution)
            break
        elif len(neighbours) == 0:
            print("Partial solution found : ")
            print(solution)
            break


