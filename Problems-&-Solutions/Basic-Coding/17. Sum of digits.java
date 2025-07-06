//Find the sum of digits of a given number.

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int a = scan.nextInt();
        int sum = 0;
        while(a != 0){
            int digit = a%10;
            sum += digit;
            a = a/10;
        }
        System.out.println(sum);
    }
}
