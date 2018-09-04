##############################
##countUnique.py##############
##Python 3 ###################
##############################

###################################################################################################
#This will contain everything needed to determine if two solutions are unique to each other       #
###################################################################################################
#The number of columns/rows needs to be dynamic so that any size puzzle can be checked            #
###################################################################################################

#Collect 2 puzzles in#
def checkUnique(solution1, solution2):
  ## Convert Columns -> Strings Array
  ## Solution 1
  solutionList1 = []
  solutionList2 = []
  for col in range(len(solution1[0])):
    solString = ""
    for row in range(len(solution1)):
      solString = solString + str(solution1[row][col])
    solutionList1.append(solString)
  print(solutionList1)


if __name__ == "__main__":
  checkUnique([[1,4,7],[2,5,8],[3,6,9]], [[1,1,1],[2,2,2],[3,3,3]])