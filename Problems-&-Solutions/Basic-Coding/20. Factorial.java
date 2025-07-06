//Write a program to print the factorial of a number

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int number = scan.nextInt();
        long factorial = 1;
        for(int i=1;i<=number;i++){
            factorial *= i;
        }
        System.out.println(factorial);
    }
}
