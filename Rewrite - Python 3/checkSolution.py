##############################
##checkSolution.py############
##Python 3 ###################
##############################

###################################################################################################
#This will contain everything needed to collect an array and check if the columns total correctly #
###################################################################################################
#The check should support dynamic solution values to easily allow testing                         #
###################################################################################################

##This will return:
##### FALSE if not a solution
##### TRUE if it is a solution

##Check Solution for a puzzle with "cog" pieces covering lower layers
def checkSolution(puzzle, value, cog = "X"): 
  ## `cog` is the icon denoting to use the below number
  response = True
  for col in range(len(puzzle[0])):
    total = 0
    rowVal = 0
    while (rowVal <= len(puzzle)):
      if puzzle[rowVal][col] == cog:
        total += puzzle[rowVal-1][col]
      else:
        total += puzzle[rowVal][col]
      rowVal += 2
    if total != value:
      response = False
      break
  return response
##NOTE: IF this returns TRUE, need to store solution to ensure uniqueness##
  