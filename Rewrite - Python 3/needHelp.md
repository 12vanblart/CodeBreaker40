# Help Needed

How to take a "puzzle" (array) and number of turns previously made and know which columns need to turn? 
- Currently know how to break the puzzle's columns into 'turnable units' (i.e. the first two rows must turn together because they are phyciscally connected in the puzzle)
  - Turnable Units = (rows - 1)/2 --- This accounts for the topmost row being a single row instead of 2 stuck together
- Max Turns = cols ^ {Turnable Units}
  - This should return the total number of turns possible for any given puzzle? 

Given the following puzzle: (Assume that in this case the rows are all individual turnable units) 
    
    1 2 3
    
    4 5 6 
    
    7 8 9

After 1 turns: 
    
    3 1 2*
    
    4 5 6
    
    7 8 9

After 2 turns: 
    
    2 3 1*
    
    4 5 6
    
    7 8 9

After 3 turns: 
    
    1 2 3*
    
    6 4 5*
    
    7 8 9

After 4 turns: 
    
    3 1 2*
    
    6 4 5
    
    7 8 9

After 5 turns: 
    
    2 3 1*
    
    6 4 5
    
    7 8 9

How can we take 5 and know that for the 6th turn, we need to turn the second row also (to get the following output)? 

After 6 turns: 
    
    1 2 3*
    
    5 6 4*
    
    7 8 9
