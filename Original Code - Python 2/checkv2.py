####################
##Tyler VanBlargan##
##January 5th, 2015#
##ACRE Project V.3##
####################
import conv

def main():

    ##First, open the file and make a list for each row##
    file = open("ACREnums2.txt", "r")
    nums = file.readlines()
    file.close()
    row1 = nums[0].split()
    row2 = nums[1].split()
    row3 = nums[2].split()
    row4 = nums[3].split()
    row5 = nums[4].split()
    row6 = nums[5].split()
    row7 = nums[6].split()
    row8 = nums[7].split()
    row9 = nums[8].split()


    ##Get numbers into rows using conv.py functions##
    row1= conv.get_nums(row1)
    row2= conv.get_nums(row2)
    row3= conv.get_nums(row3)
    row4= conv.get_nums(row4)
    row5= conv.get_nums(row5)
    row6= conv.get_nums(row6)
    row7= conv.get_nums(row7)
    row8= conv.get_nums(row8)
    row9= conv.get_nums(row9)


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
    #while trials <= 1000000000000000:
    ##Open file to store records in######################

    #item1 = 0  #this serves the purpose of letting the columns be checked at the end of the turns####
    #item2 = 0
    #item3 = 0
    #item4 = 0
    #item5 = 0
    #item6 = 0
    #item7 = 0
    ##Accumulator#################
    ##& Solution Counter##########
    item1 = 0  #this serves the purpose of letting the columns be checked at the end of the turns####
    item2 = 0
    item3 = 0
    item4 = 0
    item5 = 0
    item6 = 0
    item7 = 0
    item8 = 0
    item9 = 0
