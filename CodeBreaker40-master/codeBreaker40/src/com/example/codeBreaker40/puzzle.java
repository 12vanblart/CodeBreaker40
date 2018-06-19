package com.example.codeBreaker50;

public class puzzle {
    /*** NOTE: -1 cannot be used as a value in the puzzle; -1 is the "X" value ***/
    /*Fields*/
    int target;
    int[][] initial_setup;
    int[][] current_setup;
    int turns_made;
    int num_cols;
    int num_rows;
    int total_turns_to_make;
    int[] row_turns;
    int num_solutions = 0;

    /*Initialize*/
    public puzzle(int target_in, int[][] puzzle_in){
        this.target = target_in;
        this.initial_setup = puzzle_in;
        this.current_setup = puzzle_in;
        this.turns_made = 0;
        this.num_cols = puzzle_in[0].length;
        this.num_rows = puzzle_in.length;
        this.total_turns_to_make = this.num_cols^(this.num_rows);
        this.row_turns = new int[this.num_rows];
    }

    /*Methods*/
    public int[] turnRow(int[] turning_row){
        int[] tempRow = new int[this.num_cols];
        for(int i=0; i < this.num_cols; i++){
            if (i == (this.num_cols-1)){
                tempRow[i] = turning_row[0];
            }else{
                tempRow[i] = turning_row[i+1];
            }
        }
        return tempRow;
    }

    public boolean isValid(){
        boolean solution = true;
        int sum;
        for(int c=0; c<this.num_cols; c++){/*for each col...*/
            sum = 0; /*Reset sum for new column*/
            for(int r=(this.num_rows-1);r>=0;r=r-2 ){/*for each row...*/
                if(this.current_setup[r][c] == -1){
                    sum += current_setup[r-1][c];
                }else{
                    sum += current_setup[r][c];
                }
            }
            /*Debugger*/
            //System.out.print("\nCurrent Sum: " + sum);
            if(sum != this.target){
                solution = false;
                break;
            }
        }

        return solution;

    }

    /*GET Methods*/
    int getTarget(){
        return this.target;
    }

    int[][] getInitialSetup(){
        return this.initial_setup;
    }

    int[][] getCurrentSetup(){
        return this.current_setup;
    }

    int getTurnsMade(){
        return this.turns_made;
    }

    int getColumns(){
        return this.num_cols;
    }

    int getRows(){
        return this.num_rows;
    }

    int getCombinations(){
        return this.total_turns_to_make;
    }

    int[] getColumnTurns(){
        return this.row_turns;
    }

    int getSolutionCount(){
        return this.num_solutions;
    }
}