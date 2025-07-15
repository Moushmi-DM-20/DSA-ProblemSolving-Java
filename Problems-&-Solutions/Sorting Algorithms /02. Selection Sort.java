// Selection Sort

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        int[] arr = {5,4,3,2,1};
        System.out.println(Arrays.toString(selectionSort(arr)));
    }
    public static int[] selectionSort(int[] arr){
        for(int i=0;i<arr.length;i++){
            int min = arr[i];
            for(int j=0;j<arr.length;j++){
                if(arr[j]<min){
                    min = arr[j];
                }
            }
            int temp = min;
            min = arr[i];
            arr[i] = temp;
        }
        return arr;
    }
}
