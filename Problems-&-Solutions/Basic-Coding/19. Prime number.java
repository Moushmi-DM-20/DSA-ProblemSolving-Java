//Check if a number is a prime number.

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int a = scan.nextInt();
        int i=2;
        boolean flag = false;
        while(i<=a/2){
            if(a%i==0){
                flag = true;
                break;
            }
            i++;
        }
        if(!flag){
            System.out.println("The number is prime.");
        }
        else{
            System.out.println("The number is not prime.");
        }
    }
}
