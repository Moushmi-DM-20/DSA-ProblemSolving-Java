//Insertion Sort

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {5,4,3,2,1};
        System.out.println(Arrays.toString(insertionSort(arr)));
    }
    public static int[] insertionSort(int[] arr){
        for(int i=1;i<arr.length;i++){
            int min = arr[i];
            int j = i-1;
            while(j>=0 && arr[j]>min){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = min;
        }
        return arr;
    }
}
