//Check if a number is a palindrome.

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int a = scan.nextInt();
        int original = a;
        int result = 0;
        while(a!=0){
            int digit = a%10;
            result = result*10+digit;
            a = a/10;
        }
        if(original == result){
            System.out.println("The number is palindrome.");
        }
        else{
            System.out.println("The number is not palindrome.");
        }
    }
}
