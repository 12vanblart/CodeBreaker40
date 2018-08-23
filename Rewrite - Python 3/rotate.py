##############################
##rotate.py ##################
##Python 3 ###################
##############################

###################################################################################################
#This will contain everything needed to rotate the puzzle                                         #
###################################################################################################

##Pass in the following variables
##### Turns Made - Number of turns made thus far. This will start as 0, then increment each time this module is called. 
##### Puzzle - The puzzle in it's current state. This will be returned as the updated puzzle state

def rotate(puzzleIn, turnsMade):
  #First, rotate the first (2) rows [Base Layer]#
  turnableUnits = int((len(puzzleIn)-1)/2)# for SC 40, this should return 3#
  for unit in range(turnableUnits): # For each turnable unit...
    print(unit)
    
    
if __name__ == "__main__":
  rotate([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]], 0)