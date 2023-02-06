import time
import SystemConfiguration
from SimCore import Simulation
import lib.rngs



# Main function 
def main():

    print("|------------------------------------------|\n")
    print("\tPMCSN Simulation Program\n")
    print("\tAuthor :    Marco Calavaro \n")
    
    print("|------------------------------------------|\n\n")
    
    inp = -1

    while (inp !=0):

        print("\n--------------------MENU--------------------\n")
        print("\t[0] Quit program \n")
        print("\t[1] Output single simulation run \n")
        print("\t[2] Validation Run\n")
        print("\t[3] Infinite Horizon study\n")
        print("\t[4] TEST Configuration 1\n")
        print("\t[5] TEST Configuration 2\n")
        print("\t[6] TEST Configuration 3\n")

        try:
            inp = int(input("Select a number from menu: "))
        except:
            print("No input on menu' quitting........")
            quit()

        if (inp == 1) :
            try:
                seed = int(input("Enter a seed for the run: "))
                singleRun(seed) # execute a single run whit seed
            except:
                print("No input starting a default........")
                singleRun(9)
            
        elif (inp == 2):
            validation(256,"outputStat/Validation")
            

        elif (inp == 3) :
            
            #batch = (1024,128) #(b,k) TODO come selezionare
            batch = (256,64)
            InfiniteHorizonStudy(batch)

        elif (inp == 4):
            print("ATTENTION CONFIGURE SYSTEM MANUALLY, CONTROL IT")
            time.sleep(1)

            file = "outputStat/Test/conf1"
            test(500,file)
        elif (inp == 5):
            print("ATTENTION CONFIGURE SYSTEM MANUALLY, CONTROL IT")
            time.sleep(1)

            file = "outputStat/Test/conf2"
            test(500,file)

        elif (inp == 6):
            print("ATTENTION CONFIGURE SYSTEM MANUALLY, CONTROL IT")
            time.sleep(1)
            
            file = "outputStat/Test/conf3"
            test(500,file)

        elif (inp == 0):
            print("\n-------------------QUIT--------------------\n")
        else:
            print("Wrong input")
        
        #time.sleep(2)

    # End program
    quit()    

def singleRun(seed = 9):
    sim = Simulation(seed)
    sim.startSimulation()

def validation(replica,file):
    seed = 123456789
    sim = Simulation(seed)
    for i in range(0,replica):
        sim.startSimulation(saveFile=file)
        seed = lib.rngs.getSeed()
        print("Run number {} completed, new seed: {}".format(i,seed))
        sim.reset_initial_state(seed)

def InfiniteHorizonStudy(batch,seed = 12345):
    simulationTime = ( batch[0] * batch[1] ) #/ SystemConfiguration.arrivalRate
    sim = Simulation(seed,simulationTime=simulationTime)
    sim.startSimulation(stationary=True,batch=batch)


def test(replica,file):
    lib.rngs.plantSeeds(9)
    sim = Simulation(None)
    for i in range(0,replica):
        sim.startSimulation(saveFile=file)
        print("Run number {} completed".format(i))
        sim.reset_initial_state(None)







#Start simulation
if __name__ == "__main__":
    main()