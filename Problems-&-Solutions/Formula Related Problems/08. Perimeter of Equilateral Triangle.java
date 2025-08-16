//Perimeter of Equilateral Triangle

//Solution

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a side of Equilateral Triangle : ");
        int a = scan.nextInt();
        int Perimeter = 3*a;
        System.out.print("Perimeter of Equilateral Triangle : "+Perimeter);
    }
}
