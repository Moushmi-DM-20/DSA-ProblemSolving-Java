//Area Of Rhombus

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter diagonal1 of the Rhombus :");
        int d1 = scan.nextInt();
        System.out.print("Enter diagonal2 of the Rhombus :");
        int d2 = scan.nextInt();
        double area = (double)(d1*d2)/2;
        System.out.println("Area of a Rhombus : "+area);
    }
}
