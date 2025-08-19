//Reverse a string

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String s1 = scan.nextLine();
        StringBuilder s2 = new StringBuilder();
        for(int i=s1.length()-1;i>=0;i--){
            s2.append(s1.charAt(i));
        }
        System.out.println(s2);
    }
}

//OR

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a string : ");
        String s1 = scan.nextLine();
        StringBuilder s2 = new StringBuilder(s1);
        System.out.println(s2.reverse());
    }
}
