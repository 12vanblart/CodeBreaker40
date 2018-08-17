##############################
##incrementArray.py ##########
##Python 3 ###################
##############################

###################################################################################################
#This will contain everything needed to increment a 2-D array                                        #
###################################################################################################
#The function should support dynamic 'max' values to easily allow testing                         #
###################################################################################################

def incrementArray(arrIn, maxVal):
  for row in arrIn:
    for col in arrIn[row]:
      arrIn[row][col] = arrIn[row][col] + 1
      if arrIn[row][col] == maxVal:
        arrIn[row][col] = 0
      else:
        break
  return arrIn