//Area Of Rectangle Program

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter length of the rectangle :");
        int l = scan.nextInt();
        System.out.print("Enter breadth of the rectangle :");
        int b = scan.nextInt();
        double area = (double)l*b;
        System.out.println("Area of a rectangle : "+area);
    }
}
