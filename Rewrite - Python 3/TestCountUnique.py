##############################
###TEST FOR COUNT UNIQUE #####
##############################

#################################################################################
##Pass in a few "solutions" to validate logic for countUnique.py  ###############
#################################################################################

from countUnique import checkUnique

def main():
  successful = 0
  totalTests = 0
  solved1 = [[1,3,2,4],[2,2,3,1],[4,"X",3,"X"]]
  solved2 = [[1,1,1,1],[2,4,3,4],[4,"X",4,"X"]]
  ## Test 1
  print("Running Test 1")
  result1 = checkUnique(solved1, solved2)
  totalTests += 1
  if (result1 == True):
    successful += 1
    print("Test 1 PASSED")
  else: 
    print("Test 1 FAILED")
  ## Test 2
  result2 = checkUnique(solved1, solved1)
  totalTests += 1
  if (result2 == False):
    successful += 1
    print("Test 2 PASSED")
  else: 
    print("Test 2 FAILED")
  
  #Print total successes count
  print("Tests passed: ", successful, "/", totalTests)
  
  
  
if __name__ == "__main__":
    main()