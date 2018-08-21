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

##Check Solution for a puzzle with no "cog" pieces covering lower layers
def checkSolution(puzzle, value):
  response = True
  for col in range(len(puzzle[0])):
    total = 0
    for row in range(len(puzzle)):
      total += puzzle[row][col]
    if total != value:
      response = False
      break
  return response

##Check Solution for a puzzle with "cog" pieces covering lower layers

