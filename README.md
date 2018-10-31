# CodeBreaker40
Program for cracking the CodeBreaker 40 Puzzle. 

### Update 10/31/18

After running this code for ~1 month straight, the code had just incremented the 4th slot to "1", and as such will take a very long time to run. Any insight for how to improve the amount of time this would take without a super computer is appreciated! 

## Folders Outline

- **CodeBreaker40-master** — Contains initial Java files i started with when rewriting the code. (Did not get very far with the java).

- **Original Code** — Contains the original Python project. This works for solving a puzzle.

## Goal

The goal is to create code that is able to run in an attempt to find a single puzzle with multiple unique solutions (if any exist).

My thought is that the it would run through every possible puzzle layout starting from a puzzle with all 0's (clearly no solution) and work up to 40 in each slot (essentially a base 41 counting system).


# Details

## Intro

**Codebreaker 40** is a puzzle game and can be purchased [here](https://www.creativecrafthouse.com/safecracker-40-puzzle-can-you-find-the-combination.html).

The goal of the puzzle is to align the numbers so that every column equates to 40. Using a brute force method and python, it has been confirmed that there exists only a single solution. 

The goal was to reconstruct the original program from Python into a Java program which accepts any puzzle size and checks how many solutions exist, but has since been reconstructed in Python instead. 

## What constitutes a Solution?

A solution consists of the following conditions:
 - All columns add to the desired number
 - Numbers do not repeat too often. (*Explained below*)

### Unique Solutions

When evaluating how many solutions a single puzzle has, we look at two numbers:
  1) How many solutions exist? 
  2) How many **unique** solutions exist? 

For example, if we have 3 columns and 2 rows (no notches):

|   |   |   |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 1 | 1 |
|   |   |   | 

Each column will add up to 2 (in this case the desired number). We can turn the top row so that the 1's are in 3 different positions (each 1 is unique), thus meaning we have a total of 3 solutions. However, if the 1's are not unique, we only have a single solution, thus we have a total of 1 unique solution. 

