//Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int sum = 0;
        String a = "";
        System.out.println("Enter a number. Type 'X' to stop : "+sum);
        while(!a.equals("x")){
            a = scan.nextLine();
            if(!a.equals("x")){
                sum += Integer.parseInt(a);
            }
        }
        System.out.println("Final Sum : "+sum);
    }
}
