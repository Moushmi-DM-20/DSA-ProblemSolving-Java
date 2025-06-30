// Print the Fibonacci series

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a Number : ");
        int num = scan.nextInt();
        int first = 0;
        int second = 1;
        for(int i=0;i<=num;i++){
            int next = first+second;
            System.out.print(next+" ");
            first = second;
            second = next;
        }
    }
}
