#Simple Coin Flip Simulation
#Author: Samuel Hicks
import random

def coin_flip(trials, num_flips):
    """This function will simulate n games of fliping a coin. It uses a random number generator
    to simulate a coin flip. Heads is denoted by a '0' and tails is denoted by a '1'. The 
    averages of the total heads and total tails are recorded. The results are then printed
    for each trial."""

    total_heads = 0
    total_tails = 0

    for i in range(1,trials+1): #Loop for running each trial
        #Initalize variables to 0 at the start of each trial
        heads_val = heads_avg = 0 
        tails_val = tails_avg = 0
        flips_sequence=[]

        for j in range(num_flips): #Loop for determining a flip
            flip = random.randint(0,1) #Random number generator for picking heads(0) or tails(1)

            if flip == 0: #If heads
                heads_val+=1 #Increament the heads counter by 1
                flips_sequence.append('H') #Apeend a 'H' to the list
            else: #If tails
                tails_val+=1 #Increament the tails counter by 1
                flips_sequence.append('T') #Append a 'T' to the list

        #Keeps track of the heads and tails averages
        heads_avg = heads_val/num_flips    
        tails_avg = tails_val/num_flips  

        #Keeps track of the total heads and tails of every trial run
        total_heads = heads_val + total_heads
        total_tails = tails_val + total_tails

        #Print the data
        print("\n==============================")
        print("\nTrial {}".format(i))
        print("Total Heads: {} | {:.0%} Heads \nTotal Tails: {} | {:.0%} Tails".format(heads_val,heads_avg,tails_val,tails_avg))
        print("Outcome of the current trial:", '[%s]' % ', '.join(map(str,flips_sequence)))
        
    #Calculate the final results
    total_num_flips = trials*num_flips
    total_heads_avg = total_heads/total_num_flips 
    total_tails_avg = total_tails/total_num_flips 

    #Print the final results of the simulation
    print("\n==============================")
    print("      Simulation Results")
    print("==============================")
    print("Number of trials preformed: {} \nNumber of flips per trial: {}".format(trials, num_flips))
    print("\nTotal Heads of {} trials: {} | {:.0%} Heads".format(trials, total_heads, total_heads_avg))
    print("Total Tails of {} trials: {} | {:.0%} Tails".format(trials, total_tails, total_tails_avg))
    print("==============================")


def main():
    #User Input data
    # print("==============================")
    # trials = int(input("How many trials are to be ran?: ")) #Number of tails to be ran
    # num_flips = int(input("How many flips per trial?: ")) #Number of flips to be done
    # print("==============================")

    #Can be used as just variables too
    trials = 10 #Number of tails to be ran
    num_flips = 20 #Number of flips to be done

    coin_flip(trials, num_flips) #Run the trials

if __name__ == "__main__":
    main()