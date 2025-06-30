//Reverse a digit

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a Number : ");
        int num = scan.nextInt();
        int digit = 0;
        while(num>0){
            int rem = num%10;
            digit = (digit*10)+rem;
            num = num/10;
        }
        System.out.println(digit);
    }
}
