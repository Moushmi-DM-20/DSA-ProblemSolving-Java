//Volume of Pyramid

//Solution

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter base length of pyramid : ");
        int l = scan.nextInt();
        System.out.print("Enter base width of pyramid : ");
        int w = scan.nextInt();
        System.out.print("Enter height of pyramid : ");
        int h = scan.nextInt();
        int Volume = (l*w*h)/3;
        System.out.println("Volume of Pyramid : "+Volume);
    }
}
