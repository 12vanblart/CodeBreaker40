##############################
##incrementArray.py ##########
##Python 3 ###################
##############################

###################################################################################################
#This will contain everything needed to increment a 2-D array                                     #
###################################################################################################
#The function should support dynamic 'max' values to easily allow testing and scaling             #
###################################################################################################

def incrementArray(arrIn, maxVal):
  arrIn[0][0] = arrIn[0][0] + 1
  for row in range(len(arrIn)):
    for col in range(len(arrIn[row])):
      if arrIn[row][col] == maxVal:
        arrIn[row][col] = 0
        if col == len(arrIn[row])-1:
          if row != len(arrIn)-1:
            #INCREMENT NEXT ROW[0]
            arrIn[row+1][0] = arrIn[row+1][0] + 1
        else:
          #INCREMENT NEXT COLUMN'S VALUE
          arrIn[row][col+1] = arrIn[row][col+1] + 1
      else:
        break
  return arrIn