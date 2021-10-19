from HillClimbing import HillClimbing
from BackTracking import BackTracking, initialize_state
from CommonFunctions import initialize_state
from BFS import BFS
from Globals import nrOfCouples 
from A_Star import A_star
# from CommonFunctions import initialize_state,person


def Menu():
    try:
        nrOfCouples = int(input("Please enter the number of couples\n"))
        if(nrOfCouples > 3):
            print("No possible solution.")
            return 
        desiredProgram = input("Please enter the desire program (BKT/BFS/Hillclimbing/A*)\n")
    except:
        print("Wrong format")
        exit()
    if(desiredProgram=="BKT"):
        BackTracking(initialize_state(nrOfCouples))
    elif(desiredProgram=="BFS"):
        BFS(initialize_state())
    elif(desiredProgram=="Hillclimbing"):
        HillClimbing(initialize_state(nrOfCouples),nrOfCouples)
    elif(desiredProgram=="A*"):
        A_star(initialize_state(nrOfCouples),nrOfCouples)
    else:
        print("Wrong algorithm")
