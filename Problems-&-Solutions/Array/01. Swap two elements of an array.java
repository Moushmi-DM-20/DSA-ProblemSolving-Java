// Swap two elements of an array

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
        System.out.println("Enter first index");
        int a = scan.nextInt();
        System.out.println("Enter second index");
        int b = scan.nextInt();
        swap(arr,a,b);
        System.out.println("After Swapping");
        System.out.println(Arrays.toString(arr));
    }
    public static void swap(int[] arr, int a,int b){
        if(a>=0 && b>=0 && a<arr.length && b<arr.length){
            int temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp;
        }
    }
}
