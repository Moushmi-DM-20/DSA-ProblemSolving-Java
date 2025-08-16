//Volume of Cylinder

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
        float Volume = (float)(Math.PI*Math.pow(r,2)*h);
        System.out.println("Volume of Prism : "+Volume);
    }
}