############################################################################################################################################################################################################################################################################################
    while item2 < len(row2):
        print(item2+1, "/ 16")
        while item3 < len(row3):
            while item4 < len(row4):
                while item5 < len(row5):
                    while item6 < len(row6):
                        while item7 < len(row7):
                            while item8 < len(row8):
                                while item9 < len(row9):
                                    solutions = 0
                                    ##Item[#] needs to be slot, not the value
                                    col1 = row1[item1%16]+row2[item2%16]+row3[item3%16]+row4[item4%16]+row5[item5%16]+row6[item6%16]+row7[item7%16]+row8[item8%16]+row9[item9%16]
                                    if row3[item3%16] != 100:
                                        col1 = col1-row2[item2]
                                    if row5[item5%16] != 100:
                                        col1 = col1-row4[item4]
                                    if row7[item7%16] != 100:
                                        col1 = col1-row6[item6]
                                    if row9[item9%16] != 100:
                                        col1 = col1-row8[item8]
                                    if row3[item3%16] == 100:
                                        col1 = col1-100
                                    if row5[item5%16] == 100:
                                        col1 = col1-100
                                    if row7[item7%16] == 100:
                                        col1 = col1-100
                                    if row9[item9%16] == 100:
                                        col1 = col1-100
                                    

                                    ####Only if the first col works, move on #### Continue this pattern for the rest of the columns.####
                                    if col1 == 50:
                                        col2 = row1[(item1+1)%16]+row2[(item2+1)%16]+row3[(item3+1)%16]+row4[(item4+1)%16]+row5[(item5+1)%16]+row6[(item6+1)%16]+row7[(item7+1)%16]+row8[(item8+1)%16]+row9[(item9+1)%16]
                                        if row3[(item3+1)%16] != 100:
                                            col2 = col2-row2[(item2+1)%16]
                                        if row5[(item5+1)%16] != 100:
                                            col2 = col2-row4[(item4+1)%16]
                                        if row7[(item7+1)%16] != 100:
                                            col2 = col2-row6[(item6+1)%16]
                                        if row9[(item9+1)%16] != 100:
                                            col2 = col2-row8[(item8+1)%16]
                                        if row3[(item3+1)%16] == 100:
                                            col2 = col2-100
                                        if row5[(item5+1)%16] == 100:
                                            col2 = col2-100
                                        if row7[(item7+1)%16] == 100:
                                            col2 = col2-100
                                        if row9[(item9+1)%16] == 100:
                                            col2 = col2-100
                                            
                                        if col2 == 50:
                                            col3 = row1[(item1+2)%16]+row2[(item2+2)%16]+row3[(item3+2)%16]+row4[(item4+2)%16]+row5[(item5+2)%16]+row6[(item6+2)%16]+row7[(item7+2)%16]+row8[(item8+2)%16]+row9[(item9+2)%16]
                                            if row3[(item3+2)%16] != 100:
                                                col3 = col3-row2[(item2+2)%16]
                                            if row5[(item5+2)%16] != 100:
                                                col3 = col3-row4[(item4+2)%16]
                                            if row7[(item7+2)%16] != 100:
                                                col3 = col3-row6[(item6+2)%16]
                                            if row9[(item9+2)%16] != 100:
                                                col3 = col3-row8[(item8+2)%16]
                                            if row3[(item3+2)%16] == 100:
                                                col3 = col3-100
                                            if row5[(item5+2)%16] == 100:
                                                col3 = col3-100
                                            if row7[(item7+2)%16] == 100:
                                                col3 = col3-100
                                            if row9[(item9+2)%16] == 100:
                                                col3 = col3-100
                                                
                                            if col3 == 50:
                                                col4 = row1[(item1+3)%16]+row2[(item2+3)%16]+row3[(item3+3)%16]+row4[(item4+3)%16]+row5[(item5+3)%16]+row6[(item6+3)%16]+row7[(item7+3)%16]+row8[(item8+3)%16]+row9[(item9+3)%16]
                                                if row3[(item3+3)%16] != 100:
                                                    col4 = col4-row2[(item2+3)%16]
                                                if row5[(item5+3)%16] != 100:
                                                    col4 = col4-row4[(item4+3)%16]
                                                if row7[(item7+3)%16] != 100:
                                                    col4 = col4-row6[(item6+3)%16]
                                                if row9[(item9+3)%16] != 100:
                                                    col4 = col4-row8[(item8+3)%16]
                                                if row3[(item3+3)%16] == 100:
                                                    col4 = col4-100
                                                if row5[(item5+3)%16] == 100:
                                                    col4 = col4-100
                                                if row7[(item7+3)%16] == 100:
                                                    col4 = col4-100
                                                if row9[(item9+3)%16] == 100:
                                                    col4 = col4-100


                                                if col4 == 50:
                                                    col5 = row1[(item1+4)%16]+row2[(item2+4)%16]+row3[(item3+4)%16]+row4[(item4+4)%16]+row5[(item5+4)%16]+row6[(item6+4)%16]+row7[(item7+4)%16]+row8[(item8+4)%16]+row9[(item9+4)%16]
                                                    if row3[(item3+4)%16] != 100:
                                                        col5 = col5-row2[(item2+4)%16]
                                                    if row5[(item5+4)%16] != 100:
                                                        col5 = col5-row4[(item4+4)%16]
                                                    if row7[(item7+4)%16] != 100:
                                                        col5 = col5-row6[(item6+4)%16]
                                                    if row9[(item9+4)%16] != 100:
                                                        col5 = col5-row8[(item8+4)%16]
                                                    if row3[(item3+4)%16] == 100:
                                                        col5 = col5-100
                                                    if row5[(item5+4)%16] == 100:
                                                        col5 = col5-100
                                                    if row7[(item7+4)%16] == 100:
                                                        col5 = col5-100
                                                    if row9[(item9+4)%16] == 100:
                                                        col5 = col5-100

                                                    if col5 == 50:
                                                        col6 = row1[(item1+5)%16]+row2[(item2+5)%16]+row3[(item3+5)%16]+row4[(item4+5)%16]+row5[(item5+5)%16]+row6[(item6+5)%16]+row7[(item7+5)%16]+row8[(item8+5)%16]+row9[(item9+5)%16]
                                                        if row3[(item3+5)%16] != 100:
                                                            col6 = col6-row2[(item2+5)%16]
                                                        if row5[(item5+5)%16] != 100:
                                                            col6 = col6-row4[(item4+5)%16]
                                                        if row7[(item7+5)%16] != 100:
                                                            col6 = col6-row6[(item6+5)%16]
                                                        if row9[(item9+5)%16] != 100:
                                                            col6 = col6-row8[(item8+5)%16]
                                                        if row3[(item3+5)%16] == 100:
                                                            col6 = col6-100
                                                        if row5[(item5+5)%16] == 100:
                                                            col6 = col6-100
                                                        if row7[(item7+5)%16] == 100:
                                                            col6 = col6-100
                                                        if row9[(item9+5)%16] == 100:
                                                            col6 = col6-100

                                                        if col6 == 50:
                                                            col7 = row1[(item1+6)%16]+row2[(item2+6)%16]+row3[(item3+6)%16]+row4[(item4+6)%16]+row5[(item5+6)%16]+row6[(item6+6)%16]+row7[(item7+6)%16]+row8[(item8+6)%16]+row9[(item9+6)%16]
                                                            if row3[(item3+6)%16] != 100:
                                                                col7 = col7-row2[(item2+6)%16]
                                                            if row5[(item5+6)%16] != 100:
                                                                col7 = col7-row4[(item4+6)%16]
                                                            if row7[(item7+6)%16] != 100:
                                                                col7 = col7-row6[(item6+6)%16]
                                                            if row9[(item9+6)%16] != 100:
                                                                col7 = col7-row8[(item8+6)%16]
                                                            if row3[(item3+6)%16] == 100:
                                                                col7 = col7-100
                                                            if row5[(item5+6)%16] == 100:
                                                                col7 = col7-100
                                                            if row7[(item7+6)%16] == 100:
                                                                col7 = col7-100
                                                            if row9[(item9+6)%16] == 100:
                                                                col7 = col7-100
                                                            if col7 == 50:
                                                                col8 = row1[(item1+7)%16]+row2[(item2+7)%16]+row3[(item3+7)%16]+row4[(item4+7)%16]+row5[(item5+7)%16]+row6[(item6+7)%16]+row7[(item7+7)%16]+row8[(item8+7)%16]+row9[(item9+7)%16]
                                                                if row3[(item3+7)%16] != 100:
                                                                    col8 = col8-row2[(item2+7)%16]
                                                                if row5[(item5+7)%16] != 100:
                                                                    col8 = col8-row4[(item4+7)%16]
                                                                if row7[(item7+7)%16] != 100:
                                                                    col8 = col8-row6[(item6+7)%16]
                                                                if row9[(item9+7)%16] != 100:
                                                                    col8 = col8-row8[(item8+7)%16]
                                                                if row3[(item3+7)%16] == 100:
                                                                    col8 = col8-100
                                                                if row5[(item5+7)%16] == 100:
                                                                    col8 = col8-100
                                                                if row7[(item7+7)%16] == 100:
                                                                    col8 = col8-100
                                                                if row9[(item9+7)%16] == 100:
                                                                    col8 = col8-100

                                                                if col8 == 50:
                                                                    col9 = row1[(item1+8)%16]+row2[(item2+8)%16]+row3[(item3+8)%16]+row4[(item4+8)%16]+row5[(item5+8)%16]+row6[(item6+8)%16]+row7[(item7+8)%16]+row8[(item8+8)%16]+row9[(item9+8)%16]
                                                                    if row3[(item3+8)%16] != 100:
                                                                        col9 = col9-row2[(item2+8)%16]
                                                                    if row5[(item5+8)%16] != 100:
                                                                        col9 = col9-row4[(item4+8)%16]
                                                                    if row7[(item7+8)%16] != 100:
                                                                        col9 = col9-row6[(item6+8)%16]
                                                                    if row9[(item9+8)%16] != 100:
                                                                        col9 = col9-row8[(item8+8)%16]
                                                                    if row3[(item3+8)%16] == 100:
                                                                        col9 = col9-100
                                                                    if row5[(item5+8)%16] == 100:
                                                                        col9 = col9-100
                                                                    if row7[(item7+8)%16] == 100:
                                                                        col9 = col9-100
                                                                    if row9[(item9+8)%16] == 100:
                                                                        col9 = col9-100

                                                                    if col9 == 50:
                                                                        col10 = row1[(item1+9)%16]+row2[(item2+9)%16]+row3[(item3+9)%16]+row4[(item4+9)%16]+row5[(item5+9)%16]+row6[(item6+9)%16]+row7[(item7+9)%16]+row8[(item8+9)%16]+row9[(item9+9)%16]
                                                                        if row3[(item3+9)%16] != 100:
                                                                            col10 = col10-row2[(item2+9)%16]
                                                                        if row5[(item5+9)%16] != 100:
                                                                            col10 = col10-row4[(item4+9)%16]
                                                                        if row7[(item7+9)%16] != 100:
                                                                            col10 = col10-row6[(item6+9)%16]
                                                                        if row9[(item9+9)%16] != 100:
                                                                            col10 = col10-row8[(item8+9)%16]
                                                                        if row3[(item3+9)%16] == 100:
                                                                            col10 = col10-100
                                                                        if row5[(item5+9)%16] == 100:
                                                                            col10 = col10-100
                                                                        if row7[(item7+9)%16] == 100:
                                                                            col10 = col10-100
                                                                        if row9[(item9+9)%16] == 100:
                                                                            col10 = col10-100

                                                                        if col10 == 50:
                                                                            col11 = row1[(item1+10)%16]+row2[(item2+10)%16]+row3[(item3+10)%16]+row4[(item4+10)%16]+row5[(item5+10)%16]+row6[(item6+10)%16]+row7[(item7+10)%16]+row8[(item8+10)%16]+row9[(item9+10)%16]
                                                                            if row3[(item3+10)%16] != 100:
                                                                                col11 = col11-row2[(item2+10)%16]
                                                                            if row5[(item5+10)%16] != 100:
                                                                                col11 = col11-row4[(item4+10)%16]
                                                                            if row7[(item7+10)%16] != 100:
                                                                                col11 = col11-row6[(item6+10)%16]
                                                                            if row9[(item9+10)%16] != 100:
                                                                                col11 = col11-row8[(item8+10)%16]
                                                                            if row3[(item3+10)%16] == 100:
                                                                                col11 = col11-100
                                                                            if row5[(item5+10)%16] == 100:
                                                                                col11 = col11-100
                                                                            if row7[(item7+10)%16] == 100:
                                                                                col11 = col11-100
                                                                            if row9[(item9+10)%16] == 100:
                                                                                col11 = col11-100

                                                                            if col11 == 50:
                                                                                col12 = row1[(item1+11)%16]+row2[(item2+11)%16]+row3[(item3+11)%16]+row4[(item4+11)%16]+row5[(item5+11)%16]+row6[(item6+11)%16]+row7[(item7+11)%16]+row8[(item8+11)%16]+row9[(item9+11)%16]
                                                                                if row3[(item3+11)%16] != 100:
                                                                                    col12 = col12-row2[(item2+11)%16]
                                                                                if row5[(item5+11)%16] != 100:
                                                                                    col12 = col12-row4[(item4+11)%16]
                                                                                if row7[(item7+11)%16] != 100:
                                                                                    col12 = col12-row6[(item6+11)%16]
                                                                                if row9[(item9+11)%16] != 100:
                                                                                    col12 = col12-row8[(item8+11)%16]
                                                                                if row3[(item3+11)%16] == 100:
                                                                                    col12 = col12-100
                                                                                if row5[(item5+11)%16] == 100:
                                                                                    col12 = col12-100
                                                                                if row7[(item7+11)%16] == 100:
                                                                                    col12 = col12-100
                                                                                if row9[(item9+11)%16] == 100:
                                                                                    col12 = col12-100

                                                                                if col12 == 50:
                                                                                    col13 = row1[(item1+12)%16]+row2[(item2+12)%16]+row3[(item3+12)%16]+row4[(item4+12)%16]+row5[(item5+12)%16]+row6[(item6+12)%16]+row7[(item7+12)%16]+row8[(item8+12)%16]+row9[(item9+12)%16]
                                                                                    if row3[(item3+12)%16] != 100:
                                                                                        col13 = col13-row2[(item2+12)%16]
                                                                                    if row5[(item5+12)%16] != 100:
                                                                                        col13 = col13-row4[(item4+12)%16]
                                                                                    if row7[(item7+12)%16] != 100:
                                                                                        col13 = col13-row6[(item6+12)%16]
                                                                                    if row9[(item9+12)%16] != 100:
                                                                                        col13 = col13-row8[(item8+12)%16]
                                                                                    if row3[(item3+12)%16] == 100:
                                                                                        col13 = col13-100
                                                                                    if row5[(item5+12)%16] == 100:
                                                                                        col13 = col13-100
                                                                                    if row7[(item7+12)%16] == 100:
                                                                                        col13 = col13-100
                                                                                    if row9[(item9+12)%16] == 100:
                                                                                        col13 = col13-100

                                                                                    if col13 == 50:
                                                                                        col14 = row1[(item1+13)%16]+row2[(item2+13)%16]+row3[(item3+13)%16]+row4[(item4+13)%16]+row5[(item5+13)%16]+row6[(item6+13)%16]+row7[(item7+13)%16]+row8[(item8+13)%16]+row9[(item9+13)%16]
                                                                                        if row3[(item3+13)%16] != 100:
                                                                                            col14 = col14-row2[(item2+13)%16]
                                                                                        if row5[(item5+13)%16] != 100:
                                                                                            col14 = col14-row4[(item4+13)%16]
                                                                                        if row7[(item7+13)%16] != 100:
                                                                                            col14 = col14-row6[(item6+13)%16]
                                                                                        if row9[(item9+13)%16] != 100:
                                                                                            col14 = col14-row8[(item8+13)%16]
                                                                                        if row3[(item3+13)%16] == 100:
                                                                                            col14 = col14-100
                                                                                        if row5[(item5+13)%16] == 100:
                                                                                            col14 = col14-100
                                                                                        if row7[(item7+13)%16] == 100:
                                                                                            col14 = col14-100
                                                                                        if row9[(item9+13)%16] == 100:
                                                                                            col14 = col14-100

                                                                                        if col14 == 50:
                                                                                            col15 = row1[(item1+14)%16]+row2[(item2+14)%16]+row3[(item3+14)%16]+row4[(item4+14)%16]+row5[(item5+14)%16]+row6[(item6+14)%16]+row7[(item7+14)%16]+row8[(item8+14)%16]+row9[(item9+14)%16]
                                                                                            if row3[(item3+14)%16] != 100:
                                                                                                col15 = col15-row2[(item2+14)%16]
                                                                                            if row5[(item5+14)%16] != 100:
                                                                                                col15 = col15-row4[(item4+14)%16]
                                                                                            if row7[(item7+14)%16] != 100:
                                                                                                col15 = col15-row6[(item6+14)%16]
                                                                                            if row9[(item9+14)%16] != 100:
                                                                                                col15 = col15-row8[(item8+14)%16]
                                                                                            if row3[(item3+14)%16] == 100:
                                                                                                col15 = col15-100
                                                                                            if row5[(item5+14)%16] == 100:
                                                                                                col15 = col15-100
                                                                                            if row7[(item7+14)%16] == 100:
                                                                                                col15 = col15-100
                                                                                            if row9[(item9+14)%16] == 100:
                                                                                                col15 = col15-100

                                                                                            if col15 == 50:
                                                                                                col16 = row1[(item1+15)%16]+row2[(item2+15)%16]+row3[(item3+15)%16]+row4[(item4+15)%16]+row5[(item5+15)%16]+row6[(item6+15)%16]+row7[(item7+15)%16]+row8[(item8+15)%16]+row9[(item9+15)%16]
                                                                                                if row3[(item3+15)%16] != 100:
                                                                                                    col16 = col16-row2[(item2+15)%16]
                                                                                                if row5[(item5+15)%16] != 100:
                                                                                                    col16 = col16-row4[(item4+15)%16]
                                                                                                if row7[(item7+15)%16] != 100:
                                                                                                    col16 = col16-row6[(item6+15)%16]
                                                                                                if row9[(item9+15)%16] != 100:
                                                                                                    col16 = col16-row8[(item8+15)%16]
                                                                                                if row3[(item3+15)%16] == 100:
                                                                                                    col16 = col16-100
                                                                                                if row5[(item5+15)%16] == 100:
                                                                                                    col16 = col16-100
                                                                                                if row7[(item7+15)%16] == 100:
                                                                                                    col16 = col16-100
                                                                                                if row9[(item9+15)%16] == 100:
                                                                                                    col16 = col16-100

                                                                                                ##FINALLY##
                                                                                                if col16 == 50:
                                                                                                    print("The solution is:", row1[item1], row2[item2], row3[item3], row4[item4], row5[item5], row6[item6], row7[item7], row8[item8], row9[item9])
                                                                                                    solutions +=1
                                    item9 += 1
                                item8 += 1
                                item9 = 0
                            item7 += 1
                            item8 = 0
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
##########################################IMPORTANT NOTE: THIS IS CHECKING THE EVEN ROWS AS SEPERATE FROM THE ATTACEHED ROWS#######################

##CALL MAIN()###
main()
