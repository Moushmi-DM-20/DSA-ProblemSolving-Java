//Take name as input and print a greeting message for that particular name.

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a name : ");
        String name = scan.nextLine();
        System.out.println("Good Morning "+name+" !" );
    }
}
