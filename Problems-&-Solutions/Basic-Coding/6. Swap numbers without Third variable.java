//Write a program to swap two numbers without using a third variable.

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter first number : ");
        int a = scan.nextInt();
        System.out.println("Enter second number : ");
        int b = scan.nextInt();
        System.out.println(" Before Swapping ");
        System.out.println(" The value of a is "+ a);
        System.out.println(" The value of a is "+ b);
        a = a+b;
        b = a-b;
        a = a-b;
        System.out.println(" After Swapping ");
        System.out.println(" The value of a is "+ a);
        System.out.println(" The value of a is "+ b);
    }
}
