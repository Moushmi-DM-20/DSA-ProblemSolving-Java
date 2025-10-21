//Print the repeting number in a digit.

//Solutions
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the digit : ");
        int digit = scan.nextInt();
        System.out.print("Enter the number : ");
        int num = scan.nextInt();
        int count = 0;
        while(digit>0){
            int rem = digit%10;
            if (rem==num){
                count++;
            }
            digit = digit/10;
        }
        System.out.println("The count of number "+num+" in given digit is "+count);
    }
}
