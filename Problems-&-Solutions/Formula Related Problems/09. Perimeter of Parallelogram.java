//Perimeter of Parallelogram

//Solution

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a side of Parallelogram : ");
        int a = scan.nextInt();
        System.out.print("Enter a base of Parallelogram : ");
        int b = scan.nextInt();
        int Perimeter = 2*(a+b);
        System.out.print("Perimeter of Parallellogram : "+Perimeter);
    }
}
