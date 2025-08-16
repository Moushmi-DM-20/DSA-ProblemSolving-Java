//Total Surface Area of Cube

//Solution

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter side of cube : ");
        int a = scan.nextInt();
        double SurfaceArea = 6*Math.pow(a,2);
        System.out.println("Surface Area of Cube : "+SurfaceArea);
    }
}
