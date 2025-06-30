//Write a recursive function to print the factorial of a number?

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int number = scan.nextInt();
        System.out.println(factorial(number));
    }
    public static long factorial(int number){
        if(number==0||number==1)
        {
            return 1;
        }
        return number*factorial(number-1);
    }
}
