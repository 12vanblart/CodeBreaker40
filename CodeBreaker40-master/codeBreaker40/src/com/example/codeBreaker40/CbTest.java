package com.example.codeBreaker50;

public class CbTest {
    puzzle testPuzzle;

    public CbTest() {

        int[][] testArray = {{1, 1}, {1, 1},{1,-1}};
        int testTarget = 2;

        this.testPuzzle = new puzzle(testTarget, testArray);

        /*Run Tests*/
        System.out.print("Number of Columns: " + this.testPuzzle.getColumns());
        System.out.print("\nNumber of Rows: " + this.testPuzzle.getRows());
        System.out.print("\nTarget: " + this.testPuzzle.getTarget());
        if(this.testPuzzle.isValid()){
            System.out.print("\nisValid is functioning as expected");
        } else {
            System.out.print("\nError: isValid encountered an error");
        }
    }
}
