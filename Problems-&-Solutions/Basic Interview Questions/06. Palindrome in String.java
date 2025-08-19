// Palindrome in String

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a String : ");
        String s1 = scan.nextLine();
        StringBuilder s2 = new StringBuilder(s1);
        s2.reverse();
        if(s1.equals(s2.toString())){
            System.out.println("Palindrome");
        }
        else{
            System.out.println("Not a Palindrome");
        }
    }
}

//OR

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a String : ");
        String s1 = scan.nextLine();
        int start = 0;
        int end = s1.length()-1;
        boolean value = true;
        while(start<end){
            if(s1.charAt(start)==s1.charAt(end)){
                start++;
                end--;
            }
            else {
                value = false;
                break;
            }
        }
        if(value){
            System.out.println("Palindrome");
        }
        else{
            System.out.println("Not a Palindrome");
        }
    }
}

//OR

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a String : ");
        String s1 = scan.nextLine();
        String s2 = new StringBuilder(s1).reverse().toString();// here stringbuilder is only used to reverse so we don't need to take reference. 
                                                              //If wee need to add, delete, update the datails again int the process we use that. 
                                                              //After it's use it can be handled by garbage collection
        if(s1.equals(s2)){
            System.out.println("Palindrome");
        }
        else{
            System.out.println("Not a Palindrome");
        }
    }
}
