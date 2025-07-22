//Area Of Triangle or Isosceles Triangle

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter length of the triangle :");
        int l = scan.nextInt();
        System.out.print("Enter breadth of the triangle :");
        int b = scan.nextInt();
        double area = 0.5*l*b;
        System.out.println("Area of a triangle : "+area);
    }
}
