##############################
##main.py#####################
##Python 3 ###################
##############################

#####################################################################
#This is the central point for running everything.                  #
#####################################################################
#Baseline test numbers can be found in ACREnums.txt files           #
#####################################################################

import countUnique
import checkSolution
import incrementArray
import rotate

def main():
    # Initialize puzzle and set target
    puzzle = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,"X",0,"X",0,"X",0,"X",0,"X",0,"X",0,"X",0,"X"],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,"X",0,"X",0,"X",0,"X",0,"X",0,"X",0,"X",0,"X"],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,"X",0,"X",0,"X",0,"X",0,"X",0,"X",0,"X",0,"X"]]
    target = 40
    cog = "X"
    solutions = []
    for i in range(268435457):
        #Increment Puzzle
        puzzle = incrementArray.incrementArray(puzzle, 40)
        print(puzzle)
        #Check for solutions
        if (checkSolution.checkSolution(puzzle, target, cog)):
            solutions.append(puzzle)
    print(solutions)
    
    
    
    
if __name__ == "__main__":
    main()