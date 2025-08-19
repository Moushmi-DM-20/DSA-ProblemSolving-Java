//Palindrome in number

//Solution

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number : ");
        int n = scan.nextInt();
        int temp = n;
        int res = 0;
        while(n>0){
            int rem = n%10;
            res = (res*10)+rem;
            n = n/10;
        }
        if(temp==res){
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
        System.out.print("Enter a number : ");
        int n1 = scan.nextInt();
        String n = Integer.toString(n1);
        int start = 0;
        int end = n.length()-1;
        boolean value = true;
        while(start<end){
            if(n.charAt(start)!=n.charAt(end)){
                value = false;
                break;
            }
            else{
                start++;
                end--;
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
