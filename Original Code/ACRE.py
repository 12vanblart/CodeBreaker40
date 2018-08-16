####################
##Tyler VanBlargan##
##January 5th, 2015#
##ACRE Project V.1##
####################

import conv
import random


##First, open the file and make a list for each row##
file = open("ACREnums.txt", "r")
nums = file.readlines()
file.close()
row1 = nums[0].split()
row2 = nums[1].split()
row3 = nums[2].split()
row4 = nums[3].split()
row5 = nums[4].split()
row6 = nums[5].split()
row7 = nums[6].split()


##Get numbers into rows using conv.py functions##
row1= conv.get_nums(row1)
row2= conv.get_nums(row2)
row3= conv.get_nums(row3)
row4= conv.get_nums(row4)
row5= conv.get_nums(row5)
row6= conv.get_nums(row6)
row7= conv.get_nums(row7)


#######################################################################################################
##These are now the rows around the circle with "0" representing the spaces in the gear-shaped pieces##
#######################################################################################################

trials = 0 
##Sample of addition for each column##
#col1 = row1[0]+row2[0]+row3[0]+row4[0]+row5[0]+row6[0]+row7[0]
#if row3[0] != "0":
#    col1 = col1-row2[0]
#if row5[0] != "0":
#    col1 = col1-row4[0]
#if row7[0] != "0":
#    col1 = col1-row6[0]
##############################
##use a WHILE loop############
##############################
##EDIT: USING FOR X in LEN(Y)#
while trials <= 1000000000000000:
    ##Open file to store records in######################
    data = open("ACREdata.txt", "a")
    item1 = 0  #this serves the purpose of letting the columns be checked at the end of the turns####
    item2 = 0
    item3 = 0
    item4 = 0
    item5 = 0
    item6 = 0
    item7 = 0
    ##Accumulator#################
    ##& Solution Counter##########
    total_checked = 0
    solutions = 0
    ##Don't need this?############
    ##for item1 in len(row1):#####

    ##Generate Random Numbers for the hidden numbers in the solution
    row2[1] = random.randint(1,27)
    row2[3] = random.randint(1,27)
    row2[5] = random.randint(1,27)
    row2[7] = random.randint(1,27)
    row2[9] = random.randint(1,27)
    row2[11] = random.randint(1,27)
    row2[13] = random.randint(1,27)

    row4[0] = random.randint(1,27)
    row4[2] = random.randint(1,27)
    row4[4] = random.randint(1,27)
    row4[6] = random.randint(1,27)
    row4[8] = random.randint(1,27)
    row4[10] = random.randint(1,27)
    row4[12] = random.randint(1,27)
    row4[14] = random.randint(1,27)

    row6[1] = random.randint(1,27)
    row6[3] = random.randint(1,27)
    row6[5] = random.randint(1,27)
    row6[7] = random.randint(1,27)
    row6[9] = random.randint(1,27)
    row6[11] = random.randint(1,27)
    row6[13] = random.randint(1,27)
    ################################################################
    while item2 < len(row2):
        print(item2+1, "/ 16")
        while item3 < len(row3):
            while item4 < len(row4):
                while item5 < len(row5):
                    while item6 < len(row6):
                        while item7 < len(row7):
                            total_checked +=1
                            ##Item[#] needs to be slot, not the value
                            col1 = row1[item1%16]+row2[item2%16]+row3[item3%16]+row4[item4%16]+row5[item5%16]+row6[item6%16]+row7[item7%16]
                            if row3[item3%16] != 0:
                                col1 = col1-row2[0]
                            if row5[item5%16] != 0:
                                col1 = col1-row4[0]
                            if row7[item7%16] != 0:
                                col1 = col1-row6[item6]

                            ####Only if the first col works, move on #### Continue this pattern for the rest of the columns.####
                            if col1 == 40:
                                col2 = row1[(item1+1)%16]+row2[(item2+1)%16]+row3[(item3+1)%16]+row4[(item4+1)%16]+row5[(item5+1)%16]+row6[(item6+1)%16]+row7[(item7+1)%16]
                                if row3[(item3+1)%16] != 0:
                                    col2 = col2-row2[(item2+1)%16]
                                if row5[(item5+1)%16] != 0:
                                    col2 = col2-row4[(item4+1)%16]
                                if row7[(item7+1)%16] != 0:
                                    col2 = col2-row6[(item6+1)%16]
                                    
                                if col2 == 40:
                                    col3 = row1[(item1+2)%16]+row2[(item2+2)%16]+row3[(item3+2)%16]+row4[(item4+2)%16]+row5[(item5+2)%16]+row6[(item6+2)%16]+row7[(item7+2)%16]
                                    if row3[(item3+2)%16] != 0:
                                        col3 = col3-row2[(item2+2)%16]
                                    if row5[(item5+2)%16] != 0:
                                        col3 = col3-row4[(item4+2)%16]
                                    if row7[(item7+2)%16] != 0:
                                        col3 = col3-row6[(item6+2)%16]
                                        
                                    if col3 == 40:
                                        col4 = row1[(item1+3)%16]+row2[(item2+3)%16]+row3[(item3+3)%16]+row4[(item4+3)%16]+row5[(item5+3)%16]+row6[(item6+3)%16]+row7[(item7+3)%16]
                                        if row3[(item3+3)%16] != 0:
                                            col4 = col4-row2[(item2+3)%16]
                                        if row5[(item5+3)%16] != 0:
                                            col4 = col4-row4[(item4+3)%16]
                                        if row7[(item7+3)%16] != 0:
                                            col4 = col4-row6[(item6+3)%16]

                                        if col4 == 40:
                                            col5 = row1[(item1+4)%16]+row2[(item2+4)%16]+row3[(item3+4)%16]+row4[(item4+4)%16]+row5[(item5+4)%16]+row6[(item6+4)%16]+row7[(item7+4)%16]
                                            if row3[(item3+4)%16] != 0:
                                                col5 = col5-row2[(item2+4)%16]
                                            if row5[(item5+4)%16] != 0:
                                                col5 = col5-row4[(item4+4)%16]
                                            if row7[(item7+4)%16] != 0:
                                                col5 = col5-row6[(item6+4)%16]

                                            if col5 == 40:
                                                col6 = row1[(item1+5)%16]+row2[(item2+5)%16]+row3[(item3+5)%16]+row4[(item4+5)%16]+row5[(item5+5)%16]+row6[(item6+5)%16]+row7[(item7+5)%16]
                                                if row3[(item3+5)%16] != 0:
                                                    col6 = col6-row2[(item2+5)%16]
                                                if row5[(item5+5)%16] != 0:
                                                    col6 = col6-row4[(item4+5)%16]
                                                if row7[(item7+5)%16] != 0:
                                                    col6 = col6-row6[(item6+5)%16]

                                                if col6 == 40:
                                                    col7 = row1[(item1+6)%16]+row2[(item2+6)%16]+row3[(item3+6)%16]+row4[(item4+6)%16]+row5[(item5+6)%16]+row6[(item6+6)%16]+row7[(item7+6)%16]
                                                    if row3[(item3+6)%16] != 0:
                                                        col7 = col7-row2[(item2+6)%16]
                                                    if row5[(item5+6)%16] != 0:
                                                        col7 = col7-row4[(item4+6)%16]
                                                    if row7[(item7+6)%16] != 0:
                                                        col7 = col7-row6[(item6+6)%16]

                                                    if col7 == 40:
                                                        col8 = row1[(item1+7)%16]+row2[(item2+7)%16]+row3[(item3+7)%16]+row4[(item4+7)%16]+row5[(item5+7)%16]+row6[(item6+7)%16]+row7[(item7+7)%16]
                                                        if row3[(item3+7)%16] != 0:
                                                            col8 = col8-row2[(item2+7)%16]
                                                        if row5[(item5+7)%16] != 0:
                                                            col8 = col8-row4[(item4+7)%16]
                                                        if row7[(item7+7)%16] != 0:
                                                            col8 = col8-row6[(item6+7)%16]

                                                        if col8 == 40:
                                                            col9 = row1[(item1+8)%16]+row2[(item2+8)%16]+row3[(item3+8)%16]+row4[(item4+8)%16]+row5[(item5+8)%16]+row6[(item6+8)%16]+row7[(item7+8)%16]
                                                            if row3[(item3+8)%16] != 0:
                                                                col9 = col9-row2[(item2+8)%16]
                                                            if row5[(item5+8)%16] != 0:
                                                                col9 = col9-row4[(item4+8)%16]
                                                            if row7[(item7+8)%16] != 0:
                                                                col9 = col9-row6[(item6+8)%16]

                                                            if col9 == 40:
                                                                col10 = row1[(item1+9)%16]+row2[(item2+9)%16]+row3[(item3+9)%16]+row4[(item4+9)%16]+row5[(item5+9)%16]+row6[(item6+9)%16]+row7[(item7+9)%16]
                                                                if row3[(item3+9)%16] != 0:
                                                                    col10 = col10-row2[(item2+9)%16]
                                                                if row5[(item5+9)%16] != 0:
                                                                    col10 = col10-row4[(item4+9)%16]
                                                                if row7[(item7+9)%16] != 0:
                                                                    col10 = col10-row6[(item6+9)%16]

                                                                if col10 == 40:
                                                                    col11 = row1[(item1+10)%16]+row2[(item2+10)%16]+row3[(item3+10)%16]+row4[(item4+10)%16]+row5[(item5+10)%16]+row6[(item6+10)%16]+row7[(item7+10)%16]
                                                                    if row3[(item3+10)%16] != 0:
                                                                        col11 = col11-row2[(item2+10)%16]
                                                                    if row5[(item5+10)%16] != 0:
                                                                        col11 = col11-row4[(item4+10)%16]
                                                                    if row7[(item7+10)%16] != 0:
                                                                        col11 = col11-row6[(item6+10)%16]

                                                                    if col11 == 40:
                                                                        col12 = row1[(item1+11)%16]+row2[(item2+11)%16]+row3[(item3+11)%16]+row4[(item4+11)%16]+row5[(item5+11)%16]+row6[(item6+11)%16]+row7[(item7+11)%16]
                                                                        if row3[(item3+11)%16] != 0:
                                                                            col12 = col12-row2[(item2+11)%16]
                                                                        if row5[(item5+11)%16] != 0:
                                                                            col12 = col12-row4[(item4+11)%16]
                                                                        if row7[(item7+11)%16] != 0:
                                                                            col12 = col12-row6[(item6+11)%16]

                                                                        if col12 == 40:
                                                                            col13 = row1[(item1+12)%16]+row2[(item2+12)%16]+row3[(item3+12)%16]+row4[(item4+12)%16]+row5[(item5+12)%16]+row6[(item6+12)%16]+row7[(item7+12)%16]
                                                                            if row3[(item3+12)%16] != 0:
                                                                                col13 = col13-row2[(item2+12)%16]
                                                                            if row5[(item5+12)%16] != 0:
                                                                                col13 = col13-row4[(item4+12)%16]
                                                                            if row7[(item7+12)%16] != 0:
                                                                                col13 = col13-row6[(item6+12)%16]

                                                                            if col13 == 40:
                                                                                col14 = row1[(item1+13)%16]+row2[(item2+13)%16]+row3[(item3+13)%16]+row4[(item4+13)%16]+row5[(item5+13)%16]+row6[(item6+13)%16]+row7[(item7+13)%16]
                                                                                if row3[(item3+13)%16] != 0:
                                                                                    col14 = col14-row2[(item2+13)%16]
                                                                                if row5[(item5+13)%16] != 0:
                                                                                    col14 = col14-row4[(item4+13)%16]
                                                                                if row7[(item7+13)%16] != 0:
                                                                                    col14 = col14-row6[(item6+13)%16]

                                                                                if col14 == 40:
                                                                                    col15 = row1[(item1+14)%16]+row2[(item2+14)%16]+row3[(item3+14)%16]+row4[(item4+14)%16]+row5[(item5+14)%16]+row6[(item6+14)%16]+row7[(item7+14)%16]
                                                                                    if row3[(item3+14)%16] != 0:
                                                                                        col15 = col15-row2[(item2+14)%16]
                                                                                    if row5[(item5+14)%16] != 0:
                                                                                        col15 = col15-row4[(item4+14)%16]
                                                                                    if row7[(item7+14)%16] != 0:
                                                                                        col15 = col15-row6[(item6+14)%16]

                                                                                    if col15 == 40:
                                                                                        col16 = row1[(item1+15)%16]+row2[(item2+15)%16]+row3[(item3+15)%16]+row4[(item4+15)%16]+row5[(item5+15)%16]+row6[(item6+15)%16]+row7[(item7+15)%16]
                                                                                        if row3[(item3+15)%16] != 0:
                                                                                            col16 = col16-row2[(item2+15)%16]
                                                                                        if row5[(item5+15)%16] != 0:
                                                                                            col16 = col16-row4[(item4+15)%16]
                                                                                        if row7[(item7+15)%16] != 0:
                                                                                            col16 = col16-row6[(item6+15)%16]

                                                                                        ##FINALLY##
                                                                                        if col16 == 40:
                                                                                            print("The solution is:", row1[item1], row2[item2], row3[item3], row4[item4], row5[item5], row6[item6], row7[item7])
                                                                                            solutions +=1
                                                                                            data.write(str(row1) + "\n")
                                                                                            data.write(str(row2) + "\n")
                                                                                            data.write(str(row3) + "\n")
                                                                                            data.write(str(row4) + "\n")
                                                                                            data.write(str(row5) + "\n")
                                                                                            data.write(str(row6) + "\n")
                                                                                            data.write(str(row7) + "\n")
                                                                                            data.write("Solutions found for these numbers: " +str(solutions) +"\n\n")
                                                                                            data.close()


                            item7 += 1
                        item6 += 1
                        item7 = 0
                    item5 += 1
                    item6 = 0
                item4 += 1
                item5 = 0
            item3 += 1
            item4 = 0
        item2 +=1
        item3 = 0
    trials+=1                ##########################################IMPORTANT NOTE: THIS IS CHECKING THE EVEN ROWS AS SEPERATE FROM THE ATTACEHED ROWS#######################









print("Total Calculations Made: ", total_checked)
print("Solutions Found: ", solutions)
###################################################################
##SAVE FOR TEST PRINTING###########################################
#print(row1, row2, row3, row4, row5, row6, row7)###################
##############################COUNTER##############################
#########################Solution Printer##########################



