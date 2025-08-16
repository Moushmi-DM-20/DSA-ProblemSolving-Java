//Volume of Cone

//Solution

import java.util.*;
import java.math.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a radius of cone : ");
        int r = scan.nextInt();
        System.out.print("Enter a height of cone : ");
        int h = scan.nextInt();
        float Volume = (float)(Math.PI*Math.pow(r,2)*(h/3));
        System.out.print("Volume of Cone : "+Volume);
    }
}
