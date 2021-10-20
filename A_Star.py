from CommonFunctions import checkIfTransitionIsValid,makeTransition
persons = []
def checkIfStateIsFinal(state,nrOfCouples):
    for i in range(0, nrOfCouples * 2 + 1):
        if state[i] == 0:
            return False
    return True
def person(nrOfCouples):
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


def displaySolution(solution):
    for i in range(1,len(solution)):
        prevState = solution[i-1]
        actuallyState = solution[i]
        sol = [x ^ y for (x, y) in zip(prevState, actuallyState)]
        strState = ""
        for j in range (1,len(sol)):
            if(j==1 and sol[j]!=0):
                strState += "h1 "
            elif(j==2 and sol[j]!=0):
                strState += "w1 "
            elif(j==3 and sol[j]!=0):
                strState += "h2 "
            elif(j==4 and sol[j]!=0):
                strState += "w2 "
            elif(j==5 and sol[j]!=0):
                strState += "h3 "
            elif(j==6 and sol[j]!=0):
                strState += "w3 "
        if(actuallyState[0]):
            strState += "->dreapta"
        else:
            strState += "->stanga"
        print(strState)

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
            if (checkIfStateIsFinal(best_choice,nrOfCouples)):
                solution = [[0,0,0,0,0]] + solution
                displaySolution(solution)
                print(solution)
                exit()
        else: 
            number = 1
            while best_choice in visited and number < len(neighbours):
                best_choice = neighbours[number]
                number += 1
            solution.append(best_choice)
            visited.append(best_choice)
            parent.append(nod)
            coada.append(best_choice)
            if (checkIfStateIsFinal(best_choice,nrOfCouples)):
                solution = [[0,0,0,0,0]] + solution
                displaySolution(solution)
                print(solution)
                exit()
        nod = nod + 1

        
