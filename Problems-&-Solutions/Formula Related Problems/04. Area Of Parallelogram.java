Area Of Parallelogram

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter base of the Parallelogram :");
        int b = scan.nextInt();
        System.out.print("Enter height of the Parallelogram :");
        int h = scan.nextInt();
        double area = b*h;
        System.out.println("Area of a Parallelogram : "+area);
    }
}
