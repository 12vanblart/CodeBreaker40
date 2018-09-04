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
def checkUnique(solution1, solution2, cog = "X"):
  ## Convert Columns -> Strings Array
  ## Solution 1
  unique = False # Assuming solutions are not unique by default
  solutionList1 = []
  solutionList2 = []
  for col in range(len(solution1[0])):
    solString = ""
    rowVal = 0
    while (rowVal <= len(solution1)):
      if solution1[rowVal][col] == cog:
        solString = solString + str(solution1[rowVal-1][col])
      else:
        solString = solString + str(solution1[rowVal][col])
      rowVal += 2
    solutionList1.append(solString)

  ## Solution 2
  for col in range(len(solution2[0])):
    solString = ""
    rowVal = 0
    while (rowVal <= len(solution2)):
      if solution2[rowVal][col] == cog:
        solString = solString + str(solution2[rowVal-1][col])
      else:
        solString = solString + str(solution2[rowVal][col])
      rowVal += 2
    solutionList2.append(solString)
  
  ##Check if Unique
  while len(solutionList1) > 0:
    if solutionList1[0] in solutionList2:
      solutionList1.pop(0)
    else: 
      unique = True # Once something doesn't match, they must be unique
      break;
  return unique

if __name__ == "__main__":
  checkUnique([[1,4,7],[2,5,8],[3,"X",9]], [[1,1,1],[2,2,2],[3,"X",3]])
  checkUnique([[1,1,1],[2,2,2],[3,3,3]], [[1,1,1],[2,2,2],[3,3,3]])