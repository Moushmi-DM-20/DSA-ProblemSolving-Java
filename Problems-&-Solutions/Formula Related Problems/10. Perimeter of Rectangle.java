//Perimeter of Rectangle

//Solution

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a length of rectangle : ");
        int l = scan.nextInt();
        System.out.print("Enter a width of rectangle : ");
        int w = scan.nextInt();
        int Perimeter = 2*(l+w);
        System.out.print("Perimeter of Rectangle : "+Perimeter);
    }
}
