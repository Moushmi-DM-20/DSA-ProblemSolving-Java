//Volume of Prism

//Solution

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter base of prism : ");
        int b = scan.nextInt();
        System.out.print("Enter height of prism : ");
        int h = scan.nextInt();
        int Volume = b*h;
        System.out.println("Volume of Prism : "+Volume);
    }
}
