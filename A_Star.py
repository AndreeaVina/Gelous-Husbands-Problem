from CommonFunctions import checkIfTransitionIsValid,makeTransition,checkIfStateIsFinal
persons = []
def person():
    global persons
    for i in range(1, 2 * nrOfCouples, 2):
        persons.append("h" + str(i // 2 + 1))
        persons.append("w" + str(i // 2 + 1))
def Heuristic_A_Star(state,nrOfCouples):
    count = 0
    for i in range(2,2*nrOfCouples+1,2):
        if state[i] == 0:
            count += 1
    return count
def get_all_neighbours(current_state,nrOfCouples):
    better_neighbours = []
    for i in range(1, 2 * nrOfCouples + 1):
            if checkIfTransitionIsValid(current_state, i, -1, 1 - current_state[0]):
                newState1 = makeTransition(current_state, i, -1, 1 - current_state[0])
                better_neighbours.append(newState1)
            for j in range(i + 1, 2 * nrOfCouples + 1):
                if checkIfTransitionIsValid(current_state, i, j, 1 - current_state[0]):
                    newState2 = makeTransition(current_state, i, j, 1 - current_state[0])
                    better_neighbours.append(newState2)
    return better_neighbours
                   

def queueSorting(states_queue,Heuristic_A_Star,nrOfCouples):
    for i in range(0,len(states_queue)):
        for j in range(i+1,len(states_queue)):
            if(Heuristic_A_Star(states_queue[i],nrOfCouples)>Heuristic_A_Star(states_queue[j],nrOfCouples)):
                aux = states_queue[i]
                states_queue[i] = states_queue[j]
                states_queue[j] = aux
    return states_queue


def revealTransition(state1, state2):
    global persons
    toDisplay = ''
    for i in range(1, len(state1)):
        if (state1[i] != state2[i]):
            toDisplay += persons[i - 1]
            toDisplay + " "
    return toDisplay


def displaySolution(parent,visited):
    current_index = len(parent) - 1
    toDisplay = []
    while parent[current_index] != -1:
        toDisplay.append(revealTransition(visited[parent[current_index]], visited[current_index]))
        current_index = parent[current_index]
    toDisplay.reverse()
    for display in toDisplay:
       print(display)


def A_star(state,nrOfCouples):
    solution = []
    coada = [state]
    visited = []
    parent = []
    visited.append(state)
    parent.append(-1)
    nod = 0
    neighbours = []
    while coada:
        current_state = coada.pop(0)
        neighbours = get_all_neighbours(current_state,nrOfCouples)
        neighbours =  queueSorting(neighbours,Heuristic_A_Star,nrOfCouples)
        best_choice = neighbours[0]
        if(best_choice not in visited ):
            solution.append(best_choice)
            visited.append(best_choice)
            parent.append(nod)
            coada.append(best_choice)
            if (checkIfStateIsFinal(best_choice)):
                print(solution)
                # displaySolution(parent,visited)
                exit()
        else: 
            number = 1
            while best_choice in visited:
                best_choice = neighbours[number]
                number += 1
            solution.append(best_choice)
            visited.append(best_choice)
            parent.append(nod)
            coada.append(best_choice)
            if (checkIfStateIsFinal(best_choice)):
                print(solution)
                # displaySolution(parent,visited)
                exit()
        nod = nod + 1

        
