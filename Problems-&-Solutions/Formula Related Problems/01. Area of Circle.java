//Area Of Circle Java Program

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter radius of the circle :");
        int r = scan.nextInt();
        double area = 3.14*r*r;
        System.out.println("Area of a circle : "+area);
    }
}
