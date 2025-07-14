// Binary Search in 2D Matrix

//Solution

import java.util.*;
class Main {
    public static void main(String[] args) {
        int[][] mat = {{1,2,3},
                        {4,5,6},
                        {7,8,9}};
        
        System.out.println(Arrays.toString(search(mat,7)));
    }
    public static int[] search(int[][] mat,int target){
        int start = 0;
        int end = mat.length-1;
        while(start<mat.length && end>=0){
            if(mat[start][end]==target){
                return new int[]{start,end};
            }
            else if(mat[start][end]>target){
                end--;
            }
            else{
                start++;
            }
        }
        return new int[]{-1,-1};
    }
}
