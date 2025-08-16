//Find commom elements without duplicates from two arrays

//Solution

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number1 : ");
        int n = scan.nextInt();
        System.out.print("Enter a number2 : ");
        int m = scan.nextInt();
        int[] arr1 = new int[n];
        int[] arr2 = new int[m];
        System.out.print("Enter "+n+" elements : " );
        for(int i=0;i<n;i++){
            arr1[i] = scan.nextInt();
        }
        System.out.print("Enter "+m+" elements : " );
        for(int i=0;i<m;i++){
            arr2[i] = scan.nextInt();
        }
        Set<Integer> hash = new HashSet<>();
        Set<Integer> common = new HashSet<>();
        for(int num : arr1){
            hash.add(num);
        }
        for(int num : arr2){
            if(hash.contains(num)){
                common.add(num);
            }
        }
        System.out.println((common));
    }
}
