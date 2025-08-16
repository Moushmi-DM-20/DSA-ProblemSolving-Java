//Perimeter of Circle

//Solution

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a radius of circle : ");
        int r = scan.nextInt();
        double Perimeter = 2*Math.PI*r;
        System.out.print("Perimeter of circle : "+Perimeter);
    }
}

//OR

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a radius of circle : ");
        int r = scan.nextInt();
        float Perimeter = (float)(2*3.14*r);
        System.out.print("Perimeter of circle : "+Perimeter);
    }
}
