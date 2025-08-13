//Minimum Element of an Array

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number");
        int n = scan.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = scan.nextInt();
        }
        int result = Minimum(arr);
        System.out.println("Minimum Element : "+result);
    }
    public static int Minimum(int[] arr){
        int min = arr[0];
        for(int i=0;i<arr.length;i++){
            if(arr[i]<min){
                min = arr[i];
            }
        }
        return min;
    }
}
