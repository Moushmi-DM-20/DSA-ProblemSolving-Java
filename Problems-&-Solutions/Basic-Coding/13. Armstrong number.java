//Check the Armstrong number.

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number : ");
        int a = scan.nextInt();
        int count = checkCount(a);
        boolean result = checkArmstrong(a,count);
        System.out.println("The given number is Armstrong Number - "+ result);
    }
    static int checkCount(int a){
        int count = 0;
        while(a>0){
            int rem = a%10;
            count ++;
            a = a/10;
        }
        return count;
    }
    static boolean checkArmstrong(int a,int count){
        int original = a;
        int sum = 0;
        while(a>0){
            int rem = a%10;
            sum += Math.pow(rem,count);
            a = a/10;    
        }
        return sum == original;
    } 
}
