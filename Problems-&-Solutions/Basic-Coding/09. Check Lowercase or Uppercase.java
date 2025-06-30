//Check if the character is lowercase or uppercase.

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a character : ");
        char a = scan.next().trim().charAt(0);
        if(a>='a' && a<='z'){
            System.out.println("Lowercase");
        }
        else{
            System.out.println("Uppercase");
        }
    }  
}
