##############################
###TEST FOR INCERMENT ARRAY###
##############################

#################################################################################
##Input an array with all 0's. Max Val 2. Increment a few times. Print result ###
#################################################################################

import incrementArray
import random

def main():
  arr = [[0,0,0],[0,0,0],[0,0,0]]
  maxVal = 2
  loops = random.randint(2,200)
  for i in range(loops):
    incrementArray.incrementArray(arr,maxVal)
  print("loops: ",loops)
  print(arr[0])
  print(arr[1])
  print(arr[2])
  
if __name__ == "__main__":
  main();