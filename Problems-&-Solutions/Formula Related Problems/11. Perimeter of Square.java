//Perimeter of square

//Solution

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a side of square : ");
        int a = scan.nextInt();
        int Perimeter = 4*a;
        System.out.print("Perimeter of Square : "+Perimeter);
    }
}
