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
  turnableUnits = int((len(puzzleIn)-1)/2)  # For SC 40, this should return 3#
  for unit in range(turnableUnits):         # For each turnable unit...
    tempArray = puzzleIn[unit*2]            # Set tempArray to the first row of the unit
    tempArray.append(tempArray.pop(0))      # Move the first item of tempArray to the end of the list
    puzzleIn[unit*2] = tempArray            # Set tempArray back to the puzzle's values
    #Repeat for 2nd portion of turnable unit
    tempArray = puzzleIn[(unit*2)+1]
    tempArray.append(tempArray.pop(0))
    puzzleIn[(unit*2)+1] = tempArray
  print(puzzleIn)
    
    
## DEV NOTES##
## 1) Always turn first turnable units. Check if Turns ( + 1?) % [# of Cols] == 0
## If true, turn next unit. Check if Turns (+ 1?) % [# of Cols]^{unit layer} == 0
## Repeat until modulo doesn't return 0. 
    
if __name__ == "__main__":
  rotate([[1,2,3],[4,5,6],[7,"X",8],[9,0,1],[2,"X",3],[4,5,6],[7,8,9]], 0)
  

##  >>> lst = ['string1', 'string2', 'string3']
##  >>> lst.append(lst.pop(lst.index('string2')))
##  Use above to pop the first item in an array to the end of the array. 

