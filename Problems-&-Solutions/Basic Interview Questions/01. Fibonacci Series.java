//Fibonacci Series

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number : ");
        int n = scan.nextInt();
        int f0 = 0;
        int f1 = 1;
        if(n<=1)
            System.out.println(n);
        else{
            System.out.println(f0);
            System.out.println(f1);
            for(int i=2;i<n;i++){
                int f2 = f0+f1;
                System.out.println(f2);
                f0 = f1;
                f1 = f2;
            }
        }
    }
}

//OR

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number : ");
        int n = scan.nextInt();
        for(int i=0;i<n;i++){
            System.out.println(fibonacci(i));
        }
    }
    public static int fibonacci(int n){
        if(n<=1) return n;
        return fibonacci(n-1)+fibonacci(n-2);
    }
}
