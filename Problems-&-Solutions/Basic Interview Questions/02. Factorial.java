//Factorial

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number : ");
        int n = scan.nextInt();
        int product = 1;
        for(int i=1;i<=n;i++){
            product *= i;
        }
        System.out.println(product);
    }
}

//OR

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number : ");
        int n = scan.nextInt();
        System.out.println(factorial(n));
    }
    public static int factorial(int n){
        if(n<=1) return 1;
        return n*factorial(n-1);
    }
}
