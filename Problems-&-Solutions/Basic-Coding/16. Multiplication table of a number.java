//Print the multiplication table of a number.

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int a = scan.nextInt();
        for(int i=1;i<=10;i++){
            System.out.println(i+"*"+a+"="+i*a);
        }
    }
}
