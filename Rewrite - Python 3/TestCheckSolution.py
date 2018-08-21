##############################
###TEST FOR CHECK SOLUTION ###
##############################

################################################################################
##Pass in a 3x3 grid with a valid solution, and one with an invalid solution ###
################################################################################

from checkSolution import checkSolution

def main():
  successful = 0
  totalTests = 0
  print("Running Test 1")
  puzzle1 = [[1,2,5],[3,2,0],[1,1,0]]
  puzzle1Solution = 5
  puzzle2 = [[1,1,1],[4,3,5],[0,1,5]]
  puzzle2Solution = 40
  result1 = checkSolution(puzzle1, puzzle1Solution)
  totalTests+= 1
  if (result1 == True):
    successful+= 1
    print("Test 1 PASSED")
  else: 
    print("Test 1 FAILED")
  result2 = checkSolution(puzzle2, puzzle2Solution)
  totalTests+= 1
  if (result2 == False ):
    successful+= 1
    print("Test 2 PASSED")
  else:
    print("Test 2 FAILED")
  #Print total successes count
  print("Tests passed: ", successful, "/", totalTests)
  
  
  
if __name__ == "__main__":
  main()