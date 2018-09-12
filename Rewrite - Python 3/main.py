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
    #Init File for results
    f = open("solutions.txt", "a")
    for i in range(268435457):
        #Increment Puzzle
        puzzle = incrementArray.incrementArray(puzzle, 40)
        print(puzzle)
        #Check for solutions
        if (checkSolution.checkSolution(puzzle, target, cog)):
            solutions.append(puzzle)
        #rotate puzzle & Check solution
        puzzleR = puzzle #Set Puzzle R to ensure that the initial puzzle is always at rotations = 0
        for j in range(64000):
            puzzleR = rotate.rotate(puzzleR, j)
            if (checkSolution.checkSolution(puzzleR, target, cog)):
                solutions.append(puzzleR)
        #Append to file
        f.write("\n")
        f.write(solutions)
        f.close()
            
    print(solutions)
    
    
    
    
if __name__ == "__main__":
    main()