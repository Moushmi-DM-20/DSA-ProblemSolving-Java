//Curved Surface Area of Cylinder

//Solution

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter radius of cylinder : ");
        int r = scan.nextInt();
        System.out.print("Enter height of cylinder : ");
        int h = scan.nextInt();
        double CSA = 2*Math.PI*r*h;
        System.out.println("Curved Surface Area of Cylinder : "+CSA);
    }
}
