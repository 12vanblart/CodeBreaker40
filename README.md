# CodeBreaker40
Program for cracking the CodeBreaker 40 Puzzle. 

## Folders Outline

CodeBreaker40-master -- Folder containing some java files from when I started rewriting the code. (Did not get very far with the java). 
Original Code -- Folder containing the original Python project. This works for solving a puzzle that is passed in. 

## Goal

The goal is to create code that is able to run in an attempt to find a single puzzle with multiple unique solutions (if any exist). 
My thought is that the it would run through every possible puzzle layout starting from a puzzle with all 0's (clearly no solution) and work up to 40 in each slot (essentially a base 41 counting system).


# Details

## Intro

Codebreaker 40 is a puzzle game and can be purchased [here](https://www.creativecrafthouse.com/safecracker-40-puzzle-can-you-find-the-combination.html)

The goal of the puzzle is to align the numbers so that every column equates to 40. Using a brute force method and python, it has been confirmed that there exists only a single solution. Now the goal is to reconstruct that original program from Python into Java and build it in a way that can check any size puzzle for how many solutions exist. 

## What constitutes a Solution?

A solution consists of the following conditions:
 - All columns add to the desired number
 - Numbers do not repeat too often. (I know, not very clear. We will get into this in a moment)

### Unique Solutions

When evaluating how many solutions a single puzzle has, we want to know 2 numbers:
  1) How many solutions exist? 
  2) How many unique solutions exist? 

For example, if we had 3 columns and 2 rows (no notches) as so:

1   1   1 </br>
1   1   1

Each column will add to 2 (in this case the desired number). We can turn the top row so that the 1's are in 3 different positions (each 1 is unique), thus meaning we have a total of 3 solutions. However, if the 1's are not unique, we only have a single solution, thus we have a total of 1 unique solution. 

