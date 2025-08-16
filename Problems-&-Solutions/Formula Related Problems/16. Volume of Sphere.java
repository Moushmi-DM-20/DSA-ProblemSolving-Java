//Volume of Sphere

//Solution

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter radius of sphere : ");
        int r = scan.nextInt();
        float Volume = (float)((4/3)*Math.PI*Math.pow(r,3));
        System.out.println("Volume of Sphere : "+Volume);
    }
}
