//Print the smallest number

//solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter first Number : ");
        int a = scan.nextInt();
        System.out.print("Enter second Number : ");
        int b = scan.nextInt();
        System.out.print("Enter third Number : ");
        int c = scan.nextInt();
        int min = Math.min(c, Math.min(a,b));
        System.out.println("Minimum Number : "+ min);    
    }
}
