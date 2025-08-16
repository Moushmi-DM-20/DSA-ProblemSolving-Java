//Area of Equilateral Triangle

//Solution

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a side of Equilateral Triangle : ");
        int a = scan.nextInt();
        double Area = (Math.sqrt(3)/4)*Math.pow(a,2);
        System.out.print("Area of Equilateral Triangle : "+Area);
    }
}

//OR

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a side of Equilateral Triangle : ");
        int a = scan.nextInt();
        float Area = (float)(Math.sqrt(3)/4)*(a*a);
        System.out.print("Area of Equilateral Triangle : "+Area);
    }
}
