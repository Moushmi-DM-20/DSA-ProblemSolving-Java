//Check the Armstrong number.

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number : ");
        int a = scan.nextInt();
        boolean result = checkArmstrong(a);
        System.out.println("The given number is Armstrong Number - "+ result);
    }
    static boolean checkArmstrong(int a){
        int original = a;
        int sum = 0;
        while(a>0){
            int rem = a%10;
            sum = sum+(rem*rem*rem);
            a = a/10;    
        }
        return sum == original;
    } 
}
