# CodeBreaker40
Program for cracking the CodeBreaker 40 Puzzle. 


##Intro
Codebreaker 40 is a puzzle game and can be purchased [here](http://www.creativecrafthouse.com/index.php?main_page=product_info&products_id=805)

The goal of the puzzle is to align the numbers so that every column equates to 40. Using a brute force method and python, it has been confirmed that there exists only a single solution. Now the goal is to reconstruct that original program from Python into Java and build it in a way that can check any size puzzle for how many solutions exist. 

##What constitutes a Solution?
A solution consists of the following conditions:
 - All columns add to the desired number
 - Numbers do not repeat too often. (I know, not very clear. We will get into this in a moment)

 ###Unique Solutions
 When evaluating how many solutions a single puzzle has, we want to know 2 numbers:
  1) How many solutions exist? 
  2) How many unique solutions exist? 

For example, if we had 3 columns and 2 rows (no notches) as so:

1   1   1 </br>
1   1   1

Each column will add to 2 (in this case the desired number). We can turn the top row so that the 1's are in 3 different positions (each 1 is unique), thus meaning we have a total of 3 solutions. However, if the 1's are not unique, we only have a single solution, thus we have a total of 1 unique solution. 
